# Troubleshooting Guide

Common errors and how to resolve them.

---

## Before Troubleshooting

Run these checks first — they resolve the majority of issues:

```bash
# 1. Verify Ansible version
ansible --version

# 2. Verify collections are installed
ansible-galaxy collection list | grep -E "cisco|vmware|paloalto|netapp"

# 3. Syntax check the playbook
ansible-playbook <platform>/site.yml -i <inventory> --syntax-check

# 4. Verify vault is accessible
ansible-vault view <platform>/group_vars/all/vault.yml

# 5. Test connectivity to target
ansible -i <inventory> all -m ping --ask-vault-pass
```

---

## Authentication and Vault Errors

### `ERROR! Decryption failed (HMAC mismatch)`

**Cause:** Wrong vault password.

**Fix:** Re-enter the vault password. If you have multiple vaults, ensure
you are using `--vault-id` or `--ask-vault-pass` for the correct file.

```bash
ansible-playbook site.yml -i inventory --ask-vault-pass
```

---

### `variable 'vault_xxx_password' is undefined`

**Cause:** The vault file is missing a required variable, or the vault
file is not in the correct location for Ansible to load it.

**Fix:**
1. Check the platform `README.md` for the complete list of required vault variables.
2. Verify your vault file defines the missing variable.
3. Ensure the vault file is in `group_vars/all/` or explicitly referenced.

```bash
# Check what vault variables the role expects
grep -r "vault_" <platform>/roles/<role>/defaults/main.yml
```

---

### `Authentication failed` / `401 Unauthorized`

**Cause:** Credential in vault is incorrect or the account is locked.

**Fix:**
1. Verify credentials manually (log in to the target system's UI or API).
2. Check if the account is locked due to failed login attempts.
3. Update the vault file with correct credentials:

```bash
ansible-vault edit <platform>/group_vars/all/vault.yml
```

---

## Collection and Module Errors

### `ERROR! couldn't resolve module/action 'cisco.aci.aci_tenant'`

**Cause:** Required Ansible collection is not installed.

**Fix:**
```bash
ansible-galaxy collection install -r <platform>/requirements.yml
```

If the collection is installed but still not found:
```bash
# Check the collection path
ansible-galaxy collection list
# Ensure ANSIBLE_COLLECTIONS_PATH is not overriding the default
echo $ANSIBLE_COLLECTIONS_PATH
```

---

### `ModuleNotFoundError: No module named 'acicobra'`

**Cause:** Required Python package is missing on the control host.

**Fix:** Install the package in the Python environment Ansible is using:

```bash
# Identify which Python Ansible uses
ansible --version | grep "python version"

# Install the missing package
pip install acicobra        # Cisco ACI
pip install ciscoisesdk     # Cisco ISE
pip install ucsmsdk         # Cisco UCS
pip install pyVmomi         # VMware
pip install netapp-lib      # NetApp
```

---

## Connectivity Errors

### `UNREACHABLE! => {"msg": "Failed to connect to the host via ssh"}`

**Cause:** SSH connection to target host failed.

**Fix:**
1. Verify the hostname/IP in your inventory is correct.
2. Confirm the target is reachable: `ping <hostname>`
3. Test SSH manually: `ssh <user>@<hostname>`
4. Check `ansible_port`, `ansible_user`, and `ansible_ssh_private_key_file`
   in your inventory.

---

### `Connection timed out` on API-based playbooks (Cisco, VMware, Palo Alto, etc.)

**Cause:** The control host cannot reach the management API endpoint.

**Fix:**
1. Confirm network path: `curl -k https://<management-ip>/api/`
2. Check firewall rules between your control host and the management network.
3. Verify `validate_certs` is not blocking connection due to an untrusted CA:

```yaml
# In inventory or group_vars — only disable for testing, not production
aci_verify_ssl: false
```

> Setting `validate_certs: false` is insecure. For production, import the
> target system's CA certificate into the control host's trust store instead.

---

### `SSL: CERTIFICATE_VERIFY_FAILED`

**Cause:** TLS certificate on the target cannot be verified.

**Fix (correct):** Add the target's CA certificate to the control host:

```bash
# Linux
sudo cp target-ca.crt /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust

# Then re-run with verify enabled
```

**Fix (temporary testing only):**
```yaml
# In inventory
aci_verify_ssl: false
vcenter_validate_certs: false
```

---

## Task Execution Errors

### Task fails with `changed=0` but expected change

**Cause:** `apply_changes` is set to `false` (dry-run mode is the default).

**Fix:** Explicitly set `apply_changes=true`:

```bash
ansible-playbook site.yml -i inventory -e "apply_changes=true" --ask-vault-pass
```

---

### `The task includes an option with an undefined variable`

**Cause:** A variable used in a task is not defined in inventory, group_vars,
or the vault file.

**Fix:**
1. Find which variable is undefined from the error message.
2. Check the role's `defaults/main.yml` to see if it should have a default.
3. Add the variable to your inventory or vault file.

```bash
# List all variables a role uses
grep -r "{{" <platform>/roles/<role>/tasks/ | grep -v "#"
```

---

### `fatal: [localhost]: FAILED! => {"msg": "AnsibleUndefinedVariable"}`

**Cause:** Often a missing loop variable or a `register` result being
used before the task that populates it.

**Fix:** Check if you are running with `--tags` that skip a task that
a later task depends on. Run without tag filtering first to identify
the dependency.

---

### `failed: maximum retries exceeded`

**Cause:** A task with `retries:` could not complete after all retry
attempts. Common on network API calls during high load.

**Fix:**
1. Check the target system's health (CPU, memory, API availability).
2. Re-run the playbook after a few minutes.
3. Run with increased verbosity to see the underlying API error:

```bash
ansible-playbook site.yml -i inventory -vvv --ask-vault-pass
```

---

## Compliance and Artifact Errors

### `Permission denied` writing to artifacts directory

**Cause:** The `artifacts_dir` path is not writable by the Ansible process.

**Fix:**
```bash
# Create and set permissions on the artifacts directory
mkdir -p /tmp/ansible-artifacts
chmod 755 /tmp/ansible-artifacts

# Or override the path in your playbook/inventory
ansible-playbook site.yml -i inventory -e "artifacts_dir=/opt/artifacts"
```

---

### Compliance artifacts show `apply_changes: false`

**Cause:** The playbook ran in dry-run mode (the default). Artifacts
generated in dry-run mode reflect query results, not applied configuration.

**Fix:** This is expected behavior. Re-run with `apply_changes=true` and
new artifacts will reflect the applied state.

---

## Platform-Specific Issues

### Cisco ACI: `Error 400: Object Already Exists`

**Cause:** The ACI module attempted to create an object that already
exists but with different parameters.

**Fix:** Run a query first to see the existing object state, then
update your variable definitions to match the desired state:

```bash
ansible-playbook cisco/site.yml -i cisco/inventory \
  -e "apply_changes=false" --tags tenants
```

Review the query output and adjust variables accordingly.

---

### Cisco ISE: `ConnectionError: Max retries exceeded`

**Cause:** ISE API rate limiting or ISE service is starting up (takes
2-5 minutes after a restart).

**Fix:** Wait 3-5 minutes and retry. If persisting, check ISE application
server health from the ISE admin UI.

---

### VMware: `vim.fault.InvalidLogin`

**Cause:** vCenter or ESXi credentials are incorrect.

**Fix:** Verify `vcenter_username` format — vCenter often requires the
full UPN format: `administrator@vsphere.local` or `DOMAIN\user`.

---

### VMware: `host is in maintenance mode`

**Cause:** The `vsphere_esxi_config` role sets maintenance mode and
a subsequent task is attempting an operation not allowed in that state.

**Fix:** This should be handled automatically by the role. If you see
this on a re-run, exit maintenance mode manually and re-run:

```bash
ansible-playbook vmware/site.yml -i inventory \
  --tags exit_maintenance --ask-vault-pass
```

---

### NetApp: `NetApp API failed: 13005: Volume does not exist`

**Cause:** A task depends on a volume that was not created in a previous
phase, or the volume name in your variables does not match what exists on
the cluster.

**Fix:** Run Phase 1 (cluster setup) before Phase 2 (SVM management) and
Phase 3 (volume provisioning), in order.

---

### RHEL: `AIDE: Couldn't load file context information`

**Cause:** SELinux contexts are not in sync. This commonly occurs when
running `aide --check` before `restorecon` has updated file contexts.

**Fix:**
```bash
# Run restorecon on affected paths before next AIDE check
sudo restorecon -Rv /etc /usr/bin /usr/sbin
```

---

## Getting More Information

### Increase verbosity

```bash
ansible-playbook site.yml -i inventory -v      # basic
ansible-playbook site.yml -i inventory -vv     # task details
ansible-playbook site.yml -i inventory -vvv    # connection details
ansible-playbook site.yml -i inventory -vvvv   # full debug
```

### Log to file

```bash
ANSIBLE_LOG_PATH=/tmp/ansible-run.log \
  ansible-playbook site.yml -i inventory --ask-vault-pass
```

### Check what a playbook will do

```bash
# List all tasks without running them
ansible-playbook site.yml -i inventory --list-tasks

# List all hosts targeted
ansible-playbook site.yml -i inventory --list-hosts

# List all available tags
ansible-playbook site.yml --list-tags
```

---

## Still Stuck?

1. Check [KNOWN_LIMITATIONS.md](KNOWN_LIMITATIONS.md) — your issue may
   be a documented limitation.
2. Increase verbosity (`-vvv`) and capture the full output.
3. Check the platform vendor's API/CLI documentation for the underlying
   error code.
4. Open a GitHub issue with the full error output and playbook name.

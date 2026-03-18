# Customer Quick Start Guide

This guide gets you from zero to a running deployment. Read it top to bottom on your first use.

---

## Before You Start

### What You Need

| Requirement | Minimum Version | Notes |
|-------------|----------------|-------|
| Ansible | 2.15+ | `ansible --version` |
| Python | 3.10+ | `python3 --version` |
| ansible-vault | Included with Ansible | For credential management |
| Network access | — | Control host must reach target systems |

### How This Repo Works

Every technology platform has its own directory (`cisco/`, `vmware/`, `vast/`, etc.). Inside each:

```
<platform>/
├── site.yml              # Entry point — run this
├── inventory.example     # Copy this, fill in your hosts/credentials
├── requirements.yml      # Collections to install
├── README.md             # Platform-specific guide
├── roles/                # Automation logic (do not edit)
└── tasks/                # Standalone task files
```

**You only need to touch three things:**
1. Your inventory file (hosts + variables)
2. Your vault file (credentials)
3. The `apply_changes` variable (dry-run vs. apply)

---

## Step 1: Choose Your Platform

Each platform is independent. Pick one to start.

| You want to automate... | Directory | README |
|------------------------|-----------|--------|
| Cisco ACI / ISE / UCS | `cisco/` | [cisco/README.md](cisco/README.md) |
| VMware vSphere / ESXi | `vmware/` | [vmware/README.md](vmware/README.md) |
| VAST Data storage | `vast/` | [vast/README.md](vast/README.md) |
| NetApp ONTAP | `netapp/` | [netapp/README.md](netapp/README.md) |
| Palo Alto firewalls | `palo_alto/` | [palo_alto/README.md](palo_alto/README.md) |
| Check Point firewalls | `checkpoint/` | [checkpoint/README.md](checkpoint/README.md) |
| F5 BIG-IP | `f5_bigip/` | [f5_bigip/README.md](f5_bigip/README.md) |
| Infoblox DNS/DHCP | `infoblox/` | [infoblox/README.md](infoblox/README.md) |
| Illumio micro-seg | `illumio/` | [illumio/README.md](illumio/README.md) |
| RHEL servers | `rhel/` | [rhel/README.md](rhel/README.md) |
| Windows servers | `windows/` | [windows/README.md](windows/README.md) |
| Kubernetes clusters | `kubernetes/` | [kubernetes/README.md](kubernetes/README.md) |
| AWS | `aws/` | [aws/README.md](aws/README.md) |
| Azure | `azure/` | [azure/README.md](azure/README.md) |
| Splunk | `splunk/` | [splunk/README.md](splunk/README.md) |
| ServiceNow CMDB | `servicenow/` | [servicenow/README.md](servicenow/README.md) |
| HashiCorp Vault | `hashicorp_vault/` | [hashicorp_vault/README.md](hashicorp_vault/README.md) |
| NIST/STIG policy | `policy_as_code/` | [policy_as_code/README.md](policy_as_code/README.md) |
| All others | See directory listing | Each has a README.md |

---

## Step 2: Install Dependencies

```bash
# Install collections for your chosen platform (example: Cisco)
ansible-galaxy collection install -r cisco/requirements.yml

# Install Python packages (check platform README for specifics)
pip install -r cisco/requirements.txt   # if present
# or
pip install acicobra acimodel ciscoisesdk  # Cisco example
```

> Each platform's `README.md` lists the exact packages required.

---

## Step 3: Set Up Your Inventory

```bash
# Copy the example inventory
cp cisco/inventory.example cisco/inventory

# Edit it with your hostnames and variable values
# (credentials go in the vault file — see Step 4)
```

The inventory file tells Ansible where your systems are and sets
non-sensitive configuration variables. Example:

```ini
[aci]
apic01.yourdomain.com

[aci:vars]
aci_verify_ssl=true
aci_use_proxy=false
```

> Refer to the platform `README.md` for the full list of required variables.

---

## Step 4: Create Your Vault File

All credentials must be stored in an encrypted vault file. **Never put
passwords in your inventory or playbooks.**

Every platform includes a `vault.yml.example` file listing every credential
variable it needs, with descriptions of where to find each value.

```bash
# 1. Copy the example to your group_vars directory
mkdir -p cisco/group_vars/all
cp cisco/vault.yml.example cisco/group_vars/all/vault.yml

# 2. Edit the file — fill in every CHANGE_ME value
vi cisco/group_vars/all/vault.yml

# 3. Encrypt it with ansible-vault
ansible-vault encrypt cisco/group_vars/all/vault.yml
```

> Each `vault.yml.example` lists only the variables for that platform.
> Required variables are marked clearly; optional ones have comments
> explaining when they are needed.

---

## Step 5: Run a Dry Run First

**Always run with `apply_changes=false` first.** This queries your
systems and reports what would change without making any modifications.

```bash
ansible-playbook cisco/site.yml \
  -i cisco/inventory \
  -e "apply_changes=false" \
  --ask-vault-pass
```

Review the output. You should see:
- `ok` — system is already in the desired state
- `changed` — this setting would be modified (review carefully)
- `skipped` — task was conditionally skipped
- `failed` — something went wrong (fix before proceeding)

> If you see unexpected `changed` results, inspect that specific task
> before applying. Use `--tags <tag>` to narrow scope.

---

## Step 6: Apply to a Single System First

Before running against all systems, validate on one:

```bash
ansible-playbook cisco/site.yml \
  -i cisco/inventory \
  -e "apply_changes=true" \
  --limit apic01.yourdomain.com \
  --ask-vault-pass
```

Verify the system is configured correctly before proceeding to the full run.

---

## Step 7: Apply to All Systems

Once you are satisfied with the single-system result:

```bash
ansible-playbook cisco/site.yml \
  -i cisco/inventory \
  -e "apply_changes=true" \
  --ask-vault-pass
```

---

## Common Patterns

### Run only a specific phase or component

```bash
# Only apply security hardening
ansible-playbook cisco/site.yml -i cisco/inventory \
  -e "apply_changes=true" --tags security --ask-vault-pass

# Only run ACI-related tasks
ansible-playbook cisco/site.yml -i cisco/inventory \
  -e "apply_changes=true" --tags aci --ask-vault-pass
```

### Check what tags are available

```bash
ansible-playbook cisco/site.yml --list-tags
```

### Run a syntax check before executing

```bash
ansible-playbook cisco/site.yml -i cisco/inventory --syntax-check
```

### Re-run safely after a partial failure

All playbooks are designed to be idempotent — tasks that have already
completed will report `ok` on a second run rather than making duplicate
changes. See [KNOWN_LIMITATIONS.md](KNOWN_LIMITATIONS.md) for the small
set of exceptions.

---

## Compliance Artifacts

After each run, compliance artifacts (JSON reports) are written to the
directory defined by `artifacts_dir` (default: `/tmp/<platform>-artifacts`).
These document what was configured, when, and which NIST/STIG controls
were addressed.

```bash
# View artifacts after a Cisco deployment
ls -la /tmp/cisco-aci-artifacts/
cat /tmp/cisco-aci-artifacts/aci_tenant_validation_report.json
```

---

## Where to Go Next

| Topic | Resource |
|-------|----------|
| Known non-idempotent tasks | [KNOWN_LIMITATIONS.md](KNOWN_LIMITATIONS.md) |
| Common errors and fixes | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |
| NIST 800-53 / STIG mapping | [COMPLIANCE_MAPPING.md](COMPLIANCE_MAPPING.md) |
| Policy-as-Code deployment | [policy_as_code/DEPLOYMENT_GUIDE.md](policy_as_code/DEPLOYMENT_GUIDE.md) |
| Full repository reference | [README.md](README.md) |
| Platform-specific guide | `<platform>/README.md` |
| Individual role reference | `<platform>/roles/<role>/README.md` |

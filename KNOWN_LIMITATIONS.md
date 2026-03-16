# Known Limitations

This document lists tasks and playbooks that have known non-idempotent
behavior, version constraints, or other limitations that customers should
be aware of before running in production.

---

## Idempotency Limitations

These tasks produce side effects that may cause failures or unexpected
behavior if the playbook is re-run without manual intervention first.

### AIDE Database Initialization

**Affects:** `rhel/roles/rhel-hardening/tasks/aide.yml`,
`splunk/roles/splunk_security_hardening/tasks/integrity_monitoring.yml`

AIDE (Advanced Intrusion Detection Environment) builds a baseline file
integrity database the first time it runs. On subsequent runs, `aide --init`
will overwrite the existing database rather than update it, which means:

- The previous baseline is lost
- Any legitimate file changes since the last init will be wiped from history
- The AIDE check cron job may fail briefly while the new database is moved into place

**Workaround:** After the first deployment, do not re-run the AIDE initialization
task. If you need to re-baseline, do so intentionally:

```bash
# Re-run only if you intend to rebuild the baseline
ansible-playbook rhel/site.yml -i inventory \
  -e "apply_changes=true" --tags aide_init
```

To re-run the playbook safely without re-initializing AIDE, use tags to
skip the init task:

```bash
ansible-playbook rhel/site.yml -i inventory \
  -e "apply_changes=true" --skip-tags aide_init
```

---

### Veeam and SQL Server Installation

**Affects:** `veeam/roles/veeam_backup_server_install/tasks/main.yml`

The Veeam installation tasks use `args: creates:` guards to check for the
installed binary before running. However, if installation completes partially
(e.g., SQL Server installs but Veeam does not), a re-run may fail because:

- The SQL Server service account creation will fail with "account already exists"
- SQL Server configuration steps may conflict with the existing partial install

**Workaround:** If a Veeam installation fails partway, clean up the partial
install manually before re-running:

```powershell
# On the Windows target — remove partial SQL Server instance if needed
# Then re-run the playbook
```

---

### Firewall Reload (RHEL)

**Affects:** `rhel/tasks/configure-firewall.yml`

The `firewall-cmd --reload` task is marked `changed_when: true` because
a firewall reload always constitutes an active change to the running
firewall state, even if the rules themselves did not change. This is
intentional and correct behavior, but means this task will always report
`changed` even on repeated runs.

**Impact:** Cosmetic only — this does not cause errors or duplicate changes.
The firewall rules themselves are managed idempotently.

---

### Windows Provisioning Scripts

**Affects:** `windows/roles/*/tasks/main.yml` (tasks using `win_shell`)

Some Windows configuration tasks use PowerShell scripts that are not fully
idempotent (e.g., enabling Windows features, joining domains). These tasks
include `creates:` or `when:` guards where possible, but complex Windows
state is difficult to check without running the operation.

**Recommendation:** Test Windows playbooks in a snapshot-enabled environment
so you can roll back if a re-run produces unexpected results.

---

## Dry-Run Behavior

All playbooks support dry-run mode via `apply_changes: false` (the default).
In dry-run mode, tasks use `state: query` instead of `state: present` for
API-based modules. This means:

- No changes are made to target systems
- Query results are reported and saved as artifacts
- `changed_when: not (apply_changes | bool)` — tasks correctly report
  `ok` during dry-run and `changed` only when applying

**Note:** Not all modules support check mode (`--check` flag). For API-based
platforms (Cisco ACI, ISE, UCS, Palo Alto, etc.), use the `apply_changes`
variable rather than `--check`.

---

## `ignore_errors` Usage

Some tasks use `ignore_errors: true` or `failed_when: false`. This is
intentional for specific scenarios:

| Scenario | Why errors are ignored |
|----------|----------------------|
| Pre-flight connectivity checks | Failure means "skip this platform", not abort |
| Querying optional features | Object may not exist yet; absence is not an error |
| `aide --check` runs | AIDE exits non-zero when it finds changes (expected) |
| Firewall rule queries | Rules may not exist on a fresh system |
| Compliance artifact writes | Artifact failure should not block configuration |

If you see `ignore_errors` on a task that you believe should fail hard,
this is a candidate for review. Open an issue or submit a PR.

---

## Version Constraints

### Ansible Collections

| Platform | Collection | Minimum Version | Notes |
|----------|-----------|----------------|-------|
| Cisco ACI | `cisco.aci` | 2.8.0 | Earlier versions missing `aci_rest` fixes |
| Cisco ISE | `cisco.ise` | 2.5.12 | ISE 3.2+ API changes |
| VMware | `community.vmware` | 4.0.0 | vSphere 7.0+ support |
| Palo Alto | `paloaltonetworks.panos` | 2.17.0 | PAN-OS 10.x compatibility |
| NetApp | `netapp.ontap` | 22.8.0 | ONTAP 9.10+ support |
| Infoblox | `infoblox.nios_modules` | 1.5.0 | NIOS 8.5+ |
| Pure Storage | `purestorage.flasharray` | 1.22.0 | Purity 6.x support |

Run `ansible-galaxy collection list` to check installed versions.

### Python Packages

| Package | Minimum Version | Used By |
|---------|----------------|---------|
| `acicobra` | 6.0.4 | Cisco ACI |
| `ciscoisesdk` | 2.0.10 | Cisco ISE |
| `ucsmsdk` | 0.9.0.2 | Cisco UCS |
| `requests` | 2.28.0 | Multiple platforms |
| `pyVmomi` | 8.0.0 | VMware |
| `netapp-lib` | 2021.6.25 | NetApp |

---

## Platform-Specific Notes

### Cisco ACI
- The `aci_fabric_deploy` role (Phase 1) must complete successfully before
  running `aci_tenant_config` (Phase 2). Running out of order will produce
  errors about missing fabric objects.
- APIC multi-site configurations require additional inventory variables not
  shown in the default `inventory.example`.

### Cisco ISE
- ISE node registration (`ise_admin__nodes_register`) is not idempotent for
  nodes that have been registered and then deregistered. Manual clean-up of
  the node from ISE admin UI is required before re-registering.
- ISE 3.3 Patch 2 or later is required for some `ciscoisesdk` operations.

### VMware
- ESXi hosts must be in maintenance mode before applying STIG hardening roles.
  The `vsphere_esxi_config` role attempts to set maintenance mode automatically,
  but this requires vCenter. If managing ESXi hosts directly (`esxi_mode: esxi`),
  place the host in maintenance mode manually first.
- vSAN hardening tasks require vSAN to be enabled and configured before running.

### RHEL
- The `rhel-hardening` role makes significant security changes (PAM, SSH,
  audit rules, kernel parameters). Run against a non-production system and
  review changes with `--check --diff` before applying to production.
- FIPS mode enablement (`rhel_enable_fips: true`) requires a system reboot.
  The playbook will not automatically reboot unless `rhel_allow_reboot: true`
  is set.

### Infoblox
- Grid join operations are not idempotent. Do not re-run the
  `infoblox_grid_bootstrap` role against a grid member that is already joined.

### HashiCorp Vault
- Vault initialization (`vault_init: true`) generates unseal keys and a root
  token. These are logged to the artifacts directory. Secure and rotate them
  immediately after deployment.
- Re-running initialization against an already-initialized Vault cluster will
  fail. Use the `vault_unseal` and `vault_configure` tags for day-2 operations.

---

## What Is Not Covered

The following items are out of scope for this automation library:

- **Initial network provisioning** — physical cabling, switch configuration, and
  underlay routing are prerequisites, not outcomes, of this automation.
- **License procurement** — products must be licensed before deployment.
  The automation assumes valid licenses are in place.
- **Active Directory domain setup** — roles that integrate with AD (ISE, VAST,
  VMware) require an existing AD domain. AD provisioning is not included.
- **Certificate authority setup** — DoD PKI certificate installation requires
  an accessible CA. The automation installs certificates; it does not operate a CA.
- **Rollback automation** — failed deployments may require manual remediation.
  See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for guidance.

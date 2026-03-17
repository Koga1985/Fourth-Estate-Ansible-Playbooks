# ise_posture__conditions_rules

Creates Cisco ISE posture conditions, remediation actions, and the policy rules that combine them. Posture conditions define endpoint compliance checks (e.g., antivirus installed and up to date, disk encryption enabled, OS patch level). Remediation actions define what ISE instructs an endpoint to do when it fails a condition. This role supports DISA STIG-mandated endpoint compliance validation.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE 3.x or later with Posture licensed and enabled
- ISE admin credentials with ERS API access
- Ansible Vault for credential management

## Role Variables

### ISE Connection

| Variable | Default | Description |
|---|---|---|
| `ise_hostname` | `{{ vault_ise_hostname }}` | ISE primary PAN hostname or IP |
| `ise_username` | `{{ vault_ise_username }}` | ISE admin username |
| `ise_password` | `{{ vault_ise_password }}` | ISE admin password (vault-protected) |
| `ise_verify_ssl` | `true` | Validate ISE TLS certificate |
| `ise_use_proxy` | `false` | Route ISE API calls through a proxy |
| `ise_debug` | `false` | Enable verbose debug logging |

### Deployment Control

| Variable | Default | Description |
|---|---|---|
| `apply_changes` | `false` | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | Local directory for generated reports |

### Posture Conditions

| Variable | Default | Description |
|---|---|---|
| `posture_conditions` | (required) | List of posture condition definitions. Each entry has: `name` (required), `type` (condition type), `attribute` (attribute name to check), `value` (expected attribute value), and `operator` (comparison operator) |

### Remediation Actions

| Variable | Default | Description |
|---|---|---|
| `remediation_actions` | `[]` | List of remediation action objects to create via the ISE ERS API |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_posture__conditions_rules_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_posture__conditions_rules_log_level` | `INFO` | Log verbosity level |
| `ise_posture__conditions_rules_log_to_syslog` | `true` | Forward events to syslog |
| `ise_posture__conditions_rules_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_posture__conditions_rules_notify_on_completion` | `false` | Send email on completion |
| `ise_posture__conditions_rules_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_posture__conditions_rules_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Configure ISE posture conditions and rules
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    posture_conditions:
      - name: "Windows-Defender-Running"
        type: "LibraryCondition"
        attribute: "AntivirusInstalled"
        value: "Windows Defender"
        operator: "Contains"
      - name: "Disk-Encryption-Enabled"
        type: "LibraryCondition"
        attribute: "DiskEncryptionInstalled"
        value: "Bitlocker"
        operator: "Contains"
      - name: "OS-Patch-Level"
        type: "LibraryCondition"
        attribute: "HotFix"
        value: "KB5000000"
        operator: "Contains"
    remediation_actions:
      - name: "Link-Remediation"
        description: "Direct user to patch management portal"
        remediationLinks:
          - "https://patching.example.com"
  roles:
    - role: cisco/roles/ise_posture__conditions_rules
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `posture` | All posture-related tasks |
| `conditions` | Posture condition creation tasks |
| `remediation` | Remediation action creation tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- Posture must be licensed in ISE; conditions created here are referenced by posture policy rules in the ISE GUI or by subsequent playbook tasks.
- All credentials must be stored in Ansible Vault.

# ise_posture__conditions_rules

Creates Cisco ISE posture conditions, remediation actions, and the policy rules that combine them. Posture conditions define endpoint compliance checks (e.g., antivirus installed and up to date, disk encryption enabled, OS patch level). Remediation actions define what ISE instructs an endpoint to do when it fails a condition. This role supports DISA STIG-mandated endpoint compliance validation.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE 3.x or later with Posture licensed and enabled
- ISE admin credentials with ERS API access
- Ansible Vault for credential management

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ise_hostname` | `"{{ vault_ise_hostname }}"` | No | ISE Connection Parameters |
| `ise_username` | `"{{ vault_ise_username }}"` | No | — |
| `ise_password` | `"{{ vault_ise_password }}"` | No | — |
| `ise_verify_ssl` | `true` | No | — |
| `ise_use_proxy` | `false` | No | — |
| `ise_debug` | `false` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `ise_artifacts_dir` | `"/tmp/ise-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Configuration |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `ise_posture__conditions_rules_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_posture__conditions_rules_log_level` | `"INFO"` | No | Logging |
| `ise_posture__conditions_rules_log_to_syslog` | `true` | No | — |
| `ise_posture__conditions_rules_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_posture__conditions_rules_notify_on_completion` | `false` | No | Notification Settings |
| `ise_posture__conditions_rules_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_posture__conditions_rules_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT

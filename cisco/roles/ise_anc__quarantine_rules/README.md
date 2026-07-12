# ise_anc__quarantine_rules

Manages Cisco ISE Adaptive Network Control (ANC) quarantine policies and endpoint assignments. This role creates and enforces ANC policies that enable automated threat response — quarantining compromised endpoints, bouncing ports, or shutting down switch ports — based on security events. It also supports DISA STIG-compliant quarantine policies, endpoint exception management, SIEM integration, and generates signed audit artifacts.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- `community.general` collection
- ISE deployment reachable from the Ansible control node
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
| `anc_policies` | `(see defaults/main.yml)` | No | ANC Quarantine Policies |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance ANC Policies |
| `disa_stig_anc_policies` | `(see defaults/main.yml)` | No | — |
| `anc_endpoint_assignments` | `[]` | No | ANC Endpoint Assignments (manual quarantine assignments) |
| `anc_exceptions` | `[]` | No | ANC Exceptions (devices exempt from automatic quarantine) |
| `anc_auto_quarantine_enabled` | `true` | No | Automated Threat Response |
| `anc_auto_quarantine_threats` | `(see defaults/main.yml)` | No | — |
| `anc_siem_integration_enabled` | `true` | No | Integration with SIEM |
| `anc_siem_endpoint` | `"{{ vault_siem_endpoint }}"` | No | — |
| `anc_notify_on_quarantine` | `true` | No | Notification Settings |
| `anc_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `anc_log_level` | `"INFO"` | No | Logging |
| `anc_log_to_syslog` | `true` | No | — |
| `anc_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `anc_default_quarantine_duration` | `86400` | No | Quarantine Duration 24 hours in seconds |
| `anc_max_quarantine_duration` | `604800` | No | 7 days in seconds |
| `anc_enable_auto_remediation` | `false` | No | Remediation Settings |
| `anc_remediation_portal_url` | `"https://{{ ise_hostname }}/remediation"` | No | — |

## Example Playbook

```yaml
- name: Configure ISE ANC quarantine rules
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    anc_endpoint_assignments:
      - mac_address: "00:11:22:33:44:55"
        policy_name: "QUARANTINE"
        reason: "Malware detected by EDR"
    anc_exceptions:
      - mac_address: "AA:BB:CC:DD:EE:FF"
        reason: "Critical infrastructure - OT controller"
        approved_by: "Security Team"
        expiry_date: "2026-12-31"
        enabled: true
  roles:
    - role: cisco/roles/ise_anc__quarantine_rules
```

### Plan Mode (no changes applied)

```yaml
- name: Audit ANC quarantine policies (plan mode)
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: false
  roles:
    - role: cisco/roles/ise_anc__quarantine_rules
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `discovery` | Gather existing ANC policies |
| `anc` | All ANC policy tasks |
| `quarantine` | Quarantine-specific policy tasks |
| `compliance` | DISA STIG compliance tasks |
| `stig` | STIG-specific policy configuration |
| `exceptions` | Exception registration tasks |
| `reporting` | Report generation tasks |
| `audit` | Audit and documentation tasks |

## Notes

- `apply_changes` defaults to `false`. The role will run in read-only/plan mode unless explicitly set to `true`.
- Credentials must be stored in Ansible Vault; never commit plain-text passwords.
- The `SHUTDOWN` ANC policy is disabled by default to prevent accidental port shutdowns.
- Generated artifacts are written to `ise_artifacts_dir` and include both a plan document and a timestamped quarantine report.

## License

MIT

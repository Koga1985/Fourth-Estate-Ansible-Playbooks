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

### ISE Connection

| Variable | Default | Required | Description |
|---|---|---|
| `ise_hostname` | `{{ vault_ise_hostname }}` | **Yes** | ISE primary PAN hostname or IP |
| `ise_username` | `{{ vault_ise_username }}` | **Yes** | ISE admin username |
| `ise_password` | `{{ vault_ise_password }}` | **Yes** | ISE admin password (vault-protected) |
| `ise_verify_ssl` | `true` | No | Validate ISE TLS certificate |
| `ise_use_proxy` | `false` | No | Route ISE API calls through a proxy |
| `ise_debug` | `false` | No | Enable verbose ISE SDK debug logging |

### Deployment Control

| Variable | Default | Required | Description |
|---|---|---|
| `apply_changes` | `false` | No | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports and plan documents |

### ANC Policies

| Variable | Default | Required | Description |
|---|---|---|
| `anc_policies` | See `defaults/main.yml` | No | List of ANC policy definitions with `name`, `actions`, `description`, and `enabled` fields |
| `anc_endpoint_assignments` | `[]` | No | List of explicit endpoint-to-policy assignments (`mac_address`, `policy_name`, `reason`) |
| `anc_exceptions` | `[]` | No | List of endpoints exempt from quarantine (`mac_address`, `reason`, `approved_by`, `expiry_date`) |

### DISA STIG Compliance

| Variable | Default | Required | Description |
|---|---|---|
| `enable_disa_stig_compliance` | `true` | No | Create additional STIG-mandated ANC policies |
| `disa_stig_anc_policies` | See `defaults/main.yml` | No | STIG-specific ANC policy list |

### Automated Threat Response

| Variable | Default | Required | Description |
|---|---|---|
| `anc_auto_quarantine_enabled` | `true` | No | Enable automated quarantine on threat detection |
| `anc_auto_quarantine_threats` | `[malware_detected, posture_failed, ...]` | No | Threat categories that trigger automatic quarantine |

### Integration and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `anc_siem_integration_enabled` | `true` | No | Forward quarantine events to SIEM |
| `anc_siem_endpoint` | `{{ vault_siem_endpoint }}` | **Yes** | SIEM ingest endpoint URL |
| `anc_notify_on_quarantine` | `true` | No | Send email on quarantine action |
| `anc_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Recipient address for quarantine alerts |
| `anc_log_to_syslog` | `true` | No | Forward ANC events to syslog |
| `anc_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |

### Quarantine Duration

| Variable | Default | Required | Description |
|---|---|---|
| `anc_default_quarantine_duration` | `86400` | No | Default quarantine duration in seconds (24 h) |
| `anc_max_quarantine_duration` | `604800` | No | Maximum quarantine duration in seconds (7 days) |
| `anc_enable_auto_remediation` | `false` | No | Redirect quarantined endpoints to a remediation portal |
| `anc_remediation_portal_url` | `https://{{ ise_hostname }}/remediation` | No | Remediation portal URL |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated audit documents |

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

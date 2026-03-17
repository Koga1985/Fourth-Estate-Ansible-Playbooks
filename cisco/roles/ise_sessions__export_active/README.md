# ise_sessions__export_active

Retrieves the current active session list from Cisco ISE and exports it in both CSV and JSON formats. This role is used to capture point-in-time network access session snapshots for compliance reporting, forensic investigation, capacity planning, and integration with asset management or SIEM systems. The export is non-destructive and read-only.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE MnT API accessible from the Ansible control node
- ISE admin credentials with MnT API read access
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
| `apply_changes` | `false` | Not used for mutation in this role |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | Local directory for generated reports and exports |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_sessions__export_active_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_sessions__export_active_log_level` | `INFO` | Log verbosity level |
| `ise_sessions__export_active_log_to_syslog` | `true` | Forward events to syslog |
| `ise_sessions__export_active_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_sessions__export_active_notify_on_completion` | `false` | Send email on completion |
| `ise_sessions__export_active_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_sessions__export_active_auto_backup` | `true` | Reserved |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Export ISE active sessions
  hosts: localhost
  gather_facts: true
  roles:
    - role: cisco/roles/ise_sessions__export_active
```

### Scheduled Snapshot

```yaml
- name: Hourly ISE session snapshot
  hosts: localhost
  gather_facts: true
  vars:
    ise_artifacts_dir: "/data/ise-snapshots"
  roles:
    - role: cisco/roles/ise_sessions__export_active
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `sessions` | Active session retrieval tasks |
| `export` | Session data export tasks (CSV and JSON) |
| `reporting` | Report generation tasks |

## Output

The role produces two files for each run:

| File | Description |
|---|---|
| `{{ ise_artifacts_dir }}/active_sessions_<epoch>.csv` | CSV export of active sessions for spreadsheet analysis |
| `{{ ise_artifacts_dir }}/active_sessions_<epoch>.json` | JSON export of active sessions for programmatic processing |

## Notes

- This role is entirely read-only with respect to ISE.
- Active session data is a point-in-time snapshot; run this role on a schedule for longitudinal tracking.
- All credentials must be stored in Ansible Vault.

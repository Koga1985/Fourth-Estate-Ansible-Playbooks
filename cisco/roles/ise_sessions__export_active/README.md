# ise_sessions__export_active

Retrieves the current active session list from Cisco ISE and exports it in both CSV and JSON formats. This role is used to capture point-in-time network access session snapshots for compliance reporting, forensic investigation, capacity planning, and integration with asset management or SIEM systems. The export is non-destructive and read-only.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE MnT API accessible from the Ansible control node
- ISE admin credentials with MnT API read access
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
| `ise_sessions__export_active_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_sessions__export_active_log_level` | `"INFO"` | No | Logging |
| `ise_sessions__export_active_log_to_syslog` | `true` | No | — |
| `ise_sessions__export_active_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_sessions__export_active_notify_on_completion` | `false` | No | Notification Settings |
| `ise_sessions__export_active_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_sessions__export_active_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT

# ise_posture__updates_channel

Manages the Cisco ISE posture update feed configuration, controlling how and when ISE retrieves updated posture check definitions (antivirus signatures, OS patches, compliance check databases) from Cisco's cloud update server or an internal update proxy. This role can configure the update schedule and optionally trigger an immediate update check.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE 3.x or later with Posture licensed and enabled
- ISE admin credentials with ERS API access
- ISE must have network connectivity to the Cisco update servers (or an internal proxy configured)
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
| `ise_posture__updates_channel_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_posture__updates_channel_log_level` | `"INFO"` | No | Logging |
| `ise_posture__updates_channel_log_to_syslog` | `true` | No | — |
| `ise_posture__updates_channel_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_posture__updates_channel_notify_on_completion` | `false` | No | Notification Settings |
| `ise_posture__updates_channel_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_posture__updates_channel_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Configure ISE posture update feed
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    posture_updates_enabled: true
    posture_update_schedule:
      intervalDays: 1
      time: "02:00"
    posture_force_update: false
  roles:
    - role: cisco/roles/ise_posture__updates_channel
```

### Force Immediate Update

```yaml
- name: Trigger immediate posture update check
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    posture_updates_enabled: true
    posture_update_schedule:
      intervalDays: 7
      time: "03:00"
    posture_force_update: true
  roles:
    - role: cisco/roles/ise_posture__updates_channel
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `posture` | All posture-related tasks |
| `updates` | Posture update feed configuration and trigger tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- `posture_force_update: true` triggers an on-demand update; this may temporarily increase CPU load on the ISE node.
- Posture must be licensed in ISE for update feed management to be available.
- All credentials must be stored in Ansible Vault.

## License

MIT

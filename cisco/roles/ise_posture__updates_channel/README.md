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

### ISE Connection

| Variable | Default | Required | Description |
|---|---|---|
| `ise_hostname` | `{{ vault_ise_hostname }}` | **Yes** | ISE primary PAN hostname or IP |
| `ise_username` | `{{ vault_ise_username }}` | **Yes** | ISE admin username |
| `ise_password` | `{{ vault_ise_password }}` | **Yes** | ISE admin password (vault-protected) |
| `ise_verify_ssl` | `true` | No | Validate ISE TLS certificate |
| `ise_use_proxy` | `false` | No | Route ISE API calls through a proxy |
| `ise_debug` | `false` | No | Enable verbose debug logging |

### Deployment Control

| Variable | Default | Required | Description |
|---|---|---|
| `apply_changes` | `false` | No | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### Posture Update Feed

| Variable | Default | Required | Description |
|---|---|---|
| `posture_updates_enabled` | (required) | No | Enable the posture update feed |
| `posture_update_schedule` | (required) | No | Update schedule configuration object passed to the ISE posture update feed API |
| `posture_force_update` | `false` | No | Trigger an immediate update check in addition to configuring the schedule (requires `apply_changes: true`) |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_posture__updates_channel_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_posture__updates_channel_log_level` | `INFO` | No | Log verbosity level |
| `ise_posture__updates_channel_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_posture__updates_channel_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_posture__updates_channel_notify_on_completion` | `false` | No | Send email on completion |
| `ise_posture__updates_channel_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_posture__updates_channel_auto_backup` | `true` | No | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

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

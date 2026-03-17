# ise_integration__mse_dnac

Integrates Cisco ISE with Cisco DNA Center (DNAC) and Mobility Services Engine (MSE) via pxGrid and REST APIs. This role enables ISE to share session and context information with DNA Center for SD-Access policy enforcement and with MSE for location-aware access control. Both integrations are independently toggleable and default to plan mode.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access and pxGrid enabled
- DNA Center API access (when `dnac_integration_enabled: true`)
- MSE API access (when `mse_integration_enabled: true`)
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

### pxGrid Settings

| Variable | Default | Description |
|---|---|---|
| `pxgrid_auto_approval` | (required) | Whether new pxGrid client registrations are automatically approved |

### DNA Center Integration

| Variable | Default | Description |
|---|---|---|
| `dnac_integration_enabled` | (required) | Enable DNA Center integration tasks |
| `dnac_hostname` | (required when enabled) | DNA Center hostname or IP |
| `dnac_auth_token` | (required when enabled) | DNA Center API authentication token |
| `dnac_ise_shared_secret` | (required when enabled) | Shared secret for the ISE-DNAC integration |

### MSE Integration

| Variable | Default | Description |
|---|---|---|
| `mse_integration_enabled` | (required) | Enable MSE integration tasks |
| `mse_hostname` | (required when enabled) | MSE hostname or IP |
| `mse_username` | (required when enabled) | MSE admin username |
| `mse_password` | (required when enabled) | MSE admin password (vault-protected) |
| `mse_verify_ssl` | `true` | Validate MSE TLS certificate |
| `mse_ise_shared_secret` | (required when enabled) | Shared secret for the ISE-MSE integration |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_integration__mse_dnac_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_integration__mse_dnac_log_level` | `INFO` | Log verbosity level |
| `ise_integration__mse_dnac_log_to_syslog` | `true` | Forward events to syslog |
| `ise_integration__mse_dnac_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_integration__mse_dnac_notify_on_completion` | `false` | Send email on completion |
| `ise_integration__mse_dnac_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_integration__mse_dnac_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Integrate ISE with DNA Center and MSE
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    pxgrid_auto_approval: false
    dnac_integration_enabled: true
    dnac_hostname: "dnac.example.com"
    dnac_auth_token: "{{ vault_dnac_token }}"
    dnac_ise_shared_secret: "{{ vault_dnac_ise_secret }}"
    mse_integration_enabled: false
  roles:
    - role: cisco/roles/ise_integration__mse_dnac
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `pxgrid` | pxGrid enablement tasks |
| `integration` | All integration tasks |
| `dnac` | DNA Center integration tasks |
| `mse` | MSE integration tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- DNA Center and MSE integrations are independently controlled via their respective `_enabled` flags.
- All secrets (shared secrets, API tokens, passwords) must be stored in Ansible Vault.

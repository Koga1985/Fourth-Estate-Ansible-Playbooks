# ise_posture__client_provisioning

Configures Cisco ISE native supplicant profiles used for client provisioning in posture assessment workflows. Native supplicant profiles define wireless network configurations (SSID, security type, certificate) that ISE pushes to endpoints during the onboarding process, enabling automatic supplicant configuration for corporate and BYOD devices. This role supports DISA STIG-compliant posture deployment.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE 3.x or later with Posture and Client Provisioning licensed
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
| `ise_debug` | `false` | No | Enable verbose debug logging |

### Deployment Control

| Variable | Default | Required | Description |
|---|---|---|
| `apply_changes` | `false` | No | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### Client Provisioning Profiles

| Variable | Default | Required | Description |
|---|---|---|
| `client_provisioning_profiles` | (required) | No | List of native supplicant profile definitions. Each entry has: `name` (required), optional `description`, and `wireless_profiles` (list of wireless profile configurations with SSID, security, and certificate details) |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_posture__client_provisioning_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_posture__client_provisioning_log_level` | `INFO` | No | Log verbosity level |
| `ise_posture__client_provisioning_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_posture__client_provisioning_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_posture__client_provisioning_notify_on_completion` | `false` | No | Send email on completion |
| `ise_posture__client_provisioning_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_posture__client_provisioning_auto_backup` | `true` | No | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Configure ISE client provisioning profiles
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    client_provisioning_profiles:
      - name: "Corp-WiFi-Supplicant"
        description: "Corporate 802.1X wireless supplicant profile"
        wireless_profiles:
          - ssid: "CORP-WIFI"
            allowedProtocol: "TLS"
            certificateTemplate: "BYOD-Certificate-Template"
      - name: "Guest-WiFi-Supplicant"
        description: "Guest open wireless supplicant profile"
        wireless_profiles:
          - ssid: "GUEST-WIFI"
            allowedProtocol: "PEAP_MSCHAPV2"
  roles:
    - role: cisco/roles/ise_posture__client_provisioning
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `posture` | All posture-related tasks |
| `provisioning` | Client provisioning profile creation tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- Posture and Client Provisioning must be licensed and enabled in ISE.
- Certificate templates referenced in wireless profiles must already exist in ISE.
- All credentials must be stored in Ansible Vault.

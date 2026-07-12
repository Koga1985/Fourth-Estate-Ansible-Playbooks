# ise_posture__client_provisioning

Configures Cisco ISE native supplicant profiles used for client provisioning in posture assessment workflows. Native supplicant profiles define wireless network configurations (SSID, security type, certificate) that ISE pushes to endpoints during the onboarding process, enabling automatic supplicant configuration for corporate and BYOD devices. This role supports DISA STIG-compliant posture deployment.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE 3.x or later with Posture and Client Provisioning licensed
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
| `ise_posture__client_provisioning_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_posture__client_provisioning_log_level` | `"INFO"` | No | Logging |
| `ise_posture__client_provisioning_log_to_syslog` | `true` | No | — |
| `ise_posture__client_provisioning_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_posture__client_provisioning_notify_on_completion` | `false` | No | Notification Settings |
| `ise_posture__client_provisioning_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_posture__client_provisioning_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT

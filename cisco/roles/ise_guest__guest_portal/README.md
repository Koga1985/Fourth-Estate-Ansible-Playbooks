# ise_guest__guest_portal

Configures the Cisco ISE guest self-registration and hotspot portal settings. This role provisions the guest portal with certificate bindings, endpoint identity group assignments, acceptable use policy (AUP) enforcement, device self-registration permissions, and optional portal branding customization. It supports compliance-aware deployments under DISA STIG and NIST frameworks.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE 3.x or later with Guest Services licensed and enabled
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
| `ise_guest__guest_portal_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_guest__guest_portal_log_level` | `"INFO"` | No | Logging |
| `ise_guest__guest_portal_log_to_syslog` | `true` | No | — |
| `ise_guest__guest_portal_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_guest__guest_portal_notify_on_completion` | `false` | No | Notification Settings |
| `ise_guest__guest_portal_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_guest__guest_portal_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Configure ISE guest portal
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    guest_portal_name: "Guest-Self-Registration"
    guest_portal_cert_group: "Default Portal Certificate Group"
    guest_endpoint_group: "GuestEndpoints"
    guest_allow_password_change: true
    guest_allow_device_registration: true
    guest_require_aup: true
    guest_portal_customization_enabled: true
    guest_portal_id: "portal-uuid-here"
    guest_portal_banner_title: "Welcome to Guest Wi-Fi"
    guest_portal_bg_color: "#FFFFFF"
  roles:
    - role: cisco/roles/ise_guest__guest_portal
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `guest` | All guest service tasks |
| `portal` | Portal configuration tasks |
| `branding` | Portal branding customization tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- Portal branding tasks are gated by both `apply_changes` and `guest_portal_customization_enabled`.
- All credentials must be stored in Ansible Vault.

## License

MIT

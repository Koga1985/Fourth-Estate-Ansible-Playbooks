# ise_guest__guest_portal

Configures the Cisco ISE guest self-registration and hotspot portal settings. This role provisions the guest portal with certificate bindings, endpoint identity group assignments, acceptable use policy (AUP) enforcement, device self-registration permissions, and optional portal branding customization. It supports compliance-aware deployments under DISA STIG and NIST frameworks.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE 3.x or later with Guest Services licensed and enabled
- ISE admin credentials with ERS API access
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

### Portal Configuration

| Variable | Default | Description |
|---|---|---|
| `guest_portal_name` | (required) | Name for the guest portal |
| `guest_portal_cert_group` | (required) | Certificate group tag for portal TLS |
| `guest_endpoint_group` | (required) | Endpoint identity group for guest devices |
| `guest_portal_language` | `ENGLISH` | Display language for the portal |
| `guest_allow_password_change` | (required) | Allow guests to change password at first login |
| `guest_allow_device_registration` | (required) | Allow guests to register additional devices |
| `guest_require_aup` | (required) | Require guests to accept an AUP |

### Portal Branding

| Variable | Default | Description |
|---|---|---|
| `guest_portal_customization_enabled` | `false` | Enable portal branding customization |
| `guest_portal_id` | (required when branding enabled) | UUID of the portal to customize |
| `guest_portal_banner_title` | (required when branding enabled) | Banner text displayed at the top of the portal |
| `guest_portal_banner_image` | (optional) | Base64-encoded banner image |
| `guest_portal_bg_color` | (required when branding enabled) | Portal background color (hex) |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_guest__guest_portal_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_guest__guest_portal_log_level` | `INFO` | Log verbosity level |
| `ise_guest__guest_portal_log_to_syslog` | `true` | Forward events to syslog |
| `ise_guest__guest_portal_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_guest__guest_portal_notify_on_completion` | `false` | Send email on completion |
| `ise_guest__guest_portal_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_guest__guest_portal_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

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

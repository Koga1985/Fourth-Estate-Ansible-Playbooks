# ise_guest__sponsor_portal

Configures the Cisco ISE sponsor portal and sponsor groups. The sponsor portal allows authorized internal users (sponsors) to create, manage, and approve guest accounts on behalf of visiting guests. This role provisions the portal settings, certificate bindings, password-change permissions, and the sponsor groups that define which guest types and locations a sponsor can manage.

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

### Sponsor Portal Configuration

| Variable | Default | Description |
|---|---|---|
| `sponsor_portal_name` | (required) | Name for the sponsor portal |
| `sponsor_portal_cert_group` | (required) | Certificate group tag for portal TLS |
| `sponsor_portal_language` | `ENGLISH` | Display language for the portal |
| `sponsor_allow_password_change` | (required) | Allow sponsors to change their own portal password |

### Sponsor Groups

| Variable | Default | Description |
|---|---|---|
| `sponsor_groups` | `[]` | List of sponsor group definitions; each entry has `name`, `is_default`, `guest_types` (list), and optional `locations` |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_guest__sponsor_portal_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_guest__sponsor_portal_log_level` | `INFO` | Log verbosity level |
| `ise_guest__sponsor_portal_log_to_syslog` | `true` | Forward events to syslog |
| `ise_guest__sponsor_portal_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_guest__sponsor_portal_notify_on_completion` | `false` | Send email on completion |
| `ise_guest__sponsor_portal_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_guest__sponsor_portal_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Configure ISE sponsor portal
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    sponsor_portal_name: "Sponsor-Portal"
    sponsor_portal_cert_group: "Default Portal Certificate Group"
    sponsor_allow_password_change: true
    sponsor_groups:
      - name: "ALL_ACCOUNTS"
        is_default: true
        guest_types:
          - "Contractor"
          - "Daily"
          - "Weekly"
        locations:
          - "San Jose"
          - "Washington DC"
      - name: "LIMITED_SPONSORS"
        is_default: false
        guest_types:
          - "Daily"
  roles:
    - role: cisco/roles/ise_guest__sponsor_portal
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `guest` | All guest service tasks |
| `sponsor` | Sponsor-specific tasks |
| `portal` | Sponsor portal configuration tasks |
| `groups` | Sponsor group configuration tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- Sponsor groups reference guest types by name; those guest types must already exist in ISE.
- All credentials must be stored in Ansible Vault.

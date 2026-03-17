# ise_pxgrid__enable_clients

Enables the Cisco ISE pxGrid service and approves registered pxGrid client nodes. pxGrid is Cisco's platform exchange grid that allows ISE to share context (session data, endpoint attributes, security group tags, threat events) with integrated security products such as Cisco Stealthwatch, DNA Center, Firepower, and third-party SIEM or SOAR platforms. This role configures the global pxGrid settings and activates approved client registrations.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE 3.x or later with pxGrid licensed and enabled
- ISE admin credentials with ERS API access and pxGrid administration permissions
- pxGrid client applications must already have registered (generated a certificate request) before this role approves them
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
| `pxgrid_auto_approval` | (required) | When `true`, new pxGrid client registrations are automatically approved without manual ISE admin action |

### pxGrid Clients

| Variable | Default | Description |
|---|---|---|
| `pxgrid_clients` | (required) | List of pxGrid client objects to approve. Each entry has `name` — the pxGrid node name as registered in ISE |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_pxgrid__enable_clients_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_pxgrid__enable_clients_log_level` | `INFO` | Log verbosity level |
| `ise_pxgrid__enable_clients_log_to_syslog` | `true` | Forward events to syslog |
| `ise_pxgrid__enable_clients_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_pxgrid__enable_clients_notify_on_completion` | `false` | Send email on completion |
| `ise_pxgrid__enable_clients_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_pxgrid__enable_clients_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Enable ISE pxGrid and approve clients
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    pxgrid_auto_approval: false
    pxgrid_clients:
      - name: "stealthwatch.example.com"
      - name: "dnac-pxgrid-client"
      - name: "splunk-ise-integration"
  roles:
    - role: cisco/roles/ise_pxgrid__enable_clients
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `pxgrid` | pxGrid service configuration tasks |
| `clients` | pxGrid client approval tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- Setting `pxgrid_auto_approval: true` reduces operational friction but may violate DISA STIG requirements; prefer explicit approval via the `pxgrid_clients` list.
- pxGrid clients must complete their certificate-based registration in ISE before they can be approved by this role.
- All credentials must be stored in Ansible Vault.

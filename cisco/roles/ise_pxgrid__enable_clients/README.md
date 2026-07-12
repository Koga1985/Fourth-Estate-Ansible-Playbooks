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
| `ise_pxgrid__enable_clients_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_pxgrid__enable_clients_log_level` | `"INFO"` | No | Logging |
| `ise_pxgrid__enable_clients_log_to_syslog` | `true` | No | — |
| `ise_pxgrid__enable_clients_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_pxgrid__enable_clients_notify_on_completion` | `false` | No | Notification Settings |
| `ise_pxgrid__enable_clients_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_pxgrid__enable_clients_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT

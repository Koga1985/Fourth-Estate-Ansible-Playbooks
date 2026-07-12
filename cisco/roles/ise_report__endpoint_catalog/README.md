# ise_report__endpoint_catalog

Retrieves the complete Cisco ISE endpoint inventory and generates a catalog report. This role enumerates all registered endpoints, analyzes the inventory by profiling category and identity group membership, and produces a timestamped JSON report. It is used for asset management, compliance auditing, and capacity planning.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API read access
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
| `ise_report__endpoint_catalog_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_report__endpoint_catalog_log_level` | `"INFO"` | No | Logging |
| `ise_report__endpoint_catalog_log_to_syslog` | `true` | No | — |
| `ise_report__endpoint_catalog_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_report__endpoint_catalog_notify_on_completion` | `false` | No | Notification Settings |
| `ise_report__endpoint_catalog_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_report__endpoint_catalog_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Generate ISE endpoint catalog report
  hosts: localhost
  gather_facts: true
  roles:
    - role: cisco/roles/ise_report__endpoint_catalog
```

### With Email Notification

```yaml
- name: Generate and email ISE endpoint catalog
  hosts: localhost
  gather_facts: true
  vars:
    ise_report__endpoint_catalog_notify_on_completion: true
  roles:
    - role: cisco/roles/ise_report__endpoint_catalog
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `discovery` | Endpoint inventory retrieval tasks |
| `endpoints` | Endpoint data processing tasks |
| `analysis` | Inventory analysis and grouping tasks |
| `reporting` | Report generation tasks |

## Output

The role produces a JSON report at:

```
{{ ise_artifacts_dir }}/endpoint_catalog_<epoch>.json
```

The report includes:
- Total endpoint count
- Endpoints grouped by profiling policy (profile ID)
- Endpoints grouped by identity group (group ID)

## Notes

- This role is entirely read-only with respect to ISE.
- For large deployments with tens of thousands of endpoints, API pagination may be required; review ISE ERS API pagination behavior for your ISE version.
- All credentials must be stored in Ansible Vault.

## License

MIT

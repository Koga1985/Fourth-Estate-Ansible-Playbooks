# servicenow_cmdb_config

Servicenow Cmdb Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `servicenow/README.md`

## Requirements

- Ansible 2.15+
- Collection: `servicenow.itsm`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `servicenow_instance` | `"{{ lookup('env', 'SN_INSTANCE') }}"` | No | ServiceNow instance connection |
| `servicenow_username` | `"{{ lookup('env', 'SN_USERNAME') }}"` | No | — |
| `servicenow_password` | `"{{ lookup('env', 'SN_PASSWORD') }}"` | No | — |
| `servicenow_client_id` | `"{{ lookup('env', 'SN_CLIENT_ID') \| default('') }}"` | No | — |
| `servicenow_client_secret` | `"{{ lookup('env', 'SN_CLIENT_SECRET') \| default('') }}"` | No | — |
| `servicenow_timeout` | `30` | No | — |
| `servicenow_validate_certs` | `true` | No | — |
| `cmdb_config_mode` | `"configure"` | No | CMDB Configuration configure, validate, report |
| `cmdb_ci_classes` | `(see defaults/main.yml)` | No | CI Class Configuration |
| `cmdb_relationship_types` | `(see defaults/main.yml)` | No | Relationship Types |
| `cmdb_reconciliation_rules` | `(see defaults/main.yml)` | No | Reconciliation Rules |
| `cmdb_identification_rules` | `(see defaults/main.yml)` | No | Identification Rules |
| `cmdb_data_sources` | `(see defaults/main.yml)` | No | Data Sources Configuration |
| `cmdb_health_checks` | `(see defaults/main.yml)` | No | CMDB Health Configuration |
| `cmdb_metrics_enabled` | `true` | No | CMDB Metrics |
| `cmdb_metrics_collection` | `(see defaults/main.yml)` | No | — |
| `fourth_estate_config` | `(see defaults/main.yml)` | No | Fourth Estate Specific Configuration |
| `cmdb_audit_enabled` | `true` | No | Audit Configuration |
| `cmdb_audit_tables` | `(see defaults/main.yml)` | No | — |
| `cmdb_notifications` | `(see defaults/main.yml)` | No | Notification Settings |

## Example Playbook

```yaml
---
- name: Servicenow Cmdb Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: servicenow/roles/servicenow_cmdb_config
```

## License

MIT

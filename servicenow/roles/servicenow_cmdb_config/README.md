# servicenow_cmdb_config

Servicenow Cmdb Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `servicenow/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `servicenow_instance` | `"{{ lookup('env', 'SN_INSTANCE') }}"` |  |
| `servicenow_username` | `"{{ lookup('env', 'SN_USERNAME') }}"` |  |
| `servicenow_password` | `"{{ lookup('env', 'SN_PASSWORD') }}"` |  |
| `servicenow_client_id` | `"{{ lookup('env', 'SN_CLIENT_ID') | No | default('')...` |
| `servicenow_client_secret` | `"{{ lookup('env', 'SN_CLIENT_SECRET') | No | default...` |
| `servicenow_timeout` | `30` |  |
| `servicenow_validate_certs` | `true` |  |
| `cmdb_config_mode` | `"configure"` | No | configure, validate, report |
| `cmdb_metrics_enabled` | `true` |  |
| `cmdb_audit_enabled` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `servicenow.itsm`
- See platform `requirements.yml` for install instructions

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

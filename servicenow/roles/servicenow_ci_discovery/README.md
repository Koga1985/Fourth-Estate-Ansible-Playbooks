# servicenow_ci_discovery

Servicenow Ci Discovery role for Fourth Estate infrastructure automation.

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
| `servicenow_timeout` | `60` | No | — |
| `servicenow_validate_certs` | `true` | No | — |
| `ci_discovery_mode` | `"discover"` | No | Discovery Mode discover, schedule, validate, report |
| `ci_discovery_schedules` | `(see defaults/main.yml)` | No | Discovery Schedules |
| `aws_discovery` | `(see defaults/main.yml)` | No | AWS Discovery Configuration |
| `azure_discovery` | `(see defaults/main.yml)` | No | Azure Discovery Configuration |
| `vmware_discovery` | `(see defaults/main.yml)` | No | VMware Discovery Configuration |
| `physical_discovery` | `(see defaults/main.yml)` | No | Physical Server Discovery Configuration |
| `network_discovery` | `(see defaults/main.yml)` | No | Network Device Discovery Configuration |
| `kubernetes_discovery` | `(see defaults/main.yml)` | No | Kubernetes Discovery Configuration |
| `discovery_patterns` | `(see defaults/main.yml)` | No | Discovery Patterns |
| `service_mapping` | `(see defaults/main.yml)` | No | Service Mapping Configuration |
| `discovery_credentials` | `(see defaults/main.yml)` | No | Credential Management |
| `fourth_estate_discovery` | `(see defaults/main.yml)` | No | Fourth Estate Specific Discovery |
| `discovery_results` | `(see defaults/main.yml)` | No | Discovery Results Processing |
| `discovery_performance` | `(see defaults/main.yml)` | No | Performance Settings |
| `discovery_notifications` | `(see defaults/main.yml)` | No | Notification Settings |

## Example Playbook

```yaml
---
- name: Servicenow Ci Discovery
  hosts: localhost
  gather_facts: false
  roles:
    - role: servicenow/roles/servicenow_ci_discovery
```

## License

MIT

# aws_route_tables

Aws Route Tables role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `route_table_state` | `"present"` | No | Route Table Configuration |
| `route_table_public_name` | `"{{ vpc_name \| default('main') }}-public-rt"` | No | — |
| `route_table_vpn_name` | `"{{ vpc_name \| default('main') }}-vpn-rt"` | No | — |
| `create_public_route_table` | `true` | No | Feature flags |
| `create_private_route_tables` | `true` | No | — |
| `create_vpn_route_table` | `false` | No | — |
| `enable_transit_gateway` | `false` | No | — |
| `enable_route_propagation` | `false` | No | — |
| `route_table_tags` | `(see defaults/main.yml)` | No | Default tags |
| `route_tables` | `[]` | No | Route tables configuration (override in inventory/playbook) |
| `private_route_tables` | `[]` | No | Private route tables per AZ (override in inventory/playbook) |
| `vpn_routes` | `[]` | No | VPN routes (override in inventory/playbook) |
| `transit_gateway_routes` | `[]` | No | Transit Gateway routes (override in inventory/playbook) |
| `route_tables_with_propagation` | `[]` | No | Route tables with VPN propagation |

## Example Playbook

```yaml
---
- name: Aws Route Tables
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_route_tables
```

## License

MIT

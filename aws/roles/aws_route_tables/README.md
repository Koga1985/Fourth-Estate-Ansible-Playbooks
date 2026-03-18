# aws_route_tables

Aws Route Tables role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `route_table_state` | `"present"` |  |
| `route_table_public_name` | `"{{ vpc_name | No | default('main') }}-public-rt"` |
| `route_table_vpn_name` | `"{{ vpc_name | No | default('main') }}-vpn-rt"` |
| `create_public_route_table` | `true` |  |
| `create_private_route_tables` | `true` |  |
| `create_vpn_route_table` | `false` |  |
| `enable_transit_gateway` | `false` |  |
| `enable_route_propagation` | `false` |  |
| `route_tables` | `[]` |  |
| `private_route_tables` | `[]` |  |
| `vpn_routes` | `[]` |  |
| `transit_gateway_routes` | `[]` |  |
| `route_tables_with_propagation` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

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

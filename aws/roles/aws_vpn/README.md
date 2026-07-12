# aws_vpn

Aws Vpn role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vpn_state` | `"present"` | No | VPN Configuration |
| `vpn_gateway_name` | `"{{ vpc_name \| default('main') }}-vgw"` | No | — |
| `vpn_gateway_type` | `"ipsec.1"` | No | — |
| `vpn_gateway_asn` | `64512` | No | — |
| `create_vpn_gateway` | `true` | No | Feature flags |
| `vpn_enable_fedramp_encryption` | `true` | No | — |
| `vpn_enable_monitoring` | `true` | No | — |
| `vpn_enable_logging` | `true` | No | — |
| `vpn_save_config` | `true` | No | — |
| `vpn_log_retention_days` | `90` | No | Logging configuration |
| `vpn_tags` | `(see defaults/main.yml)` | No | Default tags |
| `customer_gateways` | `[]` | No | Customer Gateways (override in inventory/playbook) |
| `vpn_connections` | `[]` | No | VPN Connections (override in inventory/playbook) |
| `vpn_alarm_sns_topic` | `""` | No | CloudWatch Monitoring |
| `vpn_fedramp_encryption` | `(see defaults/main.yml)` | No | FedRAMP compliant encryption settings (applied automatically) |

## Example Playbook

```yaml
---
- name: Aws Vpn
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_vpn
```

## License

MIT

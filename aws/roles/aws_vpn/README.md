# aws_vpn

Aws Vpn role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vpn_state` | `"present"` |  |
| `vpn_gateway_name` | `"{{ vpc_name | No | default('main') }}-vgw"` |
| `vpn_gateway_type` | `"ipsec.1"` |  |
| `vpn_gateway_asn` | `64512` |  |
| `create_vpn_gateway` | `true` |  |
| `vpn_enable_fedramp_encryption` | `true` |  |
| `vpn_enable_monitoring` | `true` |  |
| `vpn_enable_logging` | `true` |  |
| `vpn_save_config` | `true` |  |
| `vpn_log_retention_days` | `90` |  |
| `customer_gateways` | `[]` |  |
| `vpn_connections` | `[]` |  |
| `vpn_alarm_sns_topic` | `""` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

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

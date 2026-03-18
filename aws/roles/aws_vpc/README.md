# aws_vpc

Aws Vpc role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vpc_name` | `"ansible-managed-vpc"` |  |
| `vpc_cidr` | `"10.0.0.0/16"` |  |
| `vpc_region` | `"{{ aws_region | No | default('us-east-1') }}"` |
| `vpc_enable_dns_support` | `true` |  |
| `vpc_enable_dns_hostnames` | `true` |  |
| `vpc_enable_ipv6` | `false` |  |
| `vpc_instance_tenancy` | `"default"` | No | default, dedicated |
| `vpc_dhcp_options_domain_name` | `""` |  |
| `vpc_dhcp_options_domain_name_servers` | `["AmazonProvidedDNS"]` |  |
| `vpc_enable_flow_logs` | `false` |  |
| `vpc_flow_logs_destination_type` | `"cloud-watch-logs"` | No | cloud-watch-logs, s3 |
| `vpc_flow_logs_log_group_name` | `"/aws/vpc/{{ vpc_name }}"` |  |
| `vpc_flow_logs_traffic_type` | `"ALL"` | No | ALL, ACCEPT, REJECT |
| `vpc_state` | `"present"` | No | present, absent |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Aws Vpc
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_vpc
```

## License

MIT

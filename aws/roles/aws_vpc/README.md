# aws_vpc

Aws Vpc role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vpc_name` | `"ansible-managed-vpc"` | No | VPC Configuration |
| `vpc_cidr` | `"10.0.0.0/16"` | No | — |
| `vpc_region` | `"{{ aws_region \| default('us-east-1') }}"` | No | — |
| `vpc_enable_dns_support` | `true` | No | DNS Settings |
| `vpc_enable_dns_hostnames` | `true` | No | — |
| `vpc_enable_ipv6` | `false` | No | IPv6 Support |
| `vpc_instance_tenancy` | `"default"` | No | Tenancy default, dedicated |
| `vpc_tags` | `(see defaults/main.yml)` | No | Resource Tags |
| `vpc_dhcp_options_domain_name` | `""` | No | DHCP Options |
| `vpc_dhcp_options_domain_name_servers` | `["AmazonProvidedDNS"]` | No | — |
| `vpc_enable_flow_logs` | `false` | No | VPC Flow Logs |
| `vpc_flow_logs_destination_type` | `"cloud-watch-logs"` | No | cloud-watch-logs, s3 |
| `vpc_flow_logs_log_group_name` | `"/aws/vpc/{{ vpc_name }}"` | No | — |
| `vpc_flow_logs_traffic_type` | `"ALL"` | No | ALL, ACCEPT, REJECT |
| `vpc_state` | `"present"` | No | State management present, absent |

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

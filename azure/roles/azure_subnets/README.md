# azure_subnets

Azure Subnets role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `azure_cloud_environment` | `"AzureUSGovernment"` |  |
| `azure_region` | `"usgovvirginia"` |  |
| `azure_resource_group` | `"rg-network-prod-usgovva"` |  |
| `azure_vnet_name` | `""` | Parent VNet name (required) |
| `azure_subnets` | `[]` |  |
| `azure_subnet_enable_private_endpoints` | `true` |  |
| `azure_subnet_private_endpoint_network_policies` | `"Disabled"` |  |
| `azure_subnet_enable_network_policies` | `true` |  |
| `azure_subnet_enable_diagnostics` | `true` |  |
| `azure_log_analytics_workspace_id` | `""` |  |
| `azure_subnet_display_summary` | `true` |  |
| `azure_environment` | `"Production"` |  |
| `azure_cost_center` | `"4thEstate-Network"` |  |
| `azure_classification` | `"SECRET"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Azure Subnets
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_subnets
```

## License

MIT

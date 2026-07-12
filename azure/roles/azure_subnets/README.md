# azure_subnets

Azure Subnets role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `azure_cloud_environment` | `"AzureUSGovernment"` | No | Azure Cloud Environment |
| `azure_region` | `"usgovvirginia"` | No | — |
| `azure_resource_group` | `"rg-network-prod-usgovva"` | No | Resource Group |
| `azure_vnet_name` | `""` | No | Virtual Network Parent VNet name (required) |
| `azure_subnets` | `[]` | No | Subnets Configuration |
| `azure_subnet_default_service_endpoints` | `(see defaults/main.yml)` | No | Service Endpoints (FedRAMP compliance) |
| `azure_subnet_enable_private_endpoints` | `true` | No | Private Endpoint Configuration |
| `azure_subnet_private_endpoint_network_policies` | `"Disabled"` | No | — |
| `azure_subnet_enable_network_policies` | `true` | No | Network Policies |
| `azure_subnet_enable_diagnostics` | `true` | No | Diagnostic Settings |
| `azure_log_analytics_workspace_id` | `""` | No | — |
| `azure_subnet_display_summary` | `true` | No | Operational Settings |
| `azure_environment` | `"Production"` | No | Cost Management |
| `azure_cost_center` | `"4thEstate-Network"` | No | — |
| `azure_classification` | `"SECRET"` | No | — |
| `azure_resource_tags` | `(see defaults/main.yml)` | No | Resource Tags |

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

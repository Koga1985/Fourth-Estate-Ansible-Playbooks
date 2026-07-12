# azure_vnet

Azure Vnet role for Fourth Estate infrastructure automation.

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
| `azure_subscription_id` | `"{{ lookup('env', 'AZURE_SUBSCRIPTION_ID') }}"` | No | — |
| `azure_resource_group` | `"rg-network-prod-usgovva"` | No | Resource Group |
| `azure_vnets` | `[]` | No | Virtual Networks Configuration |
| `azure_vnet_name` | `""` | No | Single VNet Mode (alternative to list) |
| `azure_vnet_address_prefixes` | `[]` | No | — |
| `azure_vnet_enable_ddos_protection` | `true` | No | DDoS Protection |
| `azure_ddos_plan_name` | `"ddos-plan-prod-usgovva"` | No | — |
| `azure_vnet_configure_peering` | `false` | No | VNet Peering |
| `azure_vnet_enable_flow_logs` | `true` | No | Flow Logs |
| `azure_flow_logs_storage_account_id` | `""` | No | — |
| `azure_flow_logs_retention_days` | `90` | No | — |
| `azure_network_watcher_rg` | `"NetworkWatcherRG"` | No | — |
| `azure_vnet_enable_diagnostics` | `true` | No | Diagnostic Settings |
| `azure_log_analytics_workspace_id` | `""` | No | — |
| `azure_log_analytics_workspace_resource_id` | `""` | No | — |
| `azure_vnet_display_summary` | `true` | No | Operational Settings |
| `azure_environment` | `"Production"` | No | Cost Management |
| `azure_cost_center` | `"4thEstate-Network"` | No | — |
| `azure_classification` | `"SECRET"` | No | — |
| `azure_resource_tags` | `(see defaults/main.yml)` | No | Resource Tags |

## Example Playbook

```yaml
---
- name: Azure Vnet
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_vnet
```

## License

MIT

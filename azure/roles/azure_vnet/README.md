# azure_vnet

Azure Vnet role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `azure_cloud_environment` | `"AzureUSGovernment"` |  |
| `azure_region` | `"usgovvirginia"` |  |
| `azure_subscription_id` | `"{{ lookup('env', 'AZURE_SUBSCRIPTION_ID') }}"` |  |
| `azure_resource_group` | `"rg-network-prod-usgovva"` |  |
| `azure_vnets` | `[]` |  |
| `azure_vnet_name` | `""` |  |
| `azure_vnet_address_prefixes` | `[]` |  |
| `azure_vnet_enable_ddos_protection` | `true` |  |
| `azure_ddos_plan_name` | `"ddos-plan-prod-usgovva"` |  |
| `azure_vnet_configure_peering` | `false` |  |
| `azure_vnet_enable_flow_logs` | `true` |  |
| `azure_flow_logs_storage_account_id` | `""` |  |
| `azure_flow_logs_retention_days` | `90` |  |
| `azure_network_watcher_rg` | `"NetworkWatcherRG"` |  |
| `azure_vnet_enable_diagnostics` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

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

# azure_sovereign_cloud

Azure Sovereign Cloud management for FedRAMP High environments

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection` (`ansible-galaxy collection install azure.azcollection`)
- Collection: `community.general` (`ansible-galaxy collection install community.general`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `azure_cloud_environment` | `"AzureUSGovernment"` | No | Azure Cloud Environment |
| `azure_region` | `"usgovvirginia"` | No | — |
| `azure_subscription_id` | `"{{ lookup('env', 'AZURE_SUBSCRIPTION_ID') }}"` | No | — |
| `azure_tenant_id` | `"{{ lookup('env', 'AZURE_TENANT_ID') }}"` | No | — |
| `azure_resource_group` | `"rg-govcloud-prod-usgovva"` | No | Resource Group |
| `azure_sovereign_cloud_config` | `[]` | No | Sovereign Cloud Configuration |
| `azure_sovereign_enable_encryption` | `true` | No | Encryption at Rest |
| `azure_sovereign_encryption_key_source` | `"Microsoft.Keyvault"` | No | — |
| `azure_key_vault_key_id` | `""` | No | — |
| `azure_sovereign_enable_private_endpoint` | `true` | No | Private Endpoints |
| `azure_sovereign_private_endpoint_subnet` | `""` | No | — |
| `azure_sovereign_enable_managed_identity` | `true` | No | Managed Identity |
| `azure_sovereign_managed_identity_type` | `"SystemAssigned"` | No | — |
| `azure_sovereign_enable_diagnostics` | `true` | No | Diagnostic Settings |
| `azure_log_analytics_workspace_id` | `""` | No | — |
| `azure_sovereign_enable_ha` | `true` | No | High Availability |
| `azure_sovereign_zone_redundant` | `true` | No | — |
| `azure_sovereign_enable_backup` | `true` | No | Backup and DR |
| `azure_sovereign_backup_retention_days` | `35` | No | — |
| `azure_sovereign_enable_network_rules` | `true` | No | Network Security |
| `azure_sovereign_allowed_ip_ranges` | `[]` | No | — |
| `azure_sovereign_service_endpoints_enabled` | `true` | No | — |
| `azure_environment` | `"Production"` | No | Cost Management |
| `azure_cost_center` | `"4thEstate-GovCloud"` | No | — |
| `azure_classification` | `"SECRET"` | No | — |
| `azure_resource_tags` | `(see defaults/main.yml)` | No | Resource Tags |
| `azure_sovereign_display_summary` | `true` | No | Operational Settings |

## Example Playbook

```yaml
- name: Use azure_sovereign_cloud
  hosts: all
  gather_facts: false
  roles:
    - role: azure_sovereign_cloud
```

## License

MIT

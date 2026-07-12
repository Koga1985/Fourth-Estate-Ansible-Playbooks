# azure_blueprints

Azure Azure Blueprints management for FedRAMP High environments

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
| `azure_resource_group` | `"rg-security-prod-usgovva"` | No | Resource Group |
| `azure_blueprints_config` | `[]` | No | Azure Blueprints Configuration |
| `azure_bp_enable_encryption` | `true` | No | Encryption at Rest |
| `azure_bp_encryption_key_source` | `"Microsoft.Keyvault"` | No | — |
| `azure_key_vault_key_id` | `""` | No | — |
| `azure_bp_enable_private_endpoint` | `true` | No | Private Endpoints |
| `azure_bp_private_endpoint_subnet` | `""` | No | — |
| `azure_bp_enable_managed_identity` | `true` | No | Managed Identity |
| `azure_bp_managed_identity_type` | `"SystemAssigned"` | No | — |
| `azure_bp_enable_diagnostics` | `true` | No | Diagnostic Settings |
| `azure_log_analytics_workspace_id` | `""` | No | — |
| `azure_bp_enable_ha` | `true` | No | High Availability |
| `azure_bp_zone_redundant` | `true` | No | — |
| `azure_bp_enable_backup` | `true` | No | Backup and DR |
| `azure_bp_backup_retention_days` | `35` | No | — |
| `azure_bp_enable_network_rules` | `true` | No | Network Security |
| `azure_bp_allowed_ip_ranges` | `[]` | No | — |
| `azure_bp_service_endpoints_enabled` | `true` | No | — |
| `azure_environment` | `"Production"` | No | Cost Management |
| `azure_cost_center` | `"4thEstate-Security"` | No | — |
| `azure_classification` | `"SECRET"` | No | — |
| `azure_resource_tags` | `(see defaults/main.yml)` | No | Resource Tags |
| `azure_bp_display_summary` | `true` | No | Operational Settings |

## Example Playbook

```yaml
- name: Use azure_blueprints
  hosts: all
  gather_facts: false
  roles:
    - role: azure_blueprints
```

## License

MIT

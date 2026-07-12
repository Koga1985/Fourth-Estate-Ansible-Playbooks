# azure_snapshot

Azure Disk Snapshots management for FedRAMP High environments

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
| `azure_resource_group` | `"rg-compute-prod-usgovva"` | No | Resource Group |
| `azure_snapshot_config` | `[]` | No | Disk Snapshots Configuration |
| `azure_snapshot_enable_encryption` | `true` | No | Encryption at Rest |
| `azure_snapshot_encryption_key_source` | `"Microsoft.Keyvault"` | No | — |
| `azure_key_vault_key_id` | `""` | No | — |
| `azure_snapshot_enable_private_endpoint` | `true` | No | Private Endpoints |
| `azure_snapshot_private_endpoint_subnet` | `""` | No | — |
| `azure_snapshot_enable_managed_identity` | `true` | No | Managed Identity |
| `azure_snapshot_managed_identity_type` | `"SystemAssigned"` | No | — |
| `azure_snapshot_enable_diagnostics` | `true` | No | Diagnostic Settings |
| `azure_log_analytics_workspace_id` | `""` | No | — |
| `azure_snapshot_enable_ha` | `true` | No | High Availability |
| `azure_snapshot_zone_redundant` | `true` | No | — |
| `azure_snapshot_enable_backup` | `true` | No | Backup and DR |
| `azure_snapshot_backup_retention_days` | `35` | No | — |
| `azure_snapshot_enable_network_rules` | `true` | No | Network Security |
| `azure_snapshot_allowed_ip_ranges` | `[]` | No | — |
| `azure_snapshot_service_endpoints_enabled` | `true` | No | — |
| `azure_environment` | `"Production"` | No | Cost Management |
| `azure_cost_center` | `"4thEstate-Compute"` | No | — |
| `azure_classification` | `"SECRET"` | No | — |
| `azure_resource_tags` | `(see defaults/main.yml)` | No | Resource Tags |
| `azure_snapshot_display_summary` | `true` | No | Operational Settings |

## Example Playbook

```yaml
- name: Use azure_snapshot
  hosts: all
  gather_facts: false
  roles:
    - role: azure_snapshot
```

## License

MIT

# azure_service_principals

Azure Service Principals role for Fourth Estate infrastructure automation.

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
| `azure_tenant_id` | `"{{ lookup('env', 'AZURE_TENANT_ID') }}"` | No | — |
| `azure_subscription_id` | `"{{ lookup('env', 'AZURE_SUBSCRIPTION_ID') }}"` | No | — |
| `azure_resource_group` | `"rg-identity-prod-usgovva"` | No | Resource Group |
| `azure_service_principals` | `[]` | No | Service Principals Configuration |
| `azure_key_vault_uri` | `"https://kv-4e-prod-usgovva.vault.usgovcloudapi.net/"` | No | Key Vault Configuration |
| `azure_store_credentials_in_keyvault` | `true` | No | — |
| `azure_sp_enable_diagnostics` | `true` | No | Audit and Compliance |
| `azure_log_analytics_workspace_id` | `""` | No | To be populated |
| `azure_sp_display_summary` | `true` | No | Operational Settings |
| `azure_environment` | `"Production"` | No | Cost Management |
| `azure_cost_center` | `"4thEstate-Identity"` | No | — |
| `azure_classification` | `"SECRET"` | No | — |
| `azure_resource_tags` | `(see defaults/main.yml)` | No | Resource Tags |

## Example Playbook

```yaml
---
- name: Azure Service Principals
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_service_principals
```

## License

MIT

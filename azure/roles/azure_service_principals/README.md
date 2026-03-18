# azure_service_principals

Azure Service Principals role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `azure_cloud_environment` | `"AzureUSGovernment"` |  |
| `azure_region` | `"usgovvirginia"` |  |
| `azure_tenant_id` | `"{{ lookup('env', 'AZURE_TENANT_ID') }}"` |  |
| `azure_subscription_id` | `"{{ lookup('env', 'AZURE_SUBSCRIPTION_ID') }}"` |  |
| `azure_resource_group` | `"rg-identity-prod-usgovva"` |  |
| `azure_service_principals` | `[]` |  |
| `azure_key_vault_uri` | `"https://kv-4e-prod-usgovva.vault.usgovcloudapi...` |  |
| `azure_store_credentials_in_keyvault` | `true` |  |
| `azure_sp_enable_diagnostics` | `true` |  |
| `azure_log_analytics_workspace_id` | `""` | No | To be populated |
| `azure_sp_display_summary` | `true` |  |
| `azure_environment` | `"Production"` |  |
| `azure_cost_center` | `"4thEstate-Identity"` |  |
| `azure_classification` | `"SECRET"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

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

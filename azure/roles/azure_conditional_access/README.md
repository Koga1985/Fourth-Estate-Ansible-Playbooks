# azure_conditional_access

Azure Conditional Access role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `azure_cloud_environment` | `"AzureUSGovernment"` |  |
| `azure_region` | `"usgovvirginia"` |  |
| `azure_tenant_id` | `"{{ lookup('env', 'AZURE_TENANT_ID') }}"` |  |
| `azure_resource_group` | `"rg-identity-prod-usgovva"` |  |
| `azure_conditional_access_policies` | `[]` |  |
| `azure_ca_deploy_baseline_policies` | `true` |  |
| `azure_breakglass_group_id` | `""` | Break-glass account group |
| `azure_ca_named_locations` | `[]` |  |
| `azure_ca_auth_strength_policies` | `[]` |  |
| `azure_ca_enable_diagnostics` | `true` |  |
| `azure_log_analytics_workspace_id` | `""` | To be populated |
| `azure_ca_display_summary` | `true` |  |
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
- name: Azure Conditional Access
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_conditional_access
```

## License

MIT

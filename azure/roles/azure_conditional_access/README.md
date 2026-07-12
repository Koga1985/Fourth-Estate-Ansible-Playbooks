# azure_conditional_access

Azure Conditional Access role for Fourth Estate infrastructure automation.

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
| `azure_resource_group` | `"rg-identity-prod-usgovva"` | No | Resource Group |
| `azure_conditional_access_policies` | `[]` | No | Conditional Access Policies |
| `azure_ca_deploy_baseline_policies` | `true` | No | Baseline Fourth Estate Policies |
| `azure_breakglass_group_id` | `""` | No | Break-glass account group |
| `azure_ca_named_locations` | `[]` | No | Named Locations |
| `azure_ca_auth_strength_policies` | `[]` | No | Authentication Strength Policies |
| `azure_ca_enable_diagnostics` | `true` | No | Audit and Compliance |
| `azure_log_analytics_workspace_id` | `""` | No | To be populated |
| `azure_ca_display_summary` | `true` | No | Operational Settings |
| `azure_environment` | `"Production"` | No | Cost Management |
| `azure_cost_center` | `"4thEstate-Identity"` | No | — |
| `azure_classification` | `"SECRET"` | No | — |
| `azure_resource_tags` | `(see defaults/main.yml)` | No | Resource Tags |

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

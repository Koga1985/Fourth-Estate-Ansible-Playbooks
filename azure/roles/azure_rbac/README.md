# azure_rbac

Azure Rbac role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `azure_cloud_environment` | `"AzureUSGovernment"` |  |
| `azure_region` | `"usgovvirginia"` |  |
| `azure_tenant_id` | `"{{ lookup('env', 'AZURE_TENANT_ID') }}"` |  |
| `azure_subscription_id` | `"{{ lookup('env', 'AZURE_SUBSCRIPTION_ID') }}"` |  |
| `azure_resource_group` | `"rg-identity-prod-usgovva"` |  |
| `azure_rbac_custom_roles` | `[]` |  |
| `azure_rbac_user_assignments` | `[]` |  |
| `azure_rbac_group_assignments` | `[]` |  |
| `azure_rbac_sp_assignments` | `[]` |  |
| `azure_rbac_pim_assignments` | `[]` |  |
| `azure_rbac_deny_assignments` | `[]` |  |
| `azure_rbac_enable_pim` | `true` |  |
| `azure_rbac_enable_audit_logging` | `true` |  |
| `azure_log_analytics_workspace_id` | `""` | To be populated |
| `azure_rbac_generate_report` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Azure Rbac
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_rbac
```

## License

MIT

# azure_rbac

Azure Rbac role for Fourth Estate infrastructure automation.

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
| `azure_rbac_custom_roles` | `[]` | No | Custom RBAC Roles |
| `azure_rbac_user_assignments` | `[]` | No | User Role Assignments |
| `azure_rbac_group_assignments` | `[]` | No | Group Role Assignments |
| `azure_rbac_sp_assignments` | `[]` | No | Service Principal Role Assignments |
| `azure_rbac_pim_assignments` | `[]` | No | Privileged Identity Management (PIM) Assignments |
| `azure_rbac_deny_assignments` | `[]` | No | Deny Assignments (Least Privilege) |
| `azure_rbac_enable_pim` | `true` | No | Privileged Identity Management |
| `azure_rbac_enable_audit_logging` | `true` | No | Audit and Compliance |
| `azure_log_analytics_workspace_id` | `""` | No | To be populated |
| `azure_rbac_generate_report` | `true` | No | Reporting |
| `azure_rbac_report_path` | `"/var/lib/ansible/rbac_compliance_report.json"` | No | — |
| `azure_rbac_display_summary` | `true` | No | Operational Settings |
| `azure_environment` | `"Production"` | No | Cost Management |
| `azure_cost_center` | `"4thEstate-Identity"` | No | — |
| `azure_classification` | `"SECRET"` | No | — |
| `azure_resource_tags` | `(see defaults/main.yml)` | No | Resource Tags |

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

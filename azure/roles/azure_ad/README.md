# azure_ad

Azure Ad role for Fourth Estate infrastructure automation.

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
| `azure_tenant_domain` | `"{{ lookup('env', 'AZURE_TENANT_DOMAIN') }}"` | No | — |
| `azure_tenant_id` | `"{{ lookup('env', 'AZURE_TENANT_ID') }}"` | No | — |
| `azure_resource_group` | `"rg-identity-prod-usgovva"` | No | Resource Group |
| `azure_ad_groups` | `[]` | No | Azure AD Groups Configuration |
| `azure_ad_users` | `[]` | No | Azure AD Users Configuration |
| `azure_ad_security_defaults_enabled` | `true` | No | Security Configuration |
| `azure_ad_manage_security_defaults` | `true` | No | — |
| `azure_ad_configure_password_policy` | `true` | No | Password Policy |
| `azure_ad_password_validity_days` | `90` | No | — |
| `azure_ad_password_notification_days` | `14` | No | — |
| `azure_ad_enable_audit_logging` | `true` | No | Audit and Compliance |
| `azure_ad_configure_diagnostics` | `true` | No | — |
| `azure_ad_diagnostic_setting_name` | `"ad-diagnostics-fedramp"` | No | — |
| `azure_log_analytics_workspace` | `"law-identity-prod-usgovva"` | No | — |
| `azure_log_analytics_workspace_id` | `""` | No | To be populated |
| `azure_ad_audit_retention_days` | `365` | No | Retention Policies (FedRAMP High requires 1 year minimum) |
| `azure_ad_signin_retention_days` | `365` | No | — |
| `azure_ad_risk_retention_days` | `365` | No | — |
| `azure_ad_no_log` | `true` | No | Operational Settings Protect sensitive data in logs |
| `azure_ad_display_summary` | `true` | No | — |
| `azure_environment` | `"Production"` | No | Cost Management |
| `azure_cost_center` | `"4thEstate-Identity"` | No | — |
| `azure_classification` | `"SECRET"` | No | — |

## Example Playbook

```yaml
---
- name: Azure Ad
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_ad
```

## License

MIT

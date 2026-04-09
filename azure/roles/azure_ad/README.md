# azure_ad

Azure Ad role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `azure_cloud_environment` | `"AzureUSGovernment"` |  |
| `azure_region` | `"usgovvirginia"` |  |
| `azure_tenant_domain` | `"{{ lookup('env', 'AZURE_TENANT_DOMAIN') }}"` |  |
| `azure_tenant_id` | `"{{ lookup('env', 'AZURE_TENANT_ID') }}"` |  |
| `azure_resource_group` | `"rg-identity-prod-usgovva"` |  |
| `azure_ad_groups` | `[]` |  |
| `azure_ad_users` | `[]` |  |
| `azure_ad_security_defaults_enabled` | `true` |  |
| `azure_ad_manage_security_defaults` | `true` |  |
| `azure_ad_configure_password_policy` | `true` |  |
| `azure_ad_password_validity_days` | `90` |  |
| `azure_ad_password_notification_days` | `14` |  |
| `azure_ad_enable_audit_logging` | `true` |  |
| `azure_ad_configure_diagnostics` | `true` |  |
| `azure_ad_diagnostic_setting_name` | `"ad-diagnostics-fedramp"` |  | Name for the Azure Monitor diagnostic setting |
| `azure_log_analytics_workspace` | `"law-identity-prod-usgovva"` |  | Log Analytics workspace name for audit log forwarding |
| `azure_log_analytics_workspace_id` | `""` | **Yes** | Log Analytics workspace ID (required for diagnostics) |
| `azure_ad_audit_retention_days` | `365` |  | Retention days for AD audit logs (FedRAMP High minimum: 365) |
| `azure_ad_signin_retention_days` | `365` |  | Retention days for sign-in logs (FedRAMP High minimum: 365) |
| `azure_ad_risk_retention_days` | `365` |  | Retention days for risk event logs |
| `azure_ad_no_log` | `true` |  | Suppress sensitive variable values from Ansible output |
| `azure_ad_display_summary` | `true` |  | Print a summary of changes at the end of the run |
| `azure_environment` | `"Production"` |  | Environment label for cost/compliance tagging |
| `azure_cost_center` | `"4thEstate-Identity"` |  | Cost center tag applied to managed resources |
| `azure_classification` | `"SECRET"` |  | Data classification tag applied to managed resources |

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

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

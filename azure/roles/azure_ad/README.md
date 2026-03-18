# azure_ad

Azure Ad role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
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
| `azure_ad_diagnostic_setting_name` | `"ad-diagnostics-fedramp"` |  |

See `defaults/main.yml` for the full variable list.

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

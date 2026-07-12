# azure_ad_mfa

Azure Ad Mfa role for Fourth Estate infrastructure automation.

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
| `azure_mfa_enable_service` | `true` | No | MFA Service Configuration |
| `azure_mfa_configure_registration` | `true` | No | — |
| `azure_mfa_security_defaults` | `true` | No | — |
| `azure_mfa_method_configurations` | `(see defaults/main.yml)` | No | MFA Method Configurations |
| `azure_mfa_configure_authenticator` | `true` | No | Microsoft Authenticator Settings |
| `azure_mfa_display_app_info` | `"enabled"` | No | — |
| `azure_mfa_display_location` | `"enabled"` | No | — |
| `azure_mfa_number_matching` | `"enabled"` | No | Phishing-resistant |
| `azure_mfa_enable_fido2` | `true` | No | FIDO2 Security Key Settings |
| `azure_mfa_fido2_self_service` | `true` | No | — |
| `azure_mfa_fido2_attestation` | `true` | No | — |
| `azure_mfa_fido2_restriction_type` | `"allow"` | No | — |
| `azure_mfa_fido2_allowed_guids` | `[]` | No | Specific FIDO2 keys allowed |
| `azure_mfa_fido2_target_group` | `"all_users"` | No | — |
| `azure_mfa_configure_sms` | `true` | No | SMS Authentication (Generally disabled for security) |
| `azure_mfa_sms_enabled` | `"disabled"` | No | — |
| `azure_mfa_sms_target_group` | `"none"` | No | — |
| `azure_mfa_per_user_settings` | `[]` | No | Per-User MFA Settings |
| `azure_mfa_enable_fraud_alert` | `true` | No | Fraud Alert Settings |
| `azure_mfa_fraud_auto_block` | `true` | No | — |
| `azure_mfa_fraud_auto_report` | `true` | No | — |
| `azure_mfa_configure_remember` | `false` | No | Remember Devices (Typically disabled for high security) |
| `azure_mfa_remember_devices` | `"disabled"` | No | — |
| `azure_mfa_remember_days` | `0` | No | — |
| `azure_mfa_enable_diagnostics` | `true` | No | Audit and Compliance |
| `azure_log_analytics_workspace_id` | `""` | No | To be populated |
| `azure_mfa_display_summary` | `true` | No | Operational Settings |
| `azure_environment` | `"Production"` | No | Cost Management |
| `azure_cost_center` | `"4thEstate-Identity"` | No | — |
| `azure_classification` | `"SECRET"` | No | — |
| `azure_resource_tags` | `(see defaults/main.yml)` | No | Resource Tags |

## Example Playbook

```yaml
---
- name: Azure Ad Mfa
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_ad_mfa
```

## License

MIT

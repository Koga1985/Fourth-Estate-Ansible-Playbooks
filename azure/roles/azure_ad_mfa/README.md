# azure_ad_mfa

Azure Ad Mfa role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `azure_cloud_environment` | `"AzureUSGovernment"` |  |
| `azure_region` | `"usgovvirginia"` |  |
| `azure_tenant_id` | `"{{ lookup('env', 'AZURE_TENANT_ID') }}"` |  |
| `azure_resource_group` | `"rg-identity-prod-usgovva"` |  |
| `azure_mfa_enable_service` | `true` |  |
| `azure_mfa_configure_registration` | `true` |  |
| `azure_mfa_security_defaults` | `true` |  |
| `azure_mfa_configure_authenticator` | `true` |  |
| `azure_mfa_display_app_info` | `"enabled"` |  |
| `azure_mfa_display_location` | `"enabled"` |  |
| `azure_mfa_number_matching` | `"enabled"` | Phishing-resistant |
| `azure_mfa_enable_fido2` | `true` |  |
| `azure_mfa_fido2_self_service` | `true` |  |
| `azure_mfa_fido2_attestation` | `true` |  |
| `azure_mfa_fido2_restriction_type` | `"allow"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

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

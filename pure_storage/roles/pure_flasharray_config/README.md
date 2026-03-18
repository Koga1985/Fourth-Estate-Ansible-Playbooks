# pure_flasharray_config

Pure Flasharray Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` |  |
| `flasharray_name` | `"{{ inventory_hostname_short }}-fa"` |  |
| `flasharray_idle_timeout` | `30` |  |
| `flasharray_login_banner` | `|` |  |
| `flasharray_ad_enabled` | `false` |  |
| `flasharray_ldap_enabled` | `false` |  |
| `flasharray_saml_enabled` | `false` |  |
| `flasharray_multi_admin_enabled` | `true` |  |
| `flasharray_smtp_sender_domain` | `"{{ domain_name | No | default('example.com') }}"` |
| `flasharray_smtp_relay_host` | `"{{ smtp_relay | No | default('smtp.example.com') }}"` |
| `flasharray_phonehome_enabled` | `true` |  |
| `flasharray_support_proxy_enabled` | `false` |  |
| `flasharray_safemode_enabled` | `true` |  |
| `flasharray_audit_retention_days` | `365` |  |
| `flasharray_organization` | `"Fourth Estate"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Pure Flasharray Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_config
```

## License

MIT

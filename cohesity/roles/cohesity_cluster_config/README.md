# cohesity_cluster_config

Cohesity Cluster Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `cohesity/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `cohesity_cluster_vip` | `"10.100.1.100"` |  |
| `cohesity_api_protocol` | `"https"` |  |
| `cohesity_api_port` | `443` |  |
| `cohesity_api_verify_ssl` | `true` |  |
| `cohesity_api_timeout` | `300` |  |
| `cohesity_admin_username` | `"admin"` |  |
| `cohesity_admin_password` | `"{{ vault_cohesity_admin_password }}"` |  |
| `cohesity_api_token` | `""` |  |
| `cohesity_ad_enabled` | `true` |  |
| `cohesity_ad_domain` | `"fourthestate.com"` |  |
| `cohesity_ad_preferred_dc` | `[]` |  |
| `cohesity_ad_username` | `"cohesity-svc@fourthestate.com"` |  |
| `cohesity_ad_password` | `"{{ vault_ad_password }}"` |  |
| `cohesity_ad_ou_path` | `"OU=Service Accounts,DC=fourthestate,DC=com"` |  |
| `cohesity_ad_trusted_domains` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Cohesity Cluster Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: cohesity/roles/cohesity_cluster_config
```

## License

MIT

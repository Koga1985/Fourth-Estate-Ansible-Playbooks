# vast_config

Vast Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vast/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vast_mgmt_host` | `"{{ vault_vast_mgmt_host }}"` |  |
| `vast_mgmt_port` | `443` |  |
| `vast_mgmt_user` | `"{{ vault_vast_mgmt_user }}"` |  |
| `vast_mgmt_password` | `"{{ vault_vast_mgmt_password }}"` |  |
| `vast_api_version` | `"v1"` |  |
| `vast_verify_ssl` | `true` |  |
| `vast_ssl_cert_path` | `"/etc/pki/tls/certs/vast-ca-bundle.crt"` |  |
| `vast_api_timeout` | `60` |  |
| `vast_cluster_name` | `"production-cluster"` |  |
| `vast_cluster_domain` | `"vast.local"` |  |
| `vast_cluster_timezone` | `"America/New_York"` |  |
| `vast_cluster_description` | `"Fourth Estate Production Storage Cluster"` |  |
| `vast_ntp_timezone` | `"America/New_York"` |  |
| `vast_smtp_enabled` | `false` |  |
| `vast_smtp_server` | `"{{ vault_smtp_server | No | default('') }}"` |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Vast Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: vast/roles/vast_config
```

## License

MIT

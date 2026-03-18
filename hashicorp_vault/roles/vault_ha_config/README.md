# vault_ha_config

Vault Ha Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `hashicorp_vault/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vault_ha_enabled` | `true` |  |
| `vault_ha_redirect_addr` | `"{{ vault_api_addr }}"` |  |
| `vault_loadbalancer_enabled` | `true` |  |
| `vault_loadbalancer_type` | `"haproxy"` | **Yes** | haproxy, nginx, aws_alb |
| `vault_loadbalancer_vip` | `""` |  |
| `vault_loadbalancer_port` | `8200` |  |
| `vault_loadbalancer_health_check_path` | `"/v1/sys/health"` |  |
| `vault_loadbalancer_health_check_interval` | `10` |  |
| `vault_loadbalancer_backend_servers` | `[]` |  |
| `vault_performance_standby_enabled` | `false` |  |
| `vault_performance_standby_count` | `2` |  |
| `vault_request_forwarding_enabled` | `true` |  |
| `vault_cluster_perf_standby_conn_limit` | `1000` |  |
| `vault_max_request_size` | `33554432` | **Yes** | 32MB |
| `vault_max_request_duration` | `"90s"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `community.hashi_vault`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Vault Ha Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: hashicorp_vault/roles/vault_ha_config
```

## License

MIT

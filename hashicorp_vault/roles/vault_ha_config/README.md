# vault_ha_config

Vault Ha Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `hashicorp_vault/README.md`

## Requirements

- Ansible 2.15+
- Collection: `community.hashi_vault`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vault_ha_enabled` | `true` | No | HA Configuration |
| `vault_ha_redirect_addr` | `"{{ vault_api_addr }}"` | No | — |
| `vault_loadbalancer_enabled` | `true` | No | Load Balancer Configuration |
| `vault_loadbalancer_type` | `"haproxy"` | No | haproxy, nginx, aws_alb |
| `vault_loadbalancer_vip` | `""` | No | — |
| `vault_loadbalancer_port` | `8200` | No | — |
| `vault_loadbalancer_health_check_path` | `"/v1/sys/health"` | No | — |
| `vault_loadbalancer_health_check_interval` | `10` | No | — |
| `vault_loadbalancer_backend_servers` | `[]` | No | — |
| `vault_performance_standby_enabled` | `false` | No | Performance Standby (Enterprise) |
| `vault_performance_standby_count` | `2` | No | — |
| `vault_request_forwarding_enabled` | `true` | No | Request forwarding |
| `vault_cluster_perf_standby_conn_limit` | `1000` | No | Cluster performance tuning |
| `vault_max_request_size` | `33554432` | No | 32MB |
| `vault_max_request_duration` | `"90s"` | No | — |
| `vault_ha_monitoring_enabled` | `true` | No | HA monitoring |
| `vault_ha_failover_test_enabled` | `false` | No | — |
| `vault_ha_backup_enabled` | `true` | No | Backup HA configuration |
| `vault_ha_backup_schedule` | `"0 */6 * * *"` | No | — |
| `vault_cluster_retry_join_enabled` | `true` | No | Network resilience |
| `vault_cluster_retry_join_max_attempts` | `10` | No | — |
| `vault_cluster_retry_join_interval` | `30` | No | — |
| `vault_active_active_enabled` | `false` | No | Active-Active (Enterprise) |
| `vault_dr_enabled` | `false` | No | Disaster Recovery |
| `vault_dr_operation_token_ttl` | `"24h"` | No | — |

## Example Playbook

```yaml
---
- name: Vault Ha Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: hashicorp_vault/roles/vault_ha_config
```

## Tags

| Tag | Description |
|-----|-------------|
| `backup` | Tasks tagged `backup` |
| `forwarding` | Tasks tagged `forwarding` |
| `ha` | Tasks tagged `ha` |
| `loadbalancer` | Tasks tagged `loadbalancer` |
| `monitoring` | Tasks tagged `monitoring` |
| `performance-standby` | Tasks tagged `performance-standby` |
| `quorum` | Tasks tagged `quorum` |
| `status` | Tasks tagged `status` |
| `validate` | Tasks tagged `validate` |
| `vault` | Tasks tagged `vault` |

## License

MIT

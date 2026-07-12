# vault_cluster

Vault Cluster role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `hashicorp_vault/README.md`

## Requirements

- Ansible 2.15+
- Collection: `community.hashi_vault`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vault_cluster_name` | `"vault-prod-cluster"` | No | Cluster configuration |
| `vault_cluster_members` | `[]` | No | List of cluster member addresses |
| `vault_cluster_leader` | `""` | No | — |
| `vault_is_cluster_primary` | `false` | No | — |
| `vault_raft_retry_join` | `(see defaults/main.yml)` | No | Raft configuration |
| `vault_raft_autopilot_reconcile_interval` | `"10s"` | No | — |
| `vault_raft_autopilot_update_interval` | `"2s"` | No | — |
| `vault_init_required` | `true` | No | Cluster initialization |
| `vault_init_secret_shares` | `5` | No | — |
| `vault_init_secret_threshold` | `3` | No | — |
| `vault_init_pgp_keys` | `[]` | No | — |
| `vault_init_root_token_pgp_key` | `""` | No | — |
| `vault_init_stored_shares` | `1` | No | — |
| `vault_init_recovery_shares` | `5` | No | — |
| `vault_init_recovery_threshold` | `3` | No | — |
| `vault_init_recovery_pgp_keys` | `[]` | No | — |
| `vault_unseal_keys` | `[]` | No | Unseal configuration Populated after init |
| `vault_auto_unseal` | `true` | No | — |
| `vault_join_cluster` | `false` | No | Join configuration |
| `vault_join_leader_api_addr` | `""` | No | — |
| `vault_join_leader_ca_cert` | `""` | No | — |
| `vault_join_retry_attempts` | `5` | No | — |
| `vault_join_retry_interval` | `10` | No | — |
| `vault_health_check_enabled` | `true` | No | Health check |
| `vault_health_check_interval` | `30` | No | — |
| `vault_cluster_tls_cert` | `""` | No | Cluster API |
| `vault_cluster_tls_key` | `""` | No | — |
| `vault_enable_replication` | `false` | No | Replication (Enterprise) |
| `vault_replication_mode` | `""` | No | performance or dr |
| `vault_replication_primary_cluster_addr` | `""` | No | — |
| `vault_replication_secondary_token` | `""` | No | — |
| `vault_snapshot_agent_enabled` | `false` | No | Backup/Recovery |
| `vault_snapshot_agent_interval` | `"1h"` | No | — |
| `vault_snapshot_local_path` | `"/backup/vault/snapshots"` | No | — |
| `vault_snapshot_storage_type` | `""` | No | s3, azure-blob, google-storage |
| `vault_snapshot_s3_bucket` | `""` | No | — |
| `vault_snapshot_s3_region` | `""` | No | — |
| `vault_enable_cluster_metrics` | `true` | No | Cluster metrics |
| `vault_dr_operation_token` | `""` | No | Disaster Recovery |
| `vault_dr_primary_cluster_addr` | `""` | No | — |
| `vault_enable_performance_standby` | `false` | No | Performance standbys (Enterprise) |
| `vault_seal_migration` | `false` | No | Seal migration |
| `vault_old_seal_type` | `""` | No | — |

## Example Playbook

```yaml
---
- name: Vault Cluster
  hosts: localhost
  gather_facts: false
  roles:
    - role: hashicorp_vault/roles/vault_cluster
```

## Tags

| Tag | Description |
|-----|-------------|
| `autopilot` | Tasks tagged `autopilot` |
| `cluster` | Tasks tagged `cluster` |
| `dr` | Tasks tagged `dr` |
| `health` | Tasks tagged `health` |
| `init` | Tasks tagged `init` |
| `join` | Tasks tagged `join` |
| `peers` | Tasks tagged `peers` |
| `replication` | Tasks tagged `replication` |
| `snapshot` | Tasks tagged `snapshot` |
| `status` | Tasks tagged `status` |
| `unseal` | Tasks tagged `unseal` |
| `validate` | Tasks tagged `validate` |
| `vault` | Tasks tagged `vault` |

## License

MIT

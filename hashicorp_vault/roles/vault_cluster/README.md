# vault_cluster

Vault Cluster role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `hashicorp_vault/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vault_cluster_name` | `"vault-prod-cluster"` |  |
| `vault_cluster_members` | `[]` | **Yes** | List of cluster member addresses |
| `vault_cluster_leader` | `""` |  |
| `vault_is_cluster_primary` | `false` |  |
| `vault_raft_autopilot_reconcile_interval` | `"10s"` |  |
| `vault_raft_autopilot_update_interval` | `"2s"` |  |
| `vault_init_required` | `true` |  |
| `vault_init_secret_shares` | `5` |  |
| `vault_init_secret_threshold` | `3` |  |
| `vault_init_pgp_keys` | `[]` |  |
| `vault_init_root_token_pgp_key` | `""` |  |
| `vault_init_stored_shares` | `1` |  |
| `vault_init_recovery_shares` | `5` |  |
| `vault_init_recovery_threshold` | `3` |  |
| `vault_init_recovery_pgp_keys` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `community.hashi_vault`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Vault Cluster
  hosts: localhost
  gather_facts: false
  roles:
    - role: hashicorp_vault/roles/vault_cluster
```

## License

MIT

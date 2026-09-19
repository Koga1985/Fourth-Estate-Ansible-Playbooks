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
| `vault_init_pgp_keys` | `[]` | No | One PGP public key per unseal share (Shamir seal) |
| `vault_init_root_token_pgp_key` | `""` | No | PGP public key the initial root token is encrypted to |
| `vault_init_stored_shares` | `1` | No | — |
| `vault_init_recovery_shares` | `5` | No | — |
| `vault_init_recovery_threshold` | `3` | No | — |
| `vault_init_recovery_pgp_keys` | `[]` | No | One PGP public key per recovery share (auto-unseal seal) |
| `vault_allow_plaintext_key_material` | `false` | No | Override the refusal to initialize without PGP — see [Key custody](#key-custody) |
| `vault_init_keys_dest` | `{{ vault_config_path }}/vault-init-keys.json` | No | Where the initialization response is written |
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


## Key custody

Initializing a Vault returns the unseal shares (or, under an auto-unseal seal,
the recovery shares) together with the initial root token. Between them they are
the entire cluster: whoever holds them can unseal it and read every secret in
it.

Splitting the key into shares only protects anything if the shares end up in
different hands. Writing all of them to one file on the Vault node gives that
up — and `mode: 0600` does not help against a backup, a snapshot, or root on
that host.

**This role refuses to initialize unless Vault will encrypt the response.**
Give it one PGP public key per share and one for the root token, and no single
file or person ever holds usable material:

```yaml
# Auto-unseal seal (vault_auto_unseal: true, the default)
vault_init_recovery_pgp_keys:
  - keybase:alice
  - keybase:bob
  - keybase:carol
  - keybase:dave
  - keybase:erin
vault_init_root_token_pgp_key: keybase:security-officer
```

Use `vault_init_pgp_keys` instead when `vault_auto_unseal: false`. Keys may be
base64 of the public key or a `keybase:<user>` reference, and the count must
equal the share count — the role checks that before initializing rather than
letting Vault fail after it has generated the master key.

The refusal is a preflight, deliberately. Failing *after* initialization would
leave a live Vault whose only copy of the shares was in a `no_log` task result
nobody can read: a cluster that can never be unsealed.

To initialize without PGP anyway — appropriate for a lab you are about to
destroy, not for a cluster that will hold real secrets:

```yaml
vault_allow_plaintext_key_material: true
```

The role then writes the plaintext response to `vault_init_keys_dest` and says
plainly what that file is and what to do about it.

### A note on what this replaced

Before this, the role wrote the unseal keys and root token to the Vault node in
plaintext and printed "IMMEDIATELY secure this file and remove from server!".
It also guarded that write with `when: vault_init_result is changed` —
and `ansible.builtin.uri` reports `changed: false` for a successful POST, so the
guard never fired. The keys were returned, held in a `no_log` register, and
discarded when the play ended. Both are fixed: the write is gated on the
response actually carrying key material, and a response with nothing to save
fails loudly instead of passing silently.

# vast_backup_dr

Vast Backup Dr role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vast/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vast_mgmt_host` | `"{{ vault_vast_mgmt_host }}"` | No | — |
| `vast_mgmt_port` | `443` | No | — |
| `vast_mgmt_user` | `"{{ vault_vast_mgmt_user }}"` | No | — |
| `vast_mgmt_password` | `"{{ vault_vast_mgmt_password }}"` | No | — |
| `vast_api_version` | `"v1"` | No | — |
| `vast_verify_ssl` | `true` | No | — |
| `vast_snapshot_enabled` | `true` | No | Snapshot Configuration |
| `vast_snapshot_schedule` | `"daily"` | No | — |
| `vast_snapshot_retention_days` | `30` | No | — |
| `vast_snapshot_prefix` | `"auto"` | No | — |
| `vast_replication_enabled` | `false` | No | Replication Configuration |
| `vast_replication_type` | `"async"` | No | Options: sync, async |
| `vast_replication_target_cluster` | `"{{ vault_vast_dr_cluster \| default('') }}"` | No | — |
| `vast_replication_target_user` | `"{{ vault_vast_dr_user \| default('') }}"` | No | — |
| `vast_replication_target_password` | `"{{ vault_vast_dr_password \| default('') }}"` | No | — |
| `vast_replication_schedule` | `"hourly"` | No | — |
| `vast_replication_bandwidth_limit_mbps` | `0` | No | 0 = unlimited |
| `vast_backup_to_external` | `false` | No | Backup Configuration |
| `vast_backup_type` | `"s3"` | No | Options: s3, nfs, smb |
| `vast_backup_destination` | `"{{ vault_backup_destination \| default('') }}"` | No | — |
| `vast_backup_schedule` | `"daily"` | No | — |
| `vast_backup_retention_days` | `90` | No | — |
| `vast_backup_encryption_enabled` | `true` | No | — |
| `vast_backup_compression_enabled` | `true` | No | — |
| `vast_dr_testing_enabled` | `false` | No | Disaster Recovery Configuration |
| `vast_dr_test_schedule` | `"quarterly"` | No | — |
| `vast_dr_rto_minutes` | `240` | No | Recovery Time Objective |
| `vast_dr_rpo_minutes` | `60` | No | Recovery Point Objective |
| `vast_protection_policies` | `(see defaults/main.yml)` | No | Protection Policies |
| `vast_backup_audit_enabled` | `true` | No | Compliance Requirements |
| `vast_backup_integrity_check` | `true` | No | — |
| `vast_backup_offsite_copy_required` | `true` | No | — |

## Example Playbook

```yaml
---
- name: Vast Backup Dr
  hosts: localhost
  gather_facts: false
  roles:
    - role: vast/roles/vast_backup_dr
```

## Tags

| Tag | Description |
|-----|-------------|
| `backup` | Tasks tagged `backup` |
| `connectivity` | Tasks tagged `connectivity` |
| `disaster_recovery` | Tasks tagged `disaster_recovery` |
| `dr` | Tasks tagged `dr` |
| `external` | Tasks tagged `external` |
| `integrity` | Tasks tagged `integrity` |
| `objectives` | Tasks tagged `objectives` |
| `policies` | Tasks tagged `policies` |
| `protection` | Tasks tagged `protection` |
| `readiness` | Tasks tagged `readiness` |
| `replication` | Tasks tagged `replication` |
| `runbook` | Tasks tagged `runbook` |
| `schedule` | Tasks tagged `schedule` |
| `snapshots` | Tasks tagged `snapshots` |
| `testing` | Tasks tagged `testing` |

## License

MIT

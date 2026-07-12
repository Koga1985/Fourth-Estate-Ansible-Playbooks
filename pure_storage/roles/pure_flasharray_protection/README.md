# pure_flasharray_protection

Pure Flasharray Protection role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` | No | Array connection |
| `flasharray_eradication_timer` | `86400` | No | Eradication timer (deleted objects retention) 24 hours (in seconds) |
| `flasharray_evidence_pg` | `"pg-evidence-preservation"` | No | Fourth Estate evidence preservation |
| `flasharray_evidence_retention_days` | `2555` | No | 7 years |
| `flasharray_default_snapshot_schedules` | `(see defaults/main.yml)` | No | Default snapshot schedules |
| `flasharray_snapshot_retention_tiers` | `(see defaults/main.yml)` | No | Snapshot retention tiers |
| `flasharray_safemode_enabled` | `true` | No | SafeMode configuration |
| `flasharray_safemode_retention_minimum` | `24` | No | hours (cannot delete before this) |
| `flasharray_safemode_retention_default` | `168` | No | hours (7 days default) |
| `flasharray_safemode_compliance_mode` | `true` | No | — |
| `flasharray_app_consistent_snapshots` | `true` | No | Application-consistent snapshots |
| `flasharray_quiesce_timeout` | `300` | No | seconds |
| `flasharray_snapshot_suffix_format` | `"{{ ansible_date_time.iso8601_basic_short }}"` | No | Snapshot naming convention |
| `flasharray_snapshot_prefix` | `"snap"` | No | — |
| `flasharray_protection_policies` | `(see defaults/main.yml)` | No | Protection policies |
| `flasharray_ransomware_protection_enabled` | `true` | No | Ransomware protection |
| `flasharray_immutable_snapshots` | `true` | No | — |
| `flasharray_snapshot_locking` | `true` | No | — |
| `flasharray_dr_snapshot_replication` | `true` | No | Disaster recovery |
| `flasharray_dr_rpo_minutes` | `15` | No | — |
| `flasharray_snapshot_audit_logging` | `true` | No | Compliance and audit |
| `flasharray_snapshot_catalog_enabled` | `true` | No | — |
| `flasharray_snapshot_verification` | `true` | No | — |
| `flasharray_snapshot_performance_impact` | `"minimal"` | No | Performance impact Pure's redirect-on-write |
| `flasharray_snapshot_space_reclamation` | `"automatic"` | No | — |
| `flasharray_fourth_estate_protection_groups` | `(see defaults/main.yml)` | No | Fourth Estate specific protection groups |

## Example Playbook

```yaml
---
- name: Pure Flasharray Protection
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_protection
```

## Tags

| Tag | Description |
|-----|-------------|
| `compliance` | Tasks tagged `compliance` |
| `evidence` | Tasks tagged `evidence` |

## License

MIT

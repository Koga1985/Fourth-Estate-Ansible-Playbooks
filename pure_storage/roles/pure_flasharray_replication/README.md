# pure_flasharray_replication

Pure Flasharray Replication role for Fourth Estate infrastructure automation.

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
| `flasharray_default_rpo_minutes` | `15` | No | Default RPO settings |
| `flasharray_critical_rpo_minutes` | `5` | No | — |
| `flasharray_standard_rpo_minutes` | `60` | No | — |
| `flasharray_activecluster_enabled` | `false` | No | ActiveCluster settings |
| `flasharray_activecluster_rpo` | `0` | No | Synchronous (zero RPO) |
| `flasharray_activecluster_auto_failover` | `true` | No | — |
| `flasharray_activecluster_witness` | `true` | No | — |
| `flasharray_activedr_enabled` | `true` | No | ActiveDR settings |
| `flasharray_activedr_compression` | `true` | No | — |
| `flasharray_activedr_dedupe` | `true` | No | — |
| `flasharray_replication_types` | `(see defaults/main.yml)` | No | Replication types |
| `flasharray_replication_use_jumbo_frames` | `true` | No | Network optimization |
| `flasharray_replication_mtu` | `9000` | No | — |
| `flasharray_replication_compression` | `true` | No | — |
| `flasharray_replication_bandwidth_unlimited` | `false` | No | Bandwidth management |
| `flasharray_default_replication_bandwidth` | `"1G"` | No | — |
| `flasharray_automated_failover` | `false` | No | Failover and failback |
| `flasharray_planned_failover_allowed` | `true` | No | — |
| `flasharray_failback_requires_approval` | `true` | No | — |
| `flasharray_monitor_replication_lag` | `true` | No | Monitoring and alerting |
| `flasharray_replication_lag_alert_threshold` | `300` | No | seconds (5 minutes) |
| `flasharray_replication_lag_critical_threshold` | `900` | No | seconds (15 minutes) |
| `flasharray_dr_site_array` | `"flasharray-dr-offsite"` | No | Fourth Estate DR configuration |
| `flasharray_dr_site_location` | `"Remote DR Datacenter"` | No | — |
| `flasharray_fourth_estate_dr_pgroups` | `(see defaults/main.yml)` | No | Fourth Estate protection groups for DR |
| `flasharray_replication_audit_logging` | `true` | No | Compliance and audit |
| `flasharray_replication_verification` | `true` | No | — |
| `flasharray_replication_test_frequency_days` | `90` | No | Test DR every quarter |
| `flasharray_airgap_replication` | `false` | No | Air-gapped replication (for Fourth Estate) If true, use snapshot shipping |
| `flasharray_geo_replication_enabled` | `true` | No | Geo-replication |
| `flasharray_cross_region_replication` | `true` | No | — |
| `flasharray_replication_performance_impact` | `"minimal"` | No | Performance impact |
| `flasharray_replication_priority` | `"high"` | No | — |
| `flasharray_replica_snapshot_retention_days` | `30` | No | Retention on replica |
| `flasharray_replica_keep_for_days` | `30` | No | — |

## Example Playbook

```yaml
---
- name: Pure Flasharray Replication
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_replication
```

## Tags

| Tag | Description |
|-----|-------------|
| `dr` | Tasks tagged `dr` |
| `fourth-estate` | Tasks tagged `fourth-estate` |

## License

MIT

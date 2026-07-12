# Role: dragos_sensor_ops

**Purpose**: sensor fleet operations.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `dragos_base_url` | `"https://tenant.dragos.com"` | No | Dragos Platform Connection |
| `dragos_token` | `"{{ lookup('env','DRAGOS_TOKEN') }}"` | No | — |
| `dragos_verify_ssl` | `true` | No | — |
| `artifacts_dir` | `"/tmp/dragos-artifacts"` | No | — |
| `page_size` | `500` | No | — |
| `dry_run` | `true` | No | — |
| `sensor_operation` | `"inventory"` | No | Sensor Operation Mode Options: deploy, configure, health, monitor, update, optimize, backup, inventory |
| `sensors` | `[]` | No | Sensor Inventory Example: [{ name: "sensor-1", id: "abc123", site: "Plant1", mgmt_ip: "10.1.1.10", mgmt_netmask: "255.255.255.0", mgmt_gateway: "10.1.1.1" }] |
| `configure_networking` | `false` | No | Network Configuration |
| `dns_servers` | `(see defaults/main.yml)` | No | — |
| `ntp_servers` | `(see defaults/main.yml)` | No | — |
| `monitor_interfaces` | `[]` | No | Monitoring Interfaces Example: [{ interface: "eth1", zone: "OT-Zone1", vlan_id: 100, mtu: 9000 }] |
| `default_pcap_filter` | `""` | No | BPF filter for packet capture |
| `snapshot_length` | `65535` | No | Packet Capture Settings |
| `capture_buffer_size` | `524288000` | No | 500 MB |
| `packet_buffer_size` | `4096` | No | — |
| `ring_buffer_size` | `8192` | No | — |
| `disable_offload` | `true` | No | — |
| `ot_protocols` | `(see defaults/main.yml)` | No | Industrial Protocol Parsers |
| `deep_protocol_inspection` | `true` | No | — |
| `enable_sampling` | `false` | No | Traffic Sampling |
| `sampling_rate` | `1` | No | 1 in N packets |
| `export_flows` | `true` | No | Flow Export |
| `flow_timeout` | `60` | No | — |
| `active_flow_timeout` | `300` | No | — |
| `configure_storage` | `false` | No | Storage Configuration |
| `pcap_retention_days` | `30` | No | — |
| `pcap_max_storage_gb` | `500` | No | — |
| `pcap_compression` | `true` | No | — |
| `pcap_rotation_policy` | `"size"` | No | Options: size, time |
| `metadata_retention_days` | `90` | No | — |
| `metadata_max_storage_gb` | `100` | No | — |
| `disk_threshold_percent` | `85` | No | — |
| `cleanup_priority` | `["pcap", "logs", "metadata"]` | No | — |
| `storage_warning_threshold` | `80` | No | — |
| `storage_critical_threshold` | `90` | No | — |
| `storage_alert_frequency` | `"daily"` | No | — |
| `performance_tuning` | `false` | No | Performance Tuning |
| `capture_cpu_cores` | `"0-3"` | No | — |
| `analysis_cpu_cores` | `"4-7"` | No | — |
| `numa_aware_processing` | `true` | No | — |
| `packet_buffer_mb` | `2048` | No | — |
| `flow_cache_mb` | `1024` | No | — |
| `asset_cache_mb` | `512` | No | — |
| `protocol_cache_mb` | `512` | No | — |
| `capture_threads` | `4` | No | — |
| `worker_threads` | `8` | No | — |
| `analysis_threads` | `4` | No | — |
| `kernel_bypass_enabled` | `false` | No | — |
| `kernel_bypass_method` | `"af_packet"` | No | Options: af_packet, pf_ring, dpdk |
| `tcp_flow_timeout` | `3600` | No | — |
| `udp_flow_timeout` | `300` | No | — |
| `icmp_flow_timeout` | `60` | No | — |
| `ot_protocol_timeout` | `7200` | No | — |
| `enable_ha` | `false` | No | High Availability |
| `ha_heartbeat_interval` | `5` | No | — |
| `ha_failover_timeout` | `30` | No | — |
| `state_sync_interval` | `10` | No | — |
| `auto_failback` | `false` | No | — |
| `health_check_interval` | `10` | No | — |
| `failure_threshold` | `3` | No | — |
| `sensor_update_version` | `""` | No | Sensor Updates |
| `update_schedule` | `"2025-02-01T02:00:00Z"` | No | — |
| `maintenance_window` | `3600` | No | seconds |
| `backup_before_update` | `true` | No | — |
| `auto_rollback` | `true` | No | — |
| `wait_for_completion` | `true` | No | — |
| `update_max_retries` | `60` | No | — |
| `update_check_interval` | `30` | No | — |
| `packet_drop_threshold` | `5.0` | No | Sensor Health Monitoring percent |
| `backup_description` | `"Scheduled configuration backup"` | No | Sensor Backup |
| `backup_include_pcap` | `false` | No | — |
| `backup_include_logs` | `true` | No | — |
| `wait_for_backup` | `true` | No | — |
| `download_backups` | `true` | No | — |
| `cleanup_old_backups` | `true` | No | — |
| `backup_retention_days` | `90` | No | — |
| `alert_webhook_url` | `""` | No | Alerting |
| `notification_webhook_url` | `""` | No | — |

## Example Playbook

```yaml
- name: Use dragos_sensor_ops
  hosts: all
  gather_facts: false
  roles:
    - role: dragos_sensor_ops
```

## Tags

| Tag | Description |
|-----|-------------|
| `backup` | Tasks tagged `backup` |
| `configure` | Tasks tagged `configure` |
| `deploy` | Tasks tagged `deploy` |
| `ha` | Tasks tagged `ha` |
| `health` | Tasks tagged `health` |
| `inventory` | Tasks tagged `inventory` |
| `maintenance` | Tasks tagged `maintenance` |
| `monitor` | Tasks tagged `monitor` |
| `monitoring` | Tasks tagged `monitoring` |
| `networking` | Tasks tagged `networking` |
| `optimize` | Tasks tagged `optimize` |
| `performance` | Tasks tagged `performance` |
| `report` | Tasks tagged `report` |
| `storage` | Tasks tagged `storage` |
| `update` | Tasks tagged `update` |

## Includes
- `dragos_sensor__inventory.yml`
- `dragos_sensor__deploy.yml`
(You can add `dragos_sensor__upgrade.yml` and `dragos_sensor__tuning.yml` later.)

## License

MIT

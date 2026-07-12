# elasticsearch_config

Elasticsearch Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `elk_stack/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `elasticsearch_cluster_name` | `"fourth-estate-logging"` | No | Cluster configuration |
| `elasticsearch_node_name` | `"{{ ansible_hostname }}"` | No | — |
| `elasticsearch_node_attr_rack` | `"{{ ansible_hostname.split('-')[0] \| default('rack1') }}"` | No | — |
| `elasticsearch_node_attr_zone` | `"{{ ansible_hostname.split('-')[1] \| default('zone1') }}"` | No | — |
| `elasticsearch_node_master` | `true` | No | Node roles |
| `elasticsearch_node_data` | `true` | No | — |
| `elasticsearch_node_data_content` | `true` | No | — |
| `elasticsearch_node_data_hot` | `true` | No | — |
| `elasticsearch_node_data_warm` | `false` | No | — |
| `elasticsearch_node_data_cold` | `false` | No | — |
| `elasticsearch_node_data_frozen` | `false` | No | — |
| `elasticsearch_node_ingest` | `true` | No | — |
| `elasticsearch_node_ml` | `false` | No | — |
| `elasticsearch_node_remote_cluster_client` | `false` | No | — |
| `elasticsearch_node_transform` | `false` | No | — |
| `elasticsearch_network_host` | `"0.0.0.0"` | No | Network settings |
| `elasticsearch_http_host` | `"0.0.0.0"` | No | — |
| `elasticsearch_http_port` | `9200` | No | — |
| `elasticsearch_transport_host` | `"0.0.0.0"` | No | — |
| `elasticsearch_transport_port` | `9300` | No | — |
| `elasticsearch_publish_host` | `"{{ ansible_default_ipv4.address }}"` | No | — |
| `elasticsearch_discovery_seed_hosts` | `[]` | No | Discovery and cluster formation |
| `elasticsearch_cluster_initial_master_nodes` | `[]` | No | — |
| `elasticsearch_path_data` | `"/var/lib/elasticsearch"` | No | Path configuration |
| `elasticsearch_path_logs` | `"/var/log/elasticsearch"` | No | — |
| `elasticsearch_path_repo` | `"/mnt/elasticsearch/snapshots"` | No | — |
| `elasticsearch_bootstrap_memory_lock` | `true` | No | Memory |
| `elasticsearch_gateway_expected_nodes` | `3` | No | Gateway and recovery |
| `elasticsearch_gateway_expected_master_nodes` | `3` | No | — |
| `elasticsearch_gateway_expected_data_nodes` | `3` | No | — |
| `elasticsearch_gateway_recover_after_time` | `"5m"` | No | — |
| `elasticsearch_gateway_recover_after_nodes` | `2` | No | — |
| `elasticsearch_gateway_recover_after_master_nodes` | `2` | No | — |
| `elasticsearch_gateway_recover_after_data_nodes` | `2` | No | — |
| `elasticsearch_cluster_routing_allocation_enable` | `"all"` | No | Cluster-level routing |
| `elasticsearch_cluster_routing_allocation_awareness_attributes` | `["rack", "zone"]` | No | — |
| `elasticsearch_cluster_routing_allocation_disk_threshold_enabled` | `true` | No | — |
| `elasticsearch_cluster_routing_allocation_disk_watermark_low` | `"85%"` | No | — |
| `elasticsearch_cluster_routing_allocation_disk_watermark_high` | `"90%"` | No | — |
| `elasticsearch_cluster_routing_allocation_disk_watermark_flood_stage` | `"95%"` | No | — |
| `elasticsearch_cluster_max_shards_per_node` | `1000` | No | Shard allocation |
| `elasticsearch_cluster_routing_allocation_node_concurrent_recoveries` | `2` | No | — |
| `elasticsearch_cluster_routing_allocation_node_initial_primaries_recoveries` | `4` | No | — |
| `elasticsearch_indices_recovery_max_bytes_per_sec` | `"100mb"` | No | — |
| `elasticsearch_thread_pool_write_queue_size` | `1000` | No | Thread pools |
| `elasticsearch_thread_pool_search_queue_size` | `1000` | No | — |
| `elasticsearch_thread_pool_get_queue_size` | `1000` | No | — |
| `elasticsearch_indices_breaker_total_limit` | `"95%"` | No | Circuit breakers |
| `elasticsearch_indices_breaker_fielddata_limit` | `"40%"` | No | — |
| `elasticsearch_indices_breaker_request_limit` | `"60%"` | No | — |
| `elasticsearch_action_auto_create_index` | `true` | No | Index settings |
| `elasticsearch_action_destructive_requires_name` | `true` | No | — |
| `elasticsearch_index_number_of_shards` | `1` | No | Default index settings |
| `elasticsearch_index_number_of_replicas` | `1` | No | — |
| `elasticsearch_index_refresh_interval` | `"1s"` | No | — |
| `elasticsearch_index_max_result_window` | `10000` | No | — |
| `elasticsearch_ilm_enabled` | `true` | No | Index lifecycle management |
| `elasticsearch_ilm_policies` | `(see defaults/main.yml)` | No | — |
| `elasticsearch_index_templates` | `(see defaults/main.yml)` | No | Index templates |
| `elasticsearch_hot_warm_enabled` | `false` | No | Hot-warm-cold architecture |
| `elasticsearch_node_temperature` | `"hot"` | No | hot, warm, cold, frozen |
| `elasticsearch_snapshot_repositories` | `(see defaults/main.yml)` | No | Snapshot repositories |
| `elasticsearch_remote_clusters` | `[]` | No | Cross-cluster search |
| `elasticsearch_monitoring_enabled` | `true` | No | Monitoring |
| `elasticsearch_monitoring_collection_enabled` | `true` | No | — |
| `elasticsearch_monitoring_collection_interval` | `"10s"` | No | — |
| `elasticsearch_watcher_enabled` | `true` | No | Watcher (alerting) |
| `elasticsearch_ml_enabled` | `false` | No | Machine Learning |
| `elasticsearch_max_ml_node_size` | `0` | No | — |
| `elasticsearch_sql_enabled` | `true` | No | SQL |
| `elasticsearch_log_level` | `"info"` | No | Logging |
| `elasticsearch_slowlog_threshold_query_warn` | `"10s"` | No | — |
| `elasticsearch_slowlog_threshold_query_info` | `"5s"` | No | — |
| `elasticsearch_slowlog_threshold_fetch_warn` | `"1s"` | No | — |
| `elasticsearch_slowlog_threshold_fetch_info` | `"800ms"` | No | — |
| `elasticsearch_slowlog_threshold_index_warn` | `"10s"` | No | — |
| `elasticsearch_slowlog_threshold_index_info` | `"5s"` | No | — |
| `elasticsearch_fourth_estate_mode` | `true` | No | Fourth Estate specific |
| `elasticsearch_retention_days` | `365` | No | — |
| `elasticsearch_compliance_mode` | `true` | No | — |
| `elasticsearch_journalist_logging` | `true` | No | — |
| `elasticsearch_source_protection` | `true` | No | — |

## Example Playbook

```yaml
---
- name: Elasticsearch Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: elk_stack/roles/elasticsearch_config
```

## License

MIT

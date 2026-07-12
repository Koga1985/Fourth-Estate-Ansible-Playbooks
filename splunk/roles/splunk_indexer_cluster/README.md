# splunk_indexer_cluster

Configures a Splunk indexer cluster (cluster master or peer nodes) with replication factor, search factor, pre-defined security indexes, and multisite support.

## Requirements

- Ansible 2.15+
- Splunk Enterprise installed (run `splunk_enterprise_install` role first)
- All cluster nodes must be reachable on management port 8089 and replication port 9887

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `splunk_cluster_mode` | `"peer"` | No | Cluster Configuration Options: master, peer |
| `splunk_cluster_master_uri` | `"https://{{ vault_cluster_master_host }}:8089"` | No | — |
| `splunk_cluster_label` | `"fourth_estate_prod_cluster"` | No | — |
| `splunk_cluster_secret` | `"{{ vault_splunk_cluster_secret }}"` | No | — |
| `splunk_cluster_replication_factor` | `3` | No | Replication Settings |
| `splunk_cluster_search_factor` | `2` | No | — |
| `splunk_replication_port` | `9887` | No | — |
| `splunk_multisite_clustering` | `false` | No | Multisite Clustering |
| `splunk_cluster_site` | `"site1"` | No | — |
| `splunk_cluster_site_replication_factor` | `"origin:2, total:3"` | No | — |
| `splunk_cluster_site_search_factor` | `"origin:1, total:2"` | No | — |
| `splunk_cluster_available_sites` | `"site1, site2, site3"` | No | — |
| `splunk_indexes` | `(see defaults/main.yml)` | No | Index Configuration |
| `splunk_storage_volumes` | `(see defaults/main.yml)` | No | Storage Volumes |
| `splunk_smartstore_enabled` | `false` | No | SmartStore Configuration |
| `splunk_smartstore_provider` | `"aws"` | No | Options: aws, azure, gcp |
| `splunk_smartstore_remote_name` | `"s3_remote"` | No | — |
| `splunk_smartstore_s3_bucket` | `"{{ vault_splunk_smartstore_bucket }}"` | No | AWS S3 SmartStore |
| `splunk_smartstore_s3_region` | `"us-east-1"` | No | — |
| `splunk_smartstore_s3_access_key` | `"{{ vault_aws_access_key }}"` | No | — |
| `splunk_smartstore_s3_secret_key` | `"{{ vault_aws_secret_key }}"` | No | — |
| `splunk_smartstore_s3_endpoint` | `"https://s3.amazonaws.com"` | No | — |
| `splunk_smartstore_s3_server_side_encryption` | `"sse-s3"` | No | — |
| `splunk_smartstore_cache_size_gb` | `100` | No | Cache Settings |
| `splunk_smartstore_max_cache_size` | `"{{ splunk_smartstore_cache_size_gb }}GB"` | No | — |
| `splunk_smartstore_hotlist_recency_secs` | `86400` | No | 1 day |
| `splunk_max_hot_buckets` | `10` | No | Bucket Rolling Policies |
| `splunk_max_warm_db_count` | `300` | No | — |
| `splunk_max_data_size` | `"auto_high_volume"` | No | — |
| `splunk_max_hot_idle_secs` | `86400` | No | — |
| `splunk_max_hot_span_secs` | `7776000` | No | 90 days |
| `splunk_security_retention_days` | `365` | No | Data Retention Policies (Fourth Estate compliance) |
| `splunk_audit_retention_days` | `730` | No | 2 years |
| `splunk_application_retention_days` | `90` | No | — |
| `splunk_infrastructure_retention_days` | `180` | No | — |
| `splunk_compress_rawdata` | `true` | No | Compression Settings |
| `splunk_rawdata_compression_level` | `6` | No | — |
| `splunk_enable_auto_repair` | `true` | No | Bucket Repair |
| `splunk_rebuild_metadata` | `true` | No | — |
| `splunk_cluster_master_apps` | `[]` | No | Cluster Master Apps |
| `splunk_cluster_peer_networks` | `(see defaults/main.yml)` | No | Cluster Peer Networks (for replication) |
| `splunk_enable_cluster_monitoring` | `true` | No | Monitoring and Health |
| `splunk_cluster_health_check_interval` | `300` | No | seconds |
| `splunk_max_concurrent_uploads` | `10` | No | Performance Tuning |
| `splunk_max_concurrent_downloads` | `10` | No | — |
| `splunk_upload_timeout` | `3600` | No | — |
| `splunk_download_timeout` | `3600` | No | — |
| `splunk_parallel_ingestion_pipelines` | `2` | No | Index Parallelization |
| `splunk_home` | `"/opt/splunk"` | No | Splunk Variables |
| `splunk_db_path` | `"/opt/splunk/var/lib/splunk"` | No | — |
| `splunk_user` | `"splunk"` | No | — |
| `splunk_group` | `"splunk"` | No | — |
| `splunk_admin_user` | `"admin"` | No | — |
| `splunk_admin_password` | `"{{ vault_splunk_admin_password }}"` | No | — |
| `splunk_management_port` | `8089` | No | — |

## Example Playbook

```yaml
---
# Run on the cluster master first
- name: Configure Splunk Cluster Master
  hosts: splunk_master
  become: true
  roles:
    - role: splunk/roles/splunk_indexer_cluster
      vars:
        splunk_cluster_mode: "master"
        splunk_cluster_replication_factor: 3
        splunk_cluster_search_factor: 2

# Then run on all peers
- name: Configure Splunk Indexer Peers
  hosts: splunk_indexers
  become: true
  roles:
    - role: splunk/roles/splunk_indexer_cluster
      vars:
        splunk_cluster_mode: "peer"
```

## License

MIT

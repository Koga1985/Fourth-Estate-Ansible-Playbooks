# splunk_indexer_cluster

Configures a Splunk indexer cluster (cluster master or peer nodes) with replication factor, search factor, pre-defined security indexes, and multisite support.

## Requirements

- Ansible 2.15+
- Splunk Enterprise installed (run `splunk_enterprise_install` role first)
- All cluster nodes must be reachable on management port 8089 and replication port 9887

## Role Variables

### Required

| Variable | Description |
|----------|-------------|
| `vault_splunk_cluster_secret` | Shared cluster security key (in vault.yml) |
| `vault_cluster_master_host` | Cluster master hostname (in vault.yml) |

### Key Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `splunk_cluster_mode` | `"peer"` | **Yes** | `master` for cluster master, `peer` for indexer peer |
| `splunk_cluster_replication_factor` | `3` | No | Number of copies of each bucket |
| `splunk_cluster_search_factor` | `2` | No | Number of searchable copies |
| `splunk_multisite_clustering` | `false` | No | Enable multisite clustering |
| `splunk_indexes` | Security/firewall/syslog indexes | No | List of index definitions |

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

# elasticsearch_config

Elasticsearch Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `elk_stack/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `elasticsearch_cluster_name` | `"fourth-estate-logging"` |  |
| `elasticsearch_node_name` | `"{{ ansible_hostname }}"` |  |
| `elasticsearch_node_attr_rack` | `"{{ ansible_hostname.split('-')[0] | default('r...` |  |
| `elasticsearch_node_attr_zone` | `"{{ ansible_hostname.split('-')[1] | default('z...` |  |
| `elasticsearch_node_master` | `true` |  |
| `elasticsearch_node_data` | `true` |  |
| `elasticsearch_node_data_content` | `true` |  |
| `elasticsearch_node_data_hot` | `true` |  |
| `elasticsearch_node_data_warm` | `false` |  |
| `elasticsearch_node_data_cold` | `false` |  |
| `elasticsearch_node_data_frozen` | `false` |  |
| `elasticsearch_node_ingest` | `true` |  |
| `elasticsearch_node_ml` | `false` |  |
| `elasticsearch_node_remote_cluster_client` | `false` |  |
| `elasticsearch_node_transform` | `false` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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

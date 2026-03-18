# elasticsearch_install

Elasticsearch Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `elk_stack/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `elasticsearch_version` | `"8.11.3"` |  |
| `elasticsearch_major_version` | `"8.x"` |  |
| `elasticsearch_install_method` | `"package"` | No | package, archive |
| `elasticsearch_use_official_repo` | `true` |  |
| `elasticsearch_repo_gpg_key` | `"https://artifacts.elastic.co/GPG-KEY-elasticse...` |  |
| `elasticsearch_user` | `"elasticsearch"` |  |
| `elasticsearch_group` | `"elasticsearch"` |  |
| `elasticsearch_home` | `"/usr/share/elasticsearch"` |  |
| `elasticsearch_config_dir` | `"/etc/elasticsearch"` |  |
| `elasticsearch_data_dir` | `"/var/lib/elasticsearch"` |  |
| `elasticsearch_log_dir` | `"/var/log/elasticsearch"` |  |
| `elasticsearch_pid_dir` | `"/var/run/elasticsearch"` |  |
| `elasticsearch_java_home` | `""` | No | Auto-detect if empty |
| `elasticsearch_heap_size` | `"{{ (ansible_memtotal_mb * 0.5) | int | min(327...` |  |
| `elasticsearch_heap_size_min` | `"{{ elasticsearch_heap_size }}"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Elasticsearch Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: elk_stack/roles/elasticsearch_install
```

## License

MIT

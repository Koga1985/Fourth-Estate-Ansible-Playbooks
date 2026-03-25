# elasticsearch_cluster

Elasticsearch Cluster role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/elk_stack/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Elasticsearch Cluster
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/elk_stack/roles/elasticsearch_cluster
```

## License

MIT

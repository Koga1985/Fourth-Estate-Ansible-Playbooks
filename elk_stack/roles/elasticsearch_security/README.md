# elasticsearch_security

Elasticsearch Security role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `elk_stack/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `elasticsearch_security_enabled` | `true` |  |
| `elasticsearch_security_auto_configure` | `true` |  |
| `elasticsearch_tls_enabled` | `true` |  |
| `elasticsearch_tls_transport_enabled` | `true` |  |
| `elasticsearch_tls_http_enabled` | `true` |  |
| `elasticsearch_certs_dir` | `"/etc/elasticsearch/certs"` |  |
| `elasticsearch_ca_cert_path` | `"{{ elasticsearch_certs_dir }}/ca/ca.crt"` |  |
| `elasticsearch_ca_key_path` | `"{{ elasticsearch_certs_dir }}/ca/ca.key"` |  |
| `elasticsearch_node_cert_path` | `"{{ elasticsearch_certs_dir }}/{{ ansible_hostn...` |  |
| `elasticsearch_node_key_path` | `"{{ elasticsearch_certs_dir }}/{{ ansible_hostn...` |  |
| `elasticsearch_generate_ca` | `true` |  |
| `elasticsearch_generate_node_certs` | `true` |  |
| `elasticsearch_cert_validity_days` | `3650` |  |
| `elasticsearch_cert_key_size` | `4096` |  |
| `elasticsearch_cert_country` | `"US"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Elasticsearch Security
  hosts: localhost
  gather_facts: false
  roles:
    - role: elk_stack/roles/elasticsearch_security
```

## License

MIT

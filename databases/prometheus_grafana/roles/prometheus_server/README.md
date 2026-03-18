# prometheus_server

Prometheus Server role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/prometheus_grafana/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Prometheus Server
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/prometheus_grafana/roles/prometheus_server
```

## License

MIT

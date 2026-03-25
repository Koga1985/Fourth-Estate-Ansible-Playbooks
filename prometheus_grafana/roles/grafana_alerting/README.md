# grafana_alerting

Grafana Alerting role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/prometheus_grafana/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Grafana Alerting
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/prometheus_grafana/roles/grafana_alerting
```

## License

MIT

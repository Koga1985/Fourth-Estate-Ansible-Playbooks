# prometheus_exporters

Prometheus Exporters role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `prometheus_grafana/README.md`

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Prometheus Exporters
  hosts: all
  become: true
  roles:
    - role: prometheus_grafana/roles/prometheus_exporters
```

## License

MIT

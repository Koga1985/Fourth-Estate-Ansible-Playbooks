# tenable_scan_zones

Tenable Scan Zones role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `tenable/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `tsc_host` | `"{{ ansible_fqdn }}"` | No | Connection Settings |
| `tsc_port` | `443` | No | — |
| `tsc_username` | `"admin"` | No | — |
| `tsc_password` | `"{{ vault_tsc_password }}"` | No | — |
| `tsc_validate_certs` | `true` | No | — |
| `tsc_scan_zones` | `(see defaults/main.yml)` | No | Scan Zones - Fourth Estate Network Segments |

## Example Playbook

```yaml
---
- name: Tenable Scan Zones
  hosts: localhost
  gather_facts: false
  roles:
    - role: tenable/roles/tenable_scan_zones
```

## License

MIT

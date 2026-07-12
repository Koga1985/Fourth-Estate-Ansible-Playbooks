# tenable_scan_policies

Tenable Scan Policies role for Fourth Estate infrastructure automation.

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
| `tsc_scan_policies` | `(see defaults/main.yml)` | No | Standard Scan Policies for Fourth Estate |
| `tsc_custom_policies` | `[]` | No | Custom Policies |
| `tsc_scan_settings` | `(see defaults/main.yml)` | No | Default Scan Settings |

## Example Playbook

```yaml
---
- name: Tenable Scan Policies
  hosts: localhost
  gather_facts: false
  roles:
    - role: tenable/roles/tenable_scan_policies
```

## License

MIT

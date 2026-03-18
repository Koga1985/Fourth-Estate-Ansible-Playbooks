# tenable_scan_policies

Tenable Scan Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `tenable/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `tsc_host` | `"{{ ansible_fqdn }}"` |  |
| `tsc_port` | `443` |  |
| `tsc_username` | `"admin"` |  |
| `tsc_password` | `"{{ vault_tsc_password }}"` |  |
| `tsc_validate_certs` | `true` |  |
| `tsc_custom_policies` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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

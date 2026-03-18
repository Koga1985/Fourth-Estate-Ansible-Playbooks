# panos_objects

Panos Objects role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `palo_alto/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `panos_ip_wildcard_objects` | `[]` |  |
| `panos_registered_ips` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `paloaltonetworks.panos`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Panos Objects
  hosts: localhost
  gather_facts: false
  roles:
    - role: palo_alto/roles/panos_objects
```

## License

MIT

# vast_monitoring

Vast Monitoring role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vast/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `vast_mgmt_host` | `"{{ vault_vast_mgmt_host }}"` |  |
| `vast_mgmt_port` | `443` |  |
| `vast_mgmt_user` | `"{{ vault_vast_mgmt_user }}"` |  |
| `vast_mgmt_password` | `"{{ vault_vast_mgmt_password }}"` |  |
| `vast_api_version` | `"v1"` |  |
| `vast_verify_ssl` | `true` |  |
| `vast_enable_snmp` | `true` |  |
| `vast_snmp_version` | `"3"` | Only SNMPv3 for DoD compliance |
| `vast_snmp_community` | `"{{ vault_vast_snmp_community }}"` |  |
| `vast_snmp_user` | `"{{ vault_vast_snmp_user | default('vastmonitor...` |  |
| `vast_snmp_auth_protocol` | `"SHA256"` | SHA256 for FIPS compliance |
| `vast_snmp_auth_password` | `"{{ vault_vast_snmp_auth_password | default('')...` |  |
| `vast_snmp_priv_protocol` | `"AES256"` | AES256 for FIPS compliance |
| `vast_snmp_priv_password` | `"{{ vault_vast_snmp_priv_password | default('')...` |  |
| `vast_enable_syslog` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Vast Monitoring
  hosts: localhost
  gather_facts: false
  roles:
    - role: vast/roles/vast_monitoring
```

## License

MIT

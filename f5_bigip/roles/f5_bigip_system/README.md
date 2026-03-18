# f5_bigip_system

F5 Bigip System role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `f5_bigip/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `f5_bigip_hostname` | `"{{ inventory_hostname_short }}"` |  |
| `f5_bigip_domain` | `"agency.gov"` |  |
| `f5_bigip_description` | `"F5 BIG-IP Load Balancer - Fourth Estate"` |  |
| `f5_bigip_contact` | `"netops@agency.gov"` |  |
| `f5_bigip_location` | `"Data Center 1"` |  |
| `f5_bigip_timezone` | `"America/New_York"` |  |
| `f5_bigip_snmp_enabled` | `true` |  |
| `f5_bigip_snmp_v3_enabled` | `true` |  |
| `f5_bigip_snmp_location` | `"{{ f5_bigip_location }}"` |  |
| `f5_bigip_snmp_contact` | `"{{ f5_bigip_contact }}"` |  |
| `f5_bigip_syslog_enabled` | `true` |  |
| `f5_bigip_audit_log_enabled` | `true` |  |
| `f5_bigip_ssh_enabled` | `true` |  |
| `f5_bigip_ssh_port` | `22` |  |
| `f5_bigip_ssh_banner` | `"Authorized access only. All activity monitored."` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `f5networks.f5_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: F5 Bigip System
  hosts: localhost
  gather_facts: false
  roles:
    - role: f5_bigip/roles/f5_bigip_system
```

## License

MIT

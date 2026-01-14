# ucs_prod_monitoring

Cisco UCS production monitoring and compliance role.

## Description

Configures comprehensive monitoring for Cisco UCS including SNMP, Call Home, and health checks with compliance reporting.

## Features

- SNMP v2c/v3 configuration
- SNMP trap destinations
- Call Home configuration
- System health monitoring
- Power and thermal monitoring
- Compliance monitoring checklists

## Requirements

- Ansible >= 2.9
- Cisco UCS Ansible collection

## Variables

See `defaults/main.yml` for configuration options.

## Example Playbook

```yaml
- name: Configure UCS Monitoring
  hosts: localhost
  roles:
    - role: ucs_prod_monitoring
      vars:
        apply_changes: true
        monitoring_enable_snmp: true
```

## License

MIT

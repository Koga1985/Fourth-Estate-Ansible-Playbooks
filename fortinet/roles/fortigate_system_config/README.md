# fortigate_system_config

Fortigate System Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `fortinet/README.md`

## Requirements

- Ansible 2.15+
- Collection: `fortinet.fortios`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `fortigate_host` | `"{{ ansible_host }}"` | No | FortiGate connection parameters |
| `fortigate_username` | `"{{ vault_fortigate_username \| default('admin') }}"` | No | — |
| `fortigate_password` | `"{{ vault_fortigate_password }}"` | No | — |
| `fortigate_api_token` | `"{{ vault_fortigate_api_token \| default('') }}"` | No | — |
| `fortigate_vdom` | `"root"` | No | — |
| `fortigate_https` | `true` | No | — |
| `fortigate_validate_certs` | `true` | No | — |
| `fortigate_hostname` | `"{{ inventory_hostname_short }}"` | No | System hostname and domain |
| `fortigate_domain` | `"{{ domain_name \| default('gov.local') }}"` | No | — |
| `fortigate_timezone` | `"85"` | No | Timezone configuration US/Eastern (see FortiGate timezone codes) |
| `fortigate_dns_primary` | `"{{ dns_primary \| default('10.0.0.10') }}"` | No | DNS servers (Fourth Estate compliance) |
| `fortigate_dns_secondary` | `"{{ dns_secondary \| default('10.0.0.11') }}"` | No | — |
| `fortigate_ntp_servers` | `(see defaults/main.yml)` | No | NTP servers (DoD/DISA approved) |
| `fortigate_ntp_sync_interval` | `60` | No | — |
| `fortigate_admin_accounts` | `(see defaults/main.yml)` | No | Admin accounts with RBAC |
| `fortigate_snmp_enabled` | `true` | No | SNMP v3 configuration (DISA STIG compliant) |
| `fortigate_snmp_v3_users` | `(see defaults/main.yml)` | No | — |
| `fortigate_snmp_community` | `(see defaults/main.yml)` | No | — |
| `fortigate_global_settings` | `(see defaults/main.yml)` | No | Global system settings |
| `fortigate_performance_tuning` | `(see defaults/main.yml)` | No | System performance tuning |
| `fortigate_pre_login_banner` | `(multi-line text — see defaults/main.yml)` | No | Banner configuration (Fourth Estate requirements) |
| `fortigate_post_login_banner` | `""` | No | — |
| `fortigate_ssh_config` | `(see defaults/main.yml)` | No | SSH configuration (DISA STIG compliant) |
| `fortigate_ssl_config` | `(see defaults/main.yml)` | No | SSL/TLS configuration (DISA STIG compliant) |
| `fortigate_certificates` | `[]` | No | Certificate management |
| `fortigate_mgmt_interface` | `"port1"` | No | System interface for management |
| `fortigate_mgmt_allowaccess` | `"https ping ssh snmp"` | No | — |
| `fortigate_password_policy` | `(see defaults/main.yml)` | No | Password policy (Fourth Estate compliance) |
| `fortigate_fortiguard` | `(see defaults/main.yml)` | No | Fortiguard settings |
| `fortigate_email_server` | `(see defaults/main.yml)` | No | Email server for alerts |
| `fortigate_syslog_enabled` | `true` | No | Syslog settings (basic - detailed in logging role) |
| `fortigate_syslog_servers` | `(see defaults/main.yml)` | No | — |
| `fortigate_automation_enabled` | `true` | No | Automation stitches for alerting |
| `fortigate_replacement_messages` | `[]` | No | Replacement messages |

## Example Playbook

```yaml
---
- name: Fortigate System Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: fortinet/roles/fortigate_system_config
```

## Tags

| Tag | Description |
|-----|-------------|
| `config` | Tasks tagged `config` |
| `fortigate` | Tasks tagged `fortigate` |
| `system` | Tasks tagged `system` |

## License

MIT

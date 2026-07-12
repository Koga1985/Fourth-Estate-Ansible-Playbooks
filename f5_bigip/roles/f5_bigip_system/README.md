# f5_bigip_system

F5 Bigip System role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `f5_bigip/README.md`

## Requirements

- Ansible 2.15+
- Collection: `f5networks.f5_modules`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `f5_bigip_provider` | `(see defaults/main.yml)` | No | F5 BIG-IP Connection Details |
| `f5_bigip_hostname` | `"{{ inventory_hostname_short }}"` | No | System Identification |
| `f5_bigip_domain` | `"agency.gov"` | No | — |
| `f5_bigip_description` | `"F5 BIG-IP Load Balancer - Fourth Estate"` | No | — |
| `f5_bigip_contact` | `"netops@agency.gov"` | No | — |
| `f5_bigip_location` | `"Data Center 1"` | No | — |
| `f5_bigip_timezone` | `"America/New_York"` | No | Time Configuration |
| `f5_bigip_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `f5_bigip_dns_nameservers` | `(see defaults/main.yml)` | No | DNS Configuration |
| `f5_bigip_dns_search_domains` | `(see defaults/main.yml)` | No | — |
| `f5_bigip_snmp_enabled` | `true` | No | SNMP Configuration (SNMPv3 for security) |
| `f5_bigip_snmp_v3_enabled` | `true` | No | — |
| `f5_bigip_snmp_location` | `"{{ f5_bigip_location }}"` | No | — |
| `f5_bigip_snmp_contact` | `"{{ f5_bigip_contact }}"` | No | — |
| `f5_bigip_snmp_allowed_addresses` | `(see defaults/main.yml)` | No | — |
| `f5_bigip_snmp_v3_users` | `(see defaults/main.yml)` | No | — |
| `f5_bigip_syslog_enabled` | `true` | No | Syslog Configuration |
| `f5_bigip_syslog_servers` | `(see defaults/main.yml)` | No | — |
| `f5_bigip_audit_log_enabled` | `true` | No | Audit Logging |
| `f5_bigip_audit_remote_servers` | `(see defaults/main.yml)` | No | — |
| `f5_bigip_ssh_enabled` | `true` | No | SSH Configuration (Hardening) |
| `f5_bigip_ssh_port` | `22` | No | — |
| `f5_bigip_ssh_access_addresses` | `(see defaults/main.yml)` | No | — |
| `f5_bigip_ssh_banner` | `"Authorized access only. All activity monitored."` | No | — |
| `f5_bigip_ssh_timeout` | `300` | No | — |
| `f5_bigip_httpd_enabled` | `true` | No | HTTP/HTTPS Management Access |
| `f5_bigip_httpd_ssl_port` | `443` | No | — |
| `f5_bigip_httpd_redirect_http_to_https` | `true` | No | — |
| `f5_bigip_httpd_allow_addresses` | `(see defaults/main.yml)` | No | — |
| `f5_bigip_httpd_ssl_protocol` | `"all -SSLv2 -SSLv3 -TLSv1 -TLSv1.1"` | No | — |
| `f5_bigip_httpd_ssl_ciphersuite` | `"DEFAULT:!aNULL:!eNULL:!LOW:!RC4:!MD5:!EXP"` | No | — |
| `f5_bigip_password_policy` | `(see defaults/main.yml)` | No | Password Policy (DISA STIG Compliant) |
| `f5_bigip_admin_users` | `[]` | No | Admin User Settings |
| `f5_bigip_license_key` | `"{{ vault_f5_license_key \| default(omit) }}"` | No | License Management |
| `f5_bigip_license_check` | `true` | No | — |
| `f5_bigip_gui_security_banner` | `true` | No | GUI Security Settings |
| `f5_bigip_gui_security_banner_text` | `(multi-line text — see defaults/main.yml)` | No | — |
| `f5_bigip_auto_check_updates` | `false` | No | Software Updates |
| `f5_bigip_auto_phonehome` | `false` | No | — |
| `f5_bigip_database_encryption_enabled` | `true` | No | Database Encryption |
| `f5_bigip_fips_enabled` | `false` | No | FIPS Mode Enable if hardware supports |
| `f5_bigip_management_interface` | `"mgmt"` | No | Interface Settings |
| `f5_bigip_management_mtu` | `1500` | No | — |
| `f5_bigip_db_variables` | `(see defaults/main.yml)` | No | System Performance |
| `f5_bigip_save_config` | `true` | No | Save Configuration |

## Example Playbook

```yaml
---
- name: F5 Bigip System
  hosts: localhost
  gather_facts: false
  roles:
    - role: f5_bigip/roles/f5_bigip_system
```

## Tags

| Tag | Description |
|-----|-------------|
| `f5_dns` | Tasks tagged `f5_dns` |
| `f5_hardening` | Tasks tagged `f5_hardening` |
| `f5_hostname` | Tasks tagged `f5_hostname` |
| `f5_httpd` | Tasks tagged `f5_httpd` |
| `f5_license` | Tasks tagged `f5_license` |
| `f5_ntp` | Tasks tagged `f5_ntp` |
| `f5_password_policy` | Tasks tagged `f5_password_policy` |
| `f5_performance` | Tasks tagged `f5_performance` |
| `f5_save` | Tasks tagged `f5_save` |
| `f5_security` | Tasks tagged `f5_security` |
| `f5_snmp` | Tasks tagged `f5_snmp` |
| `f5_ssh` | Tasks tagged `f5_ssh` |
| `f5_syslog` | Tasks tagged `f5_syslog` |
| `f5_system` | Tasks tagged `f5_system` |
| `f5_users` | Tasks tagged `f5_users` |

## License

MIT

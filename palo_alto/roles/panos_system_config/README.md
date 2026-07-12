# panos_system_config

Panos System Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `palo_alto/README.md`

## Requirements

- Ansible 2.15+
- Collection: `paloaltonetworks.panos`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `panos_provider` | `(see defaults/main.yml)` | No | PAN-OS provider connection details |
| `panos_hostname` | `"fw01"` | No | System identification |
| `panos_domain` | `"example.local"` | No | — |
| `panos_timezone` | `"America/New_York"` | No | — |
| `panos_dns_primary` | `"8.8.8.8"` | No | DNS configuration |
| `panos_dns_secondary` | `"8.8.4.4"` | No | — |
| `panos_ntp_primary` | `"time.nist.gov"` | No | NTP configuration (Fourth Estate should use internal NTP) |
| `panos_ntp_secondary` | `"time.google.com"` | No | — |
| `panos_login_banner` | `(multi-line text — see defaults/main.yml)` | No | Login banner (DISA STIG compliant) |
| `panos_idle_timeout` | `10` | No | Session timeout (in minutes) |
| `panos_global_session_timeout` | `15` | No | — |
| `panos_password_min_length` | `15` | No | Password complexity requirements (DISA STIG compliant) |
| `panos_password_min_uppercase` | `1` | No | — |
| `panos_password_min_lowercase` | `1` | No | — |
| `panos_password_min_numeric` | `1` | No | — |
| `panos_password_min_special` | `1` | No | — |
| `panos_password_block_repeated` | `3` | No | — |
| `panos_password_history_count` | `24` | No | — |
| `panos_password_differs_by` | `4` | No | — |
| `panos_password_expiration_days` | `90` | No | — |
| `panos_password_expiration_warning_days` | `14` | No | — |
| `panos_password_post_expiration_logins` | `0` | No | — |
| `panos_password_post_expiration_grace_days` | `0` | No | — |
| `panos_administrators` | `(see defaults/main.yml)` | No | Administrator accounts |
| `panos_radius_profiles` | `(see defaults/main.yml)` | No | RADIUS authentication for MFA |
| `panos_radius_server_profiles` | `(see defaults/main.yml)` | No | — |
| `panos_tacacs_profiles` | `[]` | No | TACACS+ authentication (alternative to RADIUS) |
| `panos_tacacs_server_profiles` | `[]` | No | — |
| `panos_enable_snmp` | `true` | No | SNMPv3 configuration (read-only monitoring) |
| `panos_snmp_v3_servers` | `(see defaults/main.yml)` | No | — |
| `panos_certificates` | `(see defaults/main.yml)` | No | Certificate management |
| `panos_mgmt_ssl_profile` | `"mgmt_ssl"` | No | SSL/TLS service profile for management |
| `panos_mgmt_ssl_certificate` | `"mgmt_cert"` | No | — |
| `panos_mgmt_ssl_min_version` | `"tls1-2"` | No | — |
| `panos_mgmt_ssl_max_version` | `"tls1-3"` | No | — |
| `panos_syslog_servers` | `(see defaults/main.yml)` | No | Syslog forwarding to SIEM (Splunk, ELK, etc.) |
| `panos_syslog_profiles` | `(see defaults/main.yml)` | No | — |
| `panos_threat_update_schedule` | `"daily"` | No | Automatic content updates |
| `panos_threat_update_time` | `"02:00"` | No | — |
| `panos_threat_update_threshold` | `24` | No | — |
| `panos_av_update_schedule` | `"daily"` | No | — |
| `panos_av_update_time` | `"03:00"` | No | — |
| `panos_permitted_mgmt_ips` | `(see defaults/main.yml)` | No | Management access control |
| `panos_require_audit_comment` | `true` | No | Audit and compliance |

## Example Playbook

```yaml
---
- name: Panos System Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: palo_alto/roles/panos_system_config
```

## Tags

| Tag | Description |
|-----|-------------|
| `admin` | Tasks tagged `admin` |
| `audit` | Tasks tagged `audit` |
| `banner` | Tasks tagged `banner` |
| `certificates` | Tasks tagged `certificates` |
| `hardening` | Tasks tagged `hardening` |
| `hostname` | Tasks tagged `hostname` |
| `logging` | Tasks tagged `logging` |
| `management` | Tasks tagged `management` |
| `mfa` | Tasks tagged `mfa` |
| `password` | Tasks tagged `password` |
| `radius` | Tasks tagged `radius` |
| `snmp` | Tasks tagged `snmp` |
| `ssl` | Tasks tagged `ssl` |
| `syslog` | Tasks tagged `syslog` |
| `system` | Tasks tagged `system` |
| `tacacs` | Tasks tagged `tacacs` |
| `timeout` | Tasks tagged `timeout` |
| `updates` | Tasks tagged `updates` |

## License

MIT

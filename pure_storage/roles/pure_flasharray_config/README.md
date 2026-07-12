# pure_flasharray_config

Pure Flasharray Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` | No | Array connection |
| `flasharray_name` | `"{{ inventory_hostname_short }}-fa"` | No | Array name |
| `flasharray_idle_timeout` | `30` | No | Session timeout (minutes) |
| `flasharray_login_banner` | `(multi-line text — see defaults/main.yml)` | No | Login banner |
| `flasharray_ad_enabled` | `false` | No | Active Directory integration |
| `flasharray_ldap_enabled` | `false` | No | LDAP integration |
| `flasharray_saml_enabled` | `false` | No | SAML SSO configuration |
| `flasharray_multi_admin_enabled` | `true` | No | Multi-admin approval (requires 2+ admins for sensitive operations) |
| `flasharray_smtp_sender_domain` | `"{{ domain_name \| default('example.com') }}"` | No | SMTP configuration |
| `flasharray_smtp_relay_host` | `"{{ smtp_relay \| default('smtp.example.com') }}"` | No | — |
| `flasharray_alert_recipients` | `(see defaults/main.yml)` | No | Alert recipients |
| `flasharray_syslog_servers` | `(see defaults/main.yml)` | No | Syslog servers |
| `flasharray_ntp_servers` | `(see defaults/main.yml)` | No | NTP configuration |
| `flasharray_phonehome_enabled` | `true` | No | Phone home (Pure1 support connection) |
| `flasharray_support_proxy_enabled` | `false` | No | Support proxy |
| `flasharray_safemode_enabled` | `true` | No | SafeMode (immutable snapshots for ransomware protection) |
| `flasharray_audit_retention_days` | `365` | No | Audit log retention |
| `flasharray_organization` | `"Fourth Estate"` | No | Fourth Estate specific |
| `flasharray_compliance_mode` | `"high-security"` | No | — |
| `flasharray_data_classification` | `"confidential"` | No | — |
| `flasharray_backup_location` | `"offsite-dr"` | No | — |
| `flasharray_min_tls_version` | `"1.2"` | No | Security settings |
| `flasharray_fips_mode` | `true` | No | — |
| `flasharray_secure_erase_enabled` | `true` | No | — |

## Example Playbook

```yaml
---
- name: Pure Flasharray Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_config
```

## License

MIT

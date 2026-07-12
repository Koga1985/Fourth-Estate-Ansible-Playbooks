# pure_flasharray_install

Pure Flasharray Install role for Fourth Estate infrastructure automation.

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
| `flasharray_name` | `"{{ inventory_hostname_short }}-fa"` | No | Array identification |
| `flasharray_management_interfaces` | `(see defaults/main.yml)` | No | Management network |
| `flasharray_dns_domain` | `"{{ domain_name \| default('example.com') }}"` | No | DNS configuration |
| `flasharray_dns_servers` | `(see defaults/main.yml)` | No | — |
| `flasharray_ntp_servers` | `(see defaults/main.yml)` | No | NTP configuration |
| `flasharray_timezone` | `"America/New_York"` | No | Timezone |
| `flasharray_phonehome_enabled` | `true` | No | Phone home (support connection) |
| `flasharray_support_proxy_enabled` | `false` | No | Support proxy |
| `flasharray_smtp_enabled` | `true` | No | SMTP configuration for alerts |
| `flasharray_smtp_sender_domain` | `"{{ domain_name \| default('example.com') }}"` | No | — |
| `flasharray_smtp_relay_host` | `"{{ smtp_relay \| default('smtp.example.com') }}"` | No | — |
| `flasharray_alert_recipients` | `(see defaults/main.yml)` | No | Alert recipients |
| `flasharray_syslog_servers` | `(see defaults/main.yml)` | No | Syslog servers |
| `flasharray_idle_timeout` | `30` | No | Session timeout (minutes) |
| `flasharray_auto_update` | `false` | No | Automatic updates |
| `flasharray_organization` | `"Fourth Estate"` | No | Fourth Estate specific settings |
| `flasharray_location` | `"{{ datacenter_name \| default('DC1') }}"` | No | — |
| `flasharray_contact` | `"storage-team@{{ domain_name \| default('example.com') }}"` | No | — |
| `flasharray_fips_mode` | `true` | No | Compliance and security |
| `flasharray_audit_retention_days` | `365` | No | — |
| `flasharray_secure_erase_enabled` | `true` | No | — |
| `flasharray_pure1_enabled` | `true` | No | Pure1 cloud monitoring |

## Example Playbook

```yaml
---
- name: Pure Flasharray Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_install
```

## License

MIT

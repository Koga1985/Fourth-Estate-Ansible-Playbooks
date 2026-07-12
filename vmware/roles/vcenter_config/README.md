# vcenter_config

Vcenter Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vmware/README.md`

## Requirements

- Ansible 2.15+
- Collection: `community.vmware`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vcenter_hostname` | `"vcsa.example.mil"` | No | vCenter connection |
| `vcenter_username` | `"administrator@vsphere.local"` | No | — |
| `vcenter_password` | `""` | No | — |
| `vcenter_validate_certs` | `false` | No | — |
| `vcenter_server_name` | `"Production vCenter"` | No | vCenter instance configuration |
| `vcenter_instance_id` | `""` | No | — |
| `vcenter_db_max_connections` | `100` | No | Database settings |
| `vcenter_task_retention_days` | `30` | No | — |
| `vcenter_event_retention_days` | `30` | No | — |
| `vcenter_timeout_normal` | `30` | No | Timeout settings (seconds) |
| `vcenter_timeout_long` | `120` | No | — |
| `vcenter_log_level` | `"info"` | No | Logging verbose\|info\|warning\|error |
| `vcenter_ntp_servers` | `(see defaults/main.yml)` | No | NTP Configuration |
| `vcenter_dns_servers` | `(see defaults/main.yml)` | No | DNS Configuration |
| `vcenter_smtp_server` | `""` | No | Mail/SMTP Configuration |
| `vcenter_smtp_port` | `25` | No | — |
| `vcenter_smtp_sender` | `"vcenter@example.mil"` | No | — |
| `vcenter_smtp_auth_enabled` | `false` | No | — |
| `vcenter_smtp_username` | `""` | No | — |
| `vcenter_smtp_password` | `""` | No | — |
| `vcenter_smtp_starttls` | `true` | No | — |
| `vcenter_syslog_server` | `""` | No | Syslog Configuration |
| `vcenter_syslog_port` | `514` | No | — |
| `vcenter_syslog_protocol` | `"tcp"` | No | tcp\|udp |
| `vcenter_snmp_enabled` | `false` | No | SNMP Configuration |
| `vcenter_snmp_syscontact` | `"admin@example.mil"` | No | — |
| `vcenter_snmp_syslocation` | `"Datacenter 1"` | No | — |
| `vcenter_snmp_communities` | `[]` | No | — |
| `vcenter_snmp_users` | `[]` | No | — |
| `vcenter_tls_enforcement` | `true` | No | TLS/SSL Settings (STIG Compliance) |
| `vcenter_tls_min_version` | `"TLSv1.2"` | No | — |
| `vcenter_session_timeout` | `30` | No | Session timeout (minutes) - STIG requirement |
| `vcenter_identity_sources` | `[]` | No | Active Directory / LDAP Integration |
| `fourth_estate_mode` | `false` | No | Fourth Estate Mode |
| `fourth_estate_syslog_server` | `"syslog.example.mil"` | No | Fourth Estate Settings |
| `fourth_estate_syslog_port` | `6514` | No | — |
| `fourth_estate_syslog_protocol` | `"tcp"` | No | — |
| `fourth_estate_servicenow_enabled` | `false` | No | — |
| `fourth_estate_servicenow_url` | `""` | No | — |
| `fourth_estate_servicenow_user` | `""` | No | — |
| `fourth_estate_servicenow_password` | `""` | No | — |
| `fourth_estate_servicenow_sync_interval` | `3600` | No | — |
| `fourth_estate_evidence_datastore` | `"Evidence_Storage"` | No | — |
| `fourth_estate_disable_console` | `true` | No | — |
| `fourth_estate_disable_dcui` | `true` | No | — |
| `fourth_estate_custom_roles` | `(see defaults/main.yml)` | No | Fourth Estate Custom Roles |
| `vcenter_advanced_settings` | `[]` | No | Advanced vCenter Settings |

## Example Playbook

```yaml
---
- name: Vcenter Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: vmware/roles/vcenter_config
```

## License

MIT

# infoblox_dhcp_config

Infoblox Dhcp Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/README.md`

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `infoblox_grid_master` | `"infoblox-master.example.com"` | No | Grid connection settings |
| `infoblox_username` | `"admin"` | No | — |
| `infoblox_password` | `"{{ vault_infoblox_password }}"` | No | — |
| `infoblox_wapi_version` | `"2.12"` | No | — |
| `infoblox_validate_certs` | `true` | No | — |
| `infoblox_enable_dhcp` | `true` | No | Global DHCP settings |
| `infoblox_enable_dhcp_thresholds` | `true` | No | — |
| `infoblox_dhcp_authority` | `true` | No | — |
| `infoblox_dhcp_email_list` | `(see defaults/main.yml)` | No | — |
| `infoblox_enable_dhcp_email_warnings` | `true` | No | — |
| `infoblox_enable_dhcp_snmp_warnings` | `true` | No | — |
| `infoblox_dhcp_failover_pairs` | `(see defaults/main.yml)` | No | DHCP Failover Pairs for High Availability |
| `infoblox_dhcp_custom_options` | `(see defaults/main.yml)` | No | Custom DHCP Options |
| `infoblox_configure_global_dhcp_options` | `true` | No | Global DHCP Options |
| `infoblox_dhcp_domain_name` | `"fourthestate.example.com"` | No | — |
| `infoblox_dhcp_dns_servers` | `(see defaults/main.yml)` | No | — |
| `infoblox_dhcp_default_gateway` | `"10.100.10.1"` | No | — |
| `infoblox_dhcp_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `infoblox_dhcp_mac_filters` | `(see defaults/main.yml)` | No | DHCP MAC Address Filters (for security zones) |
| `infoblox_dhcp_fingerprint_filters` | `(see defaults/main.yml)` | No | DHCP Fingerprint Filters (for device classification) |
| `infoblox_dhcp_default_lease_time` | `86400` | No | DHCP Lease Time Settings 24 hours |
| `infoblox_dhcp_pxe_lease_time` | `300` | No | 5 minutes for PXE boot |
| `infoblox_dhcp_reservations` | `(see defaults/main.yml)` | No | Fixed Address Reservations |
| `infoblox_dhcp_relay_agents` | `(see defaults/main.yml)` | No | DHCP Relay Agents |
| `infoblox_enable_pxe_boot` | `false` | No | PXE Boot Configuration |
| `infoblox_pxe_boot_server` | `""` | No | — |
| `infoblox_pxe_boot_file` | `""` | No | — |
| `infoblox_enable_ddns` | `true` | No | Dynamic DNS (DDNS) Integration |
| `infoblox_ddns_domain` | `"dynamic.fourthestate.example.com"` | No | — |
| `infoblox_ddns_generate_hostname` | `true` | No | — |
| `infoblox_ddns_server_always_updates` | `true` | No | — |
| `infoblox_ddns_ttl` | `3600` | No | — |
| `infoblox_ddns_update_fixed_addresses` | `false` | No | — |
| `infoblox_enable_dhcp_audit_log` | `true` | No | DHCP Logging and Audit |
| `infoblox_log_dhcp_lease_events` | `true` | No | — |
| `infoblox_enable_fingerprint_tracking` | `true` | No | — |
| `infoblox_dhcp_threshold_emails` | `(see defaults/main.yml)` | No | DHCP Threshold Monitoring |
| `infoblox_dhcp_threshold_warning` | `80` | No | Alert at 80% utilization |
| `infoblox_dhcp_threshold_critical` | `90` | No | Critical at 90% utilization |
| `infoblox_enable_dhcpv6` | `false` | No | IPv6 DHCP (DHCPv6) |
| `infoblox_dhcpv6_options` | `[]` | No | — |
| `infoblox_journalist_dhcp_enabled` | `true` | No | Fourth Estate specific DHCP settings Journalist DHCP pools configuration |
| `infoblox_source_protection_dhcp_enabled` | `true` | No | Source protection network DHCP isolation |
| `infoblox_security_zone_dhcp_separation` | `true` | No | DHCP scope design for security zones |
| `infoblox_dhcp_lease_tracking_enabled` | `true` | No | DHCP lease tracking for security analysis |
| `infoblox_dhcp_siem_integration` | `true` | No | Integration with SIEM for DHCP events |

## Example Playbook

```yaml
---
- name: Infoblox Dhcp Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/roles/infoblox_dhcp_config
```

## Tags

| Tag | Description |
|-----|-------------|
| `audit` | Tasks tagged `audit` |
| `config` | Tasks tagged `config` |
| `ddns` | Tasks tagged `ddns` |
| `dhcp` | Tasks tagged `dhcp` |
| `failover` | Tasks tagged `failover` |
| `filters` | Tasks tagged `filters` |
| `ha` | Tasks tagged `ha` |
| `infoblox` | Tasks tagged `infoblox` |
| `ipv6` | Tasks tagged `ipv6` |
| `lease` | Tasks tagged `lease` |
| `logging` | Tasks tagged `logging` |
| `monitoring` | Tasks tagged `monitoring` |
| `options` | Tasks tagged `options` |
| `pxe` | Tasks tagged `pxe` |
| `relay` | Tasks tagged `relay` |
| `reservations` | Tasks tagged `reservations` |
| `security` | Tasks tagged `security` |

## License

MIT

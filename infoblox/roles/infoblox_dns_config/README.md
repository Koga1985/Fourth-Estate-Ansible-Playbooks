# infoblox_dns_config

Infoblox Dns Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/README.md`

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `infoblox_grid_master` | `"infoblox-master.example.com"` | No | Grid connection settings (inherited from grid_config) |
| `infoblox_username` | `"admin"` | No | — |
| `infoblox_password` | `"{{ vault_infoblox_password }}"` | No | — |
| `infoblox_wapi_version` | `"2.12"` | No | — |
| `infoblox_validate_certs` | `true` | No | — |
| `infoblox_dns_views` | `(see defaults/main.yml)` | No | DNS Views for Split DNS (Fourth Estate: internal/external) |
| `infoblox_forwarder_group_name` | `"fourth-estate-forwarders"` | No | DNS Forwarders |
| `infoblox_dns_forwarders` | `(see defaults/main.yml)` | No | — |
| `infoblox_configure_root_hints` | `false` | No | Root Hints (use default IANA root servers unless airgapped) |
| `infoblox_root_hints` | `[]` | No | — |
| `infoblox_enable_dnssec` | `true` | No | DNSSEC Configuration |
| `infoblox_enable_dnssec_validation` | `true` | No | — |
| `infoblox_dnssec_validation_policy` | `"strict"` | No | — |
| `infoblox_dnssec_key_algorithm` | `"RSASHA256"` | No | — |
| `infoblox_dnssec_ksk_size` | `2048` | No | — |
| `infoblox_dnssec_zsk_size` | `1024` | No | — |
| `infoblox_dnssec_ksk_rollover` | `"AUTO"` | No | — |
| `infoblox_dnssec_zsk_rollover` | `"AUTO"` | No | — |
| `infoblox_enable_rrl` | `true` | No | Response Rate Limiting (RRL) for DDoS protection |
| `infoblox_rrl_ipv4_prefix` | `24` | No | — |
| `infoblox_rrl_ipv6_prefix` | `56` | No | — |
| `infoblox_rrl_responses_per_second` | `5` | No | — |
| `infoblox_rrl_errors_per_second` | `5` | No | — |
| `infoblox_rrl_nxdomains_per_second` | `5` | No | — |
| `infoblox_rrl_slip_ratio` | `2` | No | — |
| `infoblox_rrl_window` | `15` | No | — |
| `infoblox_allow_recursive_queries` | `true` | No | Recursive Queries Configuration |
| `infoblox_recursive_query_acl` | `(see defaults/main.yml)` | No | — |
| `infoblox_dns_query_source` | `""` | No | DNS Query Source Leave empty for automatic |
| `infoblox_dns_query_source_v6` | `""` | No | — |
| `infoblox_max_cache_ttl` | `86400` | No | DNS Cache Settings 1 day |
| `infoblox_max_ncache_ttl` | `10800` | No | 3 hours |
| `infoblox_max_cached_lifetime` | `604800` | No | 7 days |
| `infoblox_lame_ttl` | `600` | No | 10 minutes |
| `infoblox_enable_query_logging` | `true` | No | DNS Logging for Security Analysis (365+ day retention via syslog) |
| `infoblox_log_queries` | `true` | No | — |
| `infoblox_log_rpz_actions` | `true` | No | — |
| `infoblox_enable_dns_stats` | `true` | No | — |
| `infoblox_dns_query_acls` | `[]` | No | DNS Query ACLs (zone-specific) |
| `infoblox_dns_blackhole_list` | `(see defaults/main.yml)` | No | DNS Blackhole List (query source restrictions) |
| `infoblox_enable_dns64` | `false` | No | DNS64 for IPv6 transition |
| `infoblox_dns64_prefix` | `""` | No | — |
| `infoblox_notify_delay` | `5` | No | DNS Notification Settings |
| `infoblox_also_notify` | `[]` | No | — |
| `infoblox_dns_sortlist` | `[]` | No | DNS Sortlist (for geographic response ordering) |
| `infoblox_split_dns_enabled` | `true` | No | Fourth Estate specific DNS settings Split DNS configuration for internal vs external resolution |
| `infoblox_dns_security_logging` | `true` | No | DNS query logging for security analysis |
| `infoblox_publication_dns_enabled` | `true` | No | Publication system DNS records management |
| `infoblox_cdn_dns_enabled` | `true` | No | Content delivery DNS management |
| `infoblox_threat_dns_enabled` | `true` | No | Threat intelligence integration |

## Example Playbook

```yaml
---
- name: Infoblox Dns Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/roles/infoblox_dns_config
```

## Tags

| Tag | Description |
|-----|-------------|
| `acl` | Tasks tagged `acl` |
| `blackhole` | Tasks tagged `blackhole` |
| `cache` | Tasks tagged `cache` |
| `dns` | Tasks tagged `dns` |
| `dnssec` | Tasks tagged `dnssec` |
| `forwarders` | Tasks tagged `forwarders` |
| `infoblox` | Tasks tagged `infoblox` |
| `ipv6` | Tasks tagged `ipv6` |
| `logging` | Tasks tagged `logging` |
| `notify` | Tasks tagged `notify` |
| `query` | Tasks tagged `query` |
| `recursion` | Tasks tagged `recursion` |
| `roothints` | Tasks tagged `roothints` |
| `rrl` | Tasks tagged `rrl` |
| `security` | Tasks tagged `security` |
| `sortlist` | Tasks tagged `sortlist` |
| `splitdns` | Tasks tagged `splitdns` |
| `views` | Tasks tagged `views` |

## License

MIT

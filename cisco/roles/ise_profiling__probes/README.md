# ise_profiling__probes

Configures Cisco ISE endpoint profiling probes on the Policy Service Node (PSN). Profiling probes are the data collection mechanisms ISE uses to gather information about endpoints — DHCP fingerprints, RADIUS attributes, SNMP MIB data, NetFlow records, DNS lookups — which feed into profiling policies to classify devices. This role enables or disables individual probes according to the network's data collection capabilities.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE with Profiling licensed and enabled
- ISE admin credentials with ERS API access
- Appropriate network infrastructure to support enabled probes (e.g., DHCP span, SNMP community strings, NetFlow export)
- Ansible Vault for credential management

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ise_hostname` | `"{{ vault_ise_hostname }}"` | No | ISE Connection Parameters |
| `ise_username` | `"{{ vault_ise_username }}"` | No | — |
| `ise_password` | `"{{ vault_ise_password }}"` | No | — |
| `ise_verify_ssl` | `true` | No | — |
| `ise_use_proxy` | `false` | No | — |
| `ise_debug` | `false` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `ise_artifacts_dir` | `"/tmp/ise-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Configuration |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `ise_profiling__probes_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_profiling__probes_log_level` | `"INFO"` | No | Logging |
| `ise_profiling__probes_log_to_syslog` | `true` | No | — |
| `ise_profiling__probes_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_profiling__probes_notify_on_completion` | `false` | No | Notification Settings |
| `ise_profiling__probes_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_profiling__probes_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Configure ISE profiling probes
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    profiling_dhcp_probe_enabled: true
    profiling_dhcp_span_enabled: false
    profiling_radius_probe_enabled: true
    profiling_snmp_probe_enabled: true
    profiling_snmp_trap_enabled: false
    profiling_netflow_probe_enabled: false
    profiling_dns_probe_enabled: true
  roles:
    - role: cisco/roles/ise_profiling__probes
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `profiling` | All profiling configuration tasks |
| `probes` | Probe enable/disable configuration tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- Enabling SNMP Query probe requires SNMP credentials configured on network devices and ISE network device objects with SNMP settings.
- Enabling DHCP SPAN probe requires a network SPAN/RSPAN session mirroring DHCP traffic to ISE.
- All credentials must be stored in Ansible Vault.

## License

MIT

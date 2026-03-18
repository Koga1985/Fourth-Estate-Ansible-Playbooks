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

### ISE Connection

| Variable | Default | Required | Description |
|---|---|---|
| `ise_hostname` | `{{ vault_ise_hostname }}` | **Yes** | ISE primary PAN hostname or IP |
| `ise_username` | `{{ vault_ise_username }}` | **Yes** | ISE admin username |
| `ise_password` | `{{ vault_ise_password }}` | **Yes** | ISE admin password (vault-protected) |
| `ise_verify_ssl` | `true` | No | Validate ISE TLS certificate |
| `ise_use_proxy` | `false` | No | Route ISE API calls through a proxy |
| `ise_debug` | `false` | No | Enable verbose debug logging |

### Deployment Control

| Variable | Default | Required | Description |
|---|---|---|
| `apply_changes` | `false` | No | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### Profiling Probe Configuration

| Variable | Default | Required | Description |
|---|---|---|
| `profiling_dhcp_probe_enabled` | (required) | No | Enable DHCP probe (ISE listens for DHCP traffic) |
| `profiling_dhcp_span_enabled` | (required) | No | Enable DHCP SPAN probe (DHCP traffic mirrored to ISE via SPAN) |
| `profiling_radius_probe_enabled` | (required) | No | Enable RADIUS probe (extract profiling data from RADIUS packets) |
| `profiling_snmp_probe_enabled` | (required) | No | Enable SNMP Query probe (ISE polls network devices via SNMP) |
| `profiling_snmp_trap_enabled` | (required) | No | Enable SNMP Trap probe (network devices send traps to ISE) |
| `profiling_netflow_probe_enabled` | (required) | No | Enable NetFlow probe (ISE receives NetFlow records) |
| `profiling_dns_probe_enabled` | (required) | No | Enable DNS probe (reverse DNS lookups for endpoint hostnames) |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_profiling__probes_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_profiling__probes_log_level` | `INFO` | No | Log verbosity level |
| `ise_profiling__probes_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_profiling__probes_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_profiling__probes_notify_on_completion` | `false` | No | Send email on completion |
| `ise_profiling__probes_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_profiling__probes_auto_backup` | `true` | No | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

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

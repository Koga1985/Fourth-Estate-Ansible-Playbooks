# sdwan_monitoring

## Requirements

- Ansible 2.15+
- Phases 15–19 complete (fabric fully deployed and hardened)
- SNMP NMS and syslog receiver configured and reachable

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sdwan_vmanage_host` | `"{{ vault_sdwan_vmanage_host }}"` | No | vManage Connection Parameters |
| `sdwan_vmanage_port` | `443` | No | — |
| `sdwan_vmanage_username` | `"{{ vault_sdwan_vmanage_username }}"` | No | — |
| `sdwan_vmanage_password` | `"{{ vault_sdwan_vmanage_password }}"` | No | — |
| `sdwan_vmanage_verify_ssl` | `true` | No | — |
| `sdwan_vmanage_timeout` | `30` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `sdwan_artifacts_dir` | `"/tmp/sdwan-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Organization |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `fourth_estate_environment` | `"production"` | No | — |
| `fourth_estate_region` | `"primary"` | No | — |
| `enable_snmp_monitoring` | `true` | No | Feature Toggles |
| `enable_syslog_monitoring` | `true` | No | — |
| `enable_streaming_telemetry` | `true` | No | — |
| `enable_alert_rules` | `true` | No | — |
| `enable_health_monitoring` | `true` | No | — |
| `sdwan_monitor_snmp_v3_enabled` | `true` | No | SNMP Monitoring (SNMPv3 only - STIG SC-8) NIST SC-8 \| CISC-ND-000090 |
| `sdwan_monitor_snmp_users` | `(see defaults/main.yml)` | No | — |
| `sdwan_monitor_snmp_traps` | `(see defaults/main.yml)` | No | — |
| `sdwan_monitor_snmp_views` | `(see defaults/main.yml)` | No | SNMP MIB views - restrict to necessary OIDs |
| `sdwan_monitor_syslog_servers` | `(see defaults/main.yml)` | No | Syslog / Audit Logging NIST AU-2, AU-12 \| CISC-ND-000700 |
| `sdwan_monitor_syslog_severity` | `"informational"` | No | — |
| `sdwan_monitor_syslog_facility` | `"local6"` | No | — |
| `sdwan_streaming_enabled` | `true` | No | Streaming Telemetry (Model-Driven Telemetry) Streams real-time metrics to SIEM / monitoring platform |
| `sdwan_streaming_profiles` | `(see defaults/main.yml)` | No | — |
| `sdwan_alert_rules` | `(see defaults/main.yml)` | No | Alert Rules |
| `sdwan_health_check_interval` | `300` | No | Health Monitoring 5-minute health check interval |
| `sdwan_health_check_vpn` | `512` | No | — |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |

## Example Playbook

```yaml
- name: Use sdwan_monitoring
  hosts: all
  gather_facts: false
  roles:
    - role: sdwan_monitoring
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`sdwan`, `monitoring`, `snmp`, `syslog`, `logging`, `telemetry`, `streaming`, `alerts`, `health`, `phase20`

## Overview

Configures monitoring and telemetry for the Cisco SD-WAN fabric via vManage: **SNMPv3** (authPriv), remote **syslog** to SIEM, **model-driven streaming telemetry**, alert rules, and fabric health checks. This is **Phase 20** of the Fourth Estate Cisco SD-WAN deployment.

## Features

- SNMPv3 authPriv with AES-128/SHA (STIG CISC-ND-000090 / NIST SC-8)
- Remote syslog to primary and secondary SIEM servers (STIG CISC-ND-000700 / NIST AU-2)
- Model-driven streaming telemetry via gRPC (tunnel stats, app-route, interfaces)
- vManage alert rules for control-connection, SLA violations, cert expiry, auth failures
- Fabric health dashboard checks
- Defaults to **dry-run mode** (`apply_changes: false`)

## Compliance

| STIG ID | Control | NIST |
|---------|---------|------|
| CISC-ND-000090 | SNMPv3 authPriv required | SC-8 |
| CISC-ND-000700 | Audit event logging | AU-2 |
| CISC-ND-000710 | Audit record content | AU-3 |
| CISC-ND-000720 | Audit log protection | AU-9, AU-12 |

## Author

Fourth Estate Infrastructure Team

## License

MIT

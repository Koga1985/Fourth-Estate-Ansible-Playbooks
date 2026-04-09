# sdwan_monitoring

## Overview

Configures monitoring and telemetry for the Cisco SD-WAN fabric via vManage: **SNMPv3** (authPriv), remote **syslog** to SIEM, **model-driven streaming telemetry**, alert rules, and fabric health checks. This is **Phase 20** of the Fourth Estate Cisco SD-WAN deployment.

## Features

- SNMPv3 authPriv with AES-128/SHA (STIG CISC-ND-000090 / NIST SC-8)
- Remote syslog to primary and secondary SIEM servers (STIG CISC-ND-000700 / NIST AU-2)
- Model-driven streaming telemetry via gRPC (tunnel stats, app-route, interfaces)
- vManage alert rules for control-connection, SLA violations, cert expiry, auth failures
- Fabric health dashboard checks
- Defaults to **dry-run mode** (`apply_changes: false`)

## Requirements

- Ansible 2.15+
- Phases 15–19 complete (fabric fully deployed and hardened)
- SNMP NMS and syslog receiver configured and reachable

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sdwan_vmanage_host` | `{{ vault_sdwan_vmanage_host }}` | **Yes** | vManage hostname or IP |
| `apply_changes` | `false` | No | Set `true` to apply |
| `sdwan_monitor_snmp_v3_enabled` | `true` | No | Enable SNMPv3 |
| `sdwan_monitor_snmp_users` | see defaults | No | SNMPv3 users (auth+priv) |
| `sdwan_monitor_syslog_servers` | see defaults | No | Remote syslog destinations |
| `sdwan_streaming_enabled` | `true` | No | Enable streaming telemetry |
| `sdwan_streaming_profiles` | see defaults | No | Telemetry stream profiles |
| `sdwan_alert_rules` | see defaults | No | vManage alert rules |

## Tags

`sdwan`, `monitoring`, `snmp`, `syslog`, `logging`, `telemetry`, `streaming`, `alerts`, `health`, `phase20`

## Compliance

| STIG ID | Control | NIST |
|---------|---------|------|
| CISC-ND-000090 | SNMPv3 authPriv required | SC-8 |
| CISC-ND-000700 | Audit event logging | AU-2 |
| CISC-ND-000710 | Audit record content | AU-3 |
| CISC-ND-000720 | Audit log protection | AU-9, AU-12 |

## Author

Fourth Estate Infrastructure Team

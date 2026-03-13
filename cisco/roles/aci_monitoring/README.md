# aci_monitoring

## Overview

This role automates the complete monitoring and observability stack for a Cisco ACI fabric deployment for Fourth Estate infrastructure. It covers SNMPv3 policy and trap configuration, syslog remote destinations, Cisco Call Home smart notifications, real-time fabric health score monitoring with configurable thresholds, and fault management with severity-based reporting. It is designed as Phase 5 of the ACI platform deployment pipeline and defaults to dry-run mode to prevent unintended changes.

## Features

- SNMP policy configuration: enforce SNMPv3 with SHA authentication and AES-128 privacy
- SNMPv3 user creation with per-user auth/priv key management
- SNMP client group configuration for source IP restriction
- SNMP trap destination configuration (v3 with priv support)
- Syslog policy creation with remote UDP/TCP destinations
- Syslog local file and console destination configuration
- Syslog severity filtering with millisecond timestamp support
- Call Home policy with SMTP relay, profile, and destination configuration
- Call Home smart licensing integration for Cisco TAC connectivity
- Fabric health score query (overall, pod, node, tenant)
- Configurable warning and critical health thresholds with pass/fail behavior
- Fault management: severity-based fault queries (critical, major, minor, warning)
- Configurable fail-on-critical and warn-on-major behavior
- JSON artifact generation for every monitoring configuration stage

## Requirements

- Ansible >= 2.15
- Collections: `cisco.aci >= 2.8.0`, `ansible.utils >= 2.10.0`
- Python packages: `acicobra`, `acimodel`, `requests`
- Network reachability to APIC management interface on port 443

## Role Variables

### Connection Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `aci_host` | `{{ vault_aci_apic_hostname }}` | APIC hostname or IP address |
| `aci_username` | `{{ vault_aci_apic_username }}` | APIC admin username |
| `aci_password` | `{{ vault_aci_apic_password }}` | APIC admin password (vault-encrypted) |
| `aci_verify_ssl` | `true` | Validate APIC TLS certificate |
| `aci_timeout` | `30` | APIC API request timeout (seconds) |
| `aci_port` | `443` | APIC HTTPS port |

### Deployment Control

`apply_changes: false` — The role defaults to **dry-run mode**. No configuration changes are written to the APIC unless `apply_changes: true` is explicitly passed. In dry-run mode, all write operations use HTTP GET instead of POST.

### Feature Toggles

| Variable | Default | Description |
|----------|---------|-------------|
| `enable_snmp` | `true` | Configure SNMP policy, v3 users, and trap destinations |
| `enable_syslog` | `true` | Configure syslog policy and remote destinations |
| `enable_callhome` | `true` | Configure Cisco Call Home |
| `enable_health_monitoring` | `true` | Query and evaluate fabric health scores |
| `enable_fault_management` | `true` | Query and report on active faults |

### SNMP Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `aci_snmp_enabled` | `true` | Enable SNMP on the fabric |
| `aci_snmp_version` | `v3` | SNMP version (v3 enforced for security) |
| `aci_snmp_community` | `{{ vault_aci_snmp_community }}` | SNMPv2c community (vault-encrypted) |
| `aci_snmp_contact` | `{{ vault_fourth_estate_contact }}` | SNMP system contact (vault ref) |
| `aci_snmp_location` | `{{ vault_aci_snmp_location }}` | SNMP system location (vault ref) |

#### SNMPv3 Users (`aci_snmp_v3_users`)

```yaml
aci_snmp_v3_users:
  - username: "fe-snmpv3-ro"
    auth_type: "SHA"
    auth_password: "{{ vault_aci_snmpv3_auth_password }}"
    priv_type: "AES-128"
    priv_password: "{{ vault_aci_snmpv3_priv_password }}"
    description: "Fourth Estate SNMPv3 Read-Only User"
```

#### SNMP Trap Destinations (`aci_snmp_trap_destinations`)

```yaml
aci_snmp_trap_destinations:
  - host: "{{ vault_snmp_trap_host_primary }}"
    port: 162
    version: "v3"
    community: "{{ vault_aci_snmp_community }}"
    description: "Primary SNMP Trap Receiver"
```

### Syslog Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `aci_syslog_enabled` | `true` | Enable syslog on the fabric |
| `aci_syslog_local_severity` | `information` | Local file log severity level |
| `aci_syslog_include_ms` | `true` | Include milliseconds in timestamps |

#### Syslog Destinations (`aci_syslog_destinations`)

```yaml
aci_syslog_destinations:
  - host: "{{ vault_syslog_server_primary }}"
    port: 514
    severity: "warnings"
    facility: "local7"
    transport: "udp"
    description: "Primary Syslog Server"
```

### Call Home Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `aci_callhome_enabled` | `true` | Enable Call Home |
| `aci_callhome_customer_id` | `{{ vault_aci_callhome_customer_id }}` | Cisco customer ID |
| `aci_callhome_contract_id` | `{{ vault_aci_callhome_contract_id }}` | Cisco contract ID |
| `aci_callhome_site_id` | `{{ vault_aci_callhome_site_id }}` | Site identifier |
| `aci_callhome_email` | `{{ vault_aci_callhome_email }}` | Notification email (vault-encrypted) |
| `aci_callhome_smtp_server` | `{{ vault_aci_callhome_smtp_server }}` | SMTP relay server |
| `aci_callhome_smtp_port` | `25` | SMTP relay port |

### Health Monitoring Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `aci_health_warn_threshold` | `75` | Health score below which warning is issued |
| `aci_health_critical_threshold` | `50` | Health score below which critical alert is issued |
| `aci_monitor_pods` | `true` | Query and report pod health scores |
| `aci_monitor_nodes` | `true` | Query and report fabric node health scores |
| `aci_monitor_tenants` | `true` | Query and report tenant health scores |
| `aci_health_fail_on_critical` | `false` | Fail playbook if fabric health is critical |

### Fault Management Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `aci_suppress_acknowledged` | `false` | Suppress acknowledged faults from reports |
| `aci_fault_page_size` | `100` | Maximum faults to retrieve per severity query |
| `aci_fault_fail_on_critical` | `false` | Fail playbook if critical faults are present |
| `aci_fault_warn_on_major` | `true` | Emit warning debug message for major faults |

## Dependencies

None

## Example Playbook

```yaml
---
- name: Phase 5 - ACI Monitoring Configuration
  hosts: localhost
  connection: local
  gather_facts: true

  vars:
    apply_changes: false
    artifacts_dir: "/tmp/aci-artifacts"
    enable_snmp: true
    enable_syslog: true
    enable_callhome: true
    enable_health_monitoring: true
    enable_fault_management: true

  roles:
    - role: aci_monitoring
```

To apply changes:

```bash
ansible-playbook -i inventory cisco_aci/playbooks/06_aci_phase5_monitoring.yml \
  -e "apply_changes=true" --ask-vault-pass
```

To run only health monitoring and fault checks:

```bash
ansible-playbook -i inventory cisco_aci/playbooks/06_aci_phase5_monitoring.yml \
  --tags "health,faults" --ask-vault-pass
```

## Tags

| Tag | Description |
|-----|-------------|
| `always` | Prerequisites and validation (always executes) |
| `prerequisites` | Connectivity checks and variable validation |
| `phase5` | All Phase 5 monitoring tasks |
| `aci` | All ACI tasks |
| `monitoring` | All monitoring-related tasks |
| `snmp` | SNMP policy, v3 users, client groups, trap destinations |
| `snmpv3` | SNMPv3-specific user configuration |
| `traps` | SNMP trap destination configuration |
| `syslog` | Syslog policy and destination tasks |
| `logging` | All logging configuration tasks |
| `callhome` | Cisco Call Home configuration tasks |
| `smartlicensing` | Smart licensing integration tasks |
| `health` | Fabric health monitoring tasks |
| `faults` | Fault management and reporting tasks |
| `validation` | Validation and verification tasks |
| `verification` | Post-configuration verification |

## Compliance

### NIST 800-53 AU (Audit and Accountability) Controls

This role directly implements the following AU controls:

- **AU-2 (Event Logging):** Syslog policy configured to collect all fabric events at `warnings` severity and above; source binding captures all event categories
- **AU-3 (Content of Audit Records):** Syslog format includes millisecond timestamps (`includeMilliSeconds: yes`) and username context
- **AU-6 (Audit Record Review):** Fault management queries provide structured fault reports enabling periodic review
- **AU-9 (Protection of Audit Information):** Syslog artifacts saved with mode `0640`; remote syslog destinations provide off-box audit record protection
- **AU-12 (Audit Record Generation):** Fabric-wide monitoring policy bound to `monCommonPol` captures events from all fabric components

### NIST 800-53 SI (System and Information Integrity) Controls

- **SI-4 (System Monitoring):** Health monitoring queries fabric, pod, node, and tenant health scores; configurable threshold-based alerting provides continuous monitoring
- **SI-4(2) (Automated Tools for Real-Time Analysis):** SNMPv3 trap configuration enables integration with real-time SNMP management platforms (SolarWinds, PRTG, Nagios)
- **SI-5 (Security Alerts):** Call Home provides automated Cisco TAC notification for hardware and software faults; fault management queries surface active conditions
- **SI-12 (Information Management and Retention):** Fault report artifacts saved with structured JSON format for retention and historical analysis

### NIST 800-53 SC (System and Communications Protection) Controls

- **SC-8 (Transmission Confidentiality):** SNMPv3 with `authPriv` security level (SHA auth + AES-128 encryption) protects SNMP traffic in transit
- **SC-28 (Protection of Information at Rest):** All artifacts saved with restricted permissions (mode `0640`)

### DoD STIG Controls

- **Category I (Critical):** SNMPv1/v2 community strings disabled when `aci_snmp_version: v3` is set; SNMP client groups restrict polling to authorized management hosts
- **Category II (High):** SNMPv3 with `authPriv` enforced; syslog forwarded to external SIEM; Call Home enabled for automated TAC engagement
- **Category III (Medium):** SNMP contact and location configured via vault references; fault thresholds configured for operational awareness

## Artifacts Generated

| File | Description |
|------|-------------|
| `aci_monitoring_metadata.json` | Role execution metadata, timestamps, and feature configuration summary |
| `aci_snmp_config.json` | SNMP policy, v3 users, client groups, and trap destination configuration record |
| `aci_syslog_config.json` | Syslog policy, remote destinations, local file, and format configuration record |
| `aci_callhome_config.json` | Call Home policy, SMTP, profile, and destination configuration record |
| `aci_health_report.json` | Fabric, pod, node, and tenant health scores with threshold evaluation |
| `aci_fault_report.json` | Active fault counts by severity, critical/major fault details, and policy settings |
| `aci_monitoring_validation_report.json` | Post-configuration validation results for all monitoring components |

All artifacts are written to `artifacts_dir` (default: `/tmp/aci-artifacts`) with permissions `0640`.

## Author

Fourth Estate Infrastructure Team

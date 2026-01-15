# ucs_prod_monitoring

Cisco UCS production monitoring and health management role for Fourth Estate deployments.

## Description

This role configures comprehensive monitoring for Cisco UCS production environments including SNMP, Call Home, system health monitoring, and compliance reporting. It provides proactive alerting, fault detection, and health status tracking for fourth estate organizations.

## Features

- **SNMP Monitoring**: SNMPv2c and SNMPv3 configuration with trap destinations
- **Call Home**: Automated alert notification via email and HTTP
- **System Health Monitoring**: Real-time health status tracking
- **Fault Management**: Critical, major, and minor fault detection
- **Power Monitoring**: Power consumption and efficiency tracking
- **Thermal Monitoring**: Temperature and cooling status
- **Compliance Checklists**: Automated compliance monitoring
- **Alerting**: Multi-channel notification system
- **Reporting**: Comprehensive health and status reports

## Requirements

- Ansible >= 2.9
- Cisco UCS Python SDK (`pip install ucsmsdk`)
- Cisco UCS Ansible collection (`ansible-galaxy collection install cisco.ucs`)
- Administrative access to UCS Manager
- SNMP trap destination server (for SNMP monitoring)
- SMTP server (for Call Home email notifications)

## Role Variables

### Connection Variables (Required)
```yaml
ucs_hostname: "ucs-manager.example.com"
ucs_username: "admin"
ucs_password: "secure_password"
```

### Deployment Control
```yaml
apply_changes: false                    # Set to true to apply changes
ucs_artifacts_dir: "/tmp/ucs-artifacts" # Artifacts output directory
```

### Monitoring Features
```yaml
monitoring_enable_snmp: true            # Enable SNMP monitoring
monitoring_callhome_enabled: true       # Enable Call Home alerts
```

### SNMP Configuration
```yaml
snmp_community: "public"                # SNMP community string (use vault)

snmp_trap_destinations:
  - host: "snmp-trap.example.com"       # SNMP trap receiver
    community: "public"                 # Trap community string
    port: 162                           # SNMP trap port
    version: "v2c"                      # SNMP version (v2c or v3)
```

**SNMP Versions:**
- **v2c**: Community-based authentication (simpler, less secure)
- **v3**: User-based authentication with encryption (recommended for production)

### Contact Information
```yaml
monitoring_contact: "Network Operations Center"
monitoring_phone: "+1-555-0100"
monitoring_email: "noc@example.com"
monitoring_address: "123 Fourth Estate Avenue"
monitoring_location: "Fourth Estate Data Center"
```

### Call Home SMTP Configuration
```yaml
monitoring_smtp_server: "smtp.example.com"
monitoring_smtp_port: 25                # SMTP port (25 or 587)
```

See `defaults/main.yml` for complete variable documentation.

## Dependencies

None

## Example Playbook

### Basic Monitoring Setup
```yaml
---
- name: Configure UCS Monitoring
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    monitoring_enable_snmp: true
    monitoring_callhome_enabled: true

  roles:
    - role: ucs_prod_monitoring
```

### SNMP-Only Monitoring
```yaml
---
- name: Configure SNMP Monitoring Only
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    monitoring_enable_snmp: true
    monitoring_callhome_enabled: false

  roles:
    - role: ucs_prod_monitoring
```

### Multiple SNMP Trap Destinations
```yaml
---
- name: Configure Multiple SNMP Trap Receivers
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    snmp_trap_destinations:
      - host: "primary-snmp.example.com"
        community: "{{ vault_snmp_community }}"
        port: 162
        version: "v2c"
      - host: "backup-snmp.example.com"
        community: "{{ vault_snmp_community }}"
        port: 162
        version: "v2c"
      - host: "siem.example.com"
        community: "{{ vault_snmp_community }}"
        port: 162
        version: "v3"

  roles:
    - role: ucs_prod_monitoring
```

## Usage

### Dry Run (Validation Only)
```bash
ansible-playbook playbooks/deploy_monitoring.yml
```

### Apply Changes
```bash
ansible-playbook playbooks/deploy_monitoring.yml -e "apply_changes=true"
```

### SNMP Only
```bash
ansible-playbook playbooks/deploy_monitoring.yml \
  -e "apply_changes=true" \
  -e "monitoring_callhome_enabled=false"
```

## Monitoring Architecture

### Fourth Estate Monitoring Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     Cisco UCS Manager                       │
│                  (Fault & Event Generation)                 │
└─────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
         ┌──────▼──────┐            ┌──────▼──────┐
         │    SNMP     │            │ Call Home   │
         │   Traps     │            │   Alerts    │
         └──────┬──────┘            └──────┬──────┘
                │                           │
         ┌──────▼──────┐            ┌──────▼──────┐
         │ SNMP Trap   │            │    SMTP     │
         │  Receiver   │            │   Server    │
         │  (Monitoring│            │   (Email)   │
         │   System)   │            │             │
         └─────────────┘            └─────────────┘
                │                           │
                └─────────────┬─────────────┘
                              │
                    ┌─────────▼─────────┐
                    │  NOC Dashboard    │
                    │  (Centralized)    │
                    └───────────────────┘
```

## Monitoring Capabilities

### Fault Severity Levels
- **Critical**: System-impacting faults (server down, fabric interconnect failure)
- **Major**: Service-impacting faults (redundancy loss, high temperature)
- **Minor**: Non-service-impacting faults (informational alerts)
- **Warning**: Potential issues (nearing thresholds)

### Health Checks
- **Hardware Health**: Server, fabric interconnect, I/O module status
- **Power Health**: Power supply status, consumption, efficiency
- **Thermal Health**: Temperature sensors, fan status, cooling
- **Network Health**: Uplink status, fabric connectivity
- **Storage Health**: SAN connectivity, LUN availability
- **Firmware Health**: Version tracking, update status

### SNMP Trap Categories
- Hardware faults (PSU, fan, DIMM failures)
- Environmental alerts (temperature, power)
- Configuration changes
- Authentication events
- Service profile association/disassociation
- Network connectivity changes
- Firmware update events

### Call Home Alert Types
- Critical system faults
- Hardware failures
- Environmental warnings
- Configuration errors
- Security events
- Compliance violations

## Compliance Monitoring

This role supports compliance monitoring for:
- **NIST 800-53**: SI-4 (Information System Monitoring), AU-6 (Audit Review)
- **DoD STIG**: Continuous monitoring requirements
- **NIST 800-171**: Security monitoring for CUI
- **FISMA**: Continuous monitoring requirements

### Automated Compliance Checks
- Password policy compliance
- Session timeout enforcement
- Audit logging status
- Cryptographic settings
- Access control configuration
- System health status

## Security Considerations

### SNMP Security
- **v2c**: Use strong community strings, restrict to management VLAN
- **v3**: Use authentication and encryption (recommended)
- **Access Control**: Limit SNMP access to authorized monitoring systems
- **Community Strings**: Store in Ansible Vault, rotate regularly

### Call Home Security
- Use authenticated SMTP (port 587 with STARTTLS)
- Verify email recipients
- Sanitize sensitive information in alerts
- Review alert content before enabling

### Data Protection
- Encrypt SNMP traffic (SNMPv3)
- Secure SMTP connections (TLS)
- Protect monitoring credentials in Ansible Vault
- Restrict access to monitoring systems

## Troubleshooting

### SNMP Traps Not Received
- Verify network connectivity to trap destination
- Check SNMP community string matches receiver
- Verify UDP port 162 is not blocked by firewall
- Test with `snmpwalk` or `snmptrap` commands
- Review UCS Manager fault policy

### Call Home Not Sending
- Verify SMTP server connectivity
- Check SMTP port (25 or 587)
- Verify email addresses are correct
- Review UCS Manager Call Home configuration
- Check SMTP authentication if required

### Health Check Failures
- Review UCS Manager system faults
- Check hardware component status
- Verify firmware versions are supported
- Review environmental conditions (temperature, power)
- Check service profile associations

## Integration

### SNMP Integration Examples
- **Nagios/Icinga**: SNMP trap receiver plugin
- **Zabbix**: SNMP monitoring with UCS templates
- **PRTG**: Cisco UCS monitoring sensors
- **SolarWinds**: Network Performance Monitor
- **Splunk**: SNMP input with UCS app

### Call Home Integration
- Email ticketing systems (ServiceNow, Jira)
- SMS gateways for critical alerts
- Slack/Teams webhooks (via email-to-webhook)
- Cisco TAC Smart Call Home (optional)

## Artifacts Generated

The role creates the following artifacts in `ucs_artifacts_dir`:
- `monitoring_plan.json`: Planned monitoring configuration
- `snmp_configuration.txt`: SNMP settings and trap destinations
- `callhome_configuration.txt`: Call Home settings
- `health_check_results.json`: System health status
- `fault_summary.txt`: Active faults summary
- `compliance_checklist.txt`: Compliance monitoring status
- `monitoring_report.txt`: Complete deployment report

## Tags

Available tags for selective execution:
- `snmp`: Configure SNMP only
- `callhome`: Configure Call Home only
- `health_check`: Run health checks only
- `compliance`: Compliance monitoring only

**Example:**
```bash
ansible-playbook playbooks/deploy_monitoring.yml --tags snmp,health_check
```

## Monitoring Best Practices

### SNMP Best Practices
1. Use SNMPv3 for production environments
2. Restrict SNMP access to management VLAN
3. Use read-only community strings for polling
4. Configure multiple trap destinations for redundancy
5. Monitor trap receiver availability
6. Document SNMP configuration in CMDB

### Call Home Best Practices
1. Configure multiple email recipients
2. Test email delivery before production use
3. Set appropriate alert severity thresholds
4. Review and filter alert types
5. Document escalation procedures
6. Integrate with ticketing system

### Health Monitoring Best Practices
1. Schedule regular health checks (hourly recommended)
2. Set up automated reports (daily/weekly)
3. Define clear escalation thresholds
4. Document normal operating parameters
5. Maintain trending data for capacity planning
6. Review fault history regularly

## Performance Considerations

- SNMP polling interval: Recommend 5-15 minutes
- Call Home throttling: Prevent alert storms
- Health check frequency: Hourly for production
- Artifact retention: 30-90 days recommended
- Log rotation: Configure on monitoring systems

## License

MIT

## Author Information

Created for Fourth Estate production monitoring deployments.

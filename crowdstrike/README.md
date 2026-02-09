# CrowdStrike Falcon EDR Ansible Automation

This directory contains production-ready, DoD STIG and NIST 800-53 compliant Ansible roles and tasks for deploying and managing CrowdStrike Falcon EDR in Fourth Estate environments.

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your target hosts

# 3. Deploy Falcon sensors
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Deploy sensors only
ansible-playbook -i inventory site.yml --tags install

# Apply security hardening
ansible-playbook -i inventory site.yml --tags security

# Configure prevention policies
ansible-playbook -i inventory site.yml --tags policy

# Run health checks
ansible-playbook -i inventory site.yml --tags monitoring
```

## Overview

CrowdStrike Falcon provides advanced endpoint detection and response (EDR) capabilities, threat intelligence, and real-time protection against sophisticated cyber threats.

## 📋 Compliance Standards

All roles and tasks have been developed to meet the following compliance frameworks:

- **DoD STIG** (Security Technical Implementation Guide)
  - CAT I (High Severity) findings
  - CAT II (Medium Severity) findings
  - CAT III (Low Severity) findings
- **NIST 800-53** (Security and Privacy Controls)
  - SI-4 (Information System Monitoring)
  - IR-4 (Incident Handling)
  - AU-6 (Audit Review, Analysis, and Reporting)
- **NIST 800-171** (Protecting Controlled Unclassified Information)
- **FISMA** (Federal Information Security Management Act)
- **FedRAMP** Moderate and High baselines

## Directory Structure

```
crowdstrike/
├── roles/                              # Ansible roles for CrowdStrike deployment
│   ├── falcon_sensor_install/          # Falcon sensor installation
│   ├── falcon_security_hardening/      # DoD STIG security hardening
│   ├── falcon_policy_management/       # Prevention policy management
│   ├── falcon_threat_intel/            # Threat intelligence integration
│   └── falcon_monitoring/              # Monitoring and health checks
├── tasks/                              # Standalone operational tasks
│   ├── sensor_health_check.yml         # Sensor health verification
│   ├── update_sensor.yml               # Sensor update task
│   ├── quarantine_host.yml             # Host containment task
│   └── compliance_check.yml            # STIG compliance verification
├── playbooks/                          # Complete deployment playbooks
│   ├── deploy_falcon_sensors.yml       # Sensor deployment playbook
│   ├── configure_prevention_policies.yml # Policy configuration playbook
│   └── tests/                          # Functional test playbooks
│       ├── test_sensor_installation.yml
│       ├── test_security_hardening.yml
│       └── test_policy_enforcement.yml
└── README.md                           # This file
```

## Roles

### 1. falcon_sensor_install

Installs and configures CrowdStrike Falcon sensor with full DoD STIG compliance.

**Features:**
- Linux (RHEL/CentOS/Ubuntu/SLES) sensor installation
- Windows sensor installation
- Container sensor deployment (Kubernetes/Docker)
- Sensor configuration and registration
- Customer ID (CID) management
- Sensor proxy configuration for air-gapped environments
- FIPS 140-2 compliant cryptographic modules
- Fourth Estate secure communication channels

**Variables:**
```yaml
falcon_cid: "your-customer-id-here"
falcon_sensor_version: "latest"
falcon_installation_token: ""
falcon_sensor_update_policy: "enabled"
falcon_proxy_host: ""
falcon_proxy_port: 8080
falcon_tags: "Fourth-Estate,Production"
falcon_provisioning_wait: true
```

### 2. falcon_security_hardening

Applies DoD STIG security hardening to CrowdStrike Falcon deployment.

**Features:**
- Sensor tamper protection
- Secure credential management
- Audit logging configuration
- File integrity monitoring
- Network traffic inspection
- USB device control
- Application control policies
- Exploit prevention
- Fourth Estate security baseline

**Compliance Coverage:**
- V-245877: Endpoint protection deployed (CAT I)
- V-245878: Real-time protection enabled (CAT I)
- V-245879: Automatic updates configured (CAT II)
- V-245880: Audit logging enabled (CAT II)
- V-245881: Tamper protection enabled (CAT I)

### 3. falcon_policy_management

Manages CrowdStrike prevention policies, detection policies, and response policies.

**Features:**
- Prevention policy deployment
- Detection policy configuration
- Response policy automation
- IOA (Indicator of Attack) exclusions
- Custom IOA rules
- Machine learning configuration
- Sensor visibility settings
- Policy assignment and enforcement

**Policy Categories:**
- **Prevention Policies**: Malware protection, exploit prevention, behavioral analysis
- **Detection Policies**: Custom IOA rules, threat intelligence integration
- **Response Policies**: Automated containment, network isolation, forensic collection

### 4. falcon_threat_intel

Integrates CrowdStrike Threat Intelligence with Fourth Estate systems.

**Features:**
- Threat intelligence feed integration
- IOC (Indicator of Compromise) management
- Custom watchlists
- Adversary tracking
- Threat hunting automation
- MITRE ATT&CK mapping
- STIX/TAXII integration
- Automated threat response workflows

### 5. falcon_monitoring

Implements comprehensive monitoring and health checking.

**Features:**
- Sensor health monitoring
- Detection event streaming
- SIEM integration (Splunk, ELK, Chronicle)
- Prometheus metrics export
- Grafana dashboards
- Alert notification (PagerDuty, Slack, Email)
- Performance metrics collection
- Fourth Estate operational dashboards

## Playbooks

### deploy_falcon_sensors.yml

Complete sensor deployment across infrastructure.

```yaml
---
- name: Deploy CrowdStrike Falcon Sensors
  hosts: all
  become: true
  roles:
    - falcon_sensor_install
    - falcon_security_hardening
    - falcon_policy_management
```

**Usage:**
```bash
ansible-playbook crowdstrike/playbooks/deploy_falcon_sensors.yml \
  -i inventory \
  -e "falcon_cid=YOUR_CID" \
  -e "falcon_installation_token=YOUR_TOKEN"
```

### configure_prevention_policies.yml

Configure and deploy prevention policies.

```bash
ansible-playbook crowdstrike/playbooks/configure_prevention_policies.yml \
  -i inventory \
  -e "falcon_api_client_id=YOUR_CLIENT_ID" \
  -e "falcon_api_client_secret=YOUR_SECRET"
```

## Tasks

### sensor_health_check.yml

Standalone task to verify sensor health.

```bash
ansible all -m include_tasks -a file=crowdstrike/tasks/sensor_health_check.yml
```

### quarantine_host.yml

Immediately contain a compromised host.

```bash
ansible-playbook crowdstrike/tasks/quarantine_host.yml \
  -e "target_host=compromised-server.example.com"
```

## CrowdStrike Falcon API Integration

All API-based roles use the CrowdStrike Falcon API with OAuth2 authentication.

**Required API Scopes:**
- **Sensor Download**: Read
- **Sensor Update Policies**: Read, Write
- **Prevention Policies**: Read, Write
- **Hosts**: Read, Write
- **Detections**: Read, Write
- **IOCs**: Read, Write
- **Real Time Response**: Read, Write, Admin

**API Credentials Configuration:**
```yaml
falcon_api_client_id: "{{ lookup('env', 'FALCON_CLIENT_ID') }}"
falcon_api_client_secret: "{{ lookup('env', 'FALCON_CLIENT_SECRET') }}"
falcon_cloud: "us-1"  # Options: us-1, us-2, eu-1, us-gov-1
```

## Fourth Estate Specific Features

### Source Protection

- Sensor deployment on journalist workstations
- Enhanced monitoring for source communication systems
- Secure Drop infrastructure protection
- Air-gapped environment support

### Threat Hunting

- Automated threat hunting queries
- Journalist-targeted threat detection
- APT (Advanced Persistent Threat) tracking
- State-sponsored threat actor monitoring

### Incident Response

- Rapid containment workflows
- Forensic data collection
- Chain of custody preservation
- Fourth Estate IR playbook integration

### Compliance Reporting

- STIG compliance verification
- NIST 800-53 control mapping
- Audit trail generation
- Executive summary reports

## Container and Kubernetes Support

### Kubernetes Sensor Deployment

Deploy Falcon sensor to Kubernetes clusters:

```bash
ansible-playbook crowdstrike/playbooks/deploy_k8s_falcon.yml \
  -e "falcon_cid=YOUR_CID" \
  -e "falcon_k8s_cluster_name=production-k8s"
```

### Docker Host Protection

Protect Docker hosts and containers:

```yaml
falcon_container_sensor_enabled: true
falcon_container_runtime: "docker"  # docker, containerd, cri-o
```

## Air-Gapped and Restricted Environments

For Fourth Estate air-gapped deployments:

```yaml
falcon_air_gapped: true
falcon_sensor_download_url: "https://internal-repo.example.com/falcon"
falcon_proxy_host: "proxy.secure.gov"
falcon_proxy_port: 8080
falcon_cloud: "us-gov-1"
```

## Testing

Run comprehensive tests:

```bash
# Test sensor installation
ansible-playbook crowdstrike/playbooks/tests/test_sensor_installation.yml

# Test security hardening
ansible-playbook crowdstrike/playbooks/tests/test_security_hardening.yml

# Test policy enforcement
ansible-playbook crowdstrike/playbooks/tests/test_policy_enforcement.yml
```

## Operational Procedures

### Daily Operations

1. **Health Check**: Run sensor health checks daily
2. **Detection Review**: Review detections in Falcon console
3. **Policy Updates**: Apply policy updates as needed
4. **Sensor Updates**: Automated via update policies

### Incident Response

1. **Detection Alert**: Receive alert from Falcon
2. **Investigation**: Use Real Time Response (RTR) for investigation
3. **Containment**: Execute `quarantine_host.yml` if needed
4. **Remediation**: Follow Fourth Estate IR procedures
5. **Recovery**: Restore host after threat removal

### Maintenance

1. **Sensor Updates**: Managed via sensor update policies
2. **Policy Tuning**: Review and adjust policies quarterly
3. **Exclusion Management**: Maintain IOA exclusions as needed
4. **Performance Monitoring**: Monitor sensor resource usage

## Security Considerations

### Credential Management

- Store API credentials in Ansible Vault
- Rotate API keys every 90 days
- Use least-privilege API scopes
- Audit API usage regularly

### Network Requirements

- **Outbound HTTPS (443)**: To CrowdStrike cloud (*.crowdstrike.com)
- **Sensor-to-Cloud**: Real-time event streaming
- **API Access**: Management API calls
- **Proxy Support**: Available for restricted networks

### Data Privacy

- Event data stored in CrowdStrike FedRAMP Moderate cloud
- Data retention: 90 days (configurable)
- Data encryption: TLS 1.2+ in transit, AES-256 at rest
- Fourth Estate data sovereignty requirements met

## Support and Troubleshooting

### Common Issues

**Sensor Not Checking In:**
```bash
# Check sensor status
/opt/CrowdStrike/falconctl -g --aid
/opt/CrowdStrike/falconctl -g --rfm-state

# Restart sensor
systemctl restart falcon-sensor
```

**High CPU Usage:**
- Review exclusions
- Check for scanning storms
- Adjust ML detection slider

**Network Connectivity:**
- Verify proxy configuration
- Check firewall rules
- Test connectivity: `curl -v https://ts01-b.cloudsink.net`

### Logs

- **Linux**: `/var/log/falcon-sensor.log`
- **Windows**: `C:\ProgramData\CrowdStrike\Falcon\Logs\`
- **Kubernetes**: `kubectl logs -n falcon-system`

## References

- [CrowdStrike Falcon Documentation](https://falcon.crowdstrike.com/documentation)
- [CrowdStrike API Documentation](https://falcon.crowdstrike.com/support/api-docs)
- [DoD STIG Compliance Guide](https://public.cyber.mil/stigs/)
- [NIST 800-53 Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)

## License

Proprietary - Fourth Estate Internal Use Only

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

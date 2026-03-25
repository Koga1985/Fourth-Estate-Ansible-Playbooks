# SentinelOne EDR Ansible Automation

This directory contains production-ready, DoD STIG and NIST 800-53 compliant Ansible roles and tasks for deploying and managing SentinelOne EDR in Fourth Estate environments.

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your target hosts

# 3. Deploy SentinelOne agents
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Deploy agents only
ansible-playbook -i inventory site.yml --tags install

# Apply security hardening
ansible-playbook -i inventory site.yml --tags security

# Configure policies
ansible-playbook -i inventory site.yml --tags policy

# Run health checks
ansible-playbook -i inventory site.yml --tags monitoring
```

## Overview

SentinelOne provides AI-powered endpoint detection and response (EDR), autonomous threat remediation, and real-time protection against advanced cyber threats.

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
sentinelone/
├── roles/                              # Ansible roles for SentinelOne deployment
│   └── s1_agent_install/               # SentinelOne agent install, configure, monitor
├── tasks/                              # Standalone operational tasks
│   ├── agent_health_check.yml          # Agent health verification
│   ├── update_agent.yml                # Agent update task
│   ├── disconnect_network.yml          # Network isolation task
│   └── compliance_check.yml            # STIG compliance verification
├── playbooks/                          # Complete deployment playbooks
│   ├── deploy_s1_agents.yml            # Agent deployment playbook
│   └── configure_policies.yml          # Policy configuration playbook
└── README.md                           # This file
```

## Roles

### s1_agent_install (1 role)

Installs and configures SentinelOne agent with full DoD STIG compliance.

**Features:**
- Linux (RHEL/CentOS/Ubuntu/Debian/SLES) agent installation
- Windows agent installation
- Container agent deployment (Kubernetes/Docker)
- Agent configuration and registration
- Site token management
- Proxy configuration for air-gapped environments
- FIPS 140-2 compliant cryptographic modules
- Fourth Estate secure communication channels

**Variables:**
```yaml
s1_site_token: "your-site-token-here"
s1_agent_version: "latest"
s1_console_url: "https://usgoveast1.sentinelone.net"
s1_management_url: "{{ s1_console_url }}"
s1_tags: "Fourth-Estate,Production"
s1_group_name: "Default"
```


## Playbooks

### deploy_s1_agents.yml

Complete agent deployment across infrastructure.

```yaml
---
- name: Deploy SentinelOne Agents
  hosts: all
  become: true
  roles:
    - s1_agent_install
```

**Usage:**
```bash
ansible-playbook sentinelone/playbooks/deploy_s1_agents.yml \
  -i inventory \
  -e "s1_site_token=YOUR_TOKEN" \
  -e "s1_console_url=https://usgoveast1.sentinelone.net"
```

### configure_policies.yml

Configure and deploy security policies.

```bash
ansible-playbook sentinelone/playbooks/configure_policies.yml \
  -i inventory \
  -e "s1_api_token=YOUR_API_TOKEN"
```

## Tasks

### agent_health_check.yml

Standalone task to verify agent health.

```bash
ansible all -m include_tasks -a file=sentinelone/tasks/agent_health_check.yml
```

### disconnect_network.yml

Immediately isolate a compromised host from network.

```bash
ansible-playbook sentinelone/tasks/disconnect_network.yml \
  -e "target_host=compromised-server.example.com"
```

## SentinelOne API Integration

All API-based roles use the SentinelOne Management Console API with API token authentication.

**Required API Permissions:**
- **Agents**: Read, Write
- **Groups**: Read, Write
- **Policies**: Read, Write
- **Threats**: Read, Write
- **Activities**: Read
- **Deep Visibility**: Read (for hunting)

**API Configuration:**
```yaml
s1_api_token: "{{ lookup('env', 'S1_API_TOKEN') }}"
s1_console_url: "https://usgoveast1.sentinelone.net"
s1_account_id: ""  # Optional: specify account
s1_site_id: ""     # Optional: specify site
```

## Fourth Estate Specific Features

### Source Protection

- Agent deployment on journalist workstations
- Enhanced monitoring for source communication systems
- Secure Drop infrastructure protection
- Air-gapped environment support

### Autonomous Response

- Automated threat remediation
- Rollback capabilities for ransomware
- Network quarantine automation
- Forensic data preservation

### Threat Hunting

- Automated threat hunting queries
- Journalist-targeted threat detection
- APT (Advanced Persistent Threat) tracking
- State-sponsored threat actor monitoring

### Incident Response

- Rapid containment workflows
- Remote shell capabilities
- Forensic data collection
- Chain of custody preservation
- Fourth Estate IR playbook integration

### Compliance Reporting

- STIG compliance verification
- NIST 800-53 control mapping
- Audit trail generation
- Executive summary reports

## Container and Kubernetes Support

### Kubernetes Agent Deployment

Deploy SentinelOne agent to Kubernetes clusters:

```bash
ansible-playbook sentinelone/playbooks/deploy_k8s_agents.yml \
  -e "s1_site_token=YOUR_TOKEN" \
  -e "s1_k8s_cluster_name=production-k8s"
```

### Docker Host Protection

Protect Docker hosts and containers:

```yaml
s1_container_enabled: true
s1_container_runtime: "docker"  # docker, containerd, cri-o
s1_k8s_namespace: "sentinelone"
```

## Air-Gapped and Restricted Environments

For Fourth Estate air-gapped deployments:

```yaml
s1_air_gapped: true
s1_agent_download_url: "https://internal-repo.example.com/sentinelone"
s1_proxy_host: "proxy.secure.gov"
s1_proxy_port: 8080
s1_update_server: "https://internal-update.example.com"
```

## Autonomous Actions

SentinelOne provides autonomous threat response capabilities:

- **Kill Process**: Terminate malicious processes
- **Quarantine File**: Isolate malicious files
- **Remediate**: Automatically remediate threats
- **Rollback**: Roll back system changes from ransomware
- **Network Quarantine**: Disconnect endpoint from network

Configuration:

```yaml
s1_auto_mitigation: true
s1_auto_remediation: true
s1_suspicious_activity_action: "detect"  # detect, protect
s1_malicious_activity_action: "protect"  # detect, protect
```

## Testing

Run agent health checks:

```bash
# Run agent health check
ansible-playbook -i inventory site.yml --tags monitoring
```

## Operational Procedures

### Daily Operations

1. **Health Check**: Run agent health checks daily
2. **Threat Review**: Review threats in SentinelOne console
3. **Policy Updates**: Apply policy updates as needed
4. **Agent Updates**: Automated via update policies

### Incident Response

1. **Threat Alert**: Receive alert from SentinelOne
2. **Investigation**: Use Deep Visibility for investigation
3. **Containment**: Execute `disconnect_network.yml` if needed
4. **Remediation**: Apply remediation actions
5. **Recovery**: Verify threat removal and restore connectivity

### Maintenance

1. **Agent Updates**: Managed via update policies
2. **Policy Tuning**: Review and adjust policies quarterly
3. **Exclusion Management**: Maintain exclusions as needed
4. **Performance Monitoring**: Monitor agent resource usage

## Security Considerations

### Credential Management

- Store API tokens in Ansible Vault
- Store site tokens securely
- Rotate API tokens every 90 days
- Use least-privilege API permissions
- Audit API usage regularly

### Network Requirements

- **Outbound HTTPS (443)**: To SentinelOne cloud
- **Agent-to-Cloud**: Real-time event streaming
- **API Access**: Management API calls
- **Proxy Support**: Available for restricted networks

**SentinelOne US GovCloud Endpoints:**
- Console: `https://usgoveast1.sentinelone.net`
- Updates: `https://usgoveast1-updates.sentinelone.net`

### Data Privacy

- Event data stored in SentinelOne FedRAMP Moderate cloud
- Data retention: configurable (default 90 days)
- Data encryption: TLS 1.2+ in transit, AES-256 at rest
- Fourth Estate data sovereignty requirements met

## Support and Troubleshooting

### Common Issues

**Agent Not Checking In:**
```bash
# Check agent status (Linux)
sudo /opt/sentinelone/bin/sentinelctl status

# Check agent status (Windows)
sc query SentinelAgent

# Restart agent
sudo systemctl restart sentinelone  # Linux
net stop SentinelAgent && net start SentinelAgent  # Windows
```

**High CPU Usage:**
- Review exclusions
- Check for scanning activity
- Adjust scan settings

**Network Connectivity:**
- Verify proxy configuration
- Check firewall rules
- Test connectivity: `curl -v https://usgoveast1.sentinelone.net`

### Logs

- **Linux**: `/var/log/sentinelone/`
- **Windows**: `C:\ProgramData\SentinelOne\Logs\`
- **Kubernetes**: `kubectl logs -n sentinelone`

### Agent Commands

```bash
# Linux
/opt/sentinelone/bin/sentinelctl status
/opt/sentinelone/bin/sentinelctl version
/opt/sentinelone/bin/sentinelctl management status

# Windows
"C:\Program Files\SentinelOne\Sentinel Agent\SentinelCtl.exe" status
```

## Deep Visibility Queries

SentinelOne Deep Visibility provides powerful threat hunting capabilities:

```sql
-- Find suspicious PowerShell execution
EventType = "Process Creation" AND ProcessName ContainsCIS "powershell"

-- Find network connections to suspicious IPs
EventType = "IP Connect" AND DstIP In ("1.2.3.4", "5.6.7.8")

-- Find file modifications in system directories
EventType = "File Modification" AND FilePath StartsWith "/etc/"
```

## References

- [SentinelOne Documentation](https://support.sentinelone.com/)
- [SentinelOne API Documentation](https://usgoveast1.sentinelone.net/api-doc/)
- [DoD STIG Compliance Guide](https://public.cyber.mil/stigs/)
- [NIST 800-53 Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)

## License

Proprietary - Fourth Estate Internal Use Only

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

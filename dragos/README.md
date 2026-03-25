# Dragos Platform Integration

This directory contains **12 Ansible roles** for integrating with **Dragos Platform** for OT/ICS threat detection, asset visibility, and security monitoring.

## Overview

Dragos Platform provides industrial cybersecurity threat detection and response. These roles automate Dragos sensor deployment, asset discovery, threat intelligence integration, and incident response workflows for Fourth Estate OT environments.

## 📋 Role Categories

### Sensor & Operations (2 roles)
- **dragos_sensor_ops** - Sensor deployment, health monitoring, and lifecycle management
- **dragos_mssp_orchestrator** - MSSP-mode multi-tenant orchestration (optional)

### Asset Management (3 roles)
- **dragos_inventory_model** - OT asset inventory and CMDB synchronization
- **dragos_topology_baseline** - Network topology baselining and change detection
- **dragos_vulnerability_mgmt** - OT vulnerability tracking and risk scoring

### Threat Intelligence & Alerts (2 roles)
- **dragos_intel_ops** - Threat intelligence feed management and IOC integration
- **dragos_alerts_pipeline** - Alert routing, deduplication, and SIEM forwarding

### Case Management (1 role)
- **dragos_cases_workflow** - Case creation, escalation, and workflow automation

### Integrations (2 roles)
- **dragos_servicenow_integration** - ServiceNow ITSM integration for ticket creation
- **dragos_jira_integration** - Jira issue tracking integration

### Governance & Segmentation (2 roles)
- **dragos_governance_pack** - Compliance reporting and governance policy enforcement
- **dragos_segmentation_assist** - Network segmentation recommendations and enforcement

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your Dragos platform details

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Deploy sensors
ansible-playbook -i inventory site.yml --tags sensors

# Configure alerts
ansible-playbook -i inventory site.yml --tags alerts

# Configure integrations
ansible-playbook -i inventory site.yml --tags integrations

# Configure governance
ansible-playbook -i inventory site.yml --tags governance
```

### Prerequisites

- Ansible 2.12.0+
- Dragos Platform license and credentials
- Network access to Dragos management interface
- API token from Dragos Platform

### Configuration

```yaml
# group_vars/dragos.yml
dragos_platform_url: "https://dragos.example.com"
dragos_api_token: "{{ vault_dragos_api_token }}"
dragos_organization: "Fourth Estate"

dragos_sensors:
  - name: "sensor-east-01"
    location: "Data Center East"
    network_segment: "OT Zone 1"
    span_port: "GigabitEthernet0/1"
```

## 📖 Common Use Cases

### Deploy Dragos Sensors

```bash
ansible-playbook -i inventory site.yml --tags sensors
```

### Synchronize Asset Inventory

```bash
ansible-playbook -i inventory site.yml --tags inventory \
  -e "sync_to_cmdb=true"
```

### Integrate with SIEM

```bash
ansible-playbook -i inventory site.yml --tags alerts \
  -e "dragos_siem_type=splunk" \
  -e "dragos_siem_host=splunk.example.com"
```

## 🛡️ Security Features

- **Protocol Visibility** - Deep packet inspection for OT protocols
- **Threat Detection** - Known ICS malware and attack patterns
- **Behavioral Analytics** - Baseline deviations and anomalies
- **Asset Visibility** - Comprehensive OT asset inventory
- **Incident Response** - Automated playbooks for common threats

## 📚 Additional Resources

- [Dragos Platform Documentation](https://www.dragos.com/resources/)
- [Dragos Threat Intelligence](https://www.dragos.com/threat-intelligence/)

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

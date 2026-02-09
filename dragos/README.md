# Dragos Platform Integration

This directory contains **12 Ansible roles** for integrating with **Dragos Platform** for OT/ICS threat detection, asset visibility, and security monitoring.

## Overview

Dragos Platform provides industrial cybersecurity threat detection and response. These roles automate Dragos sensor deployment, asset discovery, threat intelligence integration, and incident response workflows for Fourth Estate OT environments.

## 📋 Role Categories

### Platform Configuration (4 roles)
- **dragos_platform_config** - Initial platform setup
- **dragos_sensor_deployment** - Deploy Dragos sensors
- **dragos_collector_config** - Data collector configuration
- **dragos_api_integration** - API client setup

### Asset Management (3 roles)
- **dragos_asset_discovery** - OT asset enumeration
- **dragos_asset_inventory** - Asset database synchronization
- **dragos_topology_mapping** - Network topology visualization

### Threat Detection (3 roles)
- **dragos_threat_intel** - Threat intelligence feed integration
- **dragos_detection_rules** - Custom detection logic
- **dragos_behavioral_analytics** - Anomaly detection baselines

### Incident Response (2 roles)
- **dragos_alert_integration** - SIEM/SOAR integration
- **dragos_incident_playbooks** - Automated response workflows

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
ansible-playbook playbooks/dragos_sensor_deployment.yml \
  -i inventory/ot_network.yml \
  -e "sensor_mode=passive"
```

### Synchronize Asset Inventory

```bash
ansible-playbook roles/dragos_asset_inventory/playbook.yml \
  -i inventory/dragos.yml \
  -e "sync_to_cmdb=true"
```

### Integrate with SIEM

```bash
ansible-playbook roles/dragos_alert_integration/playbook.yml \
  -i inventory/dragos.yml \
  -e "siem_platform=splunk" \
  -e "siem_host=splunk.example.com"
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

# Claroty xDome Platform

This directory contains **11 Ansible roles** for automating **Claroty xDome** OT/IoT security platform including asset inventory, vulnerability management, secure access, network segmentation, and compliance reporting.

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your Claroty xDome details

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Configure inventory export
ansible-playbook -i inventory site.yml --tags inventory

# Configure alerts/SIEM integration
ansible-playbook -i inventory site.yml --tags alerts

# Configure secure access
ansible-playbook -i inventory site.yml --tags access

# Configure segmentation
ansible-playbook -i inventory site.yml --tags segmentation

# Configure compliance reporting
ansible-playbook -i inventory site.yml --tags compliance
```

## 📋 Roles

### Inventory Management (3 roles)
- **claroty_xdome_inventory_export** - Asset inventory export
- **claroty_xdome_inventory_scheduler** - Scheduled inventory updates
- **claroty_xdome_inventory_normalize_cmdb** - CMDB normalization

### Security Integration (2 roles)
- **claroty_xdome_alerts_siem** - SIEM integration for alerts
- **claroty_xdome_vuln_risk** - Vulnerability risk assessment

### Secure Access (3 roles)
- **claroty_xdome_secure_access_onboarding** - User onboarding
- **claroty_xdome_secure_access_session_policy** - Session policies
- **claroty_xdome_secure_access_audit_export** - Audit log export

### Network & Compliance (3 roles)
- **claroty_xdome_segmentation** - Network segmentation recommendations
- **claroty_xdome_reporting_compliance_pack** - Compliance reporting
- **claroty_xdome_reporting_exec_summary** - Executive dashboards

## ⚙️ Configuration

```yaml
# group_vars/claroty.yml
claroty_api_url: "https://xdome.example.com"
claroty_api_key: "{{ vault_claroty_api_key }}"
claroty_organization: "Fourth Estate"

# SIEM Integration
claroty_siem_enabled: true
claroty_siem_type: "splunk"
claroty_siem_host: "splunk.example.com"
```

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

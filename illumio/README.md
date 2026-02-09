# Illumio Core Zero Trust Segmentation

This directory contains **3 Ansible roles** for managing **Illumio Core** zero trust micro-segmentation platform.

## Overview

Illumio Core provides application-centric segmentation and zero trust security. These roles automate policy lifecycle management, VEN (Virtual Enforcement Node) deployment, and security posture reporting for Fourth Estate environments.

## 📋 Roles

### Policy Management (1 role)
- **illumio_policy_lifecycle** - Policy creation, testing, enforcement
  - Draft policies
  - Test mode validation
  - Production enforcement
  - Policy versioning

### VEN Fleet Management (1 role)
- **illumio_ven_fleet_management** - VEN deployment and lifecycle
  - VEN installation
  - Pairing keys
  - Health monitoring
  - Version management

### Reporting & Analytics (1 role)
- **illumio_reporting_analytics** - Security posture reporting
  - Traffic flow visibility
  - Policy coverage analysis
  - Compliance reporting
  - Risk assessment

## 🚀 Quick Start

### Prerequisites

- Ansible 2.12.0+
- Illumio PCE (Policy Compute Engine) access
- API credentials with appropriate permissions
- VEN compatible workloads (Linux, Windows, Kubernetes)

### Configuration

```yaml
# group_vars/illumio.yml
illumio_pce_host: "pce.example.com"
illumio_pce_port: 443
illumio_api_key: "{{ vault_illumio_api_key }}"
illumio_api_secret: "{{ vault_illumio_api_secret }}"
illumio_org_id: 1

illumio_policy_mode: "test"  # draft, test, enforced
```

## 📖 Common Use Cases

### Deploy VENs to Workloads

```bash
ansible-playbook playbooks/illumio_ven_deployment.yml \
  -i inventory/workloads.yml \
  -e "pairing_profile=fourth-estate-prod"
```

### Create and Test Segmentation Policy

```bash
ansible-playbook roles/illumio_policy_lifecycle/playbook.yml \
  -i inventory/illumio.yml \
  -e "policy_name=web-to-db-segmentation" \
  -e "policy_mode=test"
```

### Generate Compliance Report

```bash
ansible-playbook roles/illumio_reporting_analytics/playbook.yml \
  -i inventory/illumio.yml \
  -e "report_type=compliance" \
  -e "output_format=html"
```

## 🛡️ Security Features

- **Zero Trust Segmentation** - Application-level microsegmentation
- **Policy Testing** - Safe policy validation before enforcement
- **Adaptive Security** - Dynamic policy based on context
- **Visibility** - Complete traffic flow visualization
- **Compliance** - PCI-DSS, HIPAA, NIST segmentation requirements

## 📚 Additional Resources

- [Illumio Documentation](https://docs.illumio.com/)
- [Illumio API Reference](https://docs.illumio.com/core/api/reference.html)

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

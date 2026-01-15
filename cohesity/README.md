# Cohesity Data Platform

This directory contains **6 Ansible roles** for automating **Cohesity Data Platform** management including cluster configuration, protection policies, recovery operations, cloud archive, Views (NAS), and agent deployment.

## Overview

Comprehensive Cohesity automation covering cluster setup, data protection policy management, backup and recovery operations, cloud archive tier configuration, NAS Views provisioning, and agent deployment to protected sources.

## 📋 Roles

### Cluster Management (1 role)
- **cohesity_cluster_config** - Cluster initialization, network configuration, and licensing

### Data Protection (2 roles)
- **cohesity_protection_policies** - Protection policy creation and management
- **cohesity_recovery** - Automated recovery workflows (VM, file, database)

### Storage & Archive (2 roles)
- **cohesity_views** - NAS Views (SMB/NFS) provisioning and management
- **cohesity_cloud_archive** - Cloud archive tier (AWS, Azure, Google Cloud) setup

### Agent Management (1 role)
- **cohesity_agents** - Agent deployment and registration to protected sources

## 🚀 Quick Start

### Prerequisites

- Ansible 2.12.0+
- `cohesity.dataplatform` collection or Python SDK
- Access to Cohesity cluster with admin privileges
- Python requests library

### Installation

```bash
# Install Cohesity collection
ansible-galaxy collection install cohesity.dataplatform

# Or install Python SDK
pip install cohesity-management-sdk
```

### Basic Configuration

```yaml
# group_vars/cohesity.yml
cohesity_cluster: "cohesity.example.com"
cohesity_username: "{{ vault_cohesity_username }}"
cohesity_password: "{{ vault_cohesity_password }}"
cohesity_validate_certs: true
```

## 📖 Common Use Cases

### Use Case 1: Configure Cohesity Cluster

```bash
ansible-playbook playbooks/cohesity_cluster_setup.yml \
  -i inventory/cohesity.yml \
  --ask-vault-pass
```

### Use Case 2: Create Protection Policy

```bash
ansible-playbook playbooks/cohesity_protection_policy.yml \
  -e "policy_name=Daily-Backup" \
  -e "retention_days=30" \
  -e "backup_type=kRegular"
```

### Use Case 3: Recover VM

```bash
ansible-playbook playbooks/cohesity_vm_recovery.yml \
  -e "vm_name=prod-web-01" \
  -e "recovery_point=latest"
```

## 🛡️ Security Features

- **Encryption at Rest** - AES-256 encryption for all data
- **Encryption in Transit** - TLS 1.2+ for all communications
- **RBAC** - Role-based access control integration
- **Immutable Snapshots** - DataLock for ransomware protection
- **Multi-Factor Authentication** - MFA support for admin access

## 📚 Additional Resources

- [Cohesity Documentation](https://docs.cohesity.com/)
- [Cohesity Ansible Collection](https://galaxy.ansible.com/cohesity/dataplatform)
- [Cohesity REST API Guide](https://developer.cohesity.com/)

---

**Last Updated:** 2026-01-15
**Maintained By:** Fourth Estate Infrastructure Team

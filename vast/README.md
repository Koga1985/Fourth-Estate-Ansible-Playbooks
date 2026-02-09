# VAST Data Storage - Production-Ready Ansible Automation

Production-ready Ansible roles, tasks, and playbooks for VAST Data Storage systems with full DoD STIG and NIST 800-53 compliance. Designed for Fourth Estate and government organizations requiring the highest security standards.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Roles](#roles)
- [Playbooks](#playbooks)
- [Security and Compliance](#security-and-compliance)
- [Usage Examples](#usage-examples)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## Overview

This repository provides comprehensive automation for VAST Data Storage infrastructure, including:

- **Base Configuration**: Cluster setup, networking, protocols, and storage management
- **Security Hardening**: DoD STIG and NIST 800-53 compliance implementation
- **Monitoring**: SNMP, syslog, performance metrics, and health checks
- **Backup & DR**: Snapshots, replication, and disaster recovery orchestration

All automation is designed to be:
- **Production-ready**: Tested for enterprise deployments
- **Security-first**: FIPS 140-2, encryption at rest/transit, audit logging
- **Compliant**: DoD STIG, NIST 800-53, NIST 800-171
- **Idempotent**: Safe to run multiple times
- **Modular**: Use individual roles or complete playbooks

## Features

### Configuration Management
- ✅ Cluster configuration and initialization
- ✅ Network and VIP pool management
- ✅ NFS, SMB, and S3 protocol configuration
- ✅ Storage optimization (deduplication, compression)
- ✅ View/filesystem creation and management

### Security Hardening (DoD STIG)
- ✅ FIPS 140-2 mode enablement
- ✅ TLS 1.2+ enforcement with approved cipher suites
- ✅ SMBv1 disablement (STIG requirement)
- ✅ SMB signing and encryption enforcement
- ✅ LDAP/Active Directory integration with Kerberos
- ✅ Password complexity and account lockout policies
- ✅ Role-based access control (RBAC)
- ✅ Multi-factor authentication support

### Audit and Compliance
- ✅ Comprehensive audit logging (NIST 800-53 AU family)
- ✅ SIEM integration for centralized logging
- ✅ 365-day log retention (configurable)
- ✅ Audit log integrity verification
- ✅ Automated compliance reporting (STIG, NIST)
- ✅ Security event alerting

### Monitoring and Alerting
- ✅ SNMPv3 configuration
- ✅ Syslog integration (TCP/TLS)
- ✅ Performance metrics collection (IOPS, throughput, latency)
- ✅ Health checks (nodes, drives, network, services)
- ✅ Capacity threshold alerting
- ✅ Hardware failure detection

### Backup and Disaster Recovery
- ✅ Automated snapshot scheduling
- ✅ Replication to DR cluster (sync/async)
- ✅ External backup (S3, NFS, SMB)
- ✅ Backup encryption and compression
- ✅ RTO/RPO objective tracking
- ✅ Protection policy management

## Requirements

### Control Node
- Ansible 2.12 or higher
- Python 3.8 or higher
- Network connectivity to VAST management interface

### VAST Cluster
- VAST Data Storage 4.x or higher
- Management API enabled
- Administrative credentials
- Network connectivity on port 443 (HTTPS)

### Collections
```bash
# No external collections required - uses ansible.builtin modules
```

## Quick Start

### 1. Clone Repository
```bash
git clone <repository-url>
cd vast/
```

### 2. Configure Inventory
```bash
cp inventories/production.ini inventories/my-cluster.ini
# Edit inventories/my-cluster.ini with your cluster details
```

### 3. Configure Variables
```bash
# Copy and customize production variables
cp vars/production.yml vars/my-cluster.yml

# Create encrypted vault for sensitive data
cp vars/vault.yml.example vars/vault.yml
ansible-vault encrypt vars/vault.yml
# Edit vault.yml with your credentials
```

### 4. Run Production Deployment
```bash
ansible-playbook playbooks/deploy_production.yml \
  -i inventories/my-cluster.ini \
  -e @vars/my-cluster.yml \
  -e @vars/vault.yml \
  --ask-vault-pass
```

## Roles

### vast_config
Base configuration for VAST Data Storage cluster.

**Tasks:**
- Prerequisites validation
- Cluster configuration (name, timezone, HA)
- Network configuration (VIP pools, DNS)
- Protocol configuration (NFS, SMB, S3)
- Storage configuration (dedup, compression)
- Monitoring setup

**Key Variables:**
- `vast_cluster_name`: Cluster name
- `vast_enable_nfs/smb/s3`: Protocol enablement
- `vast_enable_deduplication`: Storage optimization

### vast_security_hardening
DoD STIG and NIST 800-53 security hardening.

**Tasks:**
- Access control (LDAP/AD, RBAC)
- Authentication (password policy, MFA, Kerberos)
- Encryption (FIPS, at-rest, in-transit, TLS 1.2+)
- Protocol security (SMBv1 disable, signing, encryption)
- Audit logging (comprehensive, SIEM integration)
- Network security (firewall, ACLs)
- Compliance verification

**Key Variables:**
- `vast_fips_140_2_mode`: Enable FIPS mode
- `vast_disable_smb1`: Disable SMBv1 (STIG)
- `vast_audit_log_retention_days`: Audit retention

### vast_monitoring
Monitoring, alerting, and health checks.

**Tasks:**
- SNMP configuration (v3 secure)
- Syslog configuration (TCP/TLS)
- Performance metric collection
- Health checks
- Alert configuration

**Key Variables:**
- `vast_enable_snmp`: Enable SNMP
- `vast_syslog_servers`: Syslog server list
- `vast_alert_on_capacity_threshold`: Alert threshold

### vast_backup_dr
Backup and disaster recovery orchestration.

**Tasks:**
- Snapshot scheduling
- Replication configuration
- External backup setup
- DR readiness verification
- Protection policy management

**Key Variables:**
- `vast_snapshot_retention_days`: Snapshot retention
- `vast_replication_enabled`: Enable DR replication
- `vast_dr_rto_minutes`: Recovery time objective

## Playbooks

### deploy_production.yml
Complete production deployment with all roles.

**Usage:**
```bash
ansible-playbook playbooks/deploy_production.yml \
  -i inventories/production.ini \
  -e @vars/production.yml \
  -e @vars/vault.yml \
  --ask-vault-pass
```

**Tags:**
- `config`: Base configuration only
- `security`: Security hardening only
- `monitoring`: Monitoring setup only
- `backup`: Backup/DR configuration only

### security_audit.yml
Security audit and compliance checking (read-only).

**Usage:**
```bash
ansible-playbook playbooks/security_audit.yml \
  -i inventories/production.ini \
  -e @vars/vault.yml \
  --ask-vault-pass
```

Generates audit report at `/tmp/vast_security_audit_<date>.txt`

### create_filesystem.yml
Interactive filesystem/view creation with security.

**Usage:**
```bash
ansible-playbook playbooks/create_filesystem.yml \
  -i inventories/production.ini \
  -e @vars/vault.yml \
  --ask-vault-pass
```

## Security and Compliance

### DoD STIG Compliance

This automation implements the following DoD STIG controls:

| Control | Requirement | Implementation |
|---------|-------------|----------------|
| V-238197 | Access Control | LDAP/AD with RBAC, least privilege |
| V-238199 | Password Policy | 15+ chars, complexity, 60-day age |
| V-238201 | Session Management | 15-min timeout, audit sessions |
| V-238203 | Encryption | FIPS 140-2, TLS 1.2+, approved ciphers |
| V-238205 | Audit Logging | All access, 365-day retention |
| V-238207 | Protocol Security | SMBv1 disabled, signing required |
| V-238211 | Network Security | Firewall, ACLs, default deny |

### NIST 800-53 Controls

| Family | Controls | Implementation |
|--------|----------|----------------|
| AC | Access Control | AC-2, AC-3, AC-6, AC-7, AC-11 |
| AU | Audit | AU-2, AU-3, AU-6, AU-9, AU-11 |
| IA | Identification/Auth | IA-2, IA-5, IA-8 |
| SC | System/Comm | SC-7, SC-8, SC-13 |
| CP | Contingency | CP-9, CP-10 |

### NIST 800-171 Compliance
Implements CUI protection requirements including:
- Access control (3.1.x)
- Awareness and training (3.2.x)
- Audit and accountability (3.3.x)
- Identification and authentication (3.5.x)
- System and communications protection (3.13.x)

## Usage Examples

### Example 1: Initial Deployment
```bash
# Full production deployment with all roles
ansible-playbook playbooks/deploy_production.yml \
  -i inventories/production.ini \
  --ask-vault-pass
```

### Example 2: Security Hardening Only
```bash
# Apply only security hardening
ansible-playbook playbooks/deploy_production.yml \
  -i inventories/production.ini \
  --tags security \
  --ask-vault-pass
```

### Example 3: Compliance Check
```bash
# Run security audit (read-only)
ansible-playbook playbooks/security_audit.yml \
  -i inventories/production.ini \
  --ask-vault-pass
```

### Example 4: Create Filesystem
```bash
# Interactive filesystem creation
ansible-playbook playbooks/create_filesystem.yml \
  -i inventories/production.ini \
  --ask-vault-pass
```

### Example 5: Using Reusable Tasks
```yaml
---
- name: Custom VAST Operations
  hosts: localhost
  tasks:
    - name: Create new view
      ansible.builtin.include_tasks: tasks/create_view.yml
      vars:
        view_name: "app-data"
        view_path: "/apps/data"
        view_quota_gb: 1000
```

## Configuration

### Credential Management

**Always use Ansible Vault for sensitive data:**

```bash
# Create vault file
ansible-vault create vars/vault.yml

# Edit vault file
ansible-vault edit vars/vault.yml

# Encrypt existing file
ansible-vault encrypt vars/vault.yml
```

**Required vault variables:**
- `vault_vast_mgmt_host`: Management hostname
- `vault_vast_mgmt_user`: Admin username
- `vault_vast_mgmt_password`: Admin password
- `vault_ldap_server`: LDAP server (if used)
- `vault_syslog_server_primary`: Syslog server

### Network Configuration

**Configure VIP pools in vars:**
```yaml
vast_vip_pool_name: "production-vip-pool"
vast_vip_pool_start: "10.10.10.100"
vast_vip_pool_end: "10.10.10.200"
vast_vip_pool_subnet: "10.10.10.0/24"
vast_vip_pool_gateway: "10.10.10.1"
```

### Compliance Settings

**Configure compliance framework:**
```yaml
vast_compliance_mode: "dod"  # Options: dod, nist, hipaa
vast_fips_mode_enabled: true
vast_audit_log_retention_days: 365
vast_generate_compliance_reports: true
```

## Troubleshooting

### Connection Issues
```bash
# Test connectivity
curl -k https://<vast-mgmt-host>/api/v1/system

# Check credentials
ansible-playbook playbooks/deploy_production.yml --check
```

### SSL Certificate Issues
```yaml
# Disable SSL verification (NOT recommended for production)
vast_verify_ssl: false

# Or provide CA bundle
vast_ssl_cert_path: "/etc/pki/tls/certs/vast-ca-bundle.crt"
```

### Debug Mode
```bash
# Run with verbose output
ansible-playbook playbooks/deploy_production.yml -vvv
```

### Common Issues

**Issue**: API returns 401 Unauthorized
**Solution**: Verify credentials in vault.yml

**Issue**: API returns 404 Not Found
**Solution**: Check API version compatibility

**Issue**: Tasks fail with SSL errors
**Solution**: Install CA certificate or set `vast_verify_ssl: false`

## Directory Structure

```
vast/
├── README.md                    # This file
├── roles/                       # Ansible roles
│   ├── vast_config/            # Base configuration
│   ├── vast_security_hardening/ # Security hardening
│   ├── vast_monitoring/        # Monitoring setup
│   └── vast_backup_dr/         # Backup and DR
├── playbooks/                   # Example playbooks
│   ├── deploy_production.yml   # Full deployment
│   ├── security_audit.yml      # Security audit
│   └── create_filesystem.yml   # Filesystem creation
├── tasks/                       # Reusable tasks
│   ├── create_view.yml         # Create filesystem
│   ├── create_quota.yml        # Create quota
│   └── verify_compliance.yml   # Verify compliance
├── inventories/                 # Inventory files
│   └── production.ini          # Production inventory
└── vars/                        # Variable files
    ├── production.yml          # Production variables
    └── vault.yml.example       # Vault template
```

## Contributing

Contributions are welcome! Please ensure:
- All changes maintain DoD STIG compliance
- Security best practices are followed
- Documentation is updated
- Testing is performed in lab environment

## Support

For issues or questions:
1. Check troubleshooting section
2. Review role documentation
3. Contact your VAST support representative

## License

MIT License - See LICENSE file for details

## References

- [VAST Data Documentation](https://support.vastdata.com)
- [DoD STIG Library](https://public.cyber.mil/stigs/)
- [NIST 800-53 Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [NIST 800-171](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- [Ansible Documentation](https://docs.ansible.com)

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

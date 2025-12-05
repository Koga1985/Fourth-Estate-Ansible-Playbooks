# Splunk Enterprise - Production-Ready Ansible Roles and Tasks

## Overview

This directory contains production-ready, DoD STIG and NIST 800-53 compliant Ansible roles and tasks for deploying and managing Splunk Enterprise in Fourth Estate environments.

## Compliance Standards

All roles and tasks have been developed to meet the following compliance frameworks:

- **DoD STIG** (Security Technical Implementation Guide)
  - CAT I (High Severity) findings
  - CAT II (Medium Severity) findings
  - CAT III (Low Severity) findings
- **NIST 800-53** (Security and Privacy Controls)
- **NIST 800-171** (Protecting Controlled Unclassified Information)
- **FISMA** (Federal Information Security Management Act)
- **FIPS 140-2** (Federal Information Processing Standard)

## Directory Structure

```
splunk/
├── roles/                          # Ansible roles for Splunk deployment
│   ├── splunk_enterprise_install/  # Core Splunk Enterprise installation
│   ├── splunk_security_hardening/  # DoD STIG security hardening
│   ├── splunk_forwarder/           # Universal Forwarder deployment
│   ├── splunk_monitoring/          # Health checks and monitoring
│   └── splunk_backup_dr/           # Backup and disaster recovery
├── tasks/                          # Standalone operational tasks
│   ├── restart_splunk.yml          # Service restart task
│   ├── health_check.yml            # Health verification task
│   ├── backup_now.yml              # Immediate backup task
│   └── compliance_check.yml        # STIG compliance verification
├── playbooks/                      # Complete deployment playbooks
│   ├── install_splunk_enterprise.yml
│   ├── deploy_forwarders.yml
│   └── tests/                      # Functional test playbooks
│       ├── test_installation.yml
│       ├── test_security_hardening.yml
│       └── test_forwarder.yml
└── README.md                       # This file
```

## Roles

### 1. splunk_enterprise_install

Installs and configures Splunk Enterprise with full DoD STIG compliance.

**Features:**
- FIPS 140-2 compliant installation
- TLS 1.2+ enforcement
- DoD PKI certificate integration
- Secure password policies (15+ characters, complexity requirements)
- Session management and timeout controls
- Multi-factor authentication support (LDAP, SAML, DUO)
- Comprehensive audit logging
- SELinux integration
- Firewall configuration

**Key Variables:**
```yaml
splunk_version: "9.2.1"
splunk_enable_fips: true
splunk_tls_min_version: "tls1.2"
splunk_admin_password: "{{ vault_splunk_admin_password }}"
splunk_enable_mfa: true
```

**Usage:**
```bash
ansible-playbook -i inventory splunk/playbooks/install_splunk_enterprise.yml \
  --tags install,splunk \
  --extra-vars "@vault.yml"
```

### 2. splunk_security_hardening

Applies DoD STIG security controls to existing Splunk installations.

**Features:**
- STIG Category I, II, and III remediation
- Access control (RBAC) enforcement
- Authentication hardening
- Cryptographic controls
- Network security controls
- File system hardening
- Application security controls
- Compliance verification and reporting

**Key Variables:**
```yaml
stig_cat1_enabled: true
stig_cat2_enabled: true
stig_cat3_enabled: true
sc_enforce_fips_140_2: true
ia_enforce_mfa: true
au_log_retention_days: 365
```

**Usage:**
```bash
ansible-playbook -i inventory splunk/playbooks/install_splunk_enterprise.yml \
  --tags security,hardening,stig
```

### 3. splunk_forwarder

Deploys Splunk Universal Forwarders with security hardening.

**Features:**
- Lightweight forwarder installation
- TLS-encrypted forwarding
- FIPS mode support
- Automatic data collection configuration
- Performance tuning

**Key Variables:**
```yaml
splunk_indexers:
  - "indexer1.example.com:9997"
  - "indexer2.example.com:9997"
splunk_forwarder_enable_ssl: true
splunk_forwarder_fips_mode: true
```

**Usage:**
```bash
ansible-playbook -i inventory splunk/playbooks/deploy_forwarders.yml
```

### 4. splunk_monitoring

Implements health checks, performance monitoring, and alerting.

**Features:**
- Automated health checks (every 5 minutes)
- Performance metric collection
- Compliance monitoring (FIPS, TLS, audit logs)
- Email alerting
- Resource utilization monitoring

**Key Variables:**
```yaml
monitoring_enable_health_checks: true
monitoring_cpu_threshold: 80
monitoring_memory_threshold: 90
monitoring_fips_compliance_check: true
```

**Usage:**
```bash
ansible-playbook -i inventory splunk/playbooks/install_splunk_enterprise.yml \
  --tags monitoring,health
```

### 5. splunk_backup_dr

Configures automated backups and disaster recovery procedures.

**Features:**
- Encrypted backups (AES-256)
- Automated backup scheduling
- 90-day backup retention
- 7-year archive retention (compliance requirement)
- Disaster recovery documentation
- DR site replication support

**Key Variables:**
```yaml
backup_enabled: true
backup_path: "/backup/splunk"
backup_retention_days: 90
backup_encryption_enabled: true
archive_retention_years: 7
```

**Usage:**
```bash
ansible-playbook -i inventory splunk/playbooks/install_splunk_enterprise.yml \
  --tags backup,dr
```

## Standalone Tasks

### restart_splunk.yml

Safely restarts Splunk services with verification.

```bash
ansible-playbook -i inventory splunk/tasks/restart_splunk.yml
```

### health_check.yml

Performs comprehensive health check and generates report.

```bash
ansible-playbook -i inventory splunk/tasks/health_check.yml
```

### backup_now.yml

Executes immediate backup (outside scheduled backups).

```bash
ansible-playbook -i inventory splunk/tasks/backup_now.yml
```

### compliance_check.yml

Verifies STIG compliance and generates report.

```bash
ansible-playbook -i inventory splunk/tasks/compliance_check.yml
```

## Testing

Comprehensive functional tests are provided to verify proper deployment:

### Test Installation

```bash
ansible-playbook -i inventory splunk/playbooks/tests/test_installation.yml
```

**Tests Include:**
- Binary existence
- User and group creation
- Service status
- Port availability
- API responsiveness
- FIPS mode verification
- TLS configuration
- Audit logging
- File permissions

### Test Security Hardening

```bash
ansible-playbook -i inventory splunk/playbooks/tests/test_security_hardening.yml
```

**Tests Include:**
- SSL/TLS version enforcement
- FIPS mode verification
- Cipher suite configuration
- Password policy enforcement
- Audit logging configuration
- Network security controls

### Test Forwarder

```bash
ansible-playbook -i inventory splunk/playbooks/tests/test_forwarder.yml
```

**Tests Include:**
- Forwarder binary
- Service status
- Configuration files
- TLS forwarding

## Prerequisites

### System Requirements

- **Operating Systems:**
  - RHEL 8/9
  - CentOS 8/9
  - Rocky Linux 8/9
  - AlmaLinux 8/9
  - Ubuntu 20.04/22.04

- **Minimum Resources:**
  - CPU: 12 cores
  - RAM: 12 GB
  - Disk: 500 GB

- **Network Ports:**
  - 8000 (Web Interface)
  - 8089 (Management API)
  - 9997 (Splunk Forwarding)
  - 8191 (KVStore)

### Ansible Requirements

- Ansible 2.12 or higher
- Python 3.6 or higher
- Collections:
  - ansible.posix
  - community.general

Install collections:
```bash
ansible-galaxy collection install ansible.posix community.general
```

### Vault Configuration

Create a vault file for sensitive credentials:

```bash
ansible-vault create vault.yml
```

**Required vault variables:**
```yaml
vault_splunk_admin_password: "YourSecurePassword123!"
vault_splunk_cluster_secret: "ClusterSecretKey"
vault_splunk_shc_secret: "SHCSecretKey"
vault_ldap_bind_password: "LDAPBindPassword"
vault_backup_encryption_key: "BackupEncryptionKey"
vault_siem_server: "siem.example.com"
vault_monitoring_email: "splunk-alerts@example.com"
```

## Quick Start

### 1. Install Splunk Enterprise (Standalone)

```bash
# Create inventory
cat > inventory << EOF
[splunk_servers]
splunk01.example.com ansible_user=ansible ansible_become=yes

[vars:all]
splunk_accept_license=true
EOF

# Run installation
ansible-playbook -i inventory \
  splunk/playbooks/install_splunk_enterprise.yml \
  --extra-vars "@vault.yml" \
  --ask-vault-pass
```

### 2. Deploy Universal Forwarders

```bash
# Create forwarder inventory
cat > forwarder_inventory << EOF
[forwarder_targets]
server01.example.com
server02.example.com

[forwarder_targets:vars]
splunk_indexers=['indexer1.example.com:9997', 'indexer2.example.com:9997']
EOF

# Deploy forwarders
ansible-playbook -i forwarder_inventory \
  splunk/playbooks/deploy_forwarders.yml
```

### 3. Run Health Check

```bash
ansible-playbook -i inventory splunk/tasks/health_check.yml
```

### 4. Verify Compliance

```bash
ansible-playbook -i inventory splunk/tasks/compliance_check.yml
```

## Security Considerations

### STIG Compliance

All roles implement DoD STIG requirements including:

- **V-258100**: Disable SSLv3, TLS 1.0, and TLS 1.1
- **V-258102**: Enable FIPS 140-2 mode
- **V-258104**: Enforce strong cipher suites
- **V-258106**: Disable anonymous access
- **V-258108**: Enable comprehensive audit logging
- **V-258112**: Configure session timeouts
- **V-258114**: Protect audit logs from modification

### Network Security

- All network communications encrypted with TLS 1.2+
- Management access restricted to trusted networks
- Firewall rules automatically configured
- Rate limiting enabled

### Data Protection

- Data at rest encryption
- Data in transit encryption
- Secure backup encryption (AES-256)
- 7-year archive retention for compliance

### Access Control

- Multi-factor authentication support
- Role-based access control (RBAC)
- Minimum 15-character passwords
- Password complexity requirements
- Account lockout after 3 failed attempts

## Troubleshooting

### Common Issues

**Issue: Splunk service won't start**
```bash
# Check logs
tail -f /opt/splunk/var/log/splunk/splunkd.log

# Verify permissions
ls -la /opt/splunk/etc/system/local/

# Check FIPS mode
cat /proc/sys/crypto/fips_enabled
```

**Issue: FIPS mode errors**
```bash
# Verify OpenSSL FIPS module
openssl version

# Check Splunk FIPS configuration
/opt/splunk/bin/splunk btool server list fips

# Run FIPS verification script
/opt/splunk/bin/verify_fips.sh
```

**Issue: Certificate errors**
```bash
# Check certificate expiry
/opt/splunk/bin/check_cert_expiry.sh

# Verify certificate files
ls -la /opt/splunk/etc/auth/mycerts/

# Test TLS connection
openssl s_client -connect localhost:8089 -tls1_2
```

## Maintenance

### Regular Tasks

- **Daily**: Review health check logs
- **Weekly**: Verify backups completed
- **Monthly**: Run compliance checks
- **Quarterly**: Test disaster recovery procedures
- **Annually**: Review and update security configurations

### Updates and Patches

```bash
# Check for updates (manual review required in production)
/opt/splunk/bin/splunk show version

# Apply updates (test in non-production first)
ansible-playbook -i inventory splunk/playbooks/update_splunk.yml
```

## Support and Documentation

### Official Splunk Documentation
- [Splunk Enterprise Documentation](https://docs.splunk.com/)
- [Splunk Security Best Practices](https://www.splunk.com/en_us/resources/securing-splunk.html)

### Compliance Documentation
- [DoD STIG Viewer](https://public.cyber.mil/stigs/)
- [NIST 800-53 Controls](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [FIPS 140-2 Standards](https://csrc.nist.gov/publications/detail/fips/140/2/final)

### Internal Support
For issues or questions:
1. Check troubleshooting section above
2. Review role-specific README files
3. Contact your security team for compliance questions
4. Contact your Splunk administrator for operational issues

## Contributing

When contributing to these roles:

1. Maintain STIG compliance
2. Update tests for new features
3. Document all changes
4. Test in non-production environment
5. Update this README

## License

MIT License - See repository root LICENSE file

## Authors

Security Team - Fourth Estate
Operations Team - Infrastructure Automation

## Version History

- **v1.0.0** (2024-12) - Initial production-ready release
  - Splunk Enterprise 9.2.1 support
  - Full DoD STIG compliance
  - NIST 800-53 controls implementation
  - FIPS 140-2 mode support
  - Comprehensive testing suite
  - Production-ready for Fourth Estate deployment

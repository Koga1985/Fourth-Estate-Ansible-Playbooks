# VAST Data Storage - Ansible Roles

This directory contains production-ready Ansible roles for VAST Data Storage automation with full DoD STIG and NIST 800-53 compliance.

## Available Roles

### vast_config
**Purpose**: Base configuration and setup of VAST Data Storage cluster

**Features**:
- Cluster initialization and naming
- Network configuration (VIP pools, DNS, NTP)
- Protocol configuration (NFS, SMB, S3)
- Storage optimization (deduplication, compression)
- Initial monitoring setup

**Usage**:
```yaml
- role: vast_config
  vars:
    vast_cluster_name: "production-cluster"
    vast_enable_nfs: true
    vast_enable_deduplication: true
```

**Tags**: `config`, `base`, `cluster`, `network`, `protocols`, `storage`

---

### vast_security_hardening
**Purpose**: Implement DoD STIG and NIST 800-53 security controls

**Features**:
- FIPS 140-2 mode enablement
- TLS 1.2+ enforcement with approved ciphers
- SMBv1 disablement (STIG requirement)
- LDAP/Active Directory integration
- Password policies and account lockout
- Comprehensive audit logging
- Network security (firewall, ACLs)
- Compliance verification

**Usage**:
```yaml
- role: vast_security_hardening
  vars:
    vast_fips_140_2_mode: true
    vast_disable_smb1: true
    vast_audit_log_retention_days: 365
```

**Tags**: `security`, `hardening`, `stig`, `nist`, `fips`, `encryption`, `audit`

**STIG Controls**: V-238197, V-238199, V-238201, V-238203, V-238205, V-238207, V-238211

---

### vast_monitoring
**Purpose**: Configure monitoring, alerting, and health checks

**Features**:
- SNMPv3 secure monitoring
- Syslog integration (TCP/TLS)
- Performance metrics (IOPS, throughput, latency)
- Automated health checks
- Capacity and hardware failure alerts

**Usage**:
```yaml
- role: vast_monitoring
  vars:
    vast_enable_snmp: true
    vast_snmp_version: "3"
    vast_alert_on_capacity_threshold: 80
```

**Tags**: `monitoring`, `snmp`, `syslog`, `performance`, `health`, `alerts`

---

### vast_backup_dr
**Purpose**: Backup and disaster recovery configuration

**Features**:
- Automated snapshot scheduling
- Cluster replication (sync/async)
- External backup (S3, NFS, SMB)
- Backup encryption and compression
- RTO/RPO tracking
- Protection policy management

**Usage**:
```yaml
- role: vast_backup_dr
  vars:
    vast_snapshot_retention_days: 30
    vast_replication_enabled: true
    vast_backup_encryption_enabled: true
```

**Tags**: `backup`, `dr`, `disaster_recovery`, `snapshots`, `replication`

---

## Role Dependencies

None of these roles have dependencies on each other, but they are designed to work together.

## Security Considerations

- **Always** encrypt credentials using ansible-vault
- **Never** commit plaintext passwords
- **Always** verify SSL certificates in production
- **Review** all defaults before deployment
- **Test** in lab environment first

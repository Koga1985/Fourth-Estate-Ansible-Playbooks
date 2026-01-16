# Oracle Database Automation

This directory contains **8 Ansible roles** for automating **Oracle Database** management including installation, configuration, Data Guard, RMAN backup, performance tuning, and security hardening.

## 📋 Roles

### Installation & Configuration (2 roles)
- **oracle_install** - Oracle Database software installation
- **oracle_database_create** - Database creation and configuration

### High Availability & DR (2 roles)
- **oracle_data_guard** - Oracle Data Guard configuration
- **oracle_rac** - Real Application Clusters setup

### Backup & Recovery (2 roles)
- **oracle_rman** - RMAN backup and recovery
- **oracle_flashback** - Flashback database configuration

### Security & Compliance (2 roles)
- **oracle_security** - Security hardening and encryption
- **oracle_audit** - Unified auditing configuration

## 🚀 Quick Start

```bash
# Install Oracle 19c
ansible-playbook playbooks/oracle_install.yml \
  -e "oracle_version=19c" \
  -e "oracle_home=/u01/app/oracle/product/19c/dbhome_1"

# Configure Data Guard
ansible-playbook playbooks/oracle_data_guard.yml \
  -e "primary_db=PRODDB" \
  -e "standby_db=DRDB"
```

## ⚙️ Configuration

```yaml
# Oracle installation
oracle_version: "19c"
oracle_edition: "EE"  # SE2, EE
oracle_base: "/u01/app/oracle"
oracle_home: "/u01/app/oracle/product/19c/dbhome_1"

# Database configuration
oracle_db_name: "PRODDB"
oracle_pdb_name: "PDB01"
oracle_sga_target: "8G"
oracle_pga_aggregate_target: "4G"

# Security
oracle_enable_tde: true
oracle_enable_unified_audit: true

# RMAN
oracle_rman_retention_days: 30
oracle_rman_archivelog_retention_days: 7
```

---

**Maintained By:** Fourth Estate Infrastructure Team

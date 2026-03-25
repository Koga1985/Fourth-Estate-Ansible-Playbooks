# Database Platforms

This directory contains **25 Ansible roles** across **3 database platforms** for automated installation, configuration, replication, backup, security hardening, and compliance.

## Overview

Enterprise database automation with emphasis on high availability, disaster recovery, and security compliance (DoD STIG, NIST 800-53) for Fourth Estate environments.

## 📋 Supported Databases

| Platform | Roles | Key Features |
|----------|-------|-------------|
| **PostgreSQL** | 9 | Installation, streaming replication, PgPool-II, Barman backup, pgAudit, restore |
| **MySQL/MariaDB** | 8 | Installation, master-replica replication, Galera cluster, XtraBackup |
| **Oracle Database** | 8 | Installation, Data Guard, RAC, RMAN, Flashback, unified auditing |

## Directory Structure

```
databases/
├── README.md              # This file
├── postgresql/            # PostgreSQL automation (8 roles)
│   ├── README.md
│   ├── roles/
│   ├── site.yml
│   └── requirements.yml
├── mysql/                 # MySQL/MariaDB automation (8 roles)
│   ├── README.md
│   ├── roles/
│   ├── site.yml
│   └── requirements.yml
└── oracle/                # Oracle Database automation (8 roles)
    ├── README.md
    ├── roles/
    ├── site.yml
    └── requirements.yml
```

## 🚀 Quick Start (Drop-In Deployment)

Each database platform supports independent drop-in deployment:

```bash
# PostgreSQL
cd databases/postgresql
ansible-galaxy collection install -r requirements.yml
cp inventory.example inventory
ansible-playbook -i inventory site.yml --ask-vault-pass

# MySQL/MariaDB
cd databases/mysql
ansible-galaxy collection install -r requirements.yml
cp inventory.example inventory
ansible-playbook -i inventory site.yml --ask-vault-pass

# Oracle Database
cd databases/oracle
ansible-galaxy collection install -r requirements.yml
cp inventory.example inventory
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Deploy only PostgreSQL replication
ansible-playbook -i inventory site.yml --tags replication

# Deploy only MySQL security hardening
ansible-playbook -i inventory site.yml --tags security

# Deploy only Oracle backup (RMAN)
ansible-playbook -i inventory site.yml --tags backup
```

## 🛡️ Security & Compliance

All database roles implement:

- **Encryption at rest** - TDE (Oracle), pgcrypto (PostgreSQL), data-at-rest encryption (MySQL)
- **Encryption in transit** - TLS/SSL for all client connections
- **Audit logging** - pgAudit, MySQL Audit Plugin, Oracle Unified Auditing
- **Access control** - Role-based access, least privilege, password policies
- **Backup encryption** - Encrypted backups with key management
- **NIST 800-53 controls** - AC, AU, IA, SC control families

## 📚 Additional Resources

See each platform's README for detailed documentation:

- [PostgreSQL README](postgresql/README.md)
- [MySQL/MariaDB README](mysql/README.md)
- [Oracle Database README](oracle/README.md)

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

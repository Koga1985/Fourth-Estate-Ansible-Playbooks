# Database Platforms

This directory contains **25 Ansible roles** across **3 database platforms** for automated installation, configuration, replication, backup, security hardening, and compliance.

## Overview

Enterprise database automation with emphasis on high availability, disaster recovery, and security compliance (DoD STIG, NIST 800-53) for Fourth Estate environments.

## 📋 Supported Databases

| Platform | Roles | Key Features |
|----------|-------|-------------|
| **PostgreSQL** | 5 | Installation, streaming replication, PgPool-II, Barman backup, pgAudit, restore |
| **IBM DB2** | 1 | DB2 V10.5 STIG hardening |

MySQL / MariaDB and Oracle Database were removed: both directories held a
`site.yml` that announced "NO AUTOMATION IMPLEMENTED" and changed nothing, and
neither ever had a `roles/` directory.

## Directory Structure

```
databases/
├── README.md              # This file
├── postgresql/            # PostgreSQL automation (5 roles)
│   ├── README.md
│   ├── roles/
│   ├── site.yml
│   └── requirements.yml
```

## 🚀 Quick Start (Drop-In Deployment)

Each database platform supports independent drop-in deployment:

```bash
# PostgreSQL
cd databases/postgresql
ansible-galaxy collection install -r requirements.yml
cp inventory.example inventory
ansible-playbook -i inventory site.yml --ask-vault-pass

# IBM DB2
ansible-galaxy collection install -r requirements.yml
cp inventory.example inventory
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Deploy only PostgreSQL replication
ansible-playbook -i inventory site.yml --tags replication

# Deploy only PostgreSQL backup
ansible-playbook -i inventory site.yml --tags backup
```

## 🛡️ Security & Compliance

All database roles implement:

- **Encryption at rest** - pgcrypto (PostgreSQL)
- **Encryption in transit** - TLS/SSL for all client connections
- **Audit logging** - pgAudit (PostgreSQL), DB2 audit facility
- **Access control** - Role-based access, least privilege, password policies
- **Backup encryption** - Encrypted backups with key management
- **NIST 800-53 controls** - AC, AU, IA, SC control families

## 📚 Additional Resources

See each platform's README for detailed documentation:

- [PostgreSQL README](postgresql/README.md)

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

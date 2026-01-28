# PostgreSQL Database Automation

This directory contains **8 Ansible roles** for automating **PostgreSQL** database management including installation, configuration, replication, backup, performance tuning, and security hardening.

## 📋 Roles

### Installation & Configuration (2 roles)
- **postgresql_install** - PostgreSQL server installation (apt/yum)
- **postgresql_config** - Server configuration and tuning

### High Availability & Replication (2 roles)
- **postgresql_replication** - Streaming replication setup
- **postgresql_pgpool** - PgPool-II for connection pooling and load balancing

### Backup & Recovery (2 roles)
- **postgresql_backup** - Automated backup with pg_dump/pg_basebackup
- **postgresql_barman** - Barman backup and recovery manager

### Security & Compliance (2 roles)
- **postgresql_security** - Security hardening and SSL/TLS
- **postgresql_audit** - pgAudit for compliance logging

## 🚀 Quick Start (Drop-In Deployment)

This platform supports **drop-in deployment**. Get started in 3 steps:

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your database servers

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

Use tags to deploy specific components:

```bash
# Install only
ansible-playbook -i inventory site.yml --tags install

# Configure replication
ansible-playbook -i inventory site.yml --tags replication

# Security hardening
ansible-playbook -i inventory site.yml --tags security

# Backup configuration
ansible-playbook -i inventory site.yml --tags backup
```

### Individual Role Execution (Alternative)

```bash
# Install PostgreSQL 15
ansible-playbook playbooks/postgresql_install.yml \
  -e "postgresql_version=15" \
  -e "postgresql_data_dir=/var/lib/postgresql/15/main"

# Configure replication
ansible-playbook playbooks/postgresql_replication.yml \
  -e "replication_user=replicator" \
  -e "standby_servers=['db02','db03']"
```

## ⚙️ Configuration

```yaml
# PostgreSQL server configuration
postgresql_version: "15"
postgresql_listen_addresses: "*"
postgresql_port: 5432
postgresql_max_connections: 200
postgresql_shared_buffers: "4GB"
postgresql_effective_cache_size: "12GB"

# Security
postgresql_enable_ssl: true
postgresql_ssl_cert_file: "/etc/postgresql/server.crt"
postgresql_ssl_key_file: "/etc/postgresql/server.key"

# Replication
postgresql_wal_level: "replica"
postgresql_max_wal_senders: 5
postgresql_wal_keep_size: "1GB"
```

---

**Maintained By:** Fourth Estate Infrastructure Team

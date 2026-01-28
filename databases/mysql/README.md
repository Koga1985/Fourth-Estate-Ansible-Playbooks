# MySQL / MariaDB Database Automation

This directory contains **8 Ansible roles** for automating **MySQL** and **MariaDB** database management including installation, configuration, replication, backup, performance tuning, and security hardening.

## 📋 Roles

### Installation & Configuration (2 roles)
- **mysql_install** - MySQL/MariaDB server installation
- **mysql_config** - Server configuration and tuning

### High Availability & Replication (2 roles)
- **mysql_replication** - Master-replica replication setup
- **mysql_galera_cluster** - Galera cluster for MariaDB

### Backup & Recovery (2 roles)
- **mysql_backup** - Automated backup with mysqldump/Percona XtraBackup
- **mysql_binlog_backup** - Binary log backup and point-in-time recovery

### Security & Compliance (2 roles)
- **mysql_security** - Security hardening and SSL/TLS
- **mysql_audit** - Audit plugin for compliance logging

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

# Galera cluster setup
ansible-playbook -i inventory site.yml --tags galera

# Security hardening
ansible-playbook -i inventory site.yml --tags security
```

### Individual Role Execution (Alternative)

```bash
# Install MySQL 8.0
ansible-playbook playbooks/mysql_install.yml \
  -e "mysql_version=8.0" \
  -e "mysql_root_password=SecurePass123!"

# Configure replication
ansible-playbook playbooks/mysql_replication.yml \
  -e "mysql_replication_role=master" \
  -e "mysql_replication_user=replicator"
```

## ⚙️ Configuration

```yaml
# MySQL server configuration
mysql_version: "8.0"
mysql_bind_address: "0.0.0.0"
mysql_port: 3306
mysql_max_connections: 200
mysql_innodb_buffer_pool_size: "4G"

# Security
mysql_enable_ssl: true
mysql_require_secure_transport: true

# Replication
mysql_server_id: 1
mysql_log_bin: "mysql-bin"
mysql_binlog_format: "ROW"
```

---

**Maintained By:** Fourth Estate Infrastructure Team

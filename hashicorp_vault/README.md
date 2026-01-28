# HashiCorp Vault

This directory contains **10 Ansible roles** for automating **HashiCorp Vault** deployment including installation, clustering, high availability, secrets engines, authentication methods, PKI management, and dynamic database credentials.

## 📋 Roles

### Installation & Clustering (3 roles)
- **vault_install** - Vault installation and binary setup
- **vault_cluster** - Multi-node cluster configuration
- **vault_ha_config** - High availability with Consul/Raft

### Secrets Management (3 roles)
- **vault_secrets_engine** - Secrets engines (KV, Transit, PKI)
- **vault_database_secrets** - Dynamic database credentials
- **vault_transit_encryption** - Encryption as a Service

### Access Control (2 roles)
- **vault_auth_methods** - Authentication methods (LDAP, OIDC, AWS, Kubernetes)
- **vault_policies** - Policy management and ACLs

### PKI & Auditing (2 roles)
- **vault_pki** - PKI secrets engine and certificate management
- **vault_audit_logging** - Audit device configuration

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your Vault servers

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Install only
ansible-playbook -i inventory site.yml --tags install

# Configure HA
ansible-playbook -i inventory site.yml --tags ha

# Configure auth methods
ansible-playbook -i inventory site.yml --tags auth

# Configure PKI
ansible-playbook -i inventory site.yml --tags pki
```

### Individual Role Execution (Alternative)

```bash
# Install Vault cluster
ansible-playbook playbooks/vault_install.yml \
  -e "vault_version=1.15.4" \
  -e "vault_cluster_name=production"

# Initialize and unseal Vault
ansible-playbook playbooks/vault_init.yml \
  -e "vault_key_shares=5" \
  -e "vault_key_threshold=3"

# Configure secrets engine
ansible-playbook playbooks/vault_secrets.yml \
  -e "engine_type=kv-v2" \
  -e "mount_path=secret"
```

## ⚙️ Configuration

### Vault Installation

```yaml
# Vault installation
vault_version: "1.15.4"
vault_user: "vault"
vault_group: "vault"
vault_install_dir: "/opt/vault"
vault_config_dir: "/etc/vault.d"
vault_data_dir: "/opt/vault/data"
vault_tls_dir: "/etc/vault.d/tls"

# Binary download
vault_download_url: "https://releases.hashicorp.com/vault/{{ vault_version }}/vault_{{ vault_version }}_linux_amd64.zip"
```

### Cluster Configuration

```yaml
# Vault cluster configuration
vault_cluster_name: "production"
vault_cluster_addr: "https://{{ ansible_default_ipv4.address }}:8201"
vault_api_addr: "https://{{ ansible_default_ipv4.address }}:8200"

# Listener configuration
vault_listener:
  tcp:
    address: "0.0.0.0:8200"
    tls_cert_file: "{{ vault_tls_dir }}/vault.crt"
    tls_key_file: "{{ vault_tls_dir }}/vault.key"
    tls_min_version: "tls12"
    tls_disable: false

# Storage backend
vault_storage:
  type: "raft"  # or consul, dynamodb
  raft:
    path: "{{ vault_data_dir }}/raft"
    node_id: "{{ inventory_hostname }}"
    retry_join:
      - leader_api_addr: "https://vault01.example.com:8200"
      - leader_api_addr: "https://vault02.example.com:8200"
      - leader_api_addr: "https://vault03.example.com:8200"
```

### High Availability Configuration

```yaml
# HA with Raft storage
vault_ha_enabled: true
vault_raft_nodes:
  - hostname: "vault01.example.com"
    ip: "10.0.1.10"
  - hostname: "vault02.example.com"
    ip: "10.0.1.11"
  - hostname: "vault03.example.com"
    ip: "10.0.1.12"

# Performance replication (Enterprise)
vault_performance_replication:
  enabled: true
  primary_cluster_addr: "https://vault-primary.example.com:8201"
```

### Secrets Engine Configuration

```yaml
# KV Secrets Engine v2
secrets_engines:
  - path: "secret/"
    type: "kv-v2"
    description: "General key-value secrets"
    config:
      max_versions: 10
      cas_required: false
      delete_version_after: "0s"

  - path: "applications/"
    type: "kv-v2"
    description: "Application secrets"

  # Transit Encryption
  - path: "transit/"
    type: "transit"
    description: "Encryption as a Service"

  # PKI
  - path: "pki/"
    type: "pki"
    description: "Internal PKI"
    config:
      max_lease_ttl: "87600h"  # 10 years

  # Database dynamic credentials
  - path: "database/"
    type: "database"
    description: "Dynamic database credentials"
```

### Database Secrets Configuration

```yaml
# Dynamic database credentials
database_connections:
  - name: "postgresql-prod"
    plugin: "postgresql-database-plugin"
    connection_url: "postgresql://{{username}}:{{password}}@postgres.example.com:5432/app"
    username: "{{ vault_db_admin_user }}"
    password: "{{ vault_db_admin_password }}"
    allowed_roles:
      - "readonly"
      - "readwrite"

  - name: "mysql-prod"
    plugin: "mysql-database-plugin"
    connection_url: "{{username}}:{{password}}@tcp(mysql.example.com:3306)/"
    username: "{{ vault_mysql_admin_user }}"
    password: "{{ vault_mysql_admin_password }}"

# Database roles
database_roles:
  - name: "readonly"
    db_name: "postgresql-prod"
    creation_statements:
      - "CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';"
      - "GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";"
    default_ttl: "1h"
    max_ttl: "24h"

  - name: "readwrite"
    db_name: "postgresql-prod"
    creation_statements:
      - "CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';"
      - "GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO \"{{name}}\";"
    default_ttl: "2h"
    max_ttl: "8h"
```

### Authentication Methods

```yaml
# Authentication methods
auth_methods:
  # LDAP authentication
  - type: "ldap"
    path: "ldap"
    config:
      url: "ldaps://ldap.example.com"
      userdn: "ou=users,dc=example,dc=com"
      groupdn: "ou=groups,dc=example,dc=com"
      binddn: "cn=vault,ou=service,dc=example,dc=com"
      bindpass: "{{ vault_ldap_password }}"
      userattr: "uid"
      groupattr: "cn"

  # AWS authentication
  - type: "aws"
    path: "aws"
    config:
      iam_server_id_header_value: "vault.example.com"

  # Kubernetes authentication
  - type: "kubernetes"
    path: "kubernetes"
    config:
      kubernetes_host: "https://kubernetes.default.svc"
      kubernetes_ca_cert: "{{ lookup('file', '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt') }}"

  # AppRole (for automation)
  - type: "approle"
    path: "approle"
```

### Policy Configuration

```yaml
# Vault policies
vault_policies:
  - name: "admin"
    policy: |
      # Full access to everything
      path "*" {
        capabilities = ["create", "read", "update", "delete", "list", "sudo"]
      }

  - name: "app-developer"
    policy: |
      # Read/write to applications secrets
      path "secret/data/applications/*" {
        capabilities = ["create", "read", "update", "delete", "list"]
      }
      # Read database credentials
      path "database/creds/readonly" {
        capabilities = ["read"]
      }

  - name: "ops-team"
    policy: |
      # Full access to infrastructure secrets
      path "secret/data/infrastructure/*" {
        capabilities = ["create", "read", "update", "delete", "list"]
      }
      # Read/write database credentials
      path "database/creds/*" {
        capabilities = ["read"]
      }
      # Transit encryption
      path "transit/encrypt/*" {
        capabilities = ["update"]
      }
      path "transit/decrypt/*" {
        capabilities = ["update"]
      }

  - name: "readonly"
    policy: |
      # Read-only access to secrets
      path "secret/data/*" {
        capabilities = ["read", "list"]
      }
```

### PKI Configuration

```yaml
# PKI secrets engine
pki_config:
  root_ca:
    path: "pki"
    common_name: "Example Root CA"
    ttl: "87600h"  # 10 years
    key_type: "rsa"
    key_bits: 4096

  intermediate_ca:
    path: "pki_int"
    common_name: "Example Intermediate CA"
    ttl: "43800h"  # 5 years
    csr_path: "/tmp/pki_intermediate.csr"

  # PKI roles for certificate issuance
  roles:
    - name: "example-dot-com"
      allowed_domains:
        - "example.com"
        - "*.example.com"
      allow_subdomains: true
      max_ttl: "8760h"  # 1 year
      key_type: "rsa"
      key_bits: 2048

    - name: "internal-servers"
      allowed_domains:
        - "*.internal.example.com"
      allow_bare_domains: false
      allow_subdomains: true
      max_ttl: "2160h"  # 90 days
```

### Audit Logging

```yaml
# Audit devices
audit_devices:
  - type: "file"
    path: "file"
    options:
      file_path: "/var/log/vault/audit.log"
      log_raw: false
      hmac_accessor: true
      mode: "0600"

  - type: "syslog"
    path: "syslog"
    options:
      facility: "LOCAL7"
      tag: "vault"

  # Send to SIEM
  - type: "socket"
    path: "socket"
    options:
      address: "siem.example.com:514"
      socket_type: "tcp"
```

## 📖 Common Use Cases

### Use Case 1: Deploy Vault HA Cluster

```yaml
---
# playbooks/vault_ha_deploy.yml
- name: Deploy Vault HA Cluster
  hosts: vault_servers
  become: true

  roles:
    - role: vault_install
      vars:
        vault_version: "1.15.4"

    - role: vault_cluster
      vars:
        vault_storage_type: "raft"

    - role: vault_ha_config
      vars:
        vault_ha_enabled: true
```

### Use Case 2: Configure Dynamic Database Credentials

```bash
ansible-playbook playbooks/vault_database.yml \
  -e "db_type=postgresql" \
  -e "db_host=postgres.example.com" \
  -e "role_name=app-readonly"
```

### Use Case 3: Setup PKI for Internal Certificates

```bash
ansible-playbook playbooks/vault_pki.yml \
  -e "root_ca_cn=Internal Root CA" \
  -e "allowed_domains=*.internal.example.com"
```

### Use Case 4: Configure LDAP Authentication

```bash
ansible-playbook playbooks/vault_auth_ldap.yml \
  -e "ldap_url=ldaps://ldap.example.com" \
  -e "ldap_userdn=ou=users,dc=example,dc=com"
```

## 🔄 Integration Examples

### Integration with Ansible

```yaml
# Use Vault secrets in Ansible playbooks
- name: Get database credentials from Vault
  set_fact:
    db_creds: "{{ lookup('hashi_vault', 'secret=database/creds/readonly') }}"

- name: Connect to database
  postgresql_db:
    login_host: postgres.example.com
    login_user: "{{ db_creds.username }}"
    login_password: "{{ db_creds.password }}"
    name: myapp
```

### Integration with Kubernetes

```yaml
# Kubernetes deployment using Vault
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  template:
    spec:
      serviceAccountName: myapp
      containers:
      - name: myapp
        image: myapp:latest
        env:
        - name: DATABASE_URL
          value: "vault:database/creds/readonly"
      initContainers:
      - name: vault-agent
        image: vault:1.15.4
        args:
        - agent
        - -config=/vault/config/agent.hcl
```

### Integration with CI/CD (GitLab)

```yaml
# .gitlab-ci.yml
variables:
  VAULT_ADDR: "https://vault.example.com"

deploy:
  script:
    - export VAULT_TOKEN=$(vault write -field=token auth/gitlab/login role=deploy jwt=$CI_JOB_JWT)
    - export DB_PASSWORD=$(vault read -field=password database/creds/deploy)
    - ./deploy.sh
```

## 🛡️ Security Best Practices

1. **Enable TLS** - Always use TLS for Vault communication
2. **Auto-Unseal** - Use cloud KMS for auto-unsealing (AWS KMS, Azure Key Vault)
3. **Audit Logging** - Enable comprehensive audit logs
4. **Least Privilege** - Grant minimal required permissions in policies
5. **Short TTL** - Use short TTLs for dynamic secrets
6. **Revocation** - Implement automated secret revocation
7. **MFA** - Enable MFA for sensitive operations
8. **Namespaces** - Use namespaces (Enterprise) for multi-tenancy
9. **Seal Wrap** - Enable seal wrapping for sensitive data
10. **Regular Rotation** - Rotate root tokens and unseal keys regularly

## 🔧 Troubleshooting

### Issue: Vault Sealed

**Symptoms:** "Vault is sealed" error

**Resolution:**
```bash
# Check seal status
vault status

# Unseal Vault (requires threshold number of keys)
vault operator unseal <unseal-key-1>
vault operator unseal <unseal-key-2>
vault operator unseal <unseal-key-3>

# Automate unsealing with Ansible
ansible-playbook playbooks/vault_unseal.yml
```

### Issue: Permission Denied

**Symptoms:** "permission denied" when accessing secrets

**Resolution:**
```bash
# Check current token capabilities
vault token capabilities secret/data/myapp

# Check policy
vault policy read app-developer

# Verify token is associated with correct policy
vault token lookup
```

### Issue: Database Connection Failed

**Symptoms:** Cannot connect to database for dynamic credentials

**Resolution:**
```bash
# Test database connection
vault write database/config/postgresql-prod \
  connection_url="postgresql://{{username}}:{{password}}@postgres:5432/app" \
  username="vault" \
  password="secret"

# Rotate root credentials
vault write -force database/rotate-root/postgresql-prod

# Test credential generation
vault read database/creds/readonly
```

## 📚 Additional Resources

- [HashiCorp Vault Documentation](https://www.vaultproject.io/docs)
- [Vault API Documentation](https://www.vaultproject.io/api-docs)
- [Vault Tutorials](https://learn.hashicorp.com/vault)
- [Vault GitHub Repository](https://github.com/hashicorp/vault)
- [Vault Community Forum](https://discuss.hashicorp.com/c/vault)
- [Ansible Vault Lookup Plugin](https://docs.ansible.com/ansible/latest/collections/community/hashi_vault/)

## 🤝 Contributing

When contributing to Vault automation:
- Test in development Vault instance first
- Never commit unseal keys or root tokens
- Use Ansible Vault for sensitive variables
- Document policy requirements
- Include rollback procedures
- Test HA failover scenarios
- Validate audit log configuration

---

**Last Updated:** 2026-01-16
**Maintained By:** Fourth Estate Infrastructure Team
**Vault Versions Supported:** 1.13+, 1.14+, 1.15+

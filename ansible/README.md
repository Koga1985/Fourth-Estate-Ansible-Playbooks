# Ansible Automation Platform

This directory contains Ansible roles and tasks for managing and configuring **Ansible Automation Platform (AAP)** and **Ansible Controller** (formerly AWX/Ansible Tower).

## Overview

The Ansible automation includes **17 roles** covering the full lifecycle of Ansible Automation Platform including controller configuration, execution environment management, inventory synchronization, credential management, and CI/CD integration.

## 📋 Role Categories

### Controller Configuration (8 roles)
- **ans_core_inventory_hygiene** - Inventory validation and cleanup
- **ans_ctrl__orgs_teams** - Organization and team management
- **ans_ctrl__projects_git** - Git project synchronization
- **ans_ctrl__credentials** - Credential management (vault, SSH, API keys)
- **ans_ctrl__ee_images_map** - Execution environment image mapping
- **ans_ctrl__ee_registries** - Container registry configuration
- **ans_ctrl__org_settings** - Organization-level settings
- **ans_ctrl__upgrade_window** - Maintenance window management

### Execution & Performance (3 roles)
- **ans_perf__forks_strategy** - Parallel execution optimization
- **ans_secrets__env_to_vault** - Environment variable to Ansible Vault migration
- **ans_ctrl__backups_export** - Backup and export automation

### CI/CD & Automation (6 roles)
- Integration with GitLab/GitHub
- Automated playbook testing
- Job template management
- Workflow orchestration
- Notification configuration
- Credential rotation

## 🚀 Quick Start

### Prerequisites

- Ansible 2.12.0 or higher
- `ansible.controller` collection (version 4.0.0+)
- Access to Ansible Controller with admin privileges
- Controller API token or username/password

### Installation

```bash
# Install required collections
ansible-galaxy collection install ansible.controller

# Verify collection
ansible-galaxy collection list | grep controller
```

### Basic Configuration

1. **Configure Controller Connection:**

```yaml
# group_vars/controller.yml
controller_hostname: "controller.example.com"
controller_username: "{{ vault_controller_username }}"
controller_password: "{{ vault_controller_password }}"
controller_validate_certs: true
```

2. **Create Organizations and Teams:**

```bash
# Run organization setup
ansible-playbook tasks/ans_ctrl__orgs_teams.yml \
  -i inventory/controller.yml \
  --ask-vault-pass
```

3. **Configure Execution Environments:**

```bash
# Set up execution environment registries
ansible-playbook tasks/ans_ctrl__ee_registries.yml \
  -i inventory/controller.yml
```

## 📁 Directory Structure

```text
ansible/
├── README.md                           # This file
├── roles/                              # Ansible roles
│   ├── ans_core_inventory_hygiene/    # Inventory validation
│   ├── ans_ctrl__credentials/         # Credential management
│   ├── ans_ctrl__ee_images_map/       # EE image mapping
│   ├── ans_ctrl__ee_registries/       # Registry config
│   ├── ans_ctrl__orgs_teams/          # Org/team management
│   ├── ans_ctrl__org_settings/        # Org settings
│   ├── ans_ctrl__projects_git/        # Git projects
│   ├── ans_ctrl__upgrade_window/      # Maintenance windows
│   ├── ans_ctrl__backups_export/      # Backup automation
│   ├── ans_perf__forks_strategy/      # Performance tuning
│   └── ans_secrets__env_to_vault/     # Secret migration
└── tasks/                              # Standalone task files
    ├── ans_ctrl__orgs_teams.yml
    ├── ans_ctrl__projects_git.yml
    ├── ans_ctrl__credentials.yml
    ├── ans_ctrl__ee_images_map.yml
    ├── ans_ctrl__ee_registries.yml
    ├── ans_ctrl__org_settings.yml
    ├── ans_ctrl__upgrade_window.yml
    ├── ans_ctrl__backups_export.yml
    ├── ans_perf__forks_strategy.yml
    └── ans_secrets__env_to_vault.yml
```

## 🔑 Key Features

### Organization Management
- Create and configure organizations
- Set up team hierarchies
- Assign RBAC permissions
- Configure organization-level settings

### Credential Management
- Secure credential storage
- Credential type management
- Vault integration
- Credential rotation automation

### Execution Environment Management
- Container registry configuration
- EE image synchronization
- Dependency management
- Custom EE building

### Performance Optimization
- Fork strategy optimization
- Parallel execution tuning
- Memory management
- Job concurrency control

### Backup & Disaster Recovery
- Automated backups
- Configuration exports
- Disaster recovery procedures
- Version control integration

## 📖 Common Use Cases

### Use Case 1: Initial Controller Setup

```yaml
---
# playbook_controller_bootstrap.yml
- name: Bootstrap Ansible Controller
  hosts: localhost
  connection: local
  gather_facts: false

  tasks:
    - name: Configure organizations
      include_tasks: tasks/ans_ctrl__orgs_teams.yml

    - name: Set up credentials
      include_tasks: tasks/ans_ctrl__credentials.yml

    - name: Configure execution environments
      include_tasks: tasks/ans_ctrl__ee_registries.yml

    - name: Sync Git projects
      include_tasks: tasks/ans_ctrl__projects_git.yml
```

### Use Case 2: Migrate Secrets to Vault

```bash
# Migrate environment variables to Ansible Vault
ansible-playbook tasks/ans_secrets__env_to_vault.yml \
  -e "source_env_file=.env" \
  -e "vault_file=group_vars/all/vault.yml"
```

### Use Case 3: Optimize Performance

```bash
# Apply performance optimizations
ansible-playbook tasks/ans_perf__forks_strategy.yml \
  -i inventory/controller.yml \
  -e "forks=50" \
  -e "job_slice_count=10"
```

### Use Case 4: Backup Controller Configuration

```bash
# Export controller configuration
ansible-playbook tasks/ans_ctrl__backups_export.yml \
  -i inventory/controller.yml \
  -e "backup_dir=/backup/controller/$(date +%Y%m%d)"
```

## ⚙️ Configuration Variables

### Controller Connection

```yaml
controller_hostname: "controller.example.com"
controller_username: "{{ vault_controller_username }}"
controller_password: "{{ vault_controller_password }}"
controller_validate_certs: true
controller_oauth_token: "{{ vault_controller_token }}"  # Alternative to username/password
```

### Organization Settings

```yaml
ans_organizations:
  - name: "Fourth Estate"
    description: "Free Press Infrastructure"
    max_hosts: 1000
    custom_virtualenv: "/opt/venvs/fourth-estate"

ans_teams:
  - name: "Infrastructure Team"
    organization: "Fourth Estate"
    description: "Core infrastructure automation"
```

### Execution Environment

```yaml
ans_ee_registries:
  - name: "quay.io"
    url: "https://quay.io"
    username: "{{ vault_quay_username }}"
    password: "{{ vault_quay_password }}"

ans_ee_images:
  - name: "fourth-estate-ee"
    image: "quay.io/org/fourth-estate-ee:latest"
    pull: "always"
```

### Performance Tuning

```yaml
ans_forks: 50                    # Parallel execution forks
ans_job_slice_count: 10          # Job slicing for large inventories
ans_fact_cache_timeout: 86400    # Fact cache duration (seconds)
ans_timeout: 600                 # Task timeout (seconds)
```

## 🛡️ Security Best Practices

1. **Use OAuth Tokens** instead of username/password for API access
2. **Enable Certificate Validation** (`controller_validate_certs: true`)
3. **Rotate Credentials** regularly using automated tasks
4. **Limit RBAC Permissions** to least privilege required
5. **Audit Logs** - Enable comprehensive audit logging
6. **Backup Regularly** - Automate daily configuration backups
7. **Use Execution Environments** for dependency isolation

## 🔧 Troubleshooting

### Issue: API Connection Failures

**Symptoms:** Playbooks fail with connection timeout or authentication errors

**Resolution:**
```bash
# Test API connectivity
curl -k https://controller.example.com/api/v2/ping/

# Verify credentials
ansible-tower-cli config host controller.example.com
ansible-tower-cli config username admin
ansible-tower-cli config password
ansible-tower-cli me
```

### Issue: Execution Environment Pull Failures

**Symptoms:** Jobs fail with "unable to pull image" errors

**Resolution:**
```bash
# Verify registry configuration
ansible-playbook tasks/ans_ctrl__ee_registries.yml --check

# Test manual pull
podman login quay.io
podman pull quay.io/org/fourth-estate-ee:latest
```

### Issue: Performance Degradation

**Symptoms:** Jobs running slower than expected

**Resolution:**
```bash
# Apply performance tuning
ansible-playbook tasks/ans_perf__forks_strategy.yml \
  -e "forks=100" \
  -e "pipelining=true"
```

## 📚 Additional Resources

- [Ansible Automation Platform Documentation](https://docs.ansible.com/automation-controller/)
- [Ansible Controller API Guide](https://docs.ansible.com/automation-controller/latest/html/controllerapi/index.html)
- [Execution Environment Guide](https://docs.ansible.com/automation-controller/latest/html/userguide/execution_environments.html)
- [Best Practices](https://docs.ansible.com/automation-controller/latest/html/userguide/best_practices.html)

## 🤝 Contributing

When contributing to Ansible automation:
- Follow the ansible.controller collection patterns
- Include comprehensive error handling
- Document all variables in role defaults
- Test against Controller 4.x and AAP 2.x
- Include backup procedures for destructive operations

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

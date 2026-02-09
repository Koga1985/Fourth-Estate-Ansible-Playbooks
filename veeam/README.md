# Veeam Backup & Replication

This directory contains **6 Ansible roles** for automating **Veeam Backup & Replication** lifecycle management including installation, backup job configuration, restore operations, replication, cloud tiering, and automated testing with SureBackup.

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your Veeam servers

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Install Veeam server
ansible-playbook -i inventory site.yml --tags install

# Configure backup jobs
ansible-playbook -i inventory site.yml --tags backup

# Configure replication
ansible-playbook -i inventory site.yml --tags replication

# Configure cloud tier
ansible-playbook -i inventory site.yml --tags cloud
```

## Overview

Comprehensive Veeam automation covering backup server installation, repository management, backup job creation and scheduling, restore operations, replication configuration, cloud archive tier setup, and automated backup testing. Where possible, playbooks use idempotent operations; however, some Veeam API calls may be inherently imperative. Review each playbook's variable list before running in production.

## 📋 Roles

### Installation & Configuration (1 role)
- **veeam_backup_server_install** - Veeam Backup & Replication server installation and initial configuration

### Backup Operations (2 roles)
- **veeam_backup_jobs** - Backup job creation, scheduling, and management
- **veeam_restore_operations** - Automated restore workflows and testing

### Advanced Features (3 roles)
- **veeam_replication** - Replication job configuration for DR
- **veeam_cloud_tier** - Cloud archive tier (AWS, Azure, S3-compatible) setup
- **veeam_surebackup** - Automated backup verification and testing

## Prerequisites

- Ansible 2.12+ (2.14+ recommended)
- Python packages on the control node: `requests`
- Access to the Veeam server(s) and API/CLI credentials

## ⚙️ Configuration

Example `group_vars/veeam.yml` (vault this file in production):

```yaml
---
veeam_server: "veeam.example.local"
veeam_user: "ansible_bot"
veeam_password: "{{ vault_veeam_password }}"
veeam_validate_certs: false
veeam_repository: "MainRepo"
veeam_repo_path: "/backup/repo"
```

### Key Variables

| Variable | Description |
|----------|-------------|
| `veeam_server` | FQDN/IP for Veeam Backup & Replication (or REST API gateway) |
| `veeam_user` | Service account with API/CLI rights |
| `veeam_password` | Vault this value; never store plaintext |
| `veeam_validate_certs` | Set `true` in production when using trusted CA |
| `veeam_repository` | Repository name or identifier |
| `veeam_repo_path` | Path for file-based repositories |
| `veeam_job_name` | Used by job creation tasks |

## 📖 Usage Examples

### Install Veeam Components

```yaml
- name: Install Veeam Backup & Replication
  hosts: localhost
  gather_facts: false
  vars_files:
    - group_vars/veeam.yml
  tasks:
    - name: Ensure Veeam MSI installed (Windows)
      win_package:
        path: "./artifacts/VeeamBackup.msi"
        state: present
      when: ansible_os_family == 'Windows'
```

### Create a Backup Job

```yaml
- name: Create a backup job
  hosts: localhost
  gather_facts: false
  vars_files:
    - group_vars/veeam.yml
  tasks:
    - include_role:
        name: veeam_backup_jobs
      vars:
        veeam_job_name: "nightly-vm-backup"
        veeam_vm_list:
          - "vm-01"
          - "vm-02"
```

## 🛡️ Security

- Store secrets in Ansible Vault or a secrets manager
- Ensure service accounts have only the permissions required for automation
- Set `veeam_validate_certs: true` in production with a trusted CA

## 🔧 Troubleshooting

- **TLS/connection errors**: Confirm `veeam_validate_certs` and network reachability
- **Authentication errors**: Verify the `veeam_user` has API privileges
- **API schema changes**: Consult Veeam API docs for your product version

## 📚 References

- [Veeam REST API Documentation](https://helpcenter.veeam.com/docs/backup/rest/)
- [Ansible URI Module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html)

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

# Cisco UCS Playbooks

## Overview

This directory contains production-ready playbooks for deploying and managing Cisco UCS infrastructure for Fourth Estate organizations.

## Playbooks

### ucs_fourth_estate_production.yml

Complete production deployment playbook for Fourth Estate UCS infrastructure.

**Features:**
- Full infrastructure deployment
- Network configuration
- Security hardening (DoD STIG + NIST 800-53)
- Monitoring setup
- Backup and disaster recovery

**Usage:**

Dry run (plan only):
```bash
ansible-playbook cisco/playbooks/ucs_fourth_estate_production.yml \
  -e "ucs_hostname=ucs-manager.example.com" \
  --ask-vault-pass
```

Apply changes:
```bash
ansible-playbook cisco/playbooks/ucs_fourth_estate_production.yml \
  -e "ucs_hostname=ucs-manager.example.com" \
  -e "apply_changes=true" \
  --ask-vault-pass
```

Run specific sections:
```bash
# Infrastructure only
ansible-playbook cisco/playbooks/ucs_fourth_estate_production.yml --tags infrastructure

# Security hardening only
ansible-playbook cisco/playbooks/ucs_fourth_estate_production.yml --tags security

# Networking only
ansible-playbook cisco/playbooks/ucs_fourth_estate_production.yml --tags networking
```

## Variables

Key variables that should be defined:

**Required:**
- `ucs_hostname`: UCS Manager IP/hostname
- `ucs_username`: Admin username
- `ucs_password`: Admin password

**Optional:**
- `apply_changes`: Set to `true` to apply (default: `false`)
- `fourth_estate_org_name`: Organization name (default: "FourthEstate")
- `ucs_artifacts_dir`: Artifacts directory (default: "/tmp/ucs-fourth-estate-artifacts")

## Ansible Vault

Store sensitive variables in Ansible Vault:

```bash
# Create vault file
ansible-vault create group_vars/all/vault.yml

# Add variables:
vault_ucs_hostname: "ucs-manager.example.com"
vault_ucs_username: "admin"
vault_ucs_password: "password"
vault_fourth_estate_contact: "Contact Name"
vault_fourth_estate_email: "contact@example.com"
vault_backup_server: "backup.example.com"
vault_backup_username: "backup"
vault_backup_password: "password"
```

## Tags

Available tags for selective execution:

- `infrastructure`: Infrastructure deployment
- `networking`: Network configuration
- `security`: Security hardening
- `hardening`: Security hardening
- `compliance`: Compliance controls
- `monitoring`: Monitoring setup
- `backup`: Backup configuration
- `dr`: Disaster recovery

## Compliance

These playbooks implement:

- **DoD STIG**: Category I, II, and III findings
- **NIST 800-53**: All relevant control families
- **NIST 800-171**: CUI protection
- **FISMA**: Moderate and High baselines

## Support

For issues or questions, refer to the role README files:

- `../roles/ucs_prod_infrastructure/README.md`
- `../roles/ucs_security_hardening/README.md`
- `../roles/ucs_prod_networking/README.md`
- `../roles/ucs_prod_monitoring/README.md`
- `../roles/ucs_prod_backup_dr/README.md`

# Splunk Roles

This directory contains **6 Ansible roles** for deploying and managing Splunk Enterprise and Universal Forwarders in DoD STIG and NIST 800-53 compliant environments.

## Roles

| Role | Description |
|------|-------------|
| **splunk_enterprise_install** | Installs Splunk Enterprise with FIPS 140-2 mode, TLS 1.2+ enforcement, DoD PKI certificate integration, secure password policies, LDAP/SAML/MFA support, comprehensive audit logging, SELinux integration, and firewall configuration. |
| **splunk_security_hardening** | Applies DoD STIG Category I, II, and III controls to an existing Splunk installation: RBAC enforcement, authentication hardening, cipher suite restriction, session timeouts, file system hardening, and compliance report generation. |
| **splunk_forwarder** | Deploys and configures the Splunk Universal Forwarder with TLS-encrypted forwarding, FIPS mode support, data input configuration, and performance tuning for log collection targets. |
| **splunk_indexer_cluster** | Configures a Splunk indexer cluster, managing replication factor, search factor, cluster manager settings, site-aware replication, and SmartStore tiering. |
| **splunk_monitoring** | Implements automated health checks, Splunk internal metrics collection, compliance monitoring for FIPS/TLS/audit settings, resource utilization alerting, and email/webhook notification. |
| **splunk_backup_dr** | Configures AES-256 encrypted backup jobs with 90-day retention, 7-year archive retention for compliance, and documents disaster recovery procedures including DR site replication. |

## Requirements

- Ansible 2.12+
- `ansible.posix` and `community.general` collections:
  ```bash
  ansible-galaxy collection install ansible.posix community.general
  ```
- Target OS: RHEL 8/9, Rocky Linux 8/9, or Ubuntu 20.04/22.04
- Minimum 12 CPU / 12 GB RAM / 500 GB disk on Splunk servers
- `become: true` for installation tasks

## Quick Start

```bash
ansible-playbook -i inventory site.yml --tags install --ask-vault-pass
```

## Example Playbook

```yaml
---
- name: Deploy Splunk Enterprise with STIG hardening
  hosts: splunk_servers
  become: true

  vars:
    splunk_version: "9.2.1"
    splunk_enable_fips: true
    splunk_tls_min_version: "tls1.2"
    splunk_admin_password: "{{ vault_splunk_admin_password }}"
    splunk_enable_mfa: true

  roles:
    - role: splunk/roles/splunk_enterprise_install
    - role: splunk/roles/splunk_security_hardening
      vars:
        stig_cat1_enabled: true
        stig_cat2_enabled: true
        stig_cat3_enabled: true
    - role: splunk/roles/splunk_monitoring
    - role: splunk/roles/splunk_backup_dr
      vars:
        backup_path: "/backup/splunk"
        backup_retention_days: 90
        backup_encryption_enabled: true
```

## Key Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `splunk_version` | `"9.2.1"` | Splunk Enterprise version to install. |
| `splunk_enable_fips` | `true` | Enable FIPS 140-2 mode. |
| `splunk_tls_min_version` | `"tls1.2"` | Minimum TLS version to accept. |
| `splunk_admin_password` | (required) | Admin password; use Ansible Vault. |
| `stig_cat1_enabled` | `true` | Apply STIG Category I (High) controls. |
| `backup_retention_days` | `90` | Days to retain local backup archives. |

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

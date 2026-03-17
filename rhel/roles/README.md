# RHEL Roles

This directory contains **5 Ansible roles** for Red Hat Enterprise Linux (RHEL) lifecycle management, covering system hardening, patch management, firewall and SELinux configuration, user access control, and audit logging. All roles are designed to satisfy DoD STIG, NIST SP 800-53 Rev 5, and CIS Benchmark requirements.

## Roles

| Role | Description |
|------|-------------|
| **rhel-hardening** | Comprehensive system hardening following DoD STIG (RHEL 8 V1R14 / RHEL 9 V1R3) and NIST SP 800-53. Covers SSH, PAM, password policies, kernel parameters, file system permissions, unnecessary service removal, and optional FIPS 140-2 enablement. |
| **rhel-patch-management** | Automated patch management with security-update prioritization, reboot scheduling, package exclusion lists, and update history tracking. Supports subscription-manager integration for RHEL repositories. |
| **rhel-firewall-selinux** | Manages firewalld zone configuration, service and port rules, rich rules, and SELinux policy enforcement mode. Includes audit2allow integration for custom policy development. |
| **rhel-user-access** | User and group lifecycle management with least-privilege enforcement, sudo configuration, SSH key management, password aging policies, account expiration, and inactive account cleanup. |
| **rhel-audit-logging** | Auditd configuration (STIG-compliant ruleset), log rotation and retention, remote syslog forwarding via rsyslog, AIDE file integrity monitoring setup, and audit log permission hardening. |

## Requirements

- Ansible 2.12+
- RHEL 8.6+ or RHEL 9.0+
- `ansible.posix` and `community.general` collections:
  ```bash
  ansible-galaxy collection install ansible.posix community.general
  ```
- `become: true` (root privileges required for all roles)

## Quick Start

```bash
ansible-playbook -i inventory site.yml --tags hardening --ask-vault-pass
```

## Example Playbook

```yaml
---
- name: Apply RHEL security baseline
  hosts: rhel_servers
  become: true

  roles:
    - role: rhel/roles/rhel-hardening
      vars:
        rhel_stig_level: high
        rhel_enable_fips: true
        rhel_ssh_permit_root_login: false

    - role: rhel/roles/rhel-firewall-selinux
      vars:
        rhel_selinux_state: enforcing
        rhel_firewall_services:
          - ssh

    - role: rhel/roles/rhel-audit-logging
      vars:
        rhel_audit_log_retention_days: 90
        rhel_remote_logging_enabled: false

    - role: rhel/roles/rhel-user-access
      vars:
        rhel_password_max_days: 60
        rhel_lock_inactive_accounts: true

    - role: rhel/roles/rhel-patch-management
      vars:
        rhel_security_updates_only: false
        rhel_auto_reboot: false
```

## Compliance Tags

All roles support granular execution via Ansible tags:

- `stig` - DoD STIG controls only
- `nist` - NIST SP 800-53 controls
- `hardening` - System hardening tasks
- `ssh` - SSH configuration
- `firewall` - Firewall rules
- `selinux` - SELinux configuration
- `audit` - Audit daemon setup
- `users` - User management
- `patching` - Patch management

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

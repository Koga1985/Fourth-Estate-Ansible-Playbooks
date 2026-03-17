# Illumio Roles

This directory contains **4 Ansible roles** for managing the Illumio Core zero trust segmentation platform, covering PCE installation, VEN fleet operations, policy lifecycle management, and security posture reporting.

## Roles

| Role | Description |
|------|-------------|
| **illumio_pce_install** | Installs and bootstraps the Illumio Policy Compute Engine (PCE), configuring certificates, database initialization, and initial admin credentials. |
| **illumio_ven_fleet** | Manages the VEN (Virtual Enforcement Node) fleet lifecycle: installs VEN packages on Linux and Windows workloads, handles pairing key distribution, upgrades, mode changes (idle/visibility/enforcement), and decommission/unpair. |
| **illumio_policy_lifecycle** | Drives the Illumio policy workflow from draft creation through test-mode validation to production enforcement. Includes brownout checks, rule apply/rollback, hitcount reporting, and shadow/overlap analysis. |
| **illumio_reporting_pack** | Generates segmentation scorecards, application coverage reports, audit event exports, and daily digest summaries for operational and compliance consumers. |

## Requirements

- Ansible 2.12+
- Illumio PCE reachable from the Ansible control host (HTTPS, default port 8443)
- PCE API key and secret (stored in Ansible Vault)
- For VEN installation roles: SSH access (Linux) or WinRM access (Windows) to target workloads
- `illumio.core` collection (if using module-based tasks):
  ```bash
  ansible-galaxy collection install illumio.core
  ```

## Quick Start

```bash
ansible-playbook -i inventory site.yml --tags ven_fleet --ask-vault-pass
```

## Example Playbook

```yaml
---
- name: Install VENs and activate enforcement
  hosts: app_servers
  become: true

  vars:
    illumio_pce_host: "pce.example.com"
    illumio_pce_port: 8443
    illumio_api_key: "{{ vault_illumio_api_key }}"
    illumio_api_secret: "{{ vault_illumio_api_secret }}"
    illumio_org_id: 1

  roles:
    - role: illumio/roles/illumio_ven_fleet
      vars:
        ven_action: install
        ven_pairing_profile: "fourth-estate-prod"

- name: Promote policy to enforcement
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: illumio/roles/illumio_policy_lifecycle
      vars:
        policy_action: promote
        target_mode: enforced
```

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

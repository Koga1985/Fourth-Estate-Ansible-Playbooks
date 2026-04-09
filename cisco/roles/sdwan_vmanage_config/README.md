# sdwan_vmanage_config

## Overview

Configures the Cisco SD-WAN **vManage** controller with user groups (RBAC), feature templates embedding STIG-compliant baselines, device templates, and SD-WAN policies. This is **Phase 16** of the Fourth Estate Cisco SD-WAN deployment.

## Features

- RBAC user group creation (netadmin, operator, readonly)
- Local break-glass and automation account creation
- Feature templates (System, AAA, Logging, NTP, Banner, SNMP, VPN)
- Composite device templates for vEdge-cloud and cEdge devices
- SD-WAN centralized policy configuration
- Defaults to **dry-run mode** (`apply_changes: false`)

## Requirements

- Ansible 2.15+
- Phase 15 (`sdwan_vmanage_deploy`) must be complete
- Vault variables populated

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sdwan_vmanage_host` | `{{ vault_sdwan_vmanage_host }}` | **Yes** | vManage hostname or IP |
| `apply_changes` | `false` | No | Set `true` to apply |
| `sdwan_vmanage_user_groups` | see defaults | No | RBAC user groups to create |
| `sdwan_vmanage_users` | see defaults | No | Local accounts to create |
| `sdwan_feature_templates` | see defaults | No | Feature templates to deploy |
| `sdwan_device_templates` | see defaults | No | Device templates to deploy |

## Example Playbook

```yaml
- name: SD-WAN vManage Configuration
  hosts: localhost
  connection: local
  gather_facts: false
  tasks:
    - ansible.builtin.include_role:
        name: sdwan_vmanage_config
```

## Tags

`sdwan`, `vmanage`, `users`, `rbac`, `templates`, `feature-templates`, `device-templates`, `policies`, `phase16`

## Compliance

User groups implement NIST AC-2, AC-3, AC-6 (Least Privilege / RBAC). Feature templates embed STIG-compliant settings for CISC-ND-001190 (AAA), CISC-ND-000700 (logging), CISC-ND-001290 (NTP), CISC-ND-000080 (banner), CISC-ND-000090 (SNMPv3).

## Author

Fourth Estate Infrastructure Team

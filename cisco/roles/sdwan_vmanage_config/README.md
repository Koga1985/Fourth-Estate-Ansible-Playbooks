# sdwan_vmanage_config

## Requirements

- Ansible 2.15+
- Phase 15 (`sdwan_vmanage_deploy`) must be complete
- Vault variables populated

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sdwan_vmanage_host` | `"{{ vault_sdwan_vmanage_host }}"` | No | vManage Connection Parameters |
| `sdwan_vmanage_port` | `443` | No | — |
| `sdwan_vmanage_username` | `"{{ vault_sdwan_vmanage_username }}"` | No | — |
| `sdwan_vmanage_password` | `"{{ vault_sdwan_vmanage_password }}"` | No | — |
| `sdwan_vmanage_verify_ssl` | `true` | No | — |
| `sdwan_vmanage_timeout` | `30` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `sdwan_artifacts_dir` | `"/tmp/sdwan-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Organization |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `fourth_estate_environment` | `"production"` | No | — |
| `fourth_estate_region` | `"primary"` | No | — |
| `enable_user_config` | `true` | No | Feature Toggles |
| `enable_feature_templates` | `true` | No | — |
| `enable_device_templates` | `true` | No | — |
| `enable_policy_config` | `true` | No | — |
| `enable_vedge_lists` | `true` | No | — |
| `sdwan_vmanage_user_groups` | `(see defaults/main.yml)` | No | vManage User Groups (RBAC) NIST AC-2, AC-3, AC-6 \| STIG CISC-ND-000360 |
| `sdwan_vmanage_users` | `(see defaults/main.yml)` | No | vManage Local Users (break-glass and automation only) |
| `sdwan_feature_templates` | `(see defaults/main.yml)` | No | Feature Templates Standard Fourth Estate SD-WAN feature template set |
| `sdwan_device_templates` | `(see defaults/main.yml)` | No | Device Templates |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |

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

## Overview

Configures the Cisco SD-WAN **vManage** controller with user groups (RBAC), feature templates embedding STIG-compliant baselines, device templates, and SD-WAN policies. This is **Phase 16** of the Fourth Estate Cisco SD-WAN deployment.

## Features

- RBAC user group creation (netadmin, operator, readonly)
- Local break-glass and automation account creation
- Feature templates (System, AAA, Logging, NTP, Banner, SNMP, VPN)
- Composite device templates for vEdge-cloud and cEdge devices
- SD-WAN centralized policy configuration
- Defaults to **dry-run mode** (`apply_changes: false`)

## Compliance

User groups implement NIST AC-2, AC-3, AC-6 (Least Privilege / RBAC). Feature templates embed STIG-compliant settings for CISC-ND-001190 (AAA), CISC-ND-000700 (logging), CISC-ND-001290 (NTP), CISC-ND-000080 (banner), CISC-ND-000090 (SNMPv3).

## Author

Fourth Estate Infrastructure Team

## License

MIT

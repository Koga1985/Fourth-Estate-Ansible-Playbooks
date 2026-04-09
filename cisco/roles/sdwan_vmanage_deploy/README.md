# sdwan_vmanage_deploy

## Overview

Deploys and initializes the Cisco SD-WAN **vManage** network management controller for the Fourth Estate SD-WAN fabric. Sets system parameters, PKI certificate configuration, VPN/interface settings, and optional HA cluster setup. This is **Phase 15** of the Fourth Estate Cisco SD-WAN deployment.

## Features

- vManage system configuration (org name, vBond address, timezone)
- PKI certificate authority initialization (enterprise CA or Symantec)
- Management VPN (VPN 512) interface configuration
- Optional vManage HA cluster setup
- Defaults to **dry-run mode** (`apply_changes: false`)

## Requirements

- Ansible 2.15+
- vManage reachable on port 443 from Ansible control node
- Vault variables populated (see defaults)

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sdwan_vmanage_host` | `{{ vault_sdwan_vmanage_host }}` | **Yes** | vManage hostname or IP |
| `sdwan_org_name` | `{{ vault_sdwan_org_name }}` | **Yes** | SD-WAN organization name |
| `sdwan_vbond_host` | `{{ vault_sdwan_vbond_host }}` | **Yes** | vBond hostname or IP |
| `sdwan_vmanage_system_ip` | `{{ vault_sdwan_vmanage_system_ip }}` | **Yes** | vManage system IP |
| `apply_changes` | `false` | No | Set `true` to apply |
| `sdwan_vmanage_cluster_enabled` | `false` | No | Enable HA cluster |
| `sdwan_cert_auth_type` | `enterprise` | No | CA type: `enterprise`, `symantec`, `manual` |

## Example Playbook

```yaml
- name: SD-WAN vManage Deployment
  hosts: localhost
  connection: local
  gather_facts: false
  tasks:
    - ansible.builtin.include_role:
        name: sdwan_vmanage_deploy
```

## Tags

`sdwan`, `vmanage`, `system`, `certificates`, `vpn`, `cluster`, `phase15`

## Author

Fourth Estate Infrastructure Team

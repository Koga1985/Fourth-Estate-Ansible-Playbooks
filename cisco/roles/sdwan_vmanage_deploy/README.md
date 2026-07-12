# sdwan_vmanage_deploy

## Requirements

- Ansible 2.15+
- vManage reachable on port 443 from Ansible control node
- Vault variables populated (see defaults)

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
| `enable_vmanage_system` | `true` | No | Feature Toggles |
| `enable_vmanage_cluster` | `true` | No | — |
| `enable_vmanage_certificates` | `true` | No | — |
| `enable_vmanage_vpn_config` | `true` | No | — |
| `sdwan_vmanage_system_ip` | `"{{ vault_sdwan_vmanage_system_ip }}"` | No | vManage System Settings |
| `sdwan_vmanage_site_id` | `"{{ vault_sdwan_vmanage_site_id }}"` | No | — |
| `sdwan_vmanage_domain_id` | `1` | No | — |
| `sdwan_vmanage_timezone` | `"UTC"` | No | — |
| `sdwan_vmanage_hostname` | `"{{ vault_sdwan_vmanage_hostname }}"` | No | — |
| `sdwan_org_name` | `"{{ vault_sdwan_org_name }}"` | No | Organization and vBond settings |
| `sdwan_vbond_host` | `"{{ vault_sdwan_vbond_host }}"` | No | — |
| `sdwan_vbond_port` | `12346` | No | — |
| `sdwan_vmanage_cluster_enabled` | `false` | No | vManage Cluster Configuration vManage HA cluster for redundancy Set true for HA deployment |
| `sdwan_vmanage_cluster_nodes` | `(see defaults/main.yml)` | No | — |
| `sdwan_vmanage_mgmt_interface` | `"eth0"` | No | VPN / Interface Configuration VPN 0: Transport (WAN) VPN 512: Management (out-of-band) |
| `sdwan_vmanage_mgmt_gateway` | `"{{ vault_sdwan_vmanage_mgmt_gateway }}"` | No | — |
| `sdwan_cert_auth_type` | `"enterprise"` | No | Certificate Management (STIG SC-17, IA-3) Options: enterprise, symantec, manual |
| `sdwan_ca_cert_file` | `"{{ vault_sdwan_ca_cert_path }}"` | No | — |
| `sdwan_root_ca_cert` | `"{{ vault_sdwan_root_ca_cert }}"` | No | — |
| `sdwan_csr_country` | `"US"` | No | — |
| `sdwan_csr_state` | `"{{ vault_sdwan_csr_state }}"` | No | — |
| `sdwan_csr_city` | `"{{ vault_sdwan_csr_city }}"` | No | — |
| `sdwan_csr_org` | `"FourthEstate"` | No | — |
| `sdwan_csr_org_unit` | `"Network Operations"` | No | — |
| `sdwan_csr_email` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |

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

## Overview

Deploys and initializes the Cisco SD-WAN **vManage** network management controller for the Fourth Estate SD-WAN fabric. Sets system parameters, PKI certificate configuration, VPN/interface settings, and optional HA cluster setup. This is **Phase 15** of the Fourth Estate Cisco SD-WAN deployment.

## Features

- vManage system configuration (org name, vBond address, timezone)
- PKI certificate authority initialization (enterprise CA or Symantec)
- Management VPN (VPN 512) interface configuration
- Optional vManage HA cluster setup
- Defaults to **dry-run mode** (`apply_changes: false`)

## Author

Fourth Estate Infrastructure Team

## License

MIT

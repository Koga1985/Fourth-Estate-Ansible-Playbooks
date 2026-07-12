# sdwan_controllers_config

## Requirements

- Ansible 2.15+
- Phases 15–16 (`sdwan_vmanage_deploy`, `sdwan_vmanage_config`) complete
- Vault variables populated

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sdwan_vmanage_host` | `"{{ vault_sdwan_vmanage_host }}"` | No | vManage Connection Parameters (used for controller config via API) |
| `sdwan_vmanage_port` | `443` | No | — |
| `sdwan_vmanage_username` | `"{{ vault_sdwan_vmanage_username }}"` | No | — |
| `sdwan_vmanage_password` | `"{{ vault_sdwan_vmanage_password }}"` | No | — |
| `sdwan_vmanage_verify_ssl` | `true` | No | — |
| `sdwan_vmanage_timeout` | `30` | No | — |
| `sdwan_vbond_host` | `"{{ vault_sdwan_vbond_host }}"` | No | vBond Direct Connection |
| `sdwan_vbond_port` | `12346` | No | — |
| `sdwan_vbond_system_ip` | `"{{ vault_sdwan_vbond_system_ip }}"` | No | — |
| `sdwan_vbond_site_id` | `"{{ vault_sdwan_vbond_site_id }}"` | No | — |
| `sdwan_vsmart_host` | `"{{ vault_sdwan_vsmart_host }}"` | No | vSmart Direct Connection |
| `sdwan_vsmart_port` | `443` | No | — |
| `sdwan_vsmart_username` | `"{{ vault_sdwan_vsmart_username }}"` | No | — |
| `sdwan_vsmart_password` | `"{{ vault_sdwan_vsmart_password }}"` | No | — |
| `sdwan_vsmart_system_ip` | `"{{ vault_sdwan_vsmart_system_ip }}"` | No | — |
| `sdwan_vsmart_site_id` | `"{{ vault_sdwan_vsmart_site_id }}"` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `sdwan_artifacts_dir` | `"/tmp/sdwan-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Organization |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `fourth_estate_environment` | `"production"` | No | — |
| `fourth_estate_region` | `"primary"` | No | — |
| `enable_vbond_config` | `true` | No | Feature Toggles |
| `enable_vsmart_config` | `true` | No | — |
| `enable_controller_certificates` | `true` | No | — |
| `enable_omp_config` | `true` | No | — |
| `enable_control_policies` | `true` | No | — |
| `sdwan_vbond_system_config` | `(see defaults/main.yml)` | No | vBond Configuration |
| `sdwan_vsmart_system_config` | `(see defaults/main.yml)` | No | vSmart Configuration |
| `sdwan_omp_config` | `(see defaults/main.yml)` | No | OMP (Overlay Management Protocol) Configuration Controls route distribution across the SD-WAN fabric |
| `sdwan_control_policies` | `(see defaults/main.yml)` | No | Control Policies (vSmart) |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |

## Example Playbook

```yaml
- name: Use sdwan_controllers_config
  hosts: all
  gather_facts: false
  roles:
    - role: sdwan_controllers_config
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`sdwan`, `controllers`, `vbond`, `vsmart`, `certificates`, `omp`, `policies`, `phase17`

## Overview

Configures the Cisco SD-WAN **vBond** orchestrator and **vSmart** policy controller — adds them to vManage, issues device certificates, configures OMP route distribution, and deploys topology control policies. This is **Phase 17** of the Fourth Estate Cisco SD-WAN deployment.

## Features

- vBond orchestrator registration in vManage
- vSmart controller registration in vManage
- PKI device certificate issuance (SC-17, IA-3)
- OMP route distribution configuration (path limit, ECMP, graceful restart)
- vSmart control policy deployment (hub-and-spoke topology)
- Defaults to **dry-run mode** (`apply_changes: false`)

## Compliance

Certificate issuance implements NIST SC-17 and IA-3 (Device Identification and Authentication).

## Author

Fourth Estate Infrastructure Team

## License

MIT

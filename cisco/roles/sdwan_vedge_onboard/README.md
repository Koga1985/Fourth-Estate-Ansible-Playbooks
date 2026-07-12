# sdwan_vedge_onboard

## Requirements

- Ansible 2.15+
- Phases 15–17 complete (vManage, config, and controllers)
- Device UUIDs and OTP tokens available (from Cisco PnP portal)
- Vault variables for device credentials populated

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
| `enable_device_inventory` | `true` | No | Feature Toggles |
| `enable_bootstrap_config` | `true` | No | — |
| `enable_template_attach` | `true` | No | — |
| `enable_device_validation` | `true` | No | — |
| `sdwan_edge_devices` | `(see defaults/main.yml)` | No | Edge Device Inventory List of vEdge/cEdge devices to onboard |
| `sdwan_bootstrap_transport` | `"cloud-init"` | No | Bootstrap Configuration Settings Options: cloud-init, bootp, ztp |
| `sdwan_bootstrap_include_certs` | `true` | No | — |
| `sdwan_bootstrap_include_vbond` | `true` | No | — |
| `sdwan_bootstrap_include_templates` | `false` | No | Push templates via vManage instead |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |

## Example Playbook

```yaml
- name: Use sdwan_vedge_onboard
  hosts: all
  gather_facts: false
  roles:
    - role: sdwan_vedge_onboard
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`sdwan`, `vedge`, `inventory`, `bootstrap`, `templates`, `attach`, `phase18`

## Overview

Onboards Cisco SD-WAN **vEdge** and **cEdge** edge routers to the SD-WAN fabric via vManage. Registers devices in inventory, generates Day-0 bootstrap configurations, and attaches DoD-compliant device templates. This is **Phase 18** of the Fourth Estate Cisco SD-WAN deployment.

## Features

- Device registration in vManage inventory (UUID + OTP token)
- Bootstrap configuration generation (cloud-init, bootp, or ZTP)
- Bootstrap configs saved to artifacts directory (mode 0600)
- Device template attachment with per-device variable injection
- Post-onboarding sync validation
- Defaults to **dry-run mode** (`apply_changes: false`)

## Example Device Entry

```yaml
sdwan_edge_devices:
  - hostname: "branch-01-vedge"
    system_ip: "10.10.1.1"
    site_id: 100
    uuid: "{{ vault_sdwan_branch01_uuid }}"
    token: "{{ vault_sdwan_branch01_otp }}"
    device_type: "vedge-cloud"
    template: "FourthEstate-vEdge-Branch"
    variables:
      system_hostname: "branch-01-vedge"
      system_site_id: 100
```

## Author

Fourth Estate Infrastructure Team

## License

MIT

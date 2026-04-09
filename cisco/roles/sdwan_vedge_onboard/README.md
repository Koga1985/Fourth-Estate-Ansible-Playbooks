# sdwan_vedge_onboard

## Overview

Onboards Cisco SD-WAN **vEdge** and **cEdge** edge routers to the SD-WAN fabric via vManage. Registers devices in inventory, generates Day-0 bootstrap configurations, and attaches DoD-compliant device templates. This is **Phase 18** of the Fourth Estate Cisco SD-WAN deployment.

## Features

- Device registration in vManage inventory (UUID + OTP token)
- Bootstrap configuration generation (cloud-init, bootp, or ZTP)
- Bootstrap configs saved to artifacts directory (mode 0600)
- Device template attachment with per-device variable injection
- Post-onboarding sync validation
- Defaults to **dry-run mode** (`apply_changes: false`)

## Requirements

- Ansible 2.15+
- Phases 15–17 complete (vManage, config, and controllers)
- Device UUIDs and OTP tokens available (from Cisco PnP portal)
- Vault variables for device credentials populated

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sdwan_vmanage_host` | `{{ vault_sdwan_vmanage_host }}` | **Yes** | vManage hostname or IP |
| `sdwan_edge_devices` | `[]` | **Yes** | List of devices to onboard (see defaults) |
| `apply_changes` | `false` | No | Set `true` to apply |
| `sdwan_bootstrap_transport` | `cloud-init` | No | Bootstrap type: `cloud-init`, `bootp`, `ztp` |

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

## Tags

`sdwan`, `vedge`, `inventory`, `bootstrap`, `templates`, `attach`, `phase18`

## Author

Fourth Estate Infrastructure Team

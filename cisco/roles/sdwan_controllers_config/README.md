# sdwan_controllers_config

## Overview

Configures the Cisco SD-WAN **vBond** orchestrator and **vSmart** policy controller — adds them to vManage, issues device certificates, configures OMP route distribution, and deploys topology control policies. This is **Phase 17** of the Fourth Estate Cisco SD-WAN deployment.

## Features

- vBond orchestrator registration in vManage
- vSmart controller registration in vManage
- PKI device certificate issuance (SC-17, IA-3)
- OMP route distribution configuration (path limit, ECMP, graceful restart)
- vSmart control policy deployment (hub-and-spoke topology)
- Defaults to **dry-run mode** (`apply_changes: false`)

## Requirements

- Ansible 2.15+
- Phases 15–16 (`sdwan_vmanage_deploy`, `sdwan_vmanage_config`) complete
- Vault variables populated

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sdwan_vmanage_host` | `{{ vault_sdwan_vmanage_host }}` | **Yes** | vManage hostname or IP |
| `sdwan_vbond_host` | `{{ vault_sdwan_vbond_host }}` | **Yes** | vBond hostname or IP |
| `sdwan_vsmart_host` | `{{ vault_sdwan_vsmart_host }}` | **Yes** | vSmart hostname or IP |
| `sdwan_vbond_system_ip` | `{{ vault_sdwan_vbond_system_ip }}` | **Yes** | vBond system IP |
| `sdwan_vsmart_system_ip` | `{{ vault_sdwan_vsmart_system_ip }}` | **Yes** | vSmart system IP |
| `apply_changes` | `false` | No | Set `true` to apply |

## Tags

`sdwan`, `controllers`, `vbond`, `vsmart`, `certificates`, `omp`, `policies`, `phase17`

## Compliance

Certificate issuance implements NIST SC-17 and IA-3 (Device Identification and Authentication).

## Author

Fourth Estate Infrastructure Team

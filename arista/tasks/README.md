# Arista Tasks

This directory contains **14 standalone task files** for Arista EOS operations. These task files can be included directly in any playbook using `ansible.builtin.include_tasks` without requiring the full role structure.

## Task Files

| File | Description |
|------|-------------|
| `arista_acl__define_and_bind.yml` | Defines ACL entries and binds them to interfaces or control-plane. |
| `arista_backup__running_config.yml` | Captures the running configuration and saves it to a timestamped file in the artifacts directory. |
| `arista_bgp__baseline.yml` | Applies a BGP baseline including AS number, peer groups, address families, and route policies. |
| `arista_cvp__inventory_model.yml` | Reconciles the CVP container hierarchy and device-to-container assignments. |
| `arista_interfaces__l3_svis.yml` | Creates or updates Layer 3 SVIs with IP addressing and description. |
| `arista_interfaces__vlans_l2.yml` | Manages the VLAN database and Layer 2 switchport interface assignments. |
| `arista_lag__port_channels.yml` | Configures LACP port-channel interfaces and member links. |
| `arista_mlag__pair.yml` | Configures MLAG domain, peer link, and keepalive settings for a switch pair. |
| `arista_ospf__baseline.yml` | Applies OSPF process configuration including area assignments, passive interfaces, and authentication. |
| `arista_platform__baseline.yml` | Standalone platform hardening task covering hostname, NTP, syslog, AAA, and management ACL. |
| `arista_routing__static.yml` | Installs static routes with optional administrative distance and descriptions. |
| `arista_stig__hardening.yml` | Applies EOS STIG hardening controls including banner, login settings, and protocol restrictions. |
| `arista_telemetry__logging_sflow_gnmi.yml` | Configures streaming telemetry via sFlow, gNMI, and remote syslog forwarding. |
| `arista_upgrade__eos_stage_boot.yml` | Stages an EOS software image and sets the boot variable; does not reboot automatically. |
| `arista_vxlan__vtep_evpn.yml` | Configures VXLAN VTEP and BGP EVPN control-plane for a leaf or spine node. |

## Usage

```yaml
---
- name: Backup Arista configurations
  hosts: arista_switches
  gather_facts: false

  tasks:
    - name: Capture running config
      ansible.builtin.include_tasks: arista/tasks/arista_backup__running_config.yml

    - name: Apply STIG hardening
      ansible.builtin.include_tasks: arista/tasks/arista_stig__hardening.yml
```

## Requirements

- Ansible 2.12+
- `arista.eos` collection
- Variables appropriate to each task (see individual task files for required vars)

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

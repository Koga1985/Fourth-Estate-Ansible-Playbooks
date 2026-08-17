# Arista Playbooks

This directory contains standalone **playbooks** for Arista EOS operations. Each one declares its own `hosts:` and is run directly with `ansible-playbook`; they are not task files and cannot be included with `ansible.builtin.include_tasks`.

## Playbooks

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

Each file here is a complete play with its own `hosts:`, so run it directly:

```bash
ansible-playbook -i inventory arista/playbooks/arista_backup__running_config.yml
ansible-playbook -i inventory arista/playbooks/arista_stig__hardening.yml
```

To chain several in one run, compose them with `import_playbook` (not
`include_tasks`, which only accepts task files):

```yaml
---
- name: Capture running config
  ansible.builtin.import_playbook: arista/playbooks/arista_backup__running_config.yml

- name: Apply STIG hardening
  ansible.builtin.import_playbook: arista/playbooks/arista_stig__hardening.yml
```

## Requirements

- Ansible 2.12+
- `arista.eos` collection
- Variables appropriate to each task (see individual task files for required vars)

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

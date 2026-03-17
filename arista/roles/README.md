# Arista Roles

This directory contains **6 Ansible roles** for managing Arista EOS network switches, covering platform baseline configuration, routing, interfaces and fabric, ACL/QoS security, CloudVision Portal (CVP) integration, and backup/restore operations.

## Roles

| Role | Description |
|------|-------------|
| **arista_platform_baseline** | Applies baseline EOS platform configuration including hostname, NTP, syslog, AAA, SNMP, and management-plane hardening with DoD-friendly defaults. |
| **arista_routing_baseline** | Configures BGP, OSPF, and static routing baselines including route maps, prefix lists, and redistribution policies. |
| **arista_interfaces_fabric** | Manages Layer 2 and Layer 3 interfaces, VLANs, SVIs, LAG/port-channels, MLAG pairs, and VXLAN VTEP/EVPN overlays. |
| **arista_acl_qos_security** | Deploys access control lists, QoS policies, and STIG hardening rules across EOS devices. |
| **arista_cvp_inventory_model** | Builds and reconciles the CloudVision Portal device inventory model, provisioning containers and assigning configlets. |
| **arista_backup_restore** | Captures running configurations to a version-controlled artifacts directory and supports emergency restore procedures. |

## Requirements

- Ansible 2.12+
- `arista.eos` collection (`ansible-galaxy collection install arista.eos`)
- Network reachability to EOS management interfaces
- AAA credentials or SSH key pair

## Quick Start

```bash
ansible-galaxy collection install arista.eos

ansible-playbook -i inventory/arista.yml site.yml \
  --ask-vault-pass
```

## Example Playbook

```yaml
---
- name: Apply Arista platform baseline
  hosts: arista_switches
  gather_facts: false

  roles:
    - role: arista/roles/arista_platform_baseline
    - role: arista/roles/arista_routing_baseline
    - role: arista/roles/arista_backup_restore
```

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

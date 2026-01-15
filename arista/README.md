# Arista EOS Networks

This directory contains **6 Ansible roles** for managing **Arista EOS** network switches including baseline configuration, routing, CloudVision Portal (CVP) integration, and compliance.

## 📋 Roles

### Configuration Management (2 roles)
- **arista_baseline_config** - Standard device configuration
  - System settings
  - Management interface
  - AAA configuration
  - NTP and syslog

- **arista_backup_restore** - Configuration backup and restore
  - Scheduled backups
  - Version control
  - Emergency restore

### Routing & Switching (2 roles)
- **arista_routing_protocols** - BGP, OSPF, VXLAN EVPN
  - Dynamic routing
  - Route maps
  - Prefix lists

- **arista_interfaces_vlans** - Interface and VLAN management
  - Port configuration
  - Trunk/access modes
  - VLAN database

### Automation & Security (2 roles)
- **arista_cvp_integration** - CloudVision Portal integration
  - Device registration
  - Configlet management
  - Change control

- **arista_acl_qos** - Access control and QoS
  - ACL policies
  - QoS marking
  - Rate limiting

## 🚀 Quick Start

### Prerequisites

- Ansible 2.12.0+
- `arista.eos` collection
- Network access to Arista devices
- AAA credentials

### Installation

```bash
ansible-galaxy collection install arista.eos
```

### Configuration

```yaml
# group_vars/arista.yml
ansible_network_os: eos
ansible_connection: network_cli
ansible_become: yes
ansible_become_method: enable

arista_ntp_servers:
  - "ntp1.example.com"
  - "ntp2.example.com"

arista_syslog_servers:
  - host: "syslog.example.com"
    severity: informational
```

## 📖 Common Use Cases

### Apply Baseline Configuration

```bash
ansible-playbook playbooks/arista_baseline.yml \
  -i inventory/arista.yml \
  --limit leaf-01
```

### Configure BGP EVPN

```bash
ansible-playbook roles/arista_routing_protocols/playbook.yml \
  -i inventory/arista.yml \
  -e "routing_protocol=bgp_evpn"
```

### Backup Configurations

```bash
ansible-playbook roles/arista_backup_restore/playbook.yml \
  -i inventory/arista.yml \
  -e "operation=backup"
```

## 📚 Additional Resources

- [Arista EOS Documentation](https://www.arista.com/en/support/software-download)
- [CloudVision Portal](https://www.arista.com/en/products/eos/eos-cloudvision)

---

**Last Updated:** 2026-01-15
**Maintained By:** Fourth Estate Infrastructure Team

# Infoblox DDI - Basic

This directory contains **12 Ansible roles** for **Infoblox** DDI (DNS, DHCP, IPAM) automation.

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your Infoblox Grid details

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Configure Grid
ansible-playbook -i inventory site.yml --tags grid

# Configure DNS
ansible-playbook -i inventory site.yml --tags dns

# Configure DHCP
ansible-playbook -i inventory site.yml --tags dhcp
```

## 📋 Roles

### Grid Management (4 roles)
- **infoblox_grid_bootstrap** - Initial Grid Manager bootstrap and setup
- **infoblox_grid_config** - Grid Manager configuration and tuning
- **infoblox_grid_upgrade** - Grid software upgrades
- **infoblox_inventory_model** - Grid asset inventory and CMDB sync

### DNS (4 roles)
- **infoblox_dns_config** - DNS views, zones, and server settings
- **infoblox_dns_records** - DNS record lifecycle management
- **infoblox_dns_views_zones** - Advanced DNS views and zone management
- **infoblox_dnssec** - DNSSEC signing and key management

### DHCP (2 roles)
- **infoblox_dhcp_config** - DHCP scopes, ranges, and options
- **infoblox_dhcp_failover** - DHCP failover peer configuration

### Security & Reporting (2 roles)
- **infoblox_rpz_policies** - Response Policy Zones (RPZ) for DNS security
- **infoblox_capacity_reports** - Grid capacity and utilization reporting

## ⚙️ Configuration

```yaml
# group_vars/infoblox.yml
nios_host: "grid-master.example.com"
nios_username: "admin"
nios_password: "{{ vault_nios_password }}"
nios_wapi_version: "2.12"
```

## Prerequisites

- Ansible 2.12.0+
- `infoblox.nios_modules` collection
- Network access to Infoblox Grid Manager

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

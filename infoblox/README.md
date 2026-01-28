# Infoblox DDI - Basic

This directory contains **3 Ansible roles** for basic **Infoblox** DDI (DNS, DHCP, IPAM) automation.

> **Note:** For comprehensive Infoblox automation with 10+ roles including grid management, DNSSEC, RPZ, and compliance, see the `infoblocks/` directory.

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

- **infoblox_grid_config** - Grid Manager configuration
- **infoblox_dns_config** - DNS zones and records
- **infoblox_dhcp_config** - DHCP scopes and options

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

**Maintained By:** Fourth Estate Infrastructure Team

# Pure Storage FlashArray

This directory contains **7 Ansible roles** for automating **Pure Storage FlashArray** including installation, configuration, volume provisioning, data protection, replication, and performance tuning.

> **Note:** For FlashBlade automation, see the `pure/` directory which includes both FlashArray and FlashBlade roles.

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your FlashArray details

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Configure FlashArray
ansible-playbook -i inventory site.yml --tags config

# Configure hosts
ansible-playbook -i inventory site.yml --tags hosts

# Provision volumes
ansible-playbook -i inventory site.yml --tags volumes

# Configure protection
ansible-playbook -i inventory site.yml --tags protection

# Configure replication
ansible-playbook -i inventory site.yml --tags replication
```

## 📋 Roles

### Installation & Configuration (2 roles)
- **pure_flasharray_install** - Initial array setup
- **pure_flasharray_config** - Array configuration

### Provisioning (2 roles)
- **pure_flasharray_hosts** - Host and host group configuration
- **pure_flasharray_volumes** - Volume provisioning

### Data Protection (2 roles)
- **pure_flasharray_protection** - Snapshot and protection groups
- **pure_flasharray_replication** - Async and sync replication

### Performance (1 role)
- **pure_flasharray_performance** - Performance tuning and QoS

## ⚙️ Configuration

```yaml
# group_vars/pure_storage.yml
pure_array_url: "flasharray.example.com"
pure_api_token: "{{ vault_pure_api_token }}"

# Volume defaults
pure_volume_size: "100G"
pure_volume_suffix: "-vol"

# Protection settings
pure_snapshot_retention: 7
pure_replication_enabled: true
```

## Prerequisites

- Ansible 2.12.0+
- `purestorage.flasharray` collection
- Pure Storage FlashArray with Purity 6.0+
- API token with appropriate permissions

---

**Maintained By:** Fourth Estate Infrastructure Team

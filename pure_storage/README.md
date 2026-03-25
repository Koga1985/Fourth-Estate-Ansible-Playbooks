# Pure Storage FlashArray

This directory contains **14 Ansible roles** for automating **Pure Storage FlashArray and FlashBlade** including installation, configuration, volume provisioning, data protection, replication, and performance tuning.

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

### FlashArray (7 roles)
- **pure_flasharray_install** - Initial array setup
- **pure_flasharray_config** - Array configuration
- **pure_flasharray_hosts** - Host and host group configuration
- **pure_flasharray_volumes** - Volume provisioning
- **pure_flasharray_protection** - Snapshot and protection groups
- **pure_flasharray_replication** - Async and sync replication
- **pure_flasharray_performance** - Performance tuning and QoS

### FlashArray Extended (4 roles)
- **pure_fa_provisioning** - Advanced FlashArray provisioning
- **pure_fa_data_protection** - Extended FlashArray data protection
- **pure_fa_ops_governance** - FlashArray operational governance
- **pure_fa_integrations** - FlashArray integrations (vSphere, Kubernetes, etc.)

### FlashBlade (3 roles)
- **pure_fb_provisioning** - FlashBlade filesystem and object store provisioning
- **pure_fb_data_protection** - FlashBlade snapshots and replication
- **pure_fb_ops** - FlashBlade operational management

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

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

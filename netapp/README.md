# NetApp ONTAP Storage Automation

This directory contains **3 Ansible roles** for automating **NetApp ONTAP** storage management including cluster configuration, SVM management, and volume provisioning.

## 📋 Roles

- **netapp_cluster_setup** - Cluster initialization and configuration
- **netapp_svm_management** - Storage Virtual Machine (SVM) management
- **netapp_volume_provisioning** - Volume, LUN, NFS, and CIFS provisioning

## 🚀 Quick Start

```bash
# Deploy full NetApp configuration
ansible-playbook -i inventory site.yml --ask-vault-pass

# Configure cluster only
ansible-playbook -i inventory site.yml --tags cluster

# Provision volumes only
ansible-playbook -i inventory site.yml --tags volumes
```

## ⚙️ Configuration

```yaml
# NetApp cluster configuration
netapp_hostname: "{{ vault_netapp_hostname }}"
netapp_username: "{{ vault_netapp_username }}"
netapp_password: "{{ vault_netapp_password }}"
netapp_validate_certs: true

# SVM configuration
netapp_svm_name: "svm01"
netapp_svm_ipspace: "Default"
netapp_svm_protocols: ["nfs", "cifs", "iscsi"]

# Volume configuration
netapp_volume_aggregate: "aggr1"
netapp_volume_size: "1TB"
netapp_volume_type: "RW"
netapp_snapshot_policy: "default"
```

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

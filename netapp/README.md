# NetApp ONTAP Storage Automation

This directory contains **12 Ansible roles** for automating **NetApp ONTAP** storage management including cluster configuration, SVM management, volume/LUN provisioning, data protection, and compliance.

## 📋 Roles

### Cluster & SVM Management (2 roles)
- **netapp_ontap_cluster** - Cluster initialization and configuration
- **netapp_svm** - Storage Virtual Machine (SVM) management

### Storage Provisioning (4 roles)
- **netapp_volumes** - FlexVol and FlexGroup volume management
- **netapp_luns** - LUN provisioning for SAN
- **netapp_nfs_exports** - NFS export configuration
- **netapp_cifs_shares** - CIFS/SMB share management

### Data Protection (2 roles)
- **netapp_snapshots** - Snapshot policy and management
- **netapp_snapmirror** - SnapMirror replication for DR

### Performance & Security (4 roles)
- **netapp_performance_tuning** - QoS and performance optimization
- **netapp_security** - Security hardening and encryption
- **netapp_backup** - SnapVault and backup configuration
- **netapp_compliance** - Compliance and audit configuration

## 🚀 Quick Start

```bash
# Configure ONTAP cluster
ansible-playbook playbooks/netapp_cluster_config.yml \
  -e "cluster_name=netapp-prod" \
  -e "cluster_mgmt_ip=10.0.1.10"

# Create NFS volume
ansible-playbook playbooks/netapp_nfs_volume.yml \
  -e "svm_name=svm01" \
  -e "volume_name=nfsdata01" \
  -e "volume_size=1TB"
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

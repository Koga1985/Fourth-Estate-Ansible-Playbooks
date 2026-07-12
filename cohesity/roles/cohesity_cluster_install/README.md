# cohesity_cluster_install

Cohesity Cluster Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `cohesity/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cohesity_cluster_name` | `"cohesity-cluster-01"` | No | Cohesity Cluster Configuration |
| `cohesity_cluster_domain` | `"cohesity.local"` | No | — |
| `cohesity_cluster_gateway` | `"10.100.1.1"` | No | — |
| `cohesity_cluster_subnet_mask` | `"255.255.255.0"` | No | — |
| `cohesity_cluster_dns_servers` | `(see defaults/main.yml)` | No | — |
| `cohesity_cluster_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `cohesity_cluster_vips` | `(see defaults/main.yml)` | No | Virtual IP (VIP) Configuration |
| `cohesity_nodes` | `(see defaults/main.yml)` | No | Node Configuration |
| `cohesity_deployment_type` | `"ve"` | No | Deployment Type (ve = Virtual Edition, physical = Physical Appliance) |
| `cohesity_ve_platform` | `"vmware"` | No | Virtual Edition Configuration vmware, hyperv, aws, azure |
| `cohesity_ve_ova_path` | `"/opt/cohesity/CohesityVirtualEdition.ova"` | No | — |
| `cohesity_ve_vcenter_host` | `"vcenter.example.com"` | No | — |
| `cohesity_ve_vcenter_username` | `"administrator@vsphere.local"` | No | — |
| `cohesity_ve_vcenter_password` | `"{{ vault_vcenter_password }}"` | No | — |
| `cohesity_ve_datacenter` | `"Datacenter"` | No | — |
| `cohesity_ve_cluster` | `"Cluster01"` | No | — |
| `cohesity_ve_datastore` | `"datastore1"` | No | — |
| `cohesity_ve_network` | `"VM Network"` | No | — |
| `cohesity_ve_vm_name_prefix` | `"cohesity-node"` | No | — |
| `cohesity_physical_ipmi_user` | `"admin"` | No | Physical Appliance Configuration |
| `cohesity_physical_ipmi_password` | `"{{ vault_ipmi_password }}"` | No | — |
| `cohesity_network_config` | `(see defaults/main.yml)` | No | Network Configuration |
| `cohesity_disk_config` | `(see defaults/main.yml)` | No | Disk Configuration |
| `cohesity_license_key` | `"{{ vault_cohesity_license }}"` | No | License Configuration |
| `cohesity_support_enabled` | `true` | No | — |
| `cohesity_phone_home_enabled` | `true` | No | — |
| `cohesity_admin_username` | `"admin"` | No | Initial Admin Configuration |
| `cohesity_admin_password` | `"{{ vault_cohesity_admin_password }}"` | No | — |
| `cohesity_admin_email` | `"backup-admin@fourthestate.com"` | No | — |
| `cohesity_smtp_server` | `"smtp.fourthestate.com"` | No | SMTP Configuration |
| `cohesity_smtp_port` | `587` | No | — |
| `cohesity_smtp_username` | `"cohesity-alerts@fourthestate.com"` | No | — |
| `cohesity_smtp_password` | `"{{ vault_smtp_password }}"` | No | — |
| `cohesity_smtp_use_tls` | `true` | No | — |
| `cohesity_smtp_from_address` | `"cohesity-alerts@fourthestate.com"` | No | — |
| `cohesity_encryption_enabled` | `true` | No | Encryption Configuration |
| `cohesity_encryption_key_rotation_days` | `90` | No | — |
| `cohesity_fips_mode_enabled` | `true` | No | — |
| `cohesity_api_protocol` | `"https"` | No | API Configuration |
| `cohesity_api_port` | `443` | No | — |
| `cohesity_api_timeout` | `300` | No | — |
| `cohesity_api_verify_ssl` | `true` | No | — |
| `cohesity_cluster_bootstrap_wait_time` | `1800` | No | Cluster Bootstrap Configuration 30 minutes |
| `cohesity_cluster_bootstrap_check_interval` | `60` | No | 1 minute |
| `cohesity_storage_domain_name` | `"DefaultStorageDomain"` | No | Storage Domain Configuration |
| `cohesity_storage_domain_compression` | `true` | No | — |
| `cohesity_storage_domain_deduplication` | `true` | No | — |
| `cohesity_storage_domain_encryption` | `true` | No | — |
| `cohesity_timezone` | `"America/New_York"` | No | Timezone Configuration |
| `cohesity_organization_name` | `"Fourth Estate Media"` | No | Fourth Estate Specific Settings |
| `cohesity_deployment_purpose` | `"Critical data protection and ransomware recovery"` | No | — |
| `cohesity_compliance_mode` | `true` | No | — |
| `cohesity_air_gap_enabled` | `true` | No | — |
| `cohesity_immutable_snapshots` | `true` | No | — |
| `cohesity_installation_mode` | `"fresh"` | No | Installation Settings fresh, add_nodes, upgrade |
| `cohesity_pre_checks_enabled` | `true` | No | — |
| `cohesity_post_checks_enabled` | `true` | No | — |
| `cohesity_backup_config_before_changes` | `true` | No | — |

## Example Playbook

```yaml
---
- name: Cohesity Cluster Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: cohesity/roles/cohesity_cluster_install
```

## License

MIT

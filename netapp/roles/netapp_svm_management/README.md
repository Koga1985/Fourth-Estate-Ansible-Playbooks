# netapp_svm_management

Netapp Svm Management role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `netapp/README.md`

## Requirements

- Ansible 2.15+
- Collection: `netapp.ontap`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `netapp_svm_hostname` | `"{{ vault_netapp_cluster_hostname \| default('netapp-cluster.example...` | No | Connection settings |
| `netapp_svm_username` | `"{{ vault_netapp_cluster_username \| default('admin') }}"` | No | — |
| `netapp_svm_password` | `"{{ vault_netapp_cluster_password }}"` | No | — |
| `netapp_svm_validate_certs` | `true` | No | — |
| `netapp_svm_name` | `"svm_prod"` | No | SVM basic configuration |
| `netapp_svm_root_volume` | `"{{ netapp_svm_name }}_root"` | No | — |
| `netapp_svm_root_aggregate` | `"aggr1_netapp01_SAS"` | No | — |
| `netapp_svm_root_security_style` | `"unix"` | No | — |
| `netapp_svm_ipspace` | `"Default"` | No | — |
| `netapp_svm_subtype` | `"default"` | No | — |
| `netapp_svm_comment` | `"Production SVM for Fourth Estate Agency"` | No | — |
| `netapp_svm_language` | `"c.UTF-8"` | No | — |
| `netapp_svm_snapshot_policy` | `"default"` | No | — |
| `netapp_svm_allowed_protocols` | `(see defaults/main.yml)` | No | Allowed protocols |
| `netapp_svm_aggr_list` | `(see defaults/main.yml)` | No | SVM aggregate list (aggregates allowed for this SVM) |
| `netapp_svm_create_mgmt_lif` | `true` | No | Management LIF configuration |
| `netapp_svm_mgmt_lif_name` | `"{{ netapp_svm_name }}_mgmt"` | No | — |
| `netapp_svm_mgmt_lif_home_port` | `"e0c"` | No | — |
| `netapp_svm_mgmt_lif_home_node` | `"netapp-01"` | No | — |
| `netapp_svm_mgmt_lif_address` | `"10.0.100.10"` | No | — |
| `netapp_svm_mgmt_lif_netmask` | `"255.255.255.0"` | No | — |
| `netapp_svm_mgmt_lif_protocols` | `(see defaults/main.yml)` | No | — |
| `netapp_svm_mgmt_lif_firewall_policy` | `"mgmt"` | No | — |
| `netapp_svm_mgmt_lif_auto_revert` | `true` | No | — |
| `netapp_svm_create_data_lifs` | `true` | No | Data LIFs configuration |
| `netapp_svm_data_lifs` | `(see defaults/main.yml)` | No | — |
| `netapp_svm_configure_dns` | `true` | No | DNS configuration |
| `netapp_svm_dns_domains` | `(see defaults/main.yml)` | No | — |
| `netapp_svm_dns_nameservers` | `(see defaults/main.yml)` | No | — |
| `netapp_svm_enable_nfs` | `true` | No | NFS configuration |
| `netapp_svm_nfs_v3_enabled` | `enabled` | No | — |
| `netapp_svm_nfs_v4_enabled` | `enabled` | No | — |
| `netapp_svm_nfs_v41_enabled` | `enabled` | No | — |
| `netapp_svm_nfs_vstorage_state` | `disabled` | No | — |
| `netapp_svm_nfs_udp` | `disabled` | No | DISA STIG: Disable UDP for NFSv4 |
| `netapp_svm_create_export_policies` | `true` | No | Export policies |
| `netapp_svm_export_policies` | `(see defaults/main.yml)` | No | — |
| `netapp_svm_enable_cifs` | `true` | No | CIFS/SMB configuration |
| `netapp_svm_cifs_server_name` | `"{{ netapp_svm_name \| upper }}"` | No | — |
| `netapp_svm_cifs_domain` | `"AGENCY.GOV"` | No | — |
| `netapp_svm_cifs_admin_user` | `"{{ vault_netapp_cifs_admin_user }}"` | No | — |
| `netapp_svm_cifs_admin_password` | `"{{ vault_netapp_cifs_admin_password }}"` | No | — |
| `netapp_svm_cifs_ou` | `"OU=Storage,OU=Servers,DC=agency,DC=gov"` | No | — |
| `netapp_svm_cifs_workgroup` | `""` | No | — |
| `netapp_svm_configure_cifs_security` | `true` | No | CIFS security settings (DISA STIG compliant) |
| `netapp_svm_cifs_signing_required` | `"true"` | No | — |
| `netapp_svm_cifs_smb2_enabled` | `"true"` | No | — |
| `netapp_svm_cifs_smb3_enabled` | `"true"` | No | — |
| `netapp_svm_enable_iscsi` | `true` | No | iSCSI configuration |
| `netapp_svm_enable_fcp` | `false` | No | FCP configuration |
| `netapp_svm_enable_nvme` | `false` | No | NVMe configuration |
| `netapp_svm_configure_ldap` | `false` | No | LDAP configuration |
| `netapp_svm_ldap_client_name` | `"ldap_client_prod"` | No | — |
| `netapp_svm_ldap_servers` | `(see defaults/main.yml)` | No | — |
| `netapp_svm_ldap_base_dn` | `"dc=agency,dc=gov"` | No | — |
| `netapp_svm_ldap_base_scope` | `"subtree"` | No | — |
| `netapp_svm_ldap_bind_dn` | `"cn=netapp-bind,ou=Service Accounts,dc=agency,dc=gov"` | No | — |
| `netapp_svm_ldap_bind_password` | `"{{ vault_netapp_ldap_bind_password }}"` | No | — |
| `netapp_svm_ldap_schema` | `"RFC-2307"` | No | — |
| `netapp_svm_ldap_use_start_tls` | `true` | No | — |
| `netapp_svm_ldap_session_security` | `"sign"` | No | DISA STIG: sign or seal |
| `netapp_svm_configure_name_service` | `true` | No | Name service switch configuration |
| `netapp_svm_name_service_switch` | `(see defaults/main.yml)` | No | — |
| `netapp_svm_configure_routes` | `true` | No | SVM routing configuration |
| `netapp_svm_routes` | `(see defaults/main.yml)` | No | — |
| `netapp_svm_create_peer_relationships` | `false` | No | SVM peer relationships for DR/replication |
| `netapp_svm_peer_relationships` | `[]` | No | — |
| `netapp_svm_enable_vscan` | `false` | No | Vscan (anti-virus) configuration |
| `netapp_svm_vscan_policy_name` | `"default_policy"` | No | — |
| `netapp_svm_vscan_scan_mandatory` | `true` | No | — |
| `netapp_svm_vscan_max_file_size` | `2147483648` | No | 2GB |
| `netapp_svm_vscan_file_ext_include` | `(see defaults/main.yml)` | No | — |
| `netapp_svm_vscan_file_ext_exclude` | `(see defaults/main.yml)` | No | — |
| `netapp_svm_verify_config` | `true` | No | Configuration verification |
| `netapp_svm_debug` | `false` | No | Debug mode |

## Example Playbook

```yaml
---
- name: Netapp Svm Management
  hosts: localhost
  gather_facts: false
  roles:
    - role: netapp/roles/netapp_svm_management
```

## License

MIT

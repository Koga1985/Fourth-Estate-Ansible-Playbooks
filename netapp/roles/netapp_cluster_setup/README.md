# netapp_cluster_setup

Netapp Cluster Setup role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `netapp/README.md`

## Requirements

- Ansible 2.15+
- Collection: `netapp.ontap`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `netapp_cluster_hostname` | `"{{ vault_netapp_cluster_hostname \| default('netapp-cluster.example...` | No | Connection settings |
| `netapp_cluster_username` | `"{{ vault_netapp_cluster_username \| default('admin') }}"` | No | — |
| `netapp_cluster_password` | `"{{ vault_netapp_cluster_password }}"` | No | — |
| `netapp_cluster_validate_certs` | `true` | No | — |
| `netapp_cluster_install_collection` | `false` | No | — |
| `netapp_cluster_name` | `"netapp-cluster-prod"` | No | Cluster basic configuration |
| `netapp_cluster_contact` | `"Fourth Estate Storage Team <storage@agency.gov>"` | **Yes** | — |
| `netapp_cluster_location` | `"Primary Data Center - Secure Facility"` | No | — |
| `netapp_cluster_configure_dns` | `true` | No | DNS configuration |
| `netapp_cluster_dns_domains` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_dns_nameservers` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_configure_ntp` | `true` | No | NTP configuration |
| `netapp_cluster_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_timezone` | `"America/New_York"` | No | Timezone configuration |
| `netapp_cluster_nodes` | `(see defaults/main.yml)` | No | Cluster nodes |
| `netapp_cluster_configure_node_settings` | `false` | No | Node settings |
| `netapp_cluster_node_settings` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_create_aggregates` | `true` | No | Aggregate configuration |
| `netapp_cluster_aggregate_encryption` | `true` | No | — |
| `netapp_cluster_aggregates` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_configure_disk_assignment` | `true` | No | Disk assignment |
| `netapp_cluster_disk_autoassign` | `"on"` | No | — |
| `netapp_cluster_enable_ha` | `true` | No | High Availability |
| `netapp_cluster_configure_mgmt_lif` | `false` | No | Management LIF configuration |
| `netapp_cluster_mgmt_lif_name` | `"cluster_mgmt"` | No | — |
| `netapp_cluster_mgmt_home_port` | `"e0M"` | No | — |
| `netapp_cluster_mgmt_home_node` | `"netapp-01"` | No | — |
| `netapp_cluster_mgmt_ip` | `"10.0.1.100"` | No | — |
| `netapp_cluster_mgmt_netmask` | `"255.255.255.0"` | No | — |
| `netapp_cluster_create_broadcast_domains` | `false` | No | Broadcast domains |
| `netapp_cluster_broadcast_domains` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_create_intercluster_lifs` | `false` | No | Intercluster LIFs for replication |
| `netapp_cluster_intercluster_lifs` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_configure_peer` | `false` | No | Cluster peering for DR/replication |
| `netapp_cluster_peer_relationships` | `[]` | No | — |
| `netapp_cluster_configure_autosupport` | `true` | No | AutoSupport configuration (DISA STIG requirement for monitoring) |
| `netapp_cluster_autosupport_mail_hosts` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_autosupport_noteto` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_autosupport_from` | `"netapp-cluster@agency.gov"` | No | — |
| `netapp_cluster_autosupport_support` | `false` | No | Disable phone-home to NetApp (air-gapped env) |
| `netapp_cluster_autosupport_transport` | `"smtp"` | No | — |
| `netapp_cluster_configure_snmp` | `true` | No | SNMP configuration for monitoring |
| `netapp_cluster_snmp_community` | `"{{ vault_netapp_snmp_community \| default('public') }}"` | No | — |
| `netapp_cluster_snmp_access_control` | `"ro"` | No | — |
| `netapp_cluster_snmp_traphosts` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_configure_sp` | `false` | No | Service Processor (SP) network configuration |
| `netapp_cluster_sp_network` | `(see defaults/main.yml)` | No | — |
| `netapp_cluster_configure_licenses` | `false` | No | License configuration |
| `netapp_cluster_licenses` | `[]` | No | — |
| `netapp_cluster_verify_health` | `true` | No | Health verification |
| `netapp_cluster_debug` | `false` | No | Debug mode |

## Example Playbook

```yaml
---
- name: Netapp Cluster Setup
  hosts: localhost
  gather_facts: false
  roles:
    - role: netapp/roles/netapp_cluster_setup
```

## License

MIT

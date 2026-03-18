# netapp_cluster_setup

Netapp Cluster Setup role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `netapp/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `netapp_cluster_hostname` | `"{{ vault_netapp_cluster_hostname | No | default('ne...` |
| `netapp_cluster_username` | `"{{ vault_netapp_cluster_username | No | default('ad...` |
| `netapp_cluster_password` | `"{{ vault_netapp_cluster_password }}"` |  |
| `netapp_cluster_validate_certs` | `true` |  |
| `netapp_cluster_install_collection` | `false` |  |
| `netapp_cluster_name` | `"netapp-cluster-prod"` |  |
| `netapp_cluster_contact` | `"Fourth Estate Storage Team <storage@agency.gov>"` |  |
| `netapp_cluster_location` | `"Primary Data Center - Secure Facility"` |  |
| `netapp_cluster_configure_dns` | `true` |  |
| `netapp_cluster_configure_ntp` | `true` |  |
| `netapp_cluster_timezone` | `"America/New_York"` |  |
| `netapp_cluster_configure_node_settings` | `false` |  |
| `netapp_cluster_create_aggregates` | `true` |  |
| `netapp_cluster_aggregate_encryption` | `true` |  |
| `netapp_cluster_configure_disk_assignment` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `netapp.ontap`
- See platform `requirements.yml` for install instructions

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

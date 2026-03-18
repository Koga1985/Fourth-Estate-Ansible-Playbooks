# netapp_svm_management

Netapp Svm Management role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `netapp/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `netapp_svm_hostname` | `"{{ vault_netapp_cluster_hostname | No | default('ne...` |
| `netapp_svm_username` | `"{{ vault_netapp_cluster_username | No | default('ad...` |
| `netapp_svm_password` | `"{{ vault_netapp_cluster_password }}"` |  |
| `netapp_svm_validate_certs` | `true` |  |
| `netapp_svm_name` | `"svm_prod"` |  |
| `netapp_svm_root_volume` | `"{{ netapp_svm_name }}_root"` |  |
| `netapp_svm_root_aggregate` | `"aggr1_netapp01_SAS"` |  |
| `netapp_svm_root_security_style` | `"unix"` |  |
| `netapp_svm_ipspace` | `"Default"` |  |
| `netapp_svm_subtype` | `"default"` |  |
| `netapp_svm_comment` | `"Production SVM for Fourth Estate Agency"` |  |
| `netapp_svm_language` | `"c.UTF-8"` |  |
| `netapp_svm_snapshot_policy` | `"default"` |  |
| `netapp_svm_create_mgmt_lif` | `true` |  |
| `netapp_svm_mgmt_lif_name` | `"{{ netapp_svm_name }}_mgmt"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `netapp.ontap`
- See platform `requirements.yml` for install instructions

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

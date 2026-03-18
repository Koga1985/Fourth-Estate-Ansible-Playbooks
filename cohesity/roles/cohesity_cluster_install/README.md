# cohesity_cluster_install

Cohesity Cluster Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `cohesity/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `cohesity_cluster_name` | `"cohesity-cluster-01"` |  |
| `cohesity_cluster_domain` | `"cohesity.local"` |  |
| `cohesity_cluster_gateway` | `"10.100.1.1"` |  |
| `cohesity_cluster_subnet_mask` | `"255.255.255.0"` |  |
| `cohesity_deployment_type` | `"ve"` |  |
| `cohesity_ve_platform` | `"vmware"` | vmware, hyperv, aws, azure |
| `cohesity_ve_ova_path` | `"/opt/cohesity/CohesityVirtualEdition.ova"` |  |
| `cohesity_ve_vcenter_host` | `"vcenter.example.com"` |  |
| `cohesity_ve_vcenter_username` | `"administrator@vsphere.local"` |  |
| `cohesity_ve_vcenter_password` | `"{{ vault_vcenter_password }}"` |  |
| `cohesity_ve_datacenter` | `"Datacenter"` |  |
| `cohesity_ve_cluster` | `"Cluster01"` |  |
| `cohesity_ve_datastore` | `"datastore1"` |  |
| `cohesity_ve_network` | `"VM Network"` |  |
| `cohesity_ve_vm_name_prefix` | `"cohesity-node"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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

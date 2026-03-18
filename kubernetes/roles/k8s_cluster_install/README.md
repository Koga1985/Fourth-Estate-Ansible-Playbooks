# k8s_cluster_install

K8S Cluster Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `kubernetes/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `k8s_version` | `"1.28.5"` |  |
| `k8s_cluster_name` | `"fourth-estate-k8s"` |  |
| `k8s_pod_network_cidr` | `"10.244.0.0/16"` |  |
| `k8s_service_cidr` | `"10.96.0.0/12"` |  |
| `k8s_dns_domain` | `"cluster.local"` |  |
| `k8s_control_plane_endpoint` | `"api.{{ k8s_cluster_name }}.local:6443"` |  |
| `k8s_control_plane_ha` | `true` |  |
| `k8s_control_plane_replicas` | `3` |  |
| `k8s_etcd_version` | `"3.5.10"` |  |
| `k8s_etcd_data_dir` | `"/var/lib/etcd"` |  |
| `k8s_etcd_backup_enabled` | `true` |  |
| `k8s_etcd_backup_retention_days` | `30` |  |
| `k8s_etcd_encryption_enabled` | `true` |  |
| `k8s_cri` | `"containerd"` |  |
| `k8s_containerd_version` | `"1.7.11"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: K8S Cluster Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: kubernetes/roles/k8s_cluster_install
```

## License

MIT

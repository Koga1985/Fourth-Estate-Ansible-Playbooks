# k8s_cluster_install

K8S Cluster Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `kubernetes/README.md`

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `k8s_version` | `"1.28.5"` | No | Cluster Configuration |
| `k8s_cluster_name` | `"fourth-estate-k8s"` | No | — |
| `k8s_pod_network_cidr` | `"10.244.0.0/16"` | No | — |
| `k8s_service_cidr` | `"10.96.0.0/12"` | No | — |
| `k8s_dns_domain` | `"cluster.local"` | No | — |
| `k8s_control_plane_endpoint` | `"api.{{ k8s_cluster_name }}.local:6443"` | No | Control Plane Configuration |
| `k8s_control_plane_ha` | `true` | No | — |
| `k8s_control_plane_replicas` | `3` | No | — |
| `k8s_api_server_cert_sans` | `(see defaults/main.yml)` | No | — |
| `k8s_etcd_version` | `"3.5.10"` | No | etcd Configuration |
| `k8s_etcd_data_dir` | `"/var/lib/etcd"` | No | — |
| `k8s_etcd_backup_enabled` | `true` | No | — |
| `k8s_etcd_backup_retention_days` | `30` | No | — |
| `k8s_etcd_encryption_enabled` | `true` | No | — |
| `k8s_cri` | `"containerd"` | No | Container Runtime (containerd) |
| `k8s_containerd_version` | `"1.7.11"` | No | — |
| `k8s_containerd_config_dir` | `"/etc/containerd"` | No | — |
| `k8s_containerd_socket` | `"/run/containerd/containerd.sock"` | No | — |
| `k8s_containerd_insecure_registries` | `[]` | No | — |
| `k8s_containerd_registry_mirrors` | `{}` | No | — |
| `k8s_cni_plugin` | `"calico"` | No | CNI Plugin Configuration Options: calico, cilium, flannel |
| `k8s_calico_version` | `"v3.27.0"` | No | — |
| `k8s_cilium_version` | `"1.14.5"` | No | — |
| `k8s_cni_mtu` | `1450` | No | — |
| `k8s_enable_ipv6` | `false` | No | Network Configuration |
| `k8s_proxy_mode` | `"ipvs"` | No | Options: iptables, ipvs |
| `k8s_network_plugin_config` | `(see defaults/main.yml)` | No | — |
| `k8s_kubelet_max_pods` | `110` | No | Kubelet Configuration |
| `k8s_kubelet_pod_pids_limit` | `4096` | No | — |
| `k8s_kubelet_system_reserved` | `(see defaults/main.yml)` | No | — |
| `k8s_kubelet_kube_reserved` | `(see defaults/main.yml)` | No | — |
| `k8s_kubelet_eviction_hard` | `(see defaults/main.yml)` | No | — |
| `k8s_cert_validity_days` | `365` | No | Certificate Management |
| `k8s_cert_auto_renew` | `true` | No | — |
| `k8s_cert_key_size` | `2048` | No | — |
| `k8s_enable_audit_logging` | `true` | No | Security Configuration |
| `k8s_audit_log_path` | `"/var/log/kubernetes/audit.log"` | No | — |
| `k8s_audit_log_maxage` | `365` | No | — |
| `k8s_audit_log_maxbackup` | `10` | No | — |
| `k8s_audit_log_maxsize` | `100` | No | — |
| `k8s_enable_admission_plugins` | `(see defaults/main.yml)` | No | — |
| `k8s_disable_admission_plugins` | `[]` | No | — |
| `k8s_api_server_extra_args` | `(see defaults/main.yml)` | No | API Server Configuration |
| `k8s_controller_manager_extra_args` | `(see defaults/main.yml)` | No | Controller Manager Configuration |
| `k8s_scheduler_extra_args` | `(see defaults/main.yml)` | No | Scheduler Configuration |
| `k8s_kubeadm_init_extra_args` | `""` | No | kubeadm Configuration |
| `k8s_kubeadm_join_extra_args` | `""` | No | — |
| `k8s_feature_gates` | `(see defaults/main.yml)` | No | Feature Gates |
| `k8s_airgap_mode` | `false` | No | Air-gapped Installation (Fourth Estate) |
| `k8s_airgap_registry` | `""` | No | — |
| `k8s_airgap_image_list` | `[]` | No | — |
| `k8s_fourth_estate_enabled` | `true` | No | Fourth Estate Specific |
| `k8s_source_protection` | `true` | No | — |
| `k8s_journalist_access_enabled` | `true` | No | — |
| `k8s_publication_pipeline` | `true` | No | — |
| `k8s_content_isolation` | `true` | No | — |
| `k8s_control_plane_labels` | `(see defaults/main.yml)` | No | Node Labels |
| `k8s_worker_labels` | `(see defaults/main.yml)` | No | — |
| `k8s_control_plane_taints` | `(see defaults/main.yml)` | No | Taints |
| `k8s_lb_enabled` | `true` | No | Load Balancer Configuration (for HA) |
| `k8s_lb_type` | `"haproxy"` | No | Options: haproxy, nginx, cloud |
| `k8s_lb_vip` | `""` | No | — |
| `k8s_enable_metrics_server` | `true` | No | Monitoring and Observability |
| `k8s_metrics_server_version` | `"v0.6.4"` | No | — |
| `k8s_backup_enabled` | `true` | No | Backup Configuration |
| `k8s_backup_schedule` | `"0 2 * * *"` | No | — |
| `k8s_backup_retention_days` | `30` | No | — |

## Example Playbook

```yaml
---
- name: K8S Cluster Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: kubernetes/roles/k8s_cluster_install
```

## Tags

| Tag | Description |
|-----|-------------|
| `cni` | Tasks tagged `cni` |
| `compliance` | Tasks tagged `compliance` |
| `container-runtime` | Tasks tagged `container-runtime` |
| `control-plane` | Tasks tagged `control-plane` |
| `cri` | Tasks tagged `cri` |
| `fourth-estate` | Tasks tagged `fourth-estate` |
| `init` | Tasks tagged `init` |
| `install` | Tasks tagged `install` |
| `join` | Tasks tagged `join` |
| `metrics-server` | Tasks tagged `metrics-server` |
| `monitoring` | Tasks tagged `monitoring` |
| `network` | Tasks tagged `network` |
| `packages` | Tasks tagged `packages` |
| `preflight` | Tasks tagged `preflight` |
| `validate` | Tasks tagged `validate` |
| `verification` | Tasks tagged `verification` |
| `workers` | Tasks tagged `workers` |

## License

MIT

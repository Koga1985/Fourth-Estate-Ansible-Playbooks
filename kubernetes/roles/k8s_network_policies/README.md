# k8s_network_policies

K8S Network Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `kubernetes/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `k8s_pod_security_standard` | `restricted` |  |
| `k8s_network_policy_default_deny_ingress` | `true` |  |
| `k8s_network_policy_default_deny_egress` | `true` |  |
| `k8s_network_policy_allow_dns` | `true` |  |
| `k8s_network_policy_dns_namespace` | `kube-system` |  |
| `k8s_network_policy_allow_monitoring` | `true` |  |
| `k8s_network_policy_monitoring_namespace` | `monitoring` |  |
| `k8s_network_policy_allow_ingress_controller` | `true` |  |
| `k8s_network_policy_ingress_namespace` | `ingress-nginx` |  |
| `k8s_network_policy_fourth_estate_enabled` | `true` |  |
| `k8s_network_policy_custom` | `[]` |  |
| `k8s_network_policy_provider` | `calico` | Options: calico, cilium, weave, antrea |
| `k8s_network_policy_enable_logging` | `true` |  |
| `k8s_network_policy_log_level` | `info` |  |
| `k8s_network_policy_compliance_mode` | `strict` | Options: strict, permissive |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: K8S Network Policies
  hosts: localhost
  gather_facts: false
  roles:
    - role: kubernetes/roles/k8s_network_policies
```

## License

MIT

# k8s_network_policies

K8S Network Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `kubernetes/README.md`

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `k8s_network_policy_namespaces` | `(see defaults/main.yml)` | No | General Settings |
| `k8s_pod_security_standard` | `restricted` | No | Pod Security Standard |
| `k8s_network_policy_default_deny_ingress` | `true` | No | Default Deny Policies |
| `k8s_network_policy_default_deny_egress` | `true` | No | — |
| `k8s_network_policy_allow_dns` | `true` | No | Allow DNS Traffic |
| `k8s_network_policy_dns_namespace` | `kube-system` | No | — |
| `k8s_network_policy_dns_selector` | `(see defaults/main.yml)` | No | — |
| `k8s_network_policy_allow_monitoring` | `true` | No | Allow Monitoring Access |
| `k8s_network_policy_monitoring_namespace` | `monitoring` | No | — |
| `k8s_network_policy_monitoring_selector` | `(see defaults/main.yml)` | No | — |
| `k8s_network_policy_allow_ingress_controller` | `true` | No | Allow Ingress Controller |
| `k8s_network_policy_ingress_namespace` | `ingress-nginx` | No | — |
| `k8s_network_policy_ingress_selector` | `(see defaults/main.yml)` | No | — |
| `k8s_network_policy_fourth_estate_enabled` | `true` | No | Fourth Estate Specific Policies |
| `k8s_network_policy_namespace_isolation` | `(see defaults/main.yml)` | No | Namespace Isolation Configuration |
| `k8s_network_policy_pod_to_pod` | `(see defaults/main.yml)` | No | Pod-to-Pod Communication Rules |
| `k8s_network_policy_external_services` | `(see defaults/main.yml)` | No | External Service Access |
| `k8s_network_policy_cidr_rules` | `(see defaults/main.yml)` | No | CIDR-Based Rules |
| `k8s_network_policy_custom` | `[]` | No | Custom Network Policies |
| `k8s_network_policy_provider` | `calico` | No | Network Policy Provider Settings Options: calico, cilium, weave, antrea |
| `k8s_network_policy_enable_logging` | `true` | No | Logging and Monitoring |
| `k8s_network_policy_log_level` | `info` | No | — |
| `k8s_network_policy_compliance_mode` | `strict` | No | Compliance Settings Options: strict, permissive |
| `k8s_network_policy_audit_logging` | `true` | No | — |
| `k8s_network_policy_divisions` | `(see defaults/main.yml)` | No | Fourth Estate Division Isolation |
| `k8s_network_policy_source_protection` | `(see defaults/main.yml)` | No | Source Protection Workload Isolation |
| `k8s_network_policy_web_properties` | `(see defaults/main.yml)` | No | Web Property Deployment |
| `k8s_network_policy_rate_limiting` | `(see defaults/main.yml)` | No | Rate Limiting (if supported by CNI) |
| `k8s_network_policy_require_mtls` | `false` | No | Encryption Requirements Set true when service mesh is deployed |

## Example Playbook

```yaml
---
- name: K8S Network Policies
  hosts: localhost
  gather_facts: false
  roles:
    - role: kubernetes/roles/k8s_network_policies
```

## Tags

| Tag | Description |
|-----|-------------|
| `cidr` | Tasks tagged `cidr` |
| `custom` | Tasks tagged `custom` |
| `deny-egress` | Tasks tagged `deny-egress` |
| `deny-ingress` | Tasks tagged `deny-ingress` |
| `dns` | Tasks tagged `dns` |
| `external-access` | Tasks tagged `external-access` |
| `fourth-estate` | Tasks tagged `fourth-estate` |
| `ingress` | Tasks tagged `ingress` |
| `isolation` | Tasks tagged `isolation` |
| `monitoring` | Tasks tagged `monitoring` |
| `namespaces` | Tasks tagged `namespaces` |
| `network-policy` | Tasks tagged `network-policy` |
| `pod-communication` | Tasks tagged `pod-communication` |
| `preflight` | Tasks tagged `preflight` |
| `validation` | Tasks tagged `validation` |

## License

MIT

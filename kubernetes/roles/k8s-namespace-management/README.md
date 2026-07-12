# Kubernetes Namespace Management Role

Manages Kubernetes namespaces with resource quotas, limit ranges, and network policies.

## Requirements

- Ansible 2.14+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `k8s_namespaces` | `(see defaults/main.yml)` | No | Namespaces to create |
| `k8s_enable_resource_quotas` | `true` | No | Resource Quotas |
| `k8s_resource_quotas` | `(see defaults/main.yml)` | No | — |
| `k8s_enable_limit_ranges` | `true` | No | Limit Ranges |
| `k8s_limit_ranges` | `(see defaults/main.yml)` | No | — |
| `k8s_namespace_network_policies` | `true` | No | Network Policies per Namespace |
| `k8s_default_deny_all` | `true` | No | — |
| `k8s_protected_namespaces` | `(see defaults/main.yml)` | No | Delete protection |

## Example

```yaml
- role: k8s-namespace-management
  vars:
    k8s_namespaces:
      - name: myapp
        labels:
          environment: prod
          pod-security.kubernetes.io/enforce: restricted
```

## Tags

| Tag | Description |
|-----|-------------|
| `limits` | Tasks tagged `limits` |
| `namespaces` | Tasks tagged `namespaces` |
| `network-policies` | Tasks tagged `network-policies` |
| `quotas` | Tasks tagged `quotas` |

## Features

- Namespace creation with labels and annotations
- Resource quotas enforcement
- Limit ranges for containers
- Default network policies
- Pod Security Standards labels
- Protected namespace management

## STIG Controls

- V-242443: Resource quotas and limits
- Network segmentation via namespace isolation

## License

MIT

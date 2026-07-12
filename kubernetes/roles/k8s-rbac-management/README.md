# k8s-rbac-management

># Kubernetes RBAC Management Role

Production-ready Ansible role for managing Kubernetes RBAC with least privilege principles and DoD STIG compliance.

## Requirements

- Ansible 2.14+
- Kubernetes 1.24+
- `kubernetes.core` collection

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `k8s_rbac_enabled` | `true` | No | RBAC Configuration |
| `k8s_create_default_roles` | `true` | No | — |
| `k8s_audit_rbac_changes` | `true` | No | — |
| `k8s_create_service_accounts` | `true` | No | Service Accounts |
| `k8s_automount_sa_token` | `false` | No | — |
| `k8s_sa_token_secret_bound` | `true` | No | — |
| `k8s_admin_users` | `[]` | No | Predefined Roles |
| `k8s_developer_users` | `[]` | No | — |
| `k8s_viewer_users` | `[]` | No | — |
| `k8s_namespaced_roles` | `(see defaults/main.yml)` | No | Namespaced Roles |
| `k8s_cluster_roles` | `(see defaults/main.yml)` | No | Cluster Roles |
| `k8s_role_bindings` | `[]` | No | Role Bindings |
| `k8s_cluster_role_bindings` | `[]` | No | — |
| `k8s_deny_system_masters` | `true` | No | Security Constraints |
| `k8s_require_rolebinding_subjects` | `true` | No | — |
| `k8s_prevent_privilege_escalation` | `true` | No | — |
| `k8s_rbac_audit_enabled` | `true` | No | Audit and Compliance |
| `k8s_rbac_periodic_review` | `true` | No | — |
| `k8s_rbac_review_interval_days` | `90` | No | — |

## Example Playbook

```yaml
- name: Use k8s-rbac-management
  hosts: all
  gather_facts: false
  roles:
    - role: k8s-rbac-management
```

## Tags

| Tag | Description |
|-----|-------------|
| `audit` | Tasks tagged `audit` |
| `bindings` | Tasks tagged `bindings` |
| `cluster-roles` | Tasks tagged `cluster-roles` |
| `compliance` | Tasks tagged `compliance` |
| `rbac` | Tasks tagged `rbac` |
| `roles` | Tasks tagged `roles` |
| `service-accounts` | Tasks tagged `service-accounts` |

## Features

- Service account management with token automount controls
- Namespaced and cluster-wide role creation
- Role binding management
- RBAC audit and compliance reporting
- System:masters group detection
- Wildcard permission analysis

## Example Usage

```yaml
---
- hosts: k8s_control_plane
  roles:
    - role: k8s-rbac-management
      vars:
        k8s_automount_sa_token: false
        k8s_namespaced_roles:
          - name: developer
            namespace: development
            rules:
              - apiGroups: ["apps"]
                resources: ["deployments"]
                verbs: ["get", "list", "create", "update"]
```

## STIG Controls

- V-242402: RBAC authorization mode
- V-242445: Service account token management

## License

MIT

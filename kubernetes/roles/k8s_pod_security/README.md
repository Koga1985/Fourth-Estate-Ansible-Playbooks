# k8s_pod_security

K8S Pod Security role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `kubernetes/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `k8s_version` | `"1.28"` |  |
| `k8s_pod_security_admission_enabled` | `true` |  |
| `k8s_pod_security_default_enforce` | `restricted` |  |
| `k8s_pod_security_default_audit` | `restricted` |  |
| `k8s_pod_security_default_warn` | `restricted` |  |
| `k8s_pod_security_psp_enabled` | `false` |  |
| `k8s_pod_security_drop_all_capabilities` | `true` |  |
| `k8s_pod_security_allowed_capabilities` | `[]` |  |
| `k8s_pod_security_enforce_non_root` | `true` |  |
| `k8s_pod_security_min_user_id` | `1000` |  |
| `k8s_pod_security_readonly_rootfs` | `true` |  |
| `k8s_pod_security_apparmor_enabled` | `true` |  |
| `k8s_pod_security_apparmor_default_profile` | `runtime/default` |  |
| `k8s_pod_security_selinux_enabled` | `true` |  |
| `k8s_pod_security_seccomp_enabled` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: K8S Pod Security
  hosts: localhost
  gather_facts: false
  roles:
    - role: kubernetes/roles/k8s_pod_security
```

## License

MIT

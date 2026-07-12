# k8s_pod_security

K8S Pod Security role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `kubernetes/README.md`

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `k8s_version` | `"1.28"` | No | Kubernetes Version |
| `k8s_pod_security_admission_enabled` | `true` | No | Pod Security Admission |
| `k8s_pod_security_default_enforce` | `restricted` | No | Default Pod Security Standards Options: privileged, baseline, restricted |
| `k8s_pod_security_default_audit` | `restricted` | No | — |
| `k8s_pod_security_default_warn` | `restricted` | No | — |
| `k8s_pod_security_namespaces` | `(see defaults/main.yml)` | No | Namespace Pod Security Configuration |
| `k8s_pod_security_psp_enabled` | `false` | No | Pod Security Policy (deprecated in K8s 1.25, removed in 1.26) |
| `k8s_pod_security_context_defaults` | `(see defaults/main.yml)` | No | Security Context Defaults |
| `k8s_pod_security_drop_all_capabilities` | `true` | No | Capabilities Management |
| `k8s_pod_security_allowed_capabilities` | `[]` | No | — |
| `k8s_pod_security_required_drop_capabilities` | `(see defaults/main.yml)` | No | — |
| `k8s_pod_security_drop_capabilities` | `(see defaults/main.yml)` | No | Additional capabilities that can be dropped |
| `k8s_pod_security_enforce_non_root` | `true` | No | Non-root User Enforcement |
| `k8s_pod_security_min_user_id` | `1000` | No | — |
| `k8s_pod_security_readonly_rootfs` | `true` | No | Read-only Root Filesystem |
| `k8s_pod_security_apparmor_enabled` | `true` | No | AppArmor Configuration |
| `k8s_pod_security_apparmor_default_profile` | `runtime/default` | No | — |
| `k8s_pod_security_apparmor_profiles` | `(see defaults/main.yml)` | No | — |
| `k8s_pod_security_selinux_enabled` | `true` | No | SELinux Configuration |
| `k8s_pod_security_selinux_options` | `(see defaults/main.yml)` | No | — |
| `k8s_pod_security_seccomp_enabled` | `true` | No | Seccomp Configuration |
| `k8s_pod_security_seccomp_default_profile` | `RuntimeDefault` | No | — |
| `k8s_pod_security_seccomp_profiles` | `(see defaults/main.yml)` | No | — |
| `k8s_pod_security_runtime_classes` | `(see defaults/main.yml)` | No | RuntimeClass Configuration |
| `k8s_pod_security_webhook_enabled` | `false` | No | Webhook Configuration |
| `k8s_pod_security_webhook_url` | `""` | No | — |
| `k8s_pod_security_allowed_volume_types` | `(see defaults/main.yml)` | No | Volume Restrictions |
| `k8s_pod_security_forbidden_volume_types` | `(see defaults/main.yml)` | No | — |
| `k8s_pod_security_allow_host_network` | `false` | No | Host Namespace Restrictions |
| `k8s_pod_security_allow_host_pid` | `false` | No | — |
| `k8s_pod_security_allow_host_ipc` | `false` | No | — |
| `k8s_pod_security_allow_privilege_escalation` | `false` | No | Privilege Escalation |
| `k8s_pod_security_default_allow_privilege_escalation` | `false` | No | — |
| `k8s_pod_security_allow_privileged` | `false` | No | Privileged Containers |
| `k8s_pod_security_allow_host_ports` | `false` | No | Host Ports |
| `k8s_pod_security_allowed_host_port_ranges` | `[]` | No | — |
| `k8s_pod_security_allowed_proc_mount_types` | `(see defaults/main.yml)` | No | Proc Mount |
| `k8s_pod_security_fourth_estate_enabled` | `true` | No | Fourth Estate Specific |
| `k8s_pod_security_source_protection_strict` | `true` | No | — |
| `k8s_pod_security_compliance_level` | `nist-800-53` | No | Compliance Options: nist-800-53, disa-stig, pci-dss |
| `k8s_pod_security_audit_logging` | `true` | No | — |

## Example Playbook

```yaml
---
- name: K8S Pod Security
  hosts: localhost
  gather_facts: false
  roles:
    - role: kubernetes/roles/k8s_pod_security
```

## Tags

| Tag | Description |
|-----|-------------|
| `apparmor` | Tasks tagged `apparmor` |
| `baseline` | Tasks tagged `baseline` |
| `capabilities` | Tasks tagged `capabilities` |
| `namespaces` | Tasks tagged `namespaces` |
| `non-root` | Tasks tagged `non-root` |
| `pod-security-admission` | Tasks tagged `pod-security-admission` |
| `pod-security-policy` | Tasks tagged `pod-security-policy` |
| `pod-security-standards` | Tasks tagged `pod-security-standards` |
| `preflight` | Tasks tagged `preflight` |
| `readonly-rootfs` | Tasks tagged `readonly-rootfs` |
| `restricted` | Tasks tagged `restricted` |
| `runtime-class` | Tasks tagged `runtime-class` |
| `seccomp` | Tasks tagged `seccomp` |
| `security-context` | Tasks tagged `security-context` |
| `selinux` | Tasks tagged `selinux` |
| `validation` | Tasks tagged `validation` |
| `webhook` | Tasks tagged `webhook` |

## License

MIT

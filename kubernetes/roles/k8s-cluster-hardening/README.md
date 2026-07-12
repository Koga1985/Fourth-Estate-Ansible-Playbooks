# Kubernetes Cluster Hardening Role

Production-ready Ansible role for hardening Kubernetes clusters according to DoD STIG V1R11 and NIST SP 800-190 standards.

## Requirements

- Ansible 2.14 or higher
- Kubernetes 1.24 or higher
- kubectl installed and configured
- Access to Kubernetes cluster with admin privileges
- `kubernetes.core` collection

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `k8s_api_server_audit_log_enabled` | `true` | No | API Server Configuration (STIG V-242381, V-242382, V-242383) |
| `k8s_api_server_audit_log_path` | `/var/log/kubernetes/audit.log` | No | — |
| `k8s_api_server_audit_log_maxage` | `30` | No | — |
| `k8s_api_server_audit_log_maxbackup` | `10` | No | — |
| `k8s_api_server_audit_log_maxsize` | `100` | No | — |
| `k8s_api_server_audit_policy_file` | `/etc/kubernetes/audit-policy.yaml` | No | — |
| `k8s_tls_min_version` | `VersionTLS12` | No | TLS and Certificate Settings (STIG V-242400, V-242401) |
| `k8s_tls_cipher_suites` | `(see defaults/main.yml)` | No | — |
| `k8s_anonymous_auth_enabled` | `false` | No | Authentication and Authorization (STIG V-242402, V-242403) |
| `k8s_basic_auth_enabled` | `false` | No | — |
| `k8s_token_auth_enabled` | `false` | No | — |
| `k8s_authorization_mode` | `(see defaults/main.yml)` | No | — |
| `k8s_enable_admission_plugins` | `(see defaults/main.yml)` | No | Admission Controllers (STIG V-242417, V-242418, V-242419) |
| `k8s_disable_admission_plugins` | `(see defaults/main.yml)` | No | — |
| `k8s_kubelet_anonymous_auth` | `false` | No | Kubelet Security (STIG V-242424, V-242425, V-242426) |
| `k8s_kubelet_authorization_mode` | `Webhook` | No | — |
| `k8s_kubelet_authentication_mode` | `x509` | No | — |
| `k8s_kubelet_read_only_port` | `0` | No | — |
| `k8s_kubelet_protect_kernel_defaults` | `true` | No | — |
| `k8s_kubelet_make_iptables_util_chains` | `true` | No | — |
| `k8s_kubelet_event_qps` | `0` | No | — |
| `k8s_kubelet_streaming_connection_idle_timeout` | `5m` | No | — |
| `k8s_kubelet_tls_cert_file` | `/var/lib/kubelet/pki/kubelet.crt` | No | — |
| `k8s_kubelet_tls_private_key_file` | `/var/lib/kubelet/pki/kubelet.key` | No | — |
| `k8s_etcd_cert_file` | `/etc/kubernetes/pki/etcd/server.crt` | No | ETCD Security (STIG V-242434, V-242435) |
| `k8s_etcd_key_file` | `/etc/kubernetes/pki/etcd/server.key` | No | — |
| `k8s_etcd_client_cert_auth` | `true` | No | — |
| `k8s_etcd_peer_client_cert_auth` | `true` | No | — |
| `k8s_etcd_peer_auto_tls` | `false` | No | — |
| `k8s_etcd_auto_tls` | `false` | No | — |
| `k8s_default_network_policy_enabled` | `true` | No | Network Policy (NIST SP 800-190) |
| `k8s_network_policy_provider` | `calico` | No | Options: calico, cilium, weave |
| `k8s_pod_security_standard` | `restricted` | No | Pod Security Standards (NIST SP 800-190) Options: privileged, baseline, restricted |
| `k8s_enforce_pod_security_standards` | `true` | No | — |
| `k8s_enable_resource_quotas` | `true` | No | Resource Limits and Quotas (STIG V-242443) |
| `k8s_enable_limit_ranges` | `true` | No | — |
| `k8s_automount_service_account_token` | `false` | No | Service Account Security (STIG V-242445) |
| `k8s_service_account_lookup` | `true` | No | — |
| `k8s_config_file_permissions` | `'0600'` | No | File Permissions (STIG V-242450 through V-242455) |
| `k8s_config_file_owner` | `root` | No | — |
| `k8s_config_file_group` | `root` | No | — |
| `k8s_event_ttl` | `1h` | No | Logging and Monitoring (NIST SP 800-92) |
| `k8s_enable_profiling` | `false` | No | — |
| `k8s_security_context_defaults` | `(see defaults/main.yml)` | No | Security Context Defaults |
| `k8s_image_pull_policy` | `Always` | No | Image Security (STIG V-242408) |
| `k8s_require_image_signature` | `true` | No | — |
| `k8s_allowed_registries` | `(see defaults/main.yml)` | No | — |
| `k8s_enable_namespace_isolation` | `true` | No | Namespace Isolation |
| `k8s_protected_namespaces` | `(see defaults/main.yml)` | No | — |
| `k8s_enable_api_rate_limiting` | `true` | No | API Rate Limiting (DoS Protection) |
| `k8s_max_requests_inflight` | `400` | No | — |
| `k8s_max_mutating_requests_inflight` | `200` | No | — |
| `k8s_encryption_provider_config` | `/etc/kubernetes/encryption-config.yaml` | No | Encryption at Rest (STIG V-242462) |
| `k8s_enable_encryption_at_rest` | `true` | No | — |
| `k8s_service_mesh_enabled` | `false` | No | Service Mesh Integration |
| `k8s_service_mesh_type` | `istio` | No | Options: istio, linkerd, consul |
| `k8s_backup_enabled` | `true` | No | Backup and DR |
| `k8s_backup_schedule` | `"0 2 * * *"` | No | — |
| `k8s_backup_retention_days` | `30` | No | — |

## Example Playbook

```yaml
---
- name: Harden Kubernetes Cluster
  hosts: k8s_control_plane
  become: true
  roles:
    - role: k8s-cluster-hardening
      vars:
        k8s_pod_security_standard: restricted
        k8s_enable_encryption_at_rest: true
```

## Tags

| Tag | Description |
|-----|-------------|
| `api-server` | Tasks tagged `api-server` |
| `audit` | Tasks tagged `audit` |
| `compliance` | Tasks tagged `compliance` |
| `encryption` | Tasks tagged `encryption` |
| `etcd` | Tasks tagged `etcd` |
| `hardening` | Tasks tagged `hardening` |
| `kubelet` | Tasks tagged `kubelet` |
| `logging` | Tasks tagged `logging` |
| `network` | Tasks tagged `network` |
| `permissions` | Tasks tagged `permissions` |
| `pod-security` | Tasks tagged `pod-security` |
| `policies` | Tasks tagged `policies` |
| `preflight` | Tasks tagged `preflight` |
| `pss` | Tasks tagged `pss` |
| `secrets` | Tasks tagged `secrets` |
| `security-context` | Tasks tagged `security-context` |
| `stig` | Tasks tagged `stig` |
| `validation` | Tasks tagged `validation` |

## Description

This role applies comprehensive security hardening to Kubernetes clusters, implementing:
- API Server hardening with audit logging
- Kubelet security configuration
- ETCD encryption and authentication
- Pod Security Standards (PSS)
- Network policies
- Encryption at rest for secrets
- File permissions and ownership
- Compliance validation

## Dependencies

Install required Ansible collection:
```bash
ansible-galaxy collection install kubernetes.core
```

## STIG Controls Implemented

| STIG ID | Control | Implementation |
|---------|---------|----------------|
| V-242381 | Audit logging must be enabled | audit-logging.yml |
| V-242382 | Audit logs must be retained for 30 days | defaults/main.yml |
| V-242400 | TLS 1.2 minimum | api-server-hardening.yml |
| V-242402 | Anonymous auth disabled | api-server-hardening.yml |
| V-242417 | Admission controllers enabled | api-server-hardening.yml |
| V-242424-433 | Kubelet hardening | kubelet-hardening.yml |
| V-242434-437 | ETCD security | etcd-hardening.yml |
| V-242450-458 | File permissions | file-permissions.yml |
| V-242462-463 | Encryption at rest | encryption-at-rest.yml |

## NIST SP 800-190 Controls

- **Container Isolation**: Pod Security Standards, security contexts
- **Network Segmentation**: Network policies, namespace isolation
- **Secure Orchestration**: RBAC, admission controllers
- **Logging & Monitoring**: Audit logs, auditd integration
- **Runtime Defense**: Seccomp, AppArmor, read-only root filesystem

## Usage

### Basic Hardening
```bash
ansible-playbook -i inventory site.yml --tags hardening
```

### Specific Components
```bash
# API Server only
ansible-playbook -i inventory site.yml --tags api-server

# Kubelet only
ansible-playbook -i inventory site.yml --tags kubelet

# Run compliance validation
ansible-playbook -i inventory site.yml --tags compliance-validation
```

## Validation

Run compliance validation:
```bash
ansible-playbook -i inventory site.yml --tags validation
```

This generates a compliance report at `/tmp/k8s-compliance-report.json`.

## Security Considerations

1. **Backup Before Changes**: This role modifies critical Kubernetes components
2. **Test in Non-Production**: Validate in test environment first
3. **Encryption Keys**: Securely manage encryption keys
4. **Certificate Rotation**: Implement automated certificate rotation
5. **Audit Log Storage**: Ensure sufficient storage for audit logs

## Troubleshooting

### API Server Won't Start
- Check `/var/log/kubernetes/audit.log` for errors
- Verify audit policy file syntax
- Check encryption config file

### Kubelet Fails to Start
- Review `/var/log/syslog` or `journalctl -u kubelet`
- Verify certificate paths
- Check file permissions on kubelet config

### Pods Rejected by PSS
- Review Pod Security Standard level (restricted is most stringent)
- Check pod security context configuration
- Use baseline or privileged for specific namespaces if needed

## Author

DevOps Team

## License

MIT

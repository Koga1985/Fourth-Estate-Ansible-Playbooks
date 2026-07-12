# Kubernetes Secrets Management Role

Secure management of Kubernetes secrets with encryption validation and access controls.

## Requirements

- Ansible 2.14+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `k8s_secrets_encryption_enabled` | `true` | No | Secret Management |
| `k8s_secrets_rotation_enabled` | `false` | No | — |
| `k8s_secrets_rotation_days` | `90` | No | — |
| `k8s_external_secrets_enabled` | `false` | No | External Secrets Integration |
| `k8s_external_secrets_provider` | `vault` | No | vault, aws, azure, gcp |
| `k8s_sealed_secrets_enabled` | `false` | No | Sealed Secrets |
| `k8s_sealed_secrets_namespace` | `kube-system` | No | — |
| `k8s_scan_for_exposed_secrets` | `true` | No | Secret Scanning |
| `k8s_prevent_secret_in_logs` | `true` | No | — |
| `k8s_restrict_secret_access` | `true` | No | RBAC for Secrets |
| `k8s_audit_secret_access` | `true` | No | — |
| `k8s_secrets` | `(see defaults/main.yml)` | No | Secret Types to Manage |
| `k8s_image_pull_secrets` | `[]` | No | Image Pull Secrets |
| `k8s_tls_secrets` | `[]` | No | TLS Secrets |
| `k8s_manage_sa_tokens` | `true` | No | Service Account Tokens |
| `k8s_sa_token_expiration` | `3600` | No | seconds |

## Example

```yaml
- role: k8s-secrets-management
  vars:
    k8s_secrets_encryption_enabled: true
    k8s_scan_for_exposed_secrets: true
```

## Tags

| Tag | Description |
|-----|-------------|
| `audit` | Tasks tagged `audit` |
| `image-pull` | Tasks tagged `image-pull` |
| `rbac` | Tasks tagged `rbac` |
| `secrets` | Tasks tagged `secrets` |
| `tls` | Tasks tagged `tls` |
| `validation` | Tasks tagged `validation` |

## Features

- Secret creation and management
- Docker registry (image pull) secrets
- TLS secrets for ingress
- Encryption at rest validation
- Secret exposure scanning
- RBAC-based access control

## STIG Compliance

- V-242462: Encryption at rest for secrets
- V-242463: Secret protection and access control

## Security Notes

- All secret operations use `no_log: true`
- Validates encryption at rest is enabled
- Scans for accidentally exposed secrets in ConfigMaps
- Implements least privilege RBAC for secret access

## License

MIT

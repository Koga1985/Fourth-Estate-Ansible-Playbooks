# gcp_iam

Gcp Iam role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `google_cloud_platform/README.md`

## Requirements

- Ansible 2.15+
- Collection: `google.cloud`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `gcp_project_id` | `""` | No | Project configuration |
| `gcp_organization_id` | `""` | No | — |
| `gcp_auth_kind` | `"serviceaccount"` | No | — |
| `gcp_service_account_file` | `""` | No | — |
| `gcp_iam_service_accounts` | `[]` | No | Service accounts to create |
| `gcp_iam_custom_roles` | `[]` | No | Custom IAM roles |
| `gcp_iam_policy_bindings` | `[]` | No | IAM policy bindings at project level |
| `gcp_iam_conditional_bindings` | `[]` | No | Conditional IAM bindings (attribute-based and time-based access) |
| `gcp_iam_enable_workload_identity` | `false` | No | Workload Identity for GKE |
| `gcp_iam_workload_identity_bindings` | `[]` | No | — |
| `gcp_iam_impersonation_bindings` | `[]` | No | Service account impersonation |
| `gcp_iam_org_policy_bindings` | `[]` | No | Organization-level IAM policies |
| `gcp_iam_folder_policy_bindings` | `[]` | No | Folder-level IAM policies |
| `gcp_iam_keys_output_dir` | `"/tmp/gcp_sa_keys"` | No | Service account key management |
| `gcp_iam_enable_key_rotation` | `true` | No | — |
| `gcp_iam_key_rotation_days` | `90` | No | — |
| `gcp_iam_enable_audit` | `true` | No | Audit and compliance |
| `gcp_iam_enable_audit_logging` | `true` | No | — |
| `gcp_iam_artifacts_dir` | `"/tmp/gcp_iam_artifacts"` | No | — |
| `gcp_iam_fedramp_mode` | `true` | No | Fourth Estate compliance settings |
| `gcp_iam_cjis_mode` | `false` | No | — |
| `gcp_iam_source_protection_mode` | `true` | No | — |
| `gcp_iam_fourth_estate_roles` | `(see defaults/main.yml)` | No | Predefined roles for Fourth Estate agencies |
| `gcp_iam_audit_log_config` | `(see defaults/main.yml)` | No | IAM audit log configuration |
| `gcp_iam_domain_restriction` | `""` | No | Domain restriction for IAM |
| `gcp_iam_sa_prefix` | `"fe"` | No | Service account naming convention Fourth Estate prefix |
| `gcp_iam_sa_environment` | `"prod"` | No | — |
| `gcp_iam_max_keys_per_sa` | `2` | No | Maximum number of service account keys per account |
| `gcp_iam_enable_policy_analyzer` | `true` | No | Enable detailed IAM policy analysis |
| `gcp_iam_audit_retention_days` | `365` | No | Retention period for IAM audit logs (days) |

## Example Playbook

```yaml
---
- name: Gcp Iam
  hosts: localhost
  gather_facts: false
  roles:
    - role: google_cloud_platform/roles/gcp_iam
```

## License

MIT

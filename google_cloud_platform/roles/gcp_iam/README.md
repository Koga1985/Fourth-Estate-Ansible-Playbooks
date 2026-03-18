# gcp_iam

Gcp Iam role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `google_cloud_platform/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `gcp_project_id` | `""` |  |
| `gcp_organization_id` | `""` |  |
| `gcp_auth_kind` | `"serviceaccount"` |  |
| `gcp_service_account_file` | `""` |  |
| `gcp_iam_service_accounts` | `[]` |  |
| `gcp_iam_custom_roles` | `[]` |  |
| `gcp_iam_policy_bindings` | `[]` |  |
| `gcp_iam_conditional_bindings` | `[]` |  |
| `gcp_iam_enable_workload_identity` | `false` |  |
| `gcp_iam_workload_identity_bindings` | `[]` |  |
| `gcp_iam_impersonation_bindings` | `[]` |  |
| `gcp_iam_org_policy_bindings` | `[]` |  |
| `gcp_iam_folder_policy_bindings` | `[]` |  |
| `gcp_iam_keys_output_dir` | `"/tmp/gcp_sa_keys"` |  |
| `gcp_iam_enable_key_rotation` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `google.cloud`
- See platform `requirements.yml` for install instructions

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

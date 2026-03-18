# gcp_project_management

Gcp Project Management role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `google_cloud_platform/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `gcp_auth_kind` | `serviceaccount` |  |
| `gcp_service_account_file` | `"{{ lookup('env', 'GCP_SERVICE_ACCOUNT_FILE') |...` |  |
| `gcp_project_id` | `""` |  |
| `gcp_project_name` | `""` |  |
| `gcp_organization_id` | `""` |  |
| `gcp_folder_id` | `""` |  |
| `gcp_billing_account_id` | `""` |  |
| `gcp_project_iam_bindings` | `[]` |  |
| `gcp_enforce_org_policies` | `true` |  |
| `gcp_disable_sa_key_creation` | `true` |  |
| `gcp_restrict_public_ips` | `true` |  |
| `gcp_enable_deletion_protection` | `true` |  |
| `gcp_enable_budget_alerts` | `true` |  |
| `gcp_budget_amount` | `10000` | No | USD per month |
| `gcp_budget_notification_channels` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `google.cloud`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Gcp Project Management
  hosts: localhost
  gather_facts: false
  roles:
    - role: google_cloud_platform/roles/gcp_project_management
```

## License

MIT

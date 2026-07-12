# gcp_project_management

Gcp Project Management role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `google_cloud_platform/README.md`

## Requirements

- Ansible 2.15+
- Collection: `google.cloud`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `gcp_auth_kind` | `serviceaccount` | No | Authentication |
| `gcp_service_account_file` | `"{{ lookup('env', 'GCP_SERVICE_ACCOUNT_FILE') \| default(omit) }}"` | No | — |
| `gcp_project_id` | `""` | No | Project configuration |
| `gcp_project_name` | `""` | No | — |
| `gcp_organization_id` | `""` | No | — |
| `gcp_folder_id` | `""` | No | — |
| `gcp_billing_account_id` | `""` | No | — |
| `gcp_project_labels` | `(see defaults/main.yml)` | No | Project labels for governance |
| `gcp_required_apis` | `(see defaults/main.yml)` | No | Required APIs for Fourth Estate operations |
| `gcp_project_iam_bindings` | `[]` | No | IAM bindings |
| `gcp_essential_contacts` | `(see defaults/main.yml)` | No | Essential contacts for security notifications |
| `gcp_enforce_org_policies` | `true` | No | Organization policies |
| `gcp_allowed_domains` | `(see defaults/main.yml)` | No | — |
| `gcp_disable_sa_key_creation` | `true` | No | — |
| `gcp_restrict_public_ips` | `true` | No | — |
| `gcp_allowed_locations` | `(see defaults/main.yml)` | No | — |
| `gcp_enable_deletion_protection` | `true` | No | Deletion protection |
| `gcp_enable_budget_alerts` | `true` | No | Budget alerts |
| `gcp_budget_amount` | `10000` | No | USD per month |
| `gcp_budget_thresholds` | `(see defaults/main.yml)` | No | — |
| `gcp_budget_notification_channels` | `[]` | No | — |
| `gcp_enable_assured_workloads` | `true` | No | Assured Workloads for compliance |
| `gcp_assured_workload_regime` | `"FEDRAMP_HIGH"` | No | Options: FEDRAMP_HIGH, FEDRAMP_MODERATE, CJIS, IL4 |
| `gcp_assured_workload_location` | `"us-east1"` | No | — |
| `gcp_enable_sovereign_controls` | `true` | No | — |
| `gcp_assured_workload_labels` | `(see defaults/main.yml)` | No | — |
| `gcp_enable_vpc_service_controls` | `true` | No | VPC Service Controls |
| `gcp_access_policy_name` | `"fourth-estate-access-policy"` | No | — |
| `gcp_access_level_name` | `"fourth-estate-staff-access"` | No | — |
| `gcp_perimeter_name` | `"fourth-estate-perimeter"` | No | — |
| `gcp_project_number` | `""` | No | Will be populated after project creation |
| `gcp_allowed_ip_ranges` | `(see defaults/main.yml)` | No | — |
| `gcp_allowed_members` | `(see defaults/main.yml)` | No | — |
| `gcp_allowed_regions` | `(see defaults/main.yml)` | No | — |
| `gcp_restricted_services` | `(see defaults/main.yml)` | No | — |
| `gcp_vpc_allowed_services` | `(see defaults/main.yml)` | No | — |
| `gcp_artifacts_dir` | `"/tmp/gcp-artifacts"` | No | Artifacts directory for metadata |

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

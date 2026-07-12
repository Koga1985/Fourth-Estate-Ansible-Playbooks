# aws_iam_access_analyzer

Aws Iam Access Analyzer role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `iam_access_analyzer_name` | `"FedRAMP-Access-Analyzer"` | No | Access Analyzer Configuration |
| `iam_access_analyzer_type` | `"ACCOUNT"` | No | ACCOUNT, ORGANIZATION |
| `iam_access_analyzer_state` | `"present"` | No | — |
| `iam_access_analyzer_tags` | `(see defaults/main.yml)` | No | Tags |
| `iam_generate_findings_report` | `true` | No | Findings Configuration |
| `iam_access_analyzer_max_findings` | `100` | No | — |
| `iam_access_analyzer_alert_threshold` | `1` | No | — |
| `iam_high_risk_resource_types` | `(see defaults/main.yml)` | No | High-risk resource types to monitor |
| `iam_access_analyzer_archive_rules` | `[]` | No | Archive rules (override in inventory/playbook) |
| `iam_create_cloudwatch_alarms` | `true` | No | CloudWatch Integration |
| `iam_access_analyzer_sns_topic` | `""` | No | — |
| `iam_enable_organization_analyzer` | `false` | No | Organization-wide analyzer |
| `security_webhook_url` | `""` | No | Webhook for security notifications |

## Example Playbook

```yaml
---
- name: Aws Iam Access Analyzer
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_iam_access_analyzer
```

## License

MIT

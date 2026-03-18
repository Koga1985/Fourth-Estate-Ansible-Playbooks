# aws_iam_access_analyzer

Aws Iam Access Analyzer role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `iam_access_analyzer_name` | `"FedRAMP-Access-Analyzer"` |  |
| `iam_access_analyzer_type` | `"ACCOUNT"` | No | ACCOUNT, ORGANIZATION |
| `iam_access_analyzer_state` | `"present"` |  |
| `iam_generate_findings_report` | `true` |  |
| `iam_access_analyzer_max_findings` | `100` |  |
| `iam_access_analyzer_alert_threshold` | `1` |  |
| `iam_access_analyzer_archive_rules` | `[]` |  |
| `iam_create_cloudwatch_alarms` | `true` |  |
| `iam_access_analyzer_sns_topic` | `""` |  |
| `iam_enable_organization_analyzer` | `false` |  |
| `security_webhook_url` | `""` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

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

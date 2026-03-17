# AWS CloudWatch Logs

Creates and manages AWS CloudWatch log groups, metric filters, and subscription filters for centralized log aggregation, monitoring, and compliance reporting.

## Requirements

- Ansible 2.14+
- `community.aws` collection: `ansible-galaxy collection install community.aws`
- Python `boto3` and `botocore` packages: `pip install boto3 botocore`
- AWS credentials configured (environment variables, `~/.aws/credentials`, or IAM role)

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cloudwatch_log_state` | `"present"` | No | Desired state for all log resources (`present` or `absent`) |
| `cloudwatch_log_retention_days` | `90` | No | Default log retention period in days applied to all log groups |
| `cloudwatch_log_tags` | See defaults | No | Default tags applied to all log groups. Includes `ManagedBy`, `Environment`, `Compliance`, and `CostCenter` |
| `cloudwatch_log_groups` | `[]` | Yes | List of log group definitions. Each entry supports `name`, `retention_days`, `kms_key_id`, `tags`, and `state` |
| `cloudwatch_metric_filters` | `[]` | No | List of metric filter definitions. Each entry requires `log_group`, `name`, `pattern`, `metric_name`, `metric_namespace`, and optionally `metric_value` and `state` |
| `cloudwatch_subscription_filters` | `[]` | No | List of subscription filter definitions for log aggregation. Each entry requires `log_group`, `name`, `pattern`, `destination_arn`, `role_arn`, and optionally `state` |
| `kms_key_id` | `""` | No | Default KMS key ARN used to encrypt log groups when not specified per group |

## Example Playbook

```yaml
---
- name: Manage CloudWatch Log Groups
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_cloudwatch_logs
      vars:
        kms_key_id: "arn:aws-us-gov:kms:us-gov-west-1:123456789012:key/abcd1234-ab12-ab12-ab12-abcdef123456"
        cloudwatch_log_groups:
          - name: "/aws/lambda/my-function"
            retention_days: 30
            state: present
          - name: "/aws/vpc/flowlogs"
            retention_days: 90
            state: present
        cloudwatch_metric_filters:
          - log_group: "/aws/cloudtrail/organization"
            name: "UnauthorizedAPICalls"
            pattern: '{ ($.errorCode = "AccessDenied") }'
            metric_name: "UnauthorizedAPICalls"
            metric_namespace: "CloudTrailMetrics"
```

## Tags

This role does not define Ansible task tags.

## License

MIT

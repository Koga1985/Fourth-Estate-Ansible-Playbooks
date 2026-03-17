# AWS CloudWatch Alarms

Creates and manages AWS CloudWatch metric alarms that monitor AWS resource metrics and trigger notifications or automated actions when thresholds are breached.

## Requirements

- Ansible 2.14+
- `community.aws` collection: `ansible-galaxy collection install community.aws`
- Python `boto3` and `botocore` packages: `pip install boto3 botocore`
- AWS credentials configured (environment variables, `~/.aws/credentials`, or IAM role)

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cloudwatch_alarm_state` | `"present"` | No | Desired state for all alarms (`present` or `absent`) |
| `cloudwatch_alarms` | `[]` | Yes | List of alarm definitions. Each entry supports `name`, `description`, `namespace`, `metric`, `statistic`, `comparison`, `threshold`, `period`, `evaluation_periods`, `datapoints_to_alarm`, `dimensions`, `alarm_actions`, `ok_actions`, `insufficient_data_actions`, `treat_missing_data`, and `state` |

## Example Playbook

```yaml
---
- name: Manage CloudWatch Alarms
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_cloudwatch_alarms
      vars:
        cloudwatch_alarms:
          - name: "high-cpu-utilization"
            description: "Alert when EC2 CPU exceeds 80%"
            namespace: "AWS/EC2"
            metric: "CPUUtilization"
            statistic: "Average"
            comparison: "GreaterThanThreshold"
            threshold: 80
            period: 300
            evaluation_periods: 2
            dimensions:
              InstanceId: "i-0abc123def456789"
            alarm_actions:
              - "arn:aws-us-gov:sns:us-gov-west-1:123456789012:alerts"
            state: present
```

## Tags

This role does not define Ansible task tags.

## License

MIT

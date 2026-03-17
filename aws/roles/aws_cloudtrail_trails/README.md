# AWS CloudTrail Trails

Creates and manages AWS CloudTrail trails for comprehensive API activity logging and audit compliance, including multi-region trails, CloudWatch Logs integration, KMS encryption, and log file validation.

## Requirements

- Ansible 2.14+
- `amazon.aws` collection: `ansible-galaxy collection install amazon.aws`
- `community.aws` collection: `ansible-galaxy collection install community.aws`
- Python `boto3` and `botocore` packages: `pip install boto3 botocore`
- AWS credentials configured (environment variables, `~/.aws/credentials`, or IAM role)

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cloudtrail_state` | `"present"` | No | Desired state for all trails (`present` or `absent`) |
| `cloudtrail_tags` | See defaults | No | Default tags applied to all trails. Includes `ManagedBy`, `Environment`, `Compliance`, `SecurityControl`, and `CostCenter` |
| `cloudtrail_trails` | `[]` | Yes | List of trail definitions to create. Each entry supports `name`, `s3_bucket`, `s3_prefix`, `sns_topic`, `include_global_events`, `multi_region`, `log_file_validation`, `kms_key_id`, `cloudwatch_log_group`, `cloudwatch_role`, `tags`, and `state` |
| `kms_key_id` | `""` | No | Default KMS key ARN used to encrypt trail log files when not specified per trail |

## Example Playbook

```yaml
---
- name: Manage CloudTrail Trails
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_cloudtrail_trails
      vars:
        kms_key_id: "arn:aws-us-gov:kms:us-gov-west-1:123456789012:key/abcd1234-ab12-ab12-ab12-abcdef123456"
        cloudtrail_trails:
          - name: "organization-trail"
            s3_bucket: "cloudtrail-logs-bucket"
            s3_prefix: "cloudtrail"
            multi_region: true
            include_global_events: true
            log_file_validation: true
            cloudwatch_log_group: "arn:aws-us-gov:logs:us-gov-west-1:123456789012:log-group:/aws/cloudtrail/organization"
            cloudwatch_role: "arn:aws-us-gov:iam::123456789012:role/CloudTrailRole"
            state: present
```

## Tags

This role does not define Ansible task tags.

## License

MIT

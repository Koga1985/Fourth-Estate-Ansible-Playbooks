# AWS Config Rules

Creates and manages AWS Config rules for continuous compliance evaluation, including custom rules and a built-in set of FedRAMP High required rules for encryption, public access, and audit logging controls.

## Requirements

- Ansible 2.14+
- `community.aws` collection: `ansible-galaxy collection install community.aws`
- Python `boto3` and `botocore` packages: `pip install boto3 botocore`
- AWS credentials configured (environment variables, `~/.aws/credentials`, or IAM role)

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `config_rule_state` | `"present"` | No | Desired state for all Config rules (`present` or `absent`) |
| `config_enable_fedramp_rules` | `true` | No | When `true`, automatically creates the built-in FedRAMP compliance rules defined in `fedramp_config_rules` |
| `config_rules` | `[]` | No | List of custom AWS Config rule definitions. Each entry supports `name`, `description`, `source`, `scope`, `input_parameters`, and `state` |
| `fedramp_config_rules` | See defaults | No | List of AWS-managed Config rules required for FedRAMP High compliance. Includes checks for EBS encryption, S3 public access, CloudTrail enablement, IAM password policy, multi-region trails, and RDS encryption |

### Built-in FedRAMP Rules (when `config_enable_fedramp_rules: true`)

| Rule Name | Source Identifier | Description |
|-----------|------------------|-------------|
| `encrypted-volumes` | `ENCRYPTED_VOLUMES` | Checks whether EBS volumes are encrypted |
| `s3-bucket-public-read-prohibited` | `S3_BUCKET_PUBLIC_READ_PROHIBITED` | Checks that S3 buckets do not allow public read |
| `s3-bucket-public-write-prohibited` | `S3_BUCKET_PUBLIC_WRITE_PROHIBITED` | Checks that S3 buckets do not allow public write |
| `cloudtrail-enabled` | `CLOUD_TRAIL_ENABLED` | Checks whether CloudTrail is enabled |
| `iam-password-policy` | `IAM_PASSWORD_POLICY` | Checks whether the account password policy meets requirements |
| `multi-region-cloudtrail-enabled` | `MULTI_REGION_CLOUD_TRAIL_ENABLED` | Checks for at least one multi-region CloudTrail |
| `rds-storage-encrypted` | `RDS_STORAGE_ENCRYPTED` | Checks whether RDS instances have encryption enabled |

## Example Playbook

```yaml
---
- name: Manage AWS Config Rules
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_config_rules
      vars:
        config_enable_fedramp_rules: true
        config_rules:
          - name: "root-account-mfa-enabled"
            description: "Checks whether the root account has MFA enabled"
            source:
              owner: "AWS"
              source_identifier: "ROOT_ACCOUNT_MFA_ENABLED"
            state: present
```

## Tags

This role does not define Ansible task tags.

## License

MIT

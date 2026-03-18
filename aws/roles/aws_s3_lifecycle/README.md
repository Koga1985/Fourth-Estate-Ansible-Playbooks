# aws_s3_lifecycle

Aws S3 Lifecycle role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `s3_lifecycle_state` | `"present"` |  |
| `s3_enable_intelligent_tiering` | `true` |  |
| `s3_lifecycle_rules` | `[]` |  |
| `s3_buckets_for_tiering` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Aws S3 Lifecycle
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_s3_lifecycle
```

## License

MIT

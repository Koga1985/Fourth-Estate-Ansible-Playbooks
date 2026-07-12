# aws_s3_lifecycle

Aws S3 Lifecycle role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `s3_lifecycle_state` | `"present"` | No | — |
| `s3_enable_intelligent_tiering` | `true` | No | — |
| `s3_lifecycle_rules` | `[]` | No | — |
| `s3_buckets_for_tiering` | `[]` | No | — |

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

# aws_guardduty_detector

Aws Guardduty Detector role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `guardduty_state` | `"present"` |  |
| `guardduty_finding_frequency` | `"FIFTEEN_MINUTES"` |  |
| `guardduty_enable_s3_protection` | `true` |  |
| `guardduty_enable_k8s_protection` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Aws Guardduty Detector
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_guardduty_detector
```

## License

MIT

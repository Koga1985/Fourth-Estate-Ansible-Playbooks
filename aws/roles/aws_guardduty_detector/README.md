# aws_guardduty_detector

Aws Guardduty Detector role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `guardduty_state` | `"present"` | No | — |
| `guardduty_finding_frequency` | `"FIFTEEN_MINUTES"` | No | — |
| `guardduty_enable_s3_protection` | `true` | No | — |
| `guardduty_enable_k8s_protection` | `true` | No | — |

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

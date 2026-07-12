# aws_lambda_functions

Aws Lambda Functions role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `lambda_state` | `"present"` | No | — |
| `lambda_enable_insights` | `true` | No | — |
| `lambda_insights_layer_arn` | `"arn:aws-us-gov:lambda:us-gov-west-1:123456789012:layer:LambdaInsig...` | No | — |
| `lambda_tags` | `(see defaults/main.yml)` | No | — |
| `lambda_functions` | `[]` | No | — |
| `kms_key_arn` | `""` | No | — |

## Example Playbook

```yaml
---
- name: Aws Lambda Functions
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_lambda_functions
```

## License

MIT

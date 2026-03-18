# aws_lambda_functions

Aws Lambda Functions role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `lambda_state` | `"present"` |  |
| `lambda_enable_insights` | `true` |  |
| `lambda_insights_layer_arn` | `"arn:aws-us-gov:lambda:us-gov-west-1:1234567890...` |  |
| `lambda_functions` | `[]` |  |
| `kms_key_arn` | `""` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

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

# aws_fedramp_compliance

Aws Fedramp Compliance role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Aws Fedramp Compliance
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_fedramp_compliance
```

## License

MIT

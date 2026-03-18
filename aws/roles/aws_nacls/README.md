# aws_nacls

Aws Nacls role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `nacl_state` | `"present"` |  |
| `nacl_public_name` | `"{{ vpc_name | No | default('main') }}-public-nacl"` |
| `nacl_private_name` | `"{{ vpc_name | No | default('main') }}-private-nacl"` |
| `nacl_database_name` | `"{{ vpc_name | No | default('main') }}-database-nacl"` |
| `nacl_dmz_name` | `"{{ vpc_name | No | default('main') }}-dmz-nacl"` |
| `create_public_nacl` | `true` |  |
| `create_private_nacl` | `true` |  |
| `create_database_nacl` | `true` |  |
| `create_dmz_nacl` | `false` |  |
| `apply_fedramp_deny_rules` | `true` |  |
| `network_acls` | `[]` |  |
| `app_subnet_cidr` | `"10.0.10.0/24"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Aws Nacls
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_nacls
```

## License

MIT

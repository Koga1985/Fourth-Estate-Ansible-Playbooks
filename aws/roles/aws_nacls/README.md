# aws_nacls

Aws Nacls role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `nacl_state` | `"present"` | No | NACL Configuration |
| `nacl_public_name` | `"{{ vpc_name \| default('main') }}-public-nacl"` | No | — |
| `nacl_private_name` | `"{{ vpc_name \| default('main') }}-private-nacl"` | No | — |
| `nacl_database_name` | `"{{ vpc_name \| default('main') }}-database-nacl"` | No | — |
| `nacl_dmz_name` | `"{{ vpc_name \| default('main') }}-dmz-nacl"` | No | — |
| `create_public_nacl` | `true` | No | Feature flags |
| `create_private_nacl` | `true` | No | — |
| `create_database_nacl` | `true` | No | — |
| `create_dmz_nacl` | `false` | No | — |
| `apply_fedramp_deny_rules` | `true` | No | — |
| `nacl_tags` | `(see defaults/main.yml)` | No | Default tags |
| `network_acls` | `[]` | No | Network ACLs configuration (override in inventory/playbook) |
| `nacl_fedramp_deny_rules` | `(see defaults/main.yml)` | No | FedRAMP compliance deny rules |
| `nacl_dmz_ingress_rules` | `(see defaults/main.yml)` | No | DMZ NACL rules (override as needed) |
| `nacl_dmz_egress_rules` | `(see defaults/main.yml)` | No | — |
| `app_subnet_cidr` | `"10.0.10.0/24"` | No | CIDR blocks |

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

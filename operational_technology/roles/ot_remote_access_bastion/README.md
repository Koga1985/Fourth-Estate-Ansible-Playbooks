# ot_remote_access_bastion

Ot Remote Access Bastion role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `operational_technology/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `verify_ssl` | `true` |  |
| `artifacts_dir` | `/tmp/ot-artifacts` |  |
| `onboard` | `[]` |  |
| `scopes` | `[]` |  |
| `session` | `{}` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Ot Remote Access Bastion
  hosts: localhost
  gather_facts: false
  roles:
    - role: operational_technology/roles/ot_remote_access_bastion
```

## License

MIT

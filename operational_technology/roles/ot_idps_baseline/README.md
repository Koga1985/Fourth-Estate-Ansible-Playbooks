# ot_idps_baseline

Ot Idps Baseline role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `operational_technology/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `verify_ssl` | `true` |  |
| `artifacts_dir` | `/tmp/ot-artifacts` |  |
| `profile` | `{}` |  |
| `exceptions` | `[]` |  |
| `targets` | `[]` |  |
| `dry_run` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Ot Idps Baseline
  hosts: localhost
  gather_facts: false
  roles:
    - role: operational_technology/roles/ot_idps_baseline
```

## License

MIT

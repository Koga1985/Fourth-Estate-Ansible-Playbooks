# sl1_platform_config

Sl1 Platform Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `sciencelogic/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/sl1-config-artifacts"` |  |
| `log_level` | `"info"` |  |
| `dry_run` | `false` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Sl1 Platform Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: sciencelogic/roles/sl1_platform_config
```

## License

MIT

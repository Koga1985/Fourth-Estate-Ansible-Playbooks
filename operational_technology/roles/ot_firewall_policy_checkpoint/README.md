# ot_firewall_policy_checkpoint

Ot Firewall Policy Checkpoint role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `operational_technology/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `verify_ssl` | `true` |  |
| `artifacts_dir` | `/tmp/ot-artifacts` |  |
| `rules` | `[]` |  |
| `dry_run` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Ot Firewall Policy Checkpoint
  hosts: localhost
  gather_facts: false
  roles:
    - role: operational_technology/roles/ot_firewall_policy_checkpoint
```

## License

MIT

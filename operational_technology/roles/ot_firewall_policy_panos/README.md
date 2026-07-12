# ot_firewall_policy_panos

Ot Firewall Policy Panos role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `operational_technology/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `verify_ssl` | `true` | No | — |
| `artifacts_dir` | `/tmp/ot-artifacts` | No | — |
| `rules` | `[]` | No | — |
| `dry_run` | `true` | No | — |

## Example Playbook

```yaml
---
- name: Ot Firewall Policy Panos
  hosts: localhost
  gather_facts: false
  roles:
    - role: operational_technology/roles/ot_firewall_policy_panos
```

## License

MIT

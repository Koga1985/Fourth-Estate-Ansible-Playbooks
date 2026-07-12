# cp_identity_awareness

Cp Identity Awareness role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `checkpoint/cp_day0_deploy_configure/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cp_layer` | `"Network"` | No | — |
| `publish_changes` | `true` | No | — |
| `artifacts_dir` | `"/tmp/checkpoint-artifacts"` | No | — |
| `ia_gateways` | `[]` | No | — |
| `ia_identity_sources` | `[]` | No | — |
| `ia_access_roles` | `[]` | No | — |
| `ia_rules` | `[]` | No | — |

## Example Playbook

```yaml
---
- name: Cp Identity Awareness
  hosts: localhost
  gather_facts: false
  roles:
    - role: checkpoint/cp_day0_deploy_configure/roles/cp_identity_awareness
```

## License

MIT

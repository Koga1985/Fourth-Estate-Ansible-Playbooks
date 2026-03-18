# cp_identity_awareness

Cp Identity Awareness role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `checkpoint/cp_day0_deploy_configure/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `cp_layer` | `"Network"` |  |
| `publish_changes` | `true` |  |
| `artifacts_dir` | `"/tmp/checkpoint-artifacts"` |  |
| `ia_gateways` | `[]` |  |
| `ia_identity_sources` | `[]` |  |
| `ia_access_roles` | `[]` |  |
| `ia_rules` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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

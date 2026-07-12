# cp_threat_prevention

Cp Threat Prevention role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `checkpoint/cp_day0_deploy_configure/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `tp_layer` | `"Threat Prevention"` | No | — |
| `policy_package` | `"Standard"` | No | — |
| `install_targets` | `[]` | No | — |
| `publish_changes` | `true` | No | — |
| `parallel_batches` | `1` | No | — |
| `tp_profile_name` | `"TP-Baseline"` | No | — |
| `tp_profile_desc` | `"Baseline protections; prevent medium+"` | No | — |
| `tp_profile_mode` | `"optimized"` | No | — |
| `tp_managed_tag` | `"tp-managed"` | No | — |

## Example Playbook

```yaml
---
- name: Cp Threat Prevention
  hosts: localhost
  gather_facts: false
  roles:
    - role: checkpoint/cp_day0_deploy_configure/roles/cp_threat_prevention
```

## License

MIT

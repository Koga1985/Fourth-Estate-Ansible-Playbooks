# cp_access_policy

Cp Access Policy role for Fourth Estate infrastructure automation.

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
| `policy_package` | `"Standard"` | No | — |
| `install_targets` | `[]` | No | — |
| `artifacts_dir` | `"/tmp/checkpoint-artifacts"` | No | — |
| `managed_tag` | `"ansible-managed"` | No | — |
| `publish_changes` | `true` | No | — |
| `parallel_batches` | `1` | No | — |

## Example Playbook

```yaml
---
- name: Cp Access Policy
  hosts: localhost
  gather_facts: false
  roles:
    - role: checkpoint/cp_day0_deploy_configure/roles/cp_access_policy
```

## License

MIT

# cp_threat_prevention

Cp Threat Prevention role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `checkpoint/cp_day0_deploy_configure/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `tp_layer` | `"Threat Prevention"` |  |
| `policy_package` | `"Standard"` |  |
| `install_targets` | `[]` |  |
| `publish_changes` | `true` |  |
| `parallel_batches` | `1` |  |
| `tp_profile_name` | `"TP-Baseline"` |  |
| `tp_profile_desc` | `"Baseline protections; prevent medium+"` |  |
| `tp_profile_mode` | `"optimized"` |  |
| `tp_managed_tag` | `"tp-managed"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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

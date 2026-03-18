# cp_access_policy

Cp Access Policy role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `checkpoint/cp_day0_deploy_configure/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cp_layer` | `"Network"` |  |
| `policy_package` | `"Standard"` |  |
| `install_targets` | `[]` |  |
| `artifacts_dir` | `"/tmp/checkpoint-artifacts"` |  |
| `managed_tag` | `"ansible-managed"` |  |
| `publish_changes` | `true` |  |
| `parallel_batches` | `1` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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

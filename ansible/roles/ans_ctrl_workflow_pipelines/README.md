# ans_ctrl_workflow_pipelines

Opinionated plan→approve→apply→verify pipelines with approval SLAs.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | — |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `controller_host` | `"{{ lookup('env', 'CONTROLLER_HOST') \| default('https://controller....` | No | — |
| `controller_oauthtoken` | `"{{ lookup('env', 'CONTROLLER_OAUTH_TOKEN') \| default('') }}"` | No | — |
| `workflow_templates` | `[]` | No | Workflow Configuration |
| `workflow_approval_required` | `true` | No | — |
| `workflow_notification_enabled` | `true` | No | — |
| `fourth_estate_deployment_pipeline` | `true` | No | Fourth Estate Workflows |
| `fourth_estate_rollback_enabled` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_ctrl_workflow_pipelines
  hosts: all
  gather_facts: false
  roles:
    - role: ans_ctrl_workflow_pipelines
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

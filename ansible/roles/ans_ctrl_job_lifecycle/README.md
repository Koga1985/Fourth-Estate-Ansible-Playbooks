# ans_ctrl_job_lifecycle

Create job/workflow templates, schedules, notifications, and instance-group placement.

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
| `job_cleanup_enabled` | `true` | No | Job Lifecycle |
| `job_retention_days` | `90` | No | — |
| `job_cleanup_schedule` | `"daily"` | No | — |
| `max_concurrent_jobs` | `100` | No | Job Limits |
| `job_timeout_default` | `3600` | No | — |
| `job_retry_count` | `3` | No | — |
| `fourth_estate_job_approval` | `true` | No | Fourth Estate |
| `fourth_estate_job_auditing` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_ctrl_job_lifecycle
  hosts: all
  gather_facts: false
  roles:
    - role: ans_ctrl_job_lifecycle
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

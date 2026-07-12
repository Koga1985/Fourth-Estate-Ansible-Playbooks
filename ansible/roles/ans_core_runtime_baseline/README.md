# ans_core_runtime_baseline

Enforce ansible.cfg, fact caching (Redis), and callbacks.

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
| `runtime_python_version` | `"3.9"` | No | Runtime Settings |
| `runtime_ansible_version` | `"2.15"` | No | — |
| `runtime_timeout` | `3600` | No | — |
| `runtime_verbosity` | `0` | No | — |
| `runtime_job_timeout` | `3600` | No | Resource Limits |
| `runtime_max_forks` | `50` | No | — |
| `runtime_job_slice_count` | `1` | No | — |
| `fourth_estate_hardened_runtime` | `true` | No | Fourth Estate Baseline |
| `fourth_estate_fips_mode` | `true` | No | — |
| `fourth_estate_audit_mode` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_core_runtime_baseline
  hosts: all
  gather_facts: false
  roles:
    - role: ans_core_runtime_baseline
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

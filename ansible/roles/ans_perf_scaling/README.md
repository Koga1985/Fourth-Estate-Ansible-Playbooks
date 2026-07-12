# ans_perf_scaling

Tune forks/strategy, SSH multiplexing, and JT→Instance Group placement.

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
| `enable_fact_caching` | `true` | No | Performance Configuration |
| `fact_cache_timeout` | `3600` | No | — |
| `enable_pipelining` | `true` | No | — |
| `max_forks` | `50` | No | — |
| `instance_group_scaling` | `true` | No | Scaling Configuration |
| `container_group_enabled` | `false` | No | — |
| `db_connection_pool_size` | `100` | No | Database Tuning |
| `db_max_overflow` | `50` | No | — |
| `fourth_estate_high_availability` | `true` | No | Fourth Estate |
| `fourth_estate_load_balancing` | `true` | No | — |
| `fourth_estate_auto_scaling` | `false` | No | — |

## Example Playbook

```yaml
- name: Use ans_perf_scaling
  hosts: all
  gather_facts: false
  roles:
    - role: ans_perf_scaling
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

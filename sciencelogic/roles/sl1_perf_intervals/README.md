# sl1_perf_intervals

Standardize polling intervals and retention tiers; safeguard for hot devices.

Defaults in `defaults/main.yml`. Artifacts in `{ artifacts_dir }`.

## Requirements

- Ansible 2.13+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sl1` | `(see defaults/main.yml)` | No | — |
| `artifacts_dir` | `"/tmp/sl1-artifacts"` | No | — |
| `dry_run` | `true` | No | — |
| `polling` | `[]` | No | [{class:'Linux Server', interval:300}] |
| `retention` | `[]` | No | [{class:'Linux Server', raw_days:7, rollup_days:365}] |
| `hot_devices` | `[]` | No | device selectors that need special care |

## Example Playbook

```yaml
- name: Use sl1_perf_intervals
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_perf_intervals
```

## License

MIT

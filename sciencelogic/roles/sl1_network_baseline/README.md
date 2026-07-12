# sl1_network_baseline

Network-device PowerPacks, SNMP creds, latency/jitter KPIs, interface hygiene.

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
| `powerpacks` | `[]` | No | — |
| `snmp_creds` | `[]` | No | — |
| `kpis` | `{ latency_warn_ms: 50, latency_crit_ms: 100 }` | No | — |
| `interface_hygiene` | `{ ignore_down: true, min_speed_mbps: 100 }` | No | — |

## Example Playbook

```yaml
- name: Use sl1_network_baseline
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_network_baseline
```

## License

MIT

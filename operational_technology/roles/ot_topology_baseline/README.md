# ot_topology_baseline

Ot Topology Baseline role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `operational_technology/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `verify_ssl` | `true` | No | — |
| `artifacts_dir` | `/tmp/ot-artifacts` | No | — |
| `api` | `{url: "", token: "", paths: {}}` | No | — |
| `topology_gold_path` | `"/path/to/golden_topology.json"` | No | — |

## Example Playbook

```yaml
---
- name: Ot Topology Baseline
  hosts: localhost
  gather_facts: false
  roles:
    - role: operational_technology/roles/ot_topology_baseline
```

## License

MIT

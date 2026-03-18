# ot_topology_baseline

Ot Topology Baseline role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `operational_technology/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `verify_ssl` | `true` |  |
| `artifacts_dir` | `/tmp/ot-artifacts` |  |
| `api` | `{url: "", token: "", paths: {}}` |  |
| `topology_gold_path` | `"/path/to/golden_topology.json"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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

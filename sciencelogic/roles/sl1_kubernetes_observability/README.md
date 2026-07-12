# sl1_kubernetes_observability

K8s/cloud-native packs, cluster/node/pod KPIs, cost labels.

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
| `kpi_rules` | `[]` | No | — |
| `cost_labels` | `["app","owner","env"]` | No | — |

## Example Playbook

```yaml
- name: Use sl1_kubernetes_observability
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_kubernetes_observability
```

## License

MIT

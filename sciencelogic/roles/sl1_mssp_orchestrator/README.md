# sl1_mssp_orchestrator

Run any sl1_* role per tenant with isolated creds/labels, artifact partitioning.

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
| `tenants` | `[]` | No | [{name, sl1:{url,token,verify_ssl}, vars:{}, roles: ['sl1_inventory_model', ...]}] |
| `action` | `""` | No | optional single role to run for all tenants |

## Example Playbook

```yaml
- name: Use sl1_mssp_orchestrator
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_mssp_orchestrator
```

## License

MIT

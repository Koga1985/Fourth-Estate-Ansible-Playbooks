# Role: dragos_mssp_orchestrator

**Purpose**: multi-tenant loops to run any `dragos_*` task with per-tenant creds.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `dragos_base_url` | `"https://tenant.dragos.com"` | No | — |
| `dragos_token` | `"{{ lookup('env','DRAGOS_TOKEN') }}"` | No | — |
| `dragos_verify_ssl` | `true` | No | — |
| `artifacts_dir` | `"/tmp/dragos-artifacts"` | No | — |
| `page_size` | `500` | No | — |
| `dry_run` | `true` | No | — |
| `tenants` | `[]` | No | [ { name: plant1, base_url: "https://...", token: "..." } ] |
| `action_task` | `""` | No | e.g., "roles/dragos_alerts_pipeline/tasks/pull_filtered.yml" |
| `action_vars` | `{}` | No | optional extra vars to pass to the included task |

## Example Playbook

```yaml
- name: Use dragos_mssp_orchestrator
  hosts: all
  gather_facts: false
  roles:
    - role: dragos_mssp_orchestrator
```

## Includes
- `dragos_int__mssp_multi_tenant.yml` (inlined as role task logic)

## License

MIT

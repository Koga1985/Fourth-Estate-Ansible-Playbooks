# Role: dragos_cases_workflow

Turn alerts into cases, attach evidence, and reconcile statuses with ITSM.

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
| `page_size` | `500` | No | — |
| `artifacts_dir` | `"/tmp/dragos-artifacts"` | No | — |
| `dry_run` | `true` | No | — |
| `assign` | `{"owner": "ot-team", "dedupe_keys": ["site","asset.ip","category"]}` | No | — |
| `external` | `{` | No | — |

## Example Playbook

```yaml
- name: Use dragos_cases_workflow
  hosts: all
  gather_facts: false
  roles:
    - role: dragos_cases_workflow
```

## License

MIT

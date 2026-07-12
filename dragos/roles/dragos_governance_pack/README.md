# Role: dragos_governance_pack

**Purpose**: scheduled governance bundle (alerts CSV, audit events, RBAC violations, compliance zip).

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
| `cron_jobs` | `[]` | No | [ { name: "dragos-delta", minute: "*/30", job: "ansible-playbook playbooks/dragos_delta.yml >> /var/log/dragos_delta.log 2>&1" } ] |

## Example Playbook

```yaml
- name: Use dragos_governance_pack
  hosts: all
  gather_facts: false
  roles:
    - role: dragos_governance_pack
```

## Includes
- `dragos_audit__events_export.yml`
- `dragos_audit__compliance_pack.yml`
- `dragos_rbac__users_roles.yml`
- `dragos_rbac__least_privilege.yml`
- `dragos_admin__scheduler_cron.yml`

## License

MIT

# sl1_itsm_enrichment

Incident/CMDB enrichers (business service, owner, runbook links); bidirectional status sync.

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
| `enrichers` | `[]` | No | [{field:'business_service', lookup:'tag:service'}, {field:'owner', lookup:'cmdb:owner'}] |
| `runbooks` | `[]` | No | [{pattern:'db-*', url:'https://wiki/runbook-db'}] |
| `status_sync` | `{ enabled: true, state_map: { opened: "New", resolved: "Resolved" } }` | No | — |

## Example Playbook

```yaml
- name: Use sl1_itsm_enrichment
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_itsm_enrichment
```

## License

MIT

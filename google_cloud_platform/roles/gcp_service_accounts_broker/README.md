# gcp_service_accounts_broker

Service Account lifecycle (keyless), Workload Identity Federation providers, per-SA least-privilege templates.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `service_accounts` | `[]` | No | — |
| `wif` | `[]` | No | — |
| `sa_policies` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use gcp_service_accounts_broker
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_service_accounts_broker
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

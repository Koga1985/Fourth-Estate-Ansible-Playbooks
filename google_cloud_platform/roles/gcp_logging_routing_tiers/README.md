# gcp_logging_routing_tiers

Aggregated sinks by tier (security/audit/data-access); Chronicle/Splunk/BQ routing; retention by IL.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `sinks` | `[]` | No | — |
| `retention` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use gcp_logging_routing_tiers
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_logging_routing_tiers
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

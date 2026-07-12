# gcp_scc_response_playbooks

SCC response playbooks: mute library, notification channels (SOAR/ITSM), finding→ticket mappings, auto-close reconciler.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `mutes` | `[]` | No | — |
| `notifications` | `[]` | No | — |
| `mappings` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use gcp_scc_response_playbooks
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_scc_response_playbooks
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

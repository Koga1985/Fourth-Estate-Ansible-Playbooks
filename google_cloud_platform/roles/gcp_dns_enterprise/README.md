# gcp_dns_enterprise

DNS policies (restricted VIP), conditional fwd, DNS logging, split-horizon with change windows.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `policies` | `[]` | No | — |
| `forwarding` | `[]` | No | — |
| `logging` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use gcp_dns_enterprise
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_dns_enterprise
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

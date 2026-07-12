# gcp_ingress_egress_controls

LB hardening (internal/external), TLS policy, mTLS backends, WAF, egress proxy patterns.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `lbs` | `[]` | No | — |
| `tls` | `{}` | No | — |
| `waf` | `{}` | No | — |
| `egress` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use gcp_ingress_egress_controls
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_ingress_egress_controls
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

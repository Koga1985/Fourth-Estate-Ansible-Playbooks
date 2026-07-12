# Role: dragos_segmentation_assist

Turn observed flows into allowlist intent and vendor-ready templates; detect drift.

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
| `deployed_policy_csv` | `"/etc/dragos/deployed_policy.csv"` | No | — |
| `exceptions` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use dragos_segmentation_assist
  hosts: all
  gather_facts: false
  roles:
    - role: dragos_segmentation_assist
```

## License

MIT

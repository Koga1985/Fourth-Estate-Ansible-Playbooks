# Role: dragos_intel_ops

Purpose: indicator lifecycle + advisories.

Includes:
- dragos_intel__ioc_ingest.yml
- dragos_intel__ioc_expire.yml
- dragos_intel__worldview_pull.yml

See defaults for `ioc`, `expire`, `artifacts_dir`.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ioc` | `{}` | No | — |
| `expire` | `{}` | No | — |
| `artifacts_dir` | `"/tmp/dragos-artifacts"` | No | — |
| `dragos_base_url` | `"https://tenant.dragos.com"` | No | — |
| `dragos_token` | `"{{ lookup('env','DRAGOS_TOKEN') }}"` | No | — |
| `dragos_verify_ssl` | `true` | No | — |
| `page_size` | `500` | No | — |
| `dry_run` | `true` | No | — |

## Example Playbook

```yaml
- name: Use dragos_intel_ops
  hosts: all
  gather_facts: false
  roles:
    - role: dragos_intel_ops
```

## License

MIT

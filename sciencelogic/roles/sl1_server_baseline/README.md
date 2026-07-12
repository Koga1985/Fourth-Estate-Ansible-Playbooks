# sl1_server_baseline

Windows/Linux packs, WMI/SSH creds, service/process monitors.

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
| `powerpacks` | `[]` | No | — |
| `wmi_creds` | `[]` | No | — |
| `ssh_creds` | `[]` | No | — |
| `monitors` | `[]` | No | [{service:'sshd', process:'nginx', thresholds:{...}}] |

## Example Playbook

```yaml
- name: Use sl1_server_baseline
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_server_baseline
```

## License

MIT

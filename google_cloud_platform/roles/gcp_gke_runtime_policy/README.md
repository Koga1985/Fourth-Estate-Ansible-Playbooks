# gcp_gke_runtime_policy

PSP→PSaC migration aids; PSA labels; Gatekeeper constraints; seccomp/AppArmor defaults.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `psa_labels` | `[]` | No | — |
| `gatekeeper` | `[]` | No | — |
| `seccomp` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use gcp_gke_runtime_policy
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_gke_runtime_policy
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

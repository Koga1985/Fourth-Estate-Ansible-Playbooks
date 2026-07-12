# gcp_supply_chain_attestations

SLSA-style attestations, provenance/SBOM verification gates (Binary AuthZ), break-glass expiry policy.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `attestors` | `[]` | No | — |
| `policies` | `{}` | No | — |
| `break_glass` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use gcp_supply_chain_attestations
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_supply_chain_attestations
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

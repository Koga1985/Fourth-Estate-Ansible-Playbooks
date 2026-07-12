# pa_vpn_remoteaccess

Deploys GlobalProtect portal & gateway with client/agent configs and exports connected users.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `pa_use_panorama` | `false` | No | — |
| `device_group` | `null` | No | — |
| `vsys` | `"vsys1"` | No | — |
| `template` | `null` | No | — |
| `template_stack` | `null` | No | — |
| `artifacts_dir` | `"/tmp/pan-artifacts"` | No | — |
| `commit_after_changes` | `true` | No | — |
| `commit_description` | `"Apply GlobalProtect (Portal/Gateway) via Ansible"` | No | — |
| `gp_portal` | `(see defaults/main.yml)` | No | — |
| `gp_gateway` | `(see defaults/main.yml)` | No | — |
| `gp_monitoring` | `(see defaults/main.yml)` | No | — |

## Example Playbook

```yaml
- name: Use pa_vpn_remoteaccess
  hosts: all
  gather_facts: false
  roles:
    - role: pa_vpn_remoteaccess
```

## License

MIT

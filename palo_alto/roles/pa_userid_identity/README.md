# pa_userid_identity

Configures LDAP profiles, group mappings, and identity-based security rules. Panorama/firewall aware.

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
| `artifacts_dir` | `"/tmp/pan-artifacts"` | No | — |
| `commit_after_changes` | `true` | No | — |
| `commit_description` | `"Apply User-ID / Identity settings via Ansible"` | No | — |
| `ldap_server_profiles` | `[]` | No | — |
| `group_mappings` | `[]` | No | — |
| `identity_rules` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use pa_userid_identity
  hosts: all
  gather_facts: false
  roles:
    - role: pa_userid_identity
```

## License

MIT

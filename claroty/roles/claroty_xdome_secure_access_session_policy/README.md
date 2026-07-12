# claroty_xdome_secure_access_session_policy
Enforces session-policy: approvals, emergency access guardrails, session recording, and limits.

## Requirements

- Ansible 2.12+
- Collection: `ansible.builtin` (`ansible-galaxy collection install ansible.builtin`)
- Collection: `community.general` (`ansible-galaxy collection install community.general`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/claroty-artifacts"` | No | — |
| `log_dir` | `"/var/log/claroty"` | No | — |
| `claroty` | `(see defaults/main.yml)` | No | Claroty xDome API Configuration |
| `session_policies` | `[]` | No | Session Policies |
| `default_session_policy` | `(see defaults/main.yml)` | No | Default Session Policy (fallback) |
| `policy_templates` | `(see defaults/main.yml)` | No | Session Policy Templates (pre-configured) |
| `monitoring` | `(see defaults/main.yml)` | No | Monitoring and Alerts |
| `compliance` | `(see defaults/main.yml)` | No | Compliance Settings |
| `reporting` | `(see defaults/main.yml)` | No | Reporting |

## Example Playbook

```yaml
- name: Use claroty_xdome_secure_access_session_policy
  hosts: all
  gather_facts: false
  roles:
    - role: claroty_xdome_secure_access_session_policy
```

## License

MIT

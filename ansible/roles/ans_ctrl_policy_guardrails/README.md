# ans_ctrl_policy_guardrails

RBAC baseline, org settings, signed-content enforcement, survey policies.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | — |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `controller_host` | `"{{ lookup('env', 'CONTROLLER_HOST') \| default('https://controller....` | No | — |
| `controller_oauthtoken` | `"{{ lookup('env', 'CONTROLLER_OAUTH_TOKEN') \| default('') }}"` | No | — |
| `policy_enforcement_enabled` | `true` | No | Policy Configuration |
| `policy_mode` | `"enforce"` | No | enforce, audit, disabled |
| `require_approval_for_production` | `true` | No | Guardrails |
| `require_change_ticket` | `true` | No | — |
| `prevent_credential_exposure` | `true` | No | — |
| `enforce_rbac` | `true` | No | — |
| `fourth_estate_mandatory_mfa` | `true` | No | Fourth Estate Policies |
| `fourth_estate_change_window_enforcement` | `true` | No | — |
| `fourth_estate_blast_radius_limit` | `100` | No | — |

## Example Playbook

```yaml
- name: Use ans_ctrl_policy_guardrails
  hosts: all
  gather_facts: false
  roles:
    - role: ans_ctrl_policy_guardrails
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

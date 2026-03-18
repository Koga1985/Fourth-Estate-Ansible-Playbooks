# ot_allowlist_assist

Ot Allowlist Assist role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `operational_technology/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `verify_ssl` | `true` |  |
| `artifacts_dir` | `/tmp/ot-artifacts` |  |
| `api` | `{url: "", token: "", paths: {}}` |  |
| `deployed_policy_csv` | `"/path/to/export.csv"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Ot Allowlist Assist
  hosts: localhost
  gather_facts: false
  roles:
    - role: operational_technology/roles/ot_allowlist_assist
```

## License

MIT

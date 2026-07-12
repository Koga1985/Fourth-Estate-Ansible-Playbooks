# sl1_platform_hardening

SSL/TLS ciphers, SSO/SAML, API tokens rotation, password/lockout policies.

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
| `tls` | `{ min_version: "TLSv1.2", ciphers: [] }` | No | — |
| `sso` | `{ enabled: false, saml_metadata_url: "" }` | No | — |
| `api_tokens` | `{ rotate_after_days: 90, notify: true }` | No | — |
| `auth_policy` | `{ password_min_len: 14, lockout_threshold: 5, lockout_minutes: 15 }` | No | — |

## Example Playbook

```yaml
- name: Use sl1_platform_hardening
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_platform_hardening
```

## License

MIT

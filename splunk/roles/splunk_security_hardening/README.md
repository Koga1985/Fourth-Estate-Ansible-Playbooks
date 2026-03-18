# splunk_security_hardening

Applies DoD STIG and NIST 800-53 security hardening to an existing Splunk Enterprise installation. Covers access control, session management, audit logging, password policy, TLS enforcement, and file permissions.

## Requirements

- Ansible 2.15+
- Splunk Enterprise installed (run `splunk_enterprise_install` role first)
- `vault_splunk_admin_password` defined in vault.yml

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `stig_cat1_enabled` | `true` | No | Apply Category I (High) findings |
| `stig_cat2_enabled` | `true` | No | Apply Category II (Medium) findings |
| `stig_cat3_enabled` | `true` | No | Apply Category III (Low) findings |
| `ac_session_timeout_minutes` | `15` | No | UI session timeout (STIG V-258014) |
| `ac_max_failed_login_attempts` | `3` | No | Lockout after N failed logins |
| `ia_password_min_length` | `15` | No | Minimum password length |
| `ia_password_max_age_days` | `60` | No | Password maximum age |
| `ia_enforce_mfa` | `true` | No | Require MFA (STIG V-258012) |
| `au_log_retention_days` | `365` | No | Audit log retention period |

## Example Playbook

```yaml
---
- name: Harden Splunk Enterprise
  hosts: splunk_servers
  become: true
  roles:
    - role: splunk/roles/splunk_security_hardening
      vars:
        stig_cat1_enabled: true
        stig_cat2_enabled: true
        ac_session_timeout_minutes: 15
        ia_enforce_mfa: true
```

## License

MIT

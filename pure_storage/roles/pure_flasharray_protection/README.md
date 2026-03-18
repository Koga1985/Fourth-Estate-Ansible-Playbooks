# pure_flasharray_protection

Pure Flasharray Protection role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` |  |
| `flasharray_eradication_timer` | `86400` | 24 hours (in seconds) |
| `flasharray_evidence_pg` | `"pg-evidence-preservation"` |  |
| `flasharray_evidence_retention_days` | `2555` | 7 years |
| `flasharray_safemode_enabled` | `true` |  |
| `flasharray_safemode_retention_minimum` | `24` | hours (cannot delete before this) |
| `flasharray_safemode_retention_default` | `168` | hours (7 days default) |
| `flasharray_safemode_compliance_mode` | `true` |  |
| `flasharray_app_consistent_snapshots` | `true` |  |
| `flasharray_quiesce_timeout` | `300` | seconds |
| `flasharray_snapshot_suffix_format` | `"{{ ansible_date_time.iso8601_basic_short }}"` |  |
| `flasharray_snapshot_prefix` | `"snap"` |  |
| `flasharray_ransomware_protection_enabled` | `true` |  |
| `flasharray_immutable_snapshots` | `true` |  |
| `flasharray_snapshot_locking` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Pure Flasharray Protection
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_protection
```

## License

MIT

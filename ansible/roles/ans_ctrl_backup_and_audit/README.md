# ans_ctrl_backup_and_audit

Exports, sandbox restore, API health, audit/event exports, retention cleaner.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | Common settings |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `controller_host` | `"{{ lookup('env', 'CONTROLLER_HOST') \| default('https://controller....` | No | Controller connection |
| `controller_oauthtoken` | `"{{ lookup('env', 'CONTROLLER_OAUTH_TOKEN') \| default('') }}"` | No | — |
| `controller_username` | `"{{ lookup('env', 'CONTROLLER_USERNAME') \| default('') }}"` | No | — |
| `controller_password` | `"{{ lookup('env', 'CONTROLLER_PASSWORD') \| default('') }}"` | No | — |
| `backup_enabled` | `true` | No | Backup Configuration |
| `backup_path` | `"{{ artifacts_dir }}/backups"` | No | — |
| `backup_filename` | `"controller_backup_{{ ansible_date_time.iso8601_basic_short }}.json"` | No | — |
| `backup_schedule` | `"daily"` | No | daily, weekly, monthly |
| `backup_retention_days` | `30` | No | — |
| `backup_compression` | `true` | No | — |
| `backup_encryption` | `false` | No | — |
| `backup_encryption_key` | `""` | No | — |
| `backup_include_credentials` | `false` | No | Backup Scope Security: exclude by default |
| `backup_include_inventory` | `true` | No | — |
| `backup_include_projects` | `true` | No | — |
| `backup_include_job_templates` | `true` | No | — |
| `backup_include_workflow_templates` | `true` | No | — |
| `backup_include_organizations` | `true` | No | — |
| `backup_include_teams` | `true` | No | — |
| `backup_include_users` | `true` | No | — |
| `backup_include_settings` | `true` | No | — |
| `backup_include_schedules` | `true` | No | — |
| `backup_include_notification_templates` | `true` | No | — |
| `dr_enabled` | `true` | No | Disaster Recovery |
| `dr_remote_storage` | `"s3"` | No | s3, azure, gcs, nfs |
| `dr_s3_bucket` | `"fourth-estate-ansible-backups"` | No | — |
| `dr_s3_region` | `"us-gov-west-1"` | No | — |
| `dr_s3_access_key` | `"{{ lookup('env', 'AWS_ACCESS_KEY_ID') \| default('') }}"` | No | — |
| `dr_s3_secret_key` | `"{{ lookup('env', 'AWS_SECRET_ACCESS_KEY') \| default('') }}"` | No | — |
| `dr_verify_backup` | `true` | No | — |
| `dr_test_restore` | `false` | No | — |
| `restore_guard_org` | `"Sandbox"` | No | Restore Configuration |
| `restore_guard_enabled` | `true` | No | — |
| `restore_dry_run` | `true` | No | — |
| `audit_enabled` | `true` | No | Audit Configuration |
| `audit_days` | `7` | No | — |
| `audit_job_runs` | `true` | No | — |
| `audit_configuration_changes` | `true` | No | — |
| `audit_user_activity` | `true` | No | — |
| `audit_output_format` | `"json"` | No | json, csv, syslog |
| `audit_syslog_server` | `"syslog.example.mil"` | No | — |
| `audit_syslog_port` | `514` | No | — |
| `audit_retention_days` | `90` | No | Audit Retention |
| `audit_archive_enabled` | `true` | No | — |
| `audit_archive_path` | `"{{ artifacts_dir }}/audit_archives"` | No | — |
| `compliance_reports_enabled` | `true` | No | Compliance Reporting |
| `compliance_standards` | `(see defaults/main.yml)` | No | — |
| `compliance_report_schedule` | `"weekly"` | No | — |
| `compliance_recipients` | `(see defaults/main.yml)` | No | — |
| `health_check_enabled` | `true` | No | Health Checks |
| `health_check_database` | `true` | No | — |
| `health_check_redis` | `true` | No | — |
| `health_check_disk_space` | `true` | No | — |
| `health_check_disk_threshold` | `80` | No | percent |
| `health_check_notification` | `true` | No | — |
| `fourth_estate_audit_logging` | `true` | No | Fourth Estate Specific |
| `fourth_estate_evidence_retention` | `365` | No | days |
| `fourth_estate_immutable_logs` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_ctrl_backup_and_audit
  hosts: all
  gather_facts: false
  roles:
    - role: ans_ctrl_backup_and_audit
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

# VAST Data Storage - Reusable Tasks

This directory contains reusable task files that can be included in playbooks or roles for common VAST operations.

## Available Tasks

### create_view.yml
Create a new VAST view (filesystem/volume)

**Required Variables**: `view_name`, `view_path`, `vast_mgmt_host`

**Usage**:
```yaml
- ansible.builtin.include_tasks: tasks/create_view.yml
  vars:
    view_name: "app-data"
    view_path: "/apps/data"
    view_quota_gb: 1000
```

### create_quota.yml
Create a quota policy

**Required Variables**: `quota_name`, `quota_size_gb`

### create_user_mapping.yml
Create user or group identity mapping

**Required Variables**: `mapping_type`, `source_identity`

### verify_compliance.yml
Verify STIG and NIST compliance status

Displays compliance summary and checks for critical findings.

## Security Notes

- Always pass credentials via ansible-vault encrypted vars
- Never hardcode passwords
- Use `no_log: true` for sensitive operations

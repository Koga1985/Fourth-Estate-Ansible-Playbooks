# Splunk Operational Playbooks

This directory contains standalone operational **playbooks** for Splunk Enterprise administration, alongside the deployment playbooks. Each one declares its own `hosts:` and is run directly with `ansible-playbook`; they are not task files and cannot be included with `include_tasks`.

## Operational Playbooks

| File | Description |
|------|-------------|
| `restart_splunk.yml` | Safely restarts the Splunk Enterprise service, waits for the management port to become available, and verifies that Splunk returns to a running state before marking complete. |
| `health_check.yml` | Performs a comprehensive Splunk health check: verifies service status, queries the internal `_introspection` index for resource metrics, checks license usage, and validates that forwarder connections are active. Generates a timestamped health report artifact. |
| `backup_now.yml` | Executes an immediate Splunk configuration and index metadata backup outside of the scheduled backup window. Writes an encrypted archive to the configured backup path and logs the result. |
| `compliance_check.yml` | Verifies STIG compliance state for the running Splunk instance: checks FIPS mode, TLS version settings, audit log configuration, session timeout values, and RBAC assignments. Outputs a compliance summary report. |

## Usage

### Standalone Use

```bash
# Run a health check
ansible-playbook -i inventory splunk/playbooks/health_check.yml

# Force an immediate backup
ansible-playbook -i inventory splunk/playbooks/backup_now.yml

# Verify STIG compliance
ansible-playbook -i inventory splunk/playbooks/compliance_check.yml
```

### Chained from another playbook

Each file here is a complete play, so compose them with `import_playbook`
rather than `include_tasks`:

```yaml
---
- name: Restart Splunk after a config change
  ansible.builtin.import_playbook: splunk/playbooks/restart_splunk.yml

- name: Verify health after the restart
  ansible.builtin.import_playbook: splunk/playbooks/health_check.yml

- name: Check STIG compliance
  ansible.builtin.import_playbook: splunk/playbooks/compliance_check.yml
```

## Requirements

- Ansible 2.12+
- `become: true` for service management tasks
- Splunk Enterprise installed at the path configured in `splunk_home` (default `/opt/splunk`)

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

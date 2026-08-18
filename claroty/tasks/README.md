# Claroty Tasks

This directory contains **4 standalone task files** for common Claroty xDome API operations. These files can be included directly in any playbook without requiring a full role.

## Task Files

| File | Description |
|------|-------------|
| `claroty_alerts__pull_filtered.yml` | Queries the xDome alerts API with configurable severity and time-window filters and registers the result for downstream processing. |
| `claroty_assets__export_delta.yml` | Fetches only assets updated since the last run timestamp (delta export), writing results to the artifacts directory and updating the marker file. |
| `claroty_assets__export_full.yml` | Performs a full paginated asset export from xDome, producing JSON and CSV files in the artifacts directory. |
| `claroty_risk__pull_findings.yml` | Retrieves vulnerability and risk findings from xDome for a given site or asset filter and registers the findings list. |

## Common Variables

All task files expect the `claroty` connection dictionary to be in scope:

```yaml
claroty:
  base_url: "https://xdome.example.com"
  token: "{{ vault_claroty_token }}"
  verify_ssl: true
```

Additional per-task variables (page size, filters, artifact paths) default to sensible values but can be overridden in the calling playbook.

## Usage

```yaml
---
- name: Pull Claroty alerts and risk data
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    claroty:
      base_url: "https://xdome.example.com"
      token: "{{ vault_claroty_token }}"
      verify_ssl: true
    artifacts_dir: "/tmp/claroty-artifacts"

  tasks:
    - name: Pull high/critical alerts
      ansible.builtin.include_tasks: claroty/tasks/claroty_alerts__pull_filtered.yml

    - name: Export delta assets
      ansible.builtin.include_tasks: claroty/tasks/claroty_assets__export_delta.yml
```

## Requirements

- Ansible 2.12+
- Network access to the Claroty xDome API (HTTPS)
- Valid bearer token in `claroty.token`

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

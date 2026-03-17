# Claroty Roles

This directory contains **11 Ansible roles** for automating the Claroty xDome OT/IoT security platform, covering asset inventory, vulnerability management, secure access, network segmentation, and compliance reporting.

## Roles

### Inventory Management

| Role | Description |
|------|-------------|
| **claroty_xdome_inventory_export** | Exports xDome assets with pagination and optional delta sync. Produces JSON and/or CSV output and updates a `last_run` marker file to support incremental pulls. |
| **claroty_xdome_inventory_normalize_cmdb** | Reads the exported JSON, normalizes site names and zone/criticality classifications using configurable rules, and pushes records to a ServiceNow CMDB table. Optionally tags assets back in xDome. |
| **claroty_xdome_inventory_scheduler** | Installs a shell wrapper and cron entry on the control host to run a delta-sync playbook on a configurable schedule. |

### Security Integration

| Role | Description |
|------|-------------|
| **claroty_xdome_alerts_siem** | Polls xDome alerts by severity and time window, writes a CSV artifact, forwards alert JSON to an HTTP SIEM endpoint, and optionally tags high/critical assets or raises tickets in ServiceNow or Jira. |
| **claroty_xdome_vuln_risk** | Pulls vulnerability and risk findings from xDome and produces prioritized reports for remediation workflows. |

### Secure Access

| Role | Description |
|------|-------------|
| **claroty_xdome_secure_access_onboarding** | Automates user and device onboarding into the Claroty Secure Access module. |
| **claroty_xdome_secure_access_session_policy** | Manages session policies including time-based access windows, recording settings, and approval workflows. |
| **claroty_xdome_secure_access_audit_export** | Exports Secure Access session audit logs to local files for retention or SIEM forwarding. |

### Network and Compliance

| Role | Description |
|------|-------------|
| **claroty_xdome_segmentation** | Pulls segmentation recommendations from xDome and renders firewall rule intents for downstream enforcement roles. |
| **claroty_xdome_reporting_compliance_pack** | Generates an ISA/IEC-62443-aligned compliance evidence bundle (CSV artifacts). |
| **claroty_xdome_reporting_exec_summary** | Produces an executive summary report of OT/IoT asset posture, alert trends, and risk scores. |

## Requirements

- Ansible 2.12+
- Network access to the Claroty xDome API (HTTPS)
- A valid xDome API bearer token (stored in Ansible Vault)
- For CMDB push: ServiceNow instance with appropriate REST API permissions
- For ticketing hooks: ServiceNow or Jira credentials

## Quick Start

```bash
# Store credentials
ansible-vault edit group_vars/all/vault.yml
# Set: vault_claroty_token, vault_snow_token

ansible-playbook -i inventory site.yml --tags inventory --ask-vault-pass
```

## Example Playbook

```yaml
---
- name: Claroty xDome inventory pipeline
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    claroty:
      base_url: "https://xdome.example.com"
      token: "{{ vault_claroty_token }}"
      verify_ssl: true

  roles:
    - role: claroty/roles/claroty_xdome_inventory_export
      vars:
        inventory_format: both
        delta_since: auto

    - role: claroty/roles/claroty_xdome_inventory_normalize_cmdb
      vars:
        cmdb_push: true
        servicenow:
          instance: yourinstance.service-now.com
          token: "{{ vault_snow_token }}"
```

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

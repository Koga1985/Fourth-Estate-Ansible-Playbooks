# ise_report__endpoint_catalog

Retrieves the complete Cisco ISE endpoint inventory and generates a catalog report. This role enumerates all registered endpoints, analyzes the inventory by profiling category and identity group membership, and produces a timestamped JSON report. It is used for asset management, compliance auditing, and capacity planning.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API read access
- Ansible Vault for credential management

## Role Variables

### ISE Connection

| Variable | Default | Required | Description |
|---|---|---|
| `ise_hostname` | `{{ vault_ise_hostname }}` | **Yes** | ISE primary PAN hostname or IP |
| `ise_username` | `{{ vault_ise_username }}` | **Yes** | ISE admin username |
| `ise_password` | `{{ vault_ise_password }}` | **Yes** | ISE admin password (vault-protected) |
| `ise_verify_ssl` | `true` | No | Validate ISE TLS certificate |
| `ise_use_proxy` | `false` | No | Route ISE API calls through a proxy |
| `ise_debug` | `false` | No | Enable verbose debug logging |

### Deployment Control

| Variable | Default | Required | Description |
|---|---|---|
| `apply_changes` | `false` | No | Not used for mutation in this role; reserved |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_report__endpoint_catalog_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_report__endpoint_catalog_log_level` | `INFO` | No | Log verbosity level |
| `ise_report__endpoint_catalog_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_report__endpoint_catalog_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_report__endpoint_catalog_notify_on_completion` | `false` | No | Send email on completion |
| `ise_report__endpoint_catalog_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_report__endpoint_catalog_auto_backup` | `true` | No | Reserved |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Generate ISE endpoint catalog report
  hosts: localhost
  gather_facts: true
  roles:
    - role: cisco/roles/ise_report__endpoint_catalog
```

### With Email Notification

```yaml
- name: Generate and email ISE endpoint catalog
  hosts: localhost
  gather_facts: true
  vars:
    ise_report__endpoint_catalog_notify_on_completion: true
  roles:
    - role: cisco/roles/ise_report__endpoint_catalog
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `discovery` | Endpoint inventory retrieval tasks |
| `endpoints` | Endpoint data processing tasks |
| `analysis` | Inventory analysis and grouping tasks |
| `reporting` | Report generation tasks |

## Output

The role produces a JSON report at:

```
{{ ise_artifacts_dir }}/endpoint_catalog_<epoch>.json
```

The report includes:
- Total endpoint count
- Endpoints grouped by profiling policy (profile ID)
- Endpoints grouped by identity group (group ID)

## Notes

- This role is entirely read-only with respect to ISE.
- For large deployments with tens of thousands of endpoints, API pagination may be required; review ISE ERS API pagination behavior for your ISE version.
- All credentials must be stored in Ansible Vault.

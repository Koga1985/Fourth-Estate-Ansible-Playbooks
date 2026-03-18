# ise_policy__hitcount_shadow_report

Retrieves policy rule hit counts from Cisco ISE and identifies shadow rules — rules with zero hits that are likely unreachable due to being masked by a broader rule above them in the evaluation order. This role produces a timestamped JSON report highlighting unused rules so that policy administrators can review and clean up the policy table, reducing complexity and improving performance.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE MnT API accessible from the Ansible control node
- ISE admin credentials with MnT API read access
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
| `apply_changes` | `false` | No | Not used for mutation; reserved for future rule cleanup automation |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_policy__hitcount_shadow_report_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_policy__hitcount_shadow_report_log_level` | `INFO` | No | Log verbosity level |
| `ise_policy__hitcount_shadow_report_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_policy__hitcount_shadow_report_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_policy__hitcount_shadow_report_notify_on_completion` | `false` | No | Send email on completion |
| `ise_policy__hitcount_shadow_report_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_policy__hitcount_shadow_report_auto_backup` | `true` | No | Reserved |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Generate ISE policy hit count and shadow rule report
  hosts: localhost
  gather_facts: true
  roles:
    - role: cisco/roles/ise_policy__hitcount_shadow_report
```

### With Email Notification

```yaml
- name: Generate and email ISE policy hit count report
  hosts: localhost
  gather_facts: true
  vars:
    ise_policy__hitcount_shadow_report_notify_on_completion: true
  roles:
    - role: cisco/roles/ise_policy__hitcount_shadow_report
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `hitcount` | Policy hit count retrieval tasks |
| `analysis` | Shadow rule identification tasks |
| `reporting` | Report generation tasks |

## Output

The role produces a JSON report at:

```
{{ ise_artifacts_dir }}/hitcount_shadow_<epoch>.json
```

The report includes:
- All policy rules with their hit counts
- List of identified shadow rules (hit count equals zero)

## Notes

- This role is entirely read-only with respect to ISE.
- Shadow rules have a hit count of zero; this may indicate they are unreachable, but could also mean they have not yet been evaluated (e.g., new rules). Review context before removal.
- All credentials must be stored in Ansible Vault.

# ise_policy__hitcount_shadow_report

Retrieves policy rule hit counts from Cisco ISE and identifies shadow rules — rules with zero hits that are likely unreachable due to being masked by a broader rule above them in the evaluation order. This role produces a timestamped JSON report highlighting unused rules so that policy administrators can review and clean up the policy table, reducing complexity and improving performance.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE MnT API accessible from the Ansible control node
- ISE admin credentials with MnT API read access
- Ansible Vault for credential management

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ise_hostname` | `"{{ vault_ise_hostname }}"` | No | ISE Connection Parameters |
| `ise_username` | `"{{ vault_ise_username }}"` | No | — |
| `ise_password` | `"{{ vault_ise_password }}"` | No | — |
| `ise_verify_ssl` | `true` | No | — |
| `ise_use_proxy` | `false` | No | — |
| `ise_debug` | `false` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `ise_artifacts_dir` | `"/tmp/ise-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Configuration |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `ise_policy__hitcount_shadow_report_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_policy__hitcount_shadow_report_log_level` | `"INFO"` | No | Logging |
| `ise_policy__hitcount_shadow_report_log_to_syslog` | `true` | No | — |
| `ise_policy__hitcount_shadow_report_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_policy__hitcount_shadow_report_notify_on_completion` | `false` | No | Notification Settings |
| `ise_policy__hitcount_shadow_report_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_policy__hitcount_shadow_report_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT

# ise_policy__radius_dacls

Creates and manages Cisco ISE Downloadable Access Control Lists (dACLs). dACLs are pushed by ISE to network access devices (switches, WLCs) as part of a RADIUS authorization response, allowing fine-grained traffic filtering per user or device session without requiring static ACL configuration on each network device. This role manages dACL definitions centrally and generates an artifact report.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access
- Ansible Vault for credential management

## Role Variables

### ISE Connection

| Variable | Default | Description |
|---|---|---|
| `ise_hostname` | `{{ vault_ise_hostname }}` | ISE primary PAN hostname or IP |
| `ise_username` | `{{ vault_ise_username }}` | ISE admin username |
| `ise_password` | `{{ vault_ise_password }}` | ISE admin password (vault-protected) |
| `ise_verify_ssl` | `true` | Validate ISE TLS certificate |
| `ise_use_proxy` | `false` | Route ISE API calls through a proxy |
| `ise_debug` | `false` | Enable verbose debug logging |

### Deployment Control

| Variable | Default | Description |
|---|---|---|
| `apply_changes` | `false` | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | Local directory for generated reports |

### Downloadable ACLs

| Variable | Default | Description |
|---|---|---|
| `downloadable_acls` | (required) | List of dACL definitions. Each entry has: `name` (required), `acl_content` (required — IOS-style ACE lines as a string), `acl_type` (default `IPV4`; also supports `IPV6`, `IP_AGNOSTIC`), and optional `description` |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_policy__radius_dacls_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_policy__radius_dacls_log_level` | `INFO` | Log verbosity level |
| `ise_policy__radius_dacls_log_to_syslog` | `true` | Forward events to syslog |
| `ise_policy__radius_dacls_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_policy__radius_dacls_notify_on_completion` | `false` | Send email on completion |
| `ise_policy__radius_dacls_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_policy__radius_dacls_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Configure ISE downloadable ACLs
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    downloadable_acls:
      - name: "PERMIT_ALL_TRAFFIC"
        description: "Permit all IPv4 traffic"
        acl_type: "IPV4"
        acl_content: "permit ip any any"
      - name: "PERMIT_INTERNET_ONLY"
        description: "Permit internet access, deny RFC1918"
        acl_type: "IPV4"
        acl_content: |
          deny ip any 10.0.0.0 0.255.255.255
          deny ip any 172.16.0.0 0.15.255.255
          deny ip any 192.168.0.0 0.0.255.255
          permit ip any any
      - name: "DENY_ALL"
        description: "Deny all traffic (quarantine)"
        acl_type: "IPV4"
        acl_content: "deny ip any any"
  roles:
    - role: cisco/roles/ise_policy__radius_dacls
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `dacl` | All dACL creation and update tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- ACL content uses IOS-style ACE syntax; each line should be a complete ACE.
- dACL names referenced in `ise_policy__authz_profiles` must match exactly.
- All credentials must be stored in Ansible Vault.

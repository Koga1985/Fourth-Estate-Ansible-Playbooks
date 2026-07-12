# ise_policy__radius_dacls

Creates and manages Cisco ISE Downloadable Access Control Lists (dACLs). dACLs are pushed by ISE to network access devices (switches, WLCs) as part of a RADIUS authorization response, allowing fine-grained traffic filtering per user or device session without requiring static ACL configuration on each network device. This role manages dACL definitions centrally and generates an artifact report.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access
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
| `ise_policy__radius_dacls_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_policy__radius_dacls_log_level` | `"INFO"` | No | Logging |
| `ise_policy__radius_dacls_log_to_syslog` | `true` | No | — |
| `ise_policy__radius_dacls_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_policy__radius_dacls_notify_on_completion` | `false` | No | Notification Settings |
| `ise_policy__radius_dacls_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_policy__radius_dacls_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT

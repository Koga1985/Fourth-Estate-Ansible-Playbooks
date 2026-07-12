# ise_byod__workflow

Configures the Cisco ISE Bring Your Own Device (BYOD) onboarding workflow. This role provisions the BYOD self-registration portal, certificate provisioning profiles, and authorization profiles required to support employee-owned device onboarding. It is designed for environments that require DISA STIG-compliant BYOD access alongside corporate-managed device policies.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE 3.x or later with BYOD licensing
- ISE admin credentials with ERS API access
- A certificate authority configured within ISE for BYOD certificate issuance
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
| `ise_byod__workflow_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_byod__workflow_log_level` | `"INFO"` | No | Logging |
| `ise_byod__workflow_log_to_syslog` | `true` | No | — |
| `ise_byod__workflow_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_byod__workflow_notify_on_completion` | `false` | No | Notification Settings |
| `ise_byod__workflow_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_byod__workflow_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Configure ISE BYOD workflow
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    byod_portal_name: "BYOD-Self-Registration"
    byod_allowed_interfaces: "eth0"
    byod_cert_group: "Default Portal Certificate Group"
    byod_endpoint_group: "RegisteredDevices"
    byod_cert_profile_name: "BYOD-Cert-Profile"
    byod_cert_authority: "ISE Internal CA"
    byod_authz_profiles:
      - name: "BYOD-Registered"
        access_type: "ACCESS_ACCEPT"
        vlan: 100
      - name: "BYOD-Onboarding"
        access_type: "ACCESS_ACCEPT"
        vlan: 200
  roles:
    - role: cisco/roles/ise_byod__workflow
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `byod` | All BYOD configuration tasks |
| `portal` | BYOD portal configuration |
| `certificates` | Certificate provisioning configuration |
| `authorization` | Authorization profile creation |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode without altering ISE.
- A certificate authority must be configured in ISE before running this role with `apply_changes: true`.
- All credentials must be stored in Ansible Vault.

## License

MIT

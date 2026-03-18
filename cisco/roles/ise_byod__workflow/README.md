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
| `apply_changes` | `false` | No | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### BYOD Portal Settings

| Variable | Default | Required | Description |
|---|---|---|
| `byod_portal_name` | (required) | No | Name of the BYOD portal to create or update |
| `byod_allowed_interfaces` | (required) | No | ISE interface(s) on which the portal listens |
| `byod_cert_group` | (required) | No | Certificate group tag used for portal TLS |
| `byod_endpoint_group` | (required) | No | Endpoint identity group for BYOD devices |

### Certificate Provisioning

| Variable | Default | Required | Description |
|---|---|---|
| `byod_cert_profile_name` | (required) | No | Name of the certificate provisioning profile |
| `byod_cert_authority` | (required) | No | ISE internal CA to issue BYOD certificates |

### Authorization Profiles

| Variable | Default | Required | Description |
|---|---|---|
| `byod_authz_profiles` | `[]` | No | List of authorization profiles; each entry has `name`, `access_type`, and optional `vlan` |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_byod__workflow_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant configuration settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_byod__workflow_log_level` | `INFO` | No | Log verbosity level |
| `ise_byod__workflow_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_byod__workflow_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_byod__workflow_notify_on_completion` | `false` | No | Send email on completion |
| `ise_byod__workflow_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_byod__workflow_auto_backup` | `true` | No | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

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

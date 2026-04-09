# claroty_xdome_secure_access_onboarding

Onboards users and vendors into Claroty xDome Secure Remote Access. Creates and updates access policies (including Just-in-Time approval workflows), access profiles (session recording, MFA, file-transfer controls), and manages credential rotation and compliance requirements. Integrates with Active Directory, ServiceNow, and Okta.

## Requirements

- Ansible 2.15+
- `CLAROTY_API_TOKEN` environment variable set (or override via `claroty.token`)
- Network access to the Claroty xDome API endpoint
- Python `requests` library on the Ansible control node

## Role Variables

### Core

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/claroty-artifacts"` | No | Directory for generated reports |
| `log_dir` | `"/var/log/claroty"` | No | Directory for operational logs |

### Claroty API

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `claroty.base_url` | `"https://xdome.claroty.com/api"` | **Yes** | xDome API base URL |
| `claroty.token` | `$CLAROTY_API_TOKEN` | **Yes** | API token (vault-protected) |
| `claroty.verify_ssl` | `true` | No | Verify xDome TLS certificate |
| `claroty.timeout` | `30` | No | API request timeout in seconds |

### Users

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `users` | `[]` | No | List of user/vendor objects to onboard (see structure below) |

Each user entry supports these keys:

```yaml
users:
  - email: "vendor@acme.com"
    name: "John Vendor"
    user_type: "vendor"            # vendor, contractor, employee
    roles: ["remote_access_user"]
    groups: ["vendor-acme"]
    mfa_required: true
    certificate_auth: false
    expiration_date: "2026-12-31"
    approval_required: true
    approvers: ["admin@agency.gov"]
    session_policy: "vendor-restricted"
    access_scope:
      sites: ["site-hq"]
      zones: ["Purdue-L2"]
      asset_groups: ["scada-systems"]
    time_windows:
      - days: ["monday", "tuesday", "wednesday", "thursday", "friday"]
        start_time: "08:00"
        end_time: "17:00"
        timezone: "America/New_York"
    ip_allowlist:
      - "203.0.113.0/24"
```

### Access Policies

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `access_policies` | `[]` | No | List of access policy objects (JIT, approval workflows, etc.) |

Key policy fields: `name`, `approval_required`, `approvers`, `approval_timeout_hours`, `max_session_duration_minutes`, `access_scope`, `protocols_allowed`, `time_restrictions`.

### Access Profiles

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `access_profiles` | `[]` | No | List of session policy profile objects |

Key profile fields: `name`, `mfa_enforcement`, `mfa_methods`, `session_recording`, `file_transfer`, `clipboard`, `idle_timeout_minutes`, `session_timeout_minutes`, `concurrent_sessions_max`.

### Credential Rotation

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `credential_rotation.enabled` | `true` | No | Enable automated credential rotation |
| `credential_rotation.rotation_interval_days` | `90` | No | Days between forced credential rotations |
| `credential_rotation.notify_before_expiration_days` | `14` | No | Days before expiration to send notification |
| `credential_rotation.force_change_on_first_login` | `true` | No | Require password change on first login |

### Access Request Workflow

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `access_request_workflow.enabled` | `true` | No | Enable self-service access request portal |
| `access_request_workflow.manager_approval_required` | `true` | No | Require manager approval for access requests |
| `access_request_workflow.security_team_approval_required` | `true` | No | Require security team approval |
| `access_request_workflow.auto_provision_on_approval` | `true` | No | Automatically provision access when approved |

### Compliance

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `compliance.log_all_onboarding_actions` | `true` | No | Audit log every onboarding action |
| `compliance.require_background_check` | `true` | No | Require background check clearance before access |
| `compliance.require_nda_acceptance` | `true` | No | Require NDA acceptance |
| `compliance.require_security_training` | `true` | No | Require security training completion |
| `compliance.periodic_access_review_days` | `90` | No | Days between periodic access reviews |

### Notifications

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `notifications.enabled` | `true` | No | Enable email notifications |
| `notifications.smtp_server` | `"smtp.agency.gov"` | No | SMTP server hostname |
| `notifications.smtp_port` | `587` | No | SMTP port |
| `notifications.from_address` | `"claroty-security@agency.gov"` | No | Notification sender address |
| `notifications.notification_recipients` | `["ot-security@agency.gov"]` | No | Default notification recipients |

### Integrations

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `integrations.active_directory.enabled` | `false` | No | Sync users from Active Directory |
| `integrations.active_directory.ldap_url` | `"ldaps://dc.agency.gov:636"` | No | LDAP URL |
| `integrations.servicenow.enabled` | `false` | No | Create ServiceNow access request tickets |
| `integrations.servicenow.token` | `$SERVICENOW_TOKEN` | **Yes if enabled** | ServiceNow API token |
| `integrations.okta.enabled` | `false` | No | Enable Okta SSO integration |
| `integrations.okta.api_token` | `$OKTA_API_TOKEN` | **Yes if enabled** | Okta API token |

## Example Playbook

```yaml
- name: Onboard vendor for OT network access
  hosts: localhost
  gather_facts: false
  roles:
    - role: claroty/roles/claroty_xdome_secure_access_onboarding
      vars:
        claroty:
          base_url: "https://xdome.agency.gov/api"
          token: "{{ vault_claroty_token }}"
        users:
          - email: "contractor@acme.com"
            name: "Jane Contractor"
            user_type: "contractor"
            roles: ["remote_access_user"]
            mfa_required: true
            expiration_date: "2026-06-30"
            approval_required: true
            approvers: ["ot-security@agency.gov"]
            access_scope:
              sites: ["site-hq"]
              zones: ["Purdue-L2", "Purdue-L3"]
            time_windows:
              - days: ["monday", "tuesday", "wednesday", "thursday", "friday"]
                start_time: "08:00"
                end_time: "17:00"
                timezone: "America/New_York"
```

## Tags

| Tag | Description |
|-----|-------------|
| `users` | Create/update user accounts |
| `policies` | Create/update access policies |
| `profiles` | Create/update access profiles |
| `credentials` | Apply credential rotation settings |
| `integrations` | Configure AD/ServiceNow/Okta integrations |

## Compliance Controls

| Framework | Control ID | Description |
|-----------|-----------|-------------|
| NIST 800-53 | AC-2 | Account Management |
| NIST 800-53 | AC-3 | Access Enforcement |
| NIST 800-53 | IA-2 | Identification and Authentication |
| NIST 800-53 | IA-5 | Authenticator Management |
| NIST 800-53 | AU-2 | Audit Events — log all onboarding actions |
| IEC 62443 | SR 1.1 | Human User Identification and Authentication |
| NERC CIP | CIP-004-6 | Personnel and Training |

## Notes

- All three primary lists (`users`, `access_policies`, `access_profiles`) default to `[]`; providing none makes this role a no-op.
- `compliance.require_background_check: true` only sets the policy flag in xDome; it does not perform background checks.
- User `expiration_date` is enforced by xDome automatically; the role does not need to run again to expire accounts.
- JIT access policies require the xDome Secure Remote Access module to be licensed.

## License

MIT

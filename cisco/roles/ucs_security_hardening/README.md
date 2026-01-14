# ucs_security_hardening

Security hardening role for Cisco UCS with DoD STIG and NIST 800-53 compliance.

## Description

This role implements comprehensive security hardening for Cisco UCS infrastructure following DoD STIG requirements and NIST 800-53 security controls. It is designed for fourth estate organizations requiring high security standards.

## Features

- **STIG Compliance**: Category I, II, and III findings remediation
- **NIST 800-53 Controls**: AC, IA, AU, SC, CM, SI, PE families
- **Authentication**: LDAP, RADIUS, TACACS+, certificate-based
- **Audit Logging**: Comprehensive logging with remote syslog
- **Cryptographic Controls**: Strong TLS/SSL, cipher suites
- **Network Security**: VLAN isolation, HTTP to HTTPS redirect
- **Access Control**: RBAC, session management, account lockout
- **Compliance Reporting**: Automated compliance verification

## Requirements

- Ansible >= 2.9
- Cisco UCS Python SDK
- Cisco UCS Ansible collection
- Administrative access to UCS Manager

## Role Variables

### Connection Variables
- `ucs_hostname`: UCS Manager hostname/IP
- `ucs_username`: Administrative username
- `ucs_password`: Administrative password

### Feature Toggles
- `stig_cat1_enabled`: Apply Category I findings (default: true)
- `stig_cat2_enabled`: Apply Category II findings (default: true)
- `stig_cat3_enabled`: Apply Category III findings (default: true)
- `ac_enforce_rbac`: Enforce RBAC (default: true)
- `ia_enable_strong_auth`: Enable strong authentication (default: true)
- `au_enable_comprehensive_logging`: Enable full logging (default: true)
- `sc_enforce_strong_crypto`: Enforce strong cryptography (default: true)

### Security Settings
- `ia_password_min_length`: Minimum password length (default: 15)
- `ia_password_max_age_days`: Password expiration (default: 60)
- `ac_session_timeout_minutes`: Session timeout (default: 15)
- `ac_max_failed_login_attempts`: Login attempts before lockout (default: 3)

See `defaults/main.yml` for complete variable documentation.

## Dependencies

None

## Example Playbook

```yaml
---
- name: Harden UCS Security
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    stig_cat1_enabled: true
    dod_banner_enabled: true

  roles:
    - role: ucs_security_hardening
```

## STIG Controls

### Category I (High Severity)
- V-230500: Default admin account management
- V-230502: Password length requirements
- V-230503: Password complexity
- V-230505: Password expiration
- V-230507: Password history
- V-230510: Disable anonymous access
- V-230515: Session timeout
- V-230520: TLS enforcement

### Category II (Medium Severity)
- V-230525: Account lockout threshold
- V-230527: Lockout duration
- V-230530: Audit logging
- V-230532: Remote syslog
- V-230535: NTP synchronization
- V-230540: HTTP to HTTPS redirect
- V-230545: SNMPv3

### Category III (Low Severity)
- V-230560: System description
- V-230562: Contact information
- V-230565: Timezone configuration
- V-230570: Configuration backup
- V-230575: Documentation

## NIST 800-53 Controls

- **AC**: Access Control
- **IA**: Identification and Authentication
- **AU**: Audit and Accountability
- **SC**: System and Communications Protection
- **CM**: Configuration Management
- **SI**: System and Information Integrity
- **PE**: Physical and Environmental Protection

## Compliance Verification

The role generates comprehensive compliance reports in the artifacts directory:
- `compliance_report.txt`: Overall compliance status
- `stig_cat[1-3]_remediation.txt`: STIG remediation details
- `access_control.json`: AC family controls
- `authentication.json`: IA family controls
- `audit_logging.json`: AU family controls
- And more...

## Security Considerations

- Always use Ansible Vault for credentials
- Review all configurations before setting `apply_changes: true`
- Test in non-production environment first
- Maintain backup before applying changes
- Document any deviations from baseline

## License

MIT

## Author Information

Created for Fourth Estate production security deployments.

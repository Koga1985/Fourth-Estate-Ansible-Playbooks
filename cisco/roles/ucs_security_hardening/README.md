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
- `cryptography.json`: SC family controls
- `network_security.json`: Network hardening status
- `session_management.json`: Session control settings
- `password_policy.json`: Password policy enforcement

## Usage

### Dry Run (Compliance Check Only)
```bash
ansible-playbook playbooks/security_hardening.yml
```

### Apply All Security Controls
```bash
ansible-playbook playbooks/security_hardening.yml -e "apply_changes=true"
```

### Apply Specific STIG Categories
```bash
# Category I only (high severity)
ansible-playbook playbooks/security_hardening.yml \
  -e "apply_changes=true" \
  -e "stig_cat1_enabled=true" \
  -e "stig_cat2_enabled=false" \
  -e "stig_cat3_enabled=false"
```

### Custom Password Policy
```bash
ansible-playbook playbooks/security_hardening.yml \
  -e "apply_changes=true" \
  -e "ia_password_min_length=20" \
  -e "ia_password_max_age_days=45"
```

## Security Architecture

### Fourth Estate Security Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    Security Framework                        │
│  DoD STIG + NIST 800-53 + NIST 800-171 + FISMA              │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   ┌────▼────┐          ┌────▼────┐          ┌────▼────┐
   │ Access  │          │  Auth   │          │  Audit  │
   │ Control │          │  (IA)   │          │  (AU)   │
   │  (AC)   │          │         │          │         │
   └─────────┘          └─────────┘          └─────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │  UCS Manager      │
                    │  (Hardened)       │
                    └───────────────────┘

STIG Categories: Cat I (8 findings) → Cat II (7 findings) → Cat III (6+ findings)
NIST Controls: 46+ controls across 7 families
```

## Security Controls Detail

### Access Control (AC) Family
- **AC-2**: Account Management
  - User account lifecycle management
  - Role-based access control (RBAC)
  - Least privilege enforcement
  - Account review and auditing

- **AC-7**: Unsuccessful Login Attempts
  - Lockout after 3 failed attempts
  - 15-minute lockout duration
  - Administrator notification

- **AC-11**: Session Lock
  - 15-minute session timeout
  - Automatic logout on inactivity
  - Session termination controls

- **AC-17**: Remote Access
  - Encrypted remote access only
  - Multi-factor authentication support
  - Remote session monitoring

### Identification & Authentication (IA) Family
- **IA-2**: User Identification
  - Unique user identifiers
  - No shared accounts
  - Multi-factor authentication support

- **IA-5**: Authenticator Management
  - Password length: 15 characters minimum
  - Password complexity: Upper, lower, numeric, special
  - Password expiration: 60 days
  - Password history: 5 passwords
  - No default passwords

- **IA-6**: Authenticator Feedback
  - Password masking
  - No clear-text display
  - Secure password transmission

### Audit & Accountability (AU) Family
- **AU-2**: Audit Events
  - Login/logout events
  - Configuration changes
  - Privileged operations
  - Security violations

- **AU-3**: Audit Record Content
  - Timestamp
  - User identification
  - Event type
  - Success/failure
  - Source/destination

- **AU-4**: Audit Storage Capacity
  - Remote syslog configured
  - 365-day retention
  - Storage monitoring
  - Alert on capacity

- **AU-9**: Protection of Audit Information
  - Audit log encryption
  - Access control on logs
  - Integrity protection

### System & Communications Protection (SC) Family
- **SC-8**: Transmission Confidentiality
  - TLS 1.2 minimum
  - Strong cipher suites only
  - No SSLv2/SSLv3

- **SC-13**: Cryptographic Protection
  - FIPS 140-2 compliant algorithms
  - Strong key management
  - Certificate-based authentication

- **SC-23**: Session Authenticity
  - Session token protection
  - Session hijacking prevention
  - Secure session management

## Troubleshooting

### Authentication Issues After Hardening
- **Check LDAP/RADIUS**: Verify external auth server connectivity
- **Local Accounts**: Ensure at least one local admin account
- **Password Policy**: Verify passwords meet new requirements
- **Account Lockout**: Check if account is locked (3 failed attempts)
- **Session Timeout**: Adjust timeout if too aggressive

### Compliance Check Failures
- **Review Prerequisites**: Ensure infrastructure role completed first
- **Check Dependencies**: Verify all required policies exist
- **Review Logs**: Check UCS Manager audit logs
- **Validate Syntax**: Review configuration syntax
- **Permissions**: Verify admin account has full privileges

### STIG Remediation Failures
- **Category I Issues**: Critical, must be resolved
- **Firmware Version**: Some STIGs require specific firmware
- **Hardware Support**: Verify hardware supports security features
- **Policy Conflicts**: Check for conflicting policies
- **Consult STIG Guide**: Review official STIG documentation

### Audit Logging Not Working
- **Syslog Server**: Verify syslog server is reachable
- **Network Connectivity**: Check firewall rules (UDP 514)
- **Syslog Format**: Verify syslog server accepts Cisco format
- **Test Logging**: Generate test event, verify reception
- **Time Sync**: Ensure NTP is configured correctly

## Tags

Available tags for selective execution:
- `stig`: All STIG remediations
- `stig_cat1`: Category I findings only
- `stig_cat2`: Category II findings only
- `stig_cat3`: Category III findings only
- `nist`: All NIST controls
- `access_control`: AC family controls only
- `authentication`: IA family controls only
- `audit_logging`: AU family controls only
- `cryptography`: SC family cryptographic controls only
- `network_security`: Network hardening only
- `compliance_check`: Run compliance verification only

**Examples:**
```bash
# Apply only Category I STIG findings
ansible-playbook playbooks/security_hardening.yml --tags stig_cat1

# Apply access control and authentication only
ansible-playbook playbooks/security_hardening.yml --tags "access_control,authentication"

# Run compliance check without applying changes
ansible-playbook playbooks/security_hardening.yml --tags compliance_check
```

## Artifacts Generated

The role creates the following artifacts in `ucs_artifacts_dir`:
- `security_hardening_plan.json`: Complete hardening plan
- `compliance_report.txt`: Overall compliance status
- `stig_cat1_remediation.txt`: Category I findings remediation
- `stig_cat2_remediation.txt`: Category II findings remediation
- `stig_cat3_remediation.txt`: Category III findings remediation
- `nist_800_53_controls.txt`: NIST 800-53 control implementation
- `nist_800_171_controls.txt`: NIST 800-171 control implementation
- `access_control.json`: AC family implementation details
- `authentication.json`: IA family configuration
- `audit_logging.json`: AU family settings
- `cryptography.json`: Cryptographic control settings
- `network_security.json`: Network hardening status
- `session_management.json`: Session control configuration
- `password_policy.json`: Password policy settings
- `security_report.txt`: Complete security hardening summary
- `compliance_checklist.txt`: Compliance verification checklist

## Best Practices

### Security Hardening Strategy
1. **Phased Approach**: Apply controls incrementally
2. **Test First**: Always test in non-production
3. **Backup First**: Create full backup before applying
4. **Document Exceptions**: Record any deviations with justification
5. **Regular Audits**: Monthly compliance reviews
6. **Update Regularly**: Stay current with STIG updates

### Password Management
1. **Strong Policies**: Enforce 15+ character passwords
2. **Regular Changes**: 60-day maximum age
3. **No Sharing**: Unique accounts for all users
4. **Vault Storage**: Never store passwords in plain text
5. **Service Accounts**: Use dedicated service accounts
6. **Emergency Access**: Maintain break-glass procedures

### Audit Logging
1. **Remote Syslog**: Always configure remote logging
2. **Redundant Servers**: Multiple syslog destinations
3. **Retention**: 365 days minimum (1 year)
4. **Review Regularly**: Weekly log reviews
5. **Alerting**: Real-time alerts for security events
6. **SIEM Integration**: Forward to central SIEM

### Authentication
1. **Multi-Factor**: Enable MFA for privileged access
2. **External Auth**: Use LDAP/RADIUS/TACACS+
3. **Local Backup**: Maintain local admin account
4. **Certificate-Based**: Implement where possible
5. **Account Reviews**: Quarterly access reviews
6. **Least Privilege**: Grant minimum necessary permissions

### Cryptography
1. **TLS 1.2+**: Disable older SSL/TLS versions
2. **Strong Ciphers**: Use FIPS 140-2 compliant ciphers
3. **Certificate Management**: Valid, trusted certificates
4. **Key Rotation**: Regular cryptographic key rotation
5. **Secure Storage**: Protected key storage

## Security Baseline

### DoD Security Technical Implementation Guide (STIG) Compliance

#### Category I (High Severity) - 8 Findings
| Finding ID | Title | Remediation |
|-----------|-------|-------------|
| V-230500 | Default Admin Password | Changed, complex password enforced |
| V-230502 | Password Length | 15 characters minimum |
| V-230503 | Password Complexity | Upper, lower, numeric, special required |
| V-230505 | Password Expiration | 60 days maximum |
| V-230507 | Password History | 5 passwords remembered |
| V-230510 | Anonymous Access | Disabled |
| V-230515 | Session Timeout | 15 minutes maximum |
| V-230520 | TLS Enforcement | TLS 1.2+ only |

#### Category II (Medium Severity) - 7 Findings
| Finding ID | Title | Remediation |
|-----------|-------|-------------|
| V-230525 | Account Lockout | 3 attempts threshold |
| V-230527 | Lockout Duration | 15 minutes minimum |
| V-230530 | Audit Logging | Comprehensive logging enabled |
| V-230532 | Remote Syslog | Configured with redundancy |
| V-230535 | NTP Synchronization | Configured and verified |
| V-230540 | HTTP to HTTPS | Redirect enforced |
| V-230545 | SNMPv3 | SNMPv3 only, v1/v2c disabled |

#### Category III (Low Severity) - 6+ Findings
| Finding ID | Title | Remediation |
|-----------|-------|-------------|
| V-230560 | System Description | Configured |
| V-230562 | Contact Information | Configured |
| V-230565 | Timezone | Configured |
| V-230570 | Configuration Backup | Automated backups enabled |
| V-230575 | Documentation | Maintained and current |

### NIST 800-53 Control Families

| Family | Controls | Implementation |
|--------|----------|----------------|
| AC | 12 controls | Access Control, RBAC, Session Management |
| IA | 8 controls | Authentication, Password Policy, MFA |
| AU | 10 controls | Audit Logging, Remote Syslog, Retention |
| SC | 8 controls | Cryptography, TLS, Secure Protocols |
| CM | 4 controls | Configuration Management, Baseline |
| SI | 3 controls | System Integrity, Flaw Remediation |
| PE | 1 control | Physical Access (DoD banner) |

**Total: 46+ controls implemented**

## Compliance Testing

### Automated Compliance Checks
```bash
# Run comprehensive compliance audit
ansible-playbook playbooks/11_ucs_compliance_audit.yml

# Generate compliance report
cat /tmp/ucs-compliance-audit-*/compliance_audit_report.txt
```

### Manual Verification Steps
1. **Password Policy**: Attempt login with weak password (should fail)
2. **Account Lockout**: Fail login 3 times (should lock account)
3. **Session Timeout**: Leave session idle 15 minutes (should logout)
4. **TLS Version**: Test with TLS 1.0/1.1 (should fail)
5. **Audit Logging**: Make configuration change, verify syslog entry
6. **SNMP**: Test SNMPv2c access (should fail if v3-only configured)

## Security Monitoring

### Continuous Monitoring
- **Daily**: Review security logs for anomalies
- **Weekly**: Check account status and failed logins
- **Monthly**: Run full compliance audit
- **Quarterly**: Review and update security policies
- **Annually**: External security assessment

### Security Metrics
- Failed login attempts per day
- Account lockout frequency
- Session timeout violations
- Configuration changes per month
- Security exception requests
- Compliance score trending

## Security Considerations

- Always use Ansible Vault for credentials
- Review all configurations before setting `apply_changes: true`
- Test in non-production environment first
- Maintain backup before applying changes
- Document any deviations from baseline
- Implement change control procedures
- Regular security training for administrators
- Maintain security incident response plan

## Regulatory Compliance

This role helps meet requirements for:
- **DoD STIG**: Department of Defense Security Technical Implementation Guide
- **NIST 800-53**: Security and Privacy Controls for Information Systems
- **NIST 800-171**: Protecting Controlled Unclassified Information
- **FISMA**: Federal Information Security Management Act
- **FedRAMP**: Federal Risk and Authorization Management Program
- **HIPAA**: Health Insurance Portability and Accountability Act (subset)
- **PCI DSS**: Payment Card Industry Data Security Standard (subset)

## License

MIT

## Author Information

Created for Fourth Estate production security deployments.

# Policy as Code - Deployment Guide

## Fourth Estate Production Deployment

This guide provides step-by-step instructions for deploying Policy as Code to Fourth Estate systems.

---

## Pre-Deployment Checklist

### 1. System Requirements

- [ ] Ansible 2.12.0 or higher installed
- [ ] Python 3.8 or higher
- [ ] Network connectivity to target systems
- [ ] Valid credentials with administrative privileges
- [ ] Change control ticket approved
- [ ] Backup of current system configuration
- [ ] Maintenance window scheduled

### 2. Documentation Requirements

- [ ] NIST 800-53 control mapping reviewed
- [ ] DoD STIG findings documented
- [ ] Security team approval obtained
- [ ] Stakeholder notification sent
- [ ] Rollback plan documented

### 3. Test Environment Validation

- [ ] Policies tested in non-production environment
- [ ] All functional tests passing
- [ ] Compliance artifacts generated successfully
- [ ] No unexpected behavior observed

---

## Deployment Workflow

### Phase 1: Pre-Deployment (T-7 days)

#### Step 1: Clone Repository

```bash
git clone https://github.com/your-org/Ansible-Playbooks-2.0.git
cd Ansible-Playbooks-2.0/policy_as_code
```

#### Step 2: Review Documentation

```bash
# Read framework documentation
cat README.md

# Review individual policy documentation
cat policies/identification_auth/password_policy.yml
cat policies/access_control/session_timeout.yml
cat policies/audit_accountability/audit_logging.yml
cat policies/system_communications/cryptographic_protection.yml
```

#### Step 3: Run Functional Tests

```bash
# Execute full test suite
ansible-playbook tests/test_policies.yml

# Review test results
cat tests/test_reports/<timestamp>/test_summary.json
```

**Expected Result:** All tests should PASS

#### Step 4: Configure Inventory

```bash
# Copy example inventory
cp inventory/example.yml inventory/production.yml

# Edit with your systems
vi inventory/production.yml
```

Example inventory:

```yaml
---
all:
  children:
    cisco_switches:
      hosts:
        switch01.example.mil:
          ansible_host: 192.168.1.10
          ansible_network_os: ios
          ansible_connection: network_cli
        switch02.example.mil:
          ansible_host: 192.168.1.11
          ansible_network_os: ios
          ansible_connection: network_cli
      vars:
        ansible_user: admin
        ansible_password: "{{ vault_cisco_password }}"
        ansible_become: yes
        ansible_become_method: enable

    cisco_ucs:
      hosts:
        ucs01.example.mil:
          ansible_host: 192.168.1.20
          ansible_connection: local
      vars:
        ucs_username: admin
        ucs_password: "{{ vault_ucs_password }}"

  vars:
    # Policy configuration
    policy_artifacts_dir: "/opt/policy-artifacts"
    deployment_environment: "production"

    # Syslog server (AU-3)
    au_syslog_server: "syslog.example.mil"
    au_syslog_port: 514
```

#### Step 5: Encrypt Sensitive Variables

```bash
# Create vault file
ansible-vault create inventory/group_vars/all/vault.yml

# Add passwords
vault_cisco_password: YourSecurePassword
vault_ucs_password: YourSecurePassword
```

---

### Phase 2: Dry-Run Validation (T-3 days)

#### Step 6: Execute Dry-Run

```bash
# Run against all hosts (no changes made)
ansible-playbook site.yml -i inventory/production.yml --ask-vault-pass

# Run against single host for validation
ansible-playbook site.yml -i inventory/production.yml --limit switch01.example.mil --ask-vault-pass

# Run specific control family only
ansible-playbook site.yml -i inventory/production.yml --tags nist_ia --ask-vault-pass
```

**Expected Output:**
```
PLAY RECAP *************************************
switch01.example.mil : ok=45  changed=0  unreachable=0  failed=0  skipped=5  rescued=0  ignored=0
```

**Key Points:**
- `changed=0` confirms no changes were made
- All tasks should show `ok` status
- Review output for any warnings or recommendations

#### Step 7: Review Dry-Run Artifacts

```bash
# List generated artifacts
ls -la /tmp/policy-artifacts/<timestamp>/

# Review compliance summary
cat /tmp/policy-artifacts/<timestamp>/IA-5_summary_switch01.json
cat /tmp/policy-artifacts/<timestamp>/AC-12_summary_switch01.json
cat /tmp/policy-artifacts/<timestamp>/AU-2_AU-12_summary_switch01.json
cat /tmp/policy-artifacts/<timestamp>/SC-8_SC-13_summary_switch01.json

# Verify checksums
sha256sum -c /tmp/policy-artifacts/<timestamp>/*.sha256
```

#### Step 8: Compliance Gap Analysis

Review each artifact to identify current vs. required state:

```bash
# Extract compliance status from all artifacts
for file in /tmp/policy-artifacts/<timestamp>/*_summary_*.json; do
  echo "=== $(basename $file) ==="
  jq '.overall_status' $file
  jq '.compliance_checks' $file
done
```

**Action Items:**
- Document current non-compliant settings
- Identify potential service impact
- Plan for any manual interventions
- Update change control ticket

---

### Phase 3: Production Deployment (T-Day)

#### Step 9: Pre-Deployment Verification

```bash
# Verify network connectivity
ansible all -i inventory/production.yml -m ping --ask-vault-pass

# Verify credentials
ansible all -i inventory/production.yml -m raw -a "show version" --ask-vault-pass

# Create backup of current configuration
ansible-playbook backup_configs.yml -i inventory/production.yml --ask-vault-pass
```

#### Step 10: Execute Phased Deployment

##### Option A: Single Host (Recommended for initial deployment)

```bash
# Deploy to single host first
ansible-playbook site.yml \
  -i inventory/production.yml \
  --limit switch01.example.mil \
  -e "apply_changes=true" \
  --ask-vault-pass
```

**Post-Deployment Validation:**
1. Verify system accessibility
2. Test authentication with new password policy
3. Confirm session timeout behavior
4. Verify audit logs are reaching syslog server
5. Test HTTPS access (HTTP should be disabled)

##### Option B: Rolling Deployment (After single host validation)

```bash
# Deploy to 10% of hosts at a time
ansible-playbook site.yml \
  -i inventory/production.yml \
  -e "apply_changes=true" \
  -e "deployment_serial=10%" \
  --ask-vault-pass

# Or deploy by groups
ansible-playbook site.yml \
  -i inventory/production.yml \
  --limit cisco_switches \
  -e "apply_changes=true" \
  --ask-vault-pass
```

##### Option C: Full Deployment (After successful rolling deployment)

```bash
# Deploy to all hosts
ansible-playbook site.yml \
  -i inventory/production.yml \
  -e "apply_changes=true" \
  --ask-vault-pass
```

#### Step 11: Post-Deployment Verification

For each deployed system:

```bash
# Verify IA-5: Password Policy
ssh admin@switch01.example.mil
show running-config | include password

# Verify AC-12: Session Timeout
show running-config | include exec-timeout

# Verify AU-2: Audit Logging
show running-config | include logging
show logging | include syslog

# Verify SC-8/SC-13: Cryptography
show fips status
show ip ssh
show running-config | include tls-version
```

#### Step 12: Compliance Verification

```bash
# Generate compliance report
ansible-playbook site.yml \
  -i inventory/production.yml \
  -e "apply_changes=false" \
  --tags compliance_check \
  --ask-vault-pass

# Review compliance artifacts
cat /opt/policy-artifacts/<timestamp>/*_summary_*.json

# Verify all controls show COMPLIANT
jq '.overall_status' /opt/policy-artifacts/<timestamp>/*_summary_*.json
```

---

### Phase 4: Post-Deployment (T+7 days)

#### Step 13: Monitor and Validate

**Day 1-3: Initial Monitoring**
- [ ] Monitor authentication failures (account lockouts)
- [ ] Verify session timeouts are working
- [ ] Confirm audit logs are being received
- [ ] Check for any service disruptions

**Day 4-7: Validation**
- [ ] Conduct user acceptance testing
- [ ] Review security team feedback
- [ ] Analyze compliance artifacts
- [ ] Document any issues or exceptions

#### Step 14: Documentation Update

- [ ] Update change control ticket with results
- [ ] Archive compliance artifacts
- [ ] Update system documentation
- [ ] Brief stakeholders on deployment outcome

#### Step 15: Ongoing Compliance

**Monthly:**
- [ ] Re-run compliance checks
- [ ] Review audit logs for policy violations
- [ ] Update passwords per policy
- [ ] Verify NIST control effectiveness

**Quarterly:**
- [ ] Full compliance audit
- [ ] Policy review and updates
- [ ] Security team assessment
- [ ] Management reporting

---

## Rollback Procedures

### Emergency Rollback (Within 1 hour of deployment)

```bash
# Restore from backup
ansible-playbook restore_configs.yml \
  -i inventory/production.yml \
  -e "backup_file=/path/to/backup" \
  --ask-vault-pass
```

### Selective Rollback (Specific policies)

```bash
# Disable specific policy
ansible-playbook site.yml \
  -i inventory/production.yml \
  -e "apply_changes=true" \
  -e "ia_password_min_length=8" \
  --tags nist_ia_5 \
  --ask-vault-pass
```

---

## Troubleshooting

### Issue: Authentication Failures After Password Policy

**Cause:** Users' current passwords don't meet new complexity requirements

**Resolution:**
1. Coordinate with users to reset passwords
2. Use administrative override if necessary
3. Document exceptions in compliance artifact

### Issue: Session Timeouts Too Aggressive

**Cause:** Operational workflows require longer sessions

**Resolution:**
1. Document business justification
2. Request exception from security team
3. Adjust timeout values with approval:
   ```bash
   ansible-playbook site.yml -e "ac_ssh_timeout_minutes=30" --tags nist_ac_12
   ```

### Issue: Audit Logs Not Reaching Syslog Server

**Cause:** Network connectivity or syslog server issues

**Resolution:**
1. Verify network connectivity: `ping syslog.example.mil`
2. Check firewall rules for UDP/514
3. Verify syslog server is accepting logs
4. Re-run audit logging policy

### Issue: FIPS Mode Requires System Reload

**Cause:** FIPS 140-2 mode requires system restart

**Resolution:**
1. Schedule maintenance window
2. Enable FIPS mode
3. Reload system: `reload`
4. Verify FIPS status after reload: `show fips status`

---

## Support and Contacts

### Security Team
- Email: security@example.mil
- Ticket System: https://tickets.example.mil

### Change Control
- Email: changecontrol@example.mil
- Process: https://wiki.example.mil/change-control

### Documentation
- Policy Framework: `policy_as_code/README.md`
- NIST 800-53 Mapping: `policy_as_code/docs/NIST_MAPPING.md`
- STIG Findings: `policy_as_code/docs/STIG_FINDINGS.md`

---

## Appendix A: Control Mapping

| NIST Control | Policy File | STIG Findings | Severity |
|--------------|-------------|---------------|----------|
| IA-5 | `policies/identification_auth/password_policy.yml` | V-230502, V-230503, V-230505, V-230507, V-230509 | Cat I |
| AC-12 | `policies/access_control/session_timeout.yml` | V-230286, V-230287 | Cat II |
| AU-2/AU-12 | `policies/audit_accountability/audit_logging.yml` | V-230315, V-230316, V-230317, V-230318 | Cat II |
| SC-8/SC-13 | `policies/system_communications/cryptographic_protection.yml` | V-230273, V-230274, V-230275, V-230276, V-230277 | Cat I |

---

## Appendix B: Compliance Verification Checklist

After deployment, verify each control:

- [ ] **IA-5: Password Policy**
  - [ ] Minimum 15 characters
  - [ ] Complexity enabled (upper, lower, numeric, special)
  - [ ] Maximum age 60 days
  - [ ] History of 5 passwords
  - [ ] Lockout after 3 attempts

- [ ] **AC-12: Session Timeout**
  - [ ] Console: 10 minutes
  - [ ] VTY (SSH): 15 minutes
  - [ ] Web UI: 15 minutes idle

- [ ] **AU-2/AU-12: Audit Logging**
  - [ ] Logging enabled globally
  - [ ] Remote syslog configured
  - [ ] Informational level or higher
  - [ ] Timestamps with timezone
  - [ ] Security events captured

- [ ] **SC-8/SC-13: Cryptographic Protection**
  - [ ] FIPS 140-2 mode enabled
  - [ ] SSH version 2 only
  - [ ] Telnet disabled
  - [ ] HTTPS enabled, HTTP disabled
  - [ ] TLS 1.2 minimum
  - [ ] Strong cipher suites only

---

**Document Version:** 1.0.0
**Last Updated:** 2026-01-15
**Classification:** UNCLASSIFIED//FOUO

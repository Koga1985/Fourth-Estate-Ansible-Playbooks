# Cisco UCS Playbooks

Production-ready Ansible playbooks for deploying, managing, and maintaining Cisco UCS infrastructure for Fourth Estate organizations.

## Overview

This directory contains 10+ production-ready playbooks covering complete UCS lifecycle management from initial deployment to ongoing maintenance and compliance auditing.

## Complete Playbook Catalog

📘 **For detailed documentation of all playbooks, see [PLAYBOOK_INDEX.md](PLAYBOOK_INDEX.md)**

The PLAYBOOK_INDEX provides:
- Detailed playbook descriptions
- Use cases and scenarios
- Complete usage examples
- Variable documentation
- Best practices and recommendations

## Playbook Categories

### Production Deployment

#### Full Deployment
- **01_ucs_full_deployment.yml** - Complete end-to-end production deployment

#### Phased Deployment (Recommended for large environments)
- **02_ucs_phase1_infrastructure.yml** - Infrastructure deployment
- **03_ucs_phase2_networking.yml** - Networking configuration
- **04_ucs_phase3_security.yml** - Security hardening
- **05_ucs_phase4_monitoring.yml** - Monitoring setup
- **06_ucs_phase5_backup_dr.yml** - Backup and disaster recovery

### Operational Playbooks
- **10_ucs_validation.yml** - System health and validation checks
- **11_ucs_compliance_audit.yml** - Security compliance auditing

### Development/Testing
- **20_ucs_quick_start.yml** - Minimal deployment for dev/test

### Maintenance
- **30_ucs_maintenance.yml** - Routine maintenance and updates

## Quick Start

### New Deployment (Full)

```bash
# Dry run (validation only)
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml

# Production deployment
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml -e "apply_changes=true"
```

### New Deployment (Phased - Recommended)

```bash
# Phase 1: Infrastructure
ansible-playbook cisco/playbooks/02_ucs_phase1_infrastructure.yml -e "apply_changes=true"

# Validate Phase 1
ansible-playbook cisco/playbooks/10_ucs_validation.yml

# Phase 2: Networking
ansible-playbook cisco/playbooks/03_ucs_phase2_networking.yml -e "apply_changes=true"

# Continue with remaining phases...
```

### Health Check

```bash
ansible-playbook cisco/playbooks/10_ucs_validation.yml
```

### Compliance Audit

```bash
ansible-playbook cisco/playbooks/11_ucs_compliance_audit.yml
```

### Maintenance Window

```bash
# Backup and health check
ansible-playbook cisco/playbooks/30_ucs_maintenance.yml -e "apply_changes=true"

# With security policy updates
ansible-playbook cisco/playbooks/30_ucs_maintenance.yml \
  -e "apply_changes=true" \
  -e "update_security_policies=true"
```

## Prerequisites

### 1. Install Ansible and Dependencies

```bash
# Install Ansible
pip install ansible

# Install Cisco UCS collection
ansible-galaxy collection install cisco.ucs

# Install UCS SDK
pip install ucsmsdk
```

### 2. Create Ansible Vault for Credentials

```bash
ansible-vault create group_vars/all/vault.yml
```

Add the following vault variables:

```yaml
---
# UCS Manager Connection
vault_ucs_hostname: "ucs-manager.example.com"
vault_ucs_username: "admin"
vault_ucs_password: "secure_password_here"

# Organization Contact
vault_fourth_estate_contact: "Fourth Estate NOC"
vault_fourth_estate_email: "noc@fourth-estate.example.com"

# Backup Server
vault_backup_server: "backup.example.com"
vault_backup_username: "backup_user"
vault_backup_password: "backup_password"
vault_backup_remote_path: "/backups/ucs/fourth-estate"

# Monitoring
vault_snmp_community: "secure_snmp_community"
vault_monitoring_contact: "Network Operations"
vault_monitoring_email: "noc@example.com"

# DR Contacts
vault_dr_primary_contact: "DR Team Lead"
vault_dr_emergency_phone: "+1-555-0911"
```

### 3. Verify Connectivity

```bash
# Test UCS Manager connectivity
ansible-playbook cisco/playbooks/10_ucs_validation.yml
```

## Common Variables

All playbooks support these common variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `apply_changes` | `false` | Set to `true` to apply changes (dry-run by default) |
| `ucs_hostname` | vault | UCS Manager hostname/IP |
| `ucs_username` | vault | Administrative username |
| `ucs_password` | vault | Administrative password |
| `fourth_estate_org_name` | "FourthEstate" | Organization name |
| `ucs_artifacts_dir` | `/tmp/ucs-*` | Artifacts output directory |

See individual playbook documentation and [PLAYBOOK_INDEX.md](PLAYBOOK_INDEX.md) for playbook-specific variables.

## Tags

All playbooks support selective execution using tags:

### Deployment Tags
- `infrastructure` - Infrastructure deployment tasks
- `networking` - Networking configuration tasks
- `security` - Security hardening tasks
- `compliance` - Compliance-related tasks
- `monitoring` - Monitoring setup tasks
- `backup` - Backup configuration tasks

### Phase Tags
- `phase1`, `phase2`, `phase3`, `phase4`, `phase5` - Specific deployment phases

### Usage Examples

```bash
# Run only security tasks
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml --tags security

# Run infrastructure and networking only
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml --tags "infrastructure,networking"

# Skip backup configuration
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml --skip-tags backup
```

## Deployment Scenarios

### Scenario 1: Greenfield Production Deployment

**Recommended:** Use phased deployment for control and validation

```bash
# Phase 1: Infrastructure
ansible-playbook cisco/playbooks/02_ucs_phase1_infrastructure.yml -e "apply_changes=true"
ansible-playbook cisco/playbooks/10_ucs_validation.yml

# Phase 2: Networking
ansible-playbook cisco/playbooks/03_ucs_phase2_networking.yml -e "apply_changes=true"
ansible-playbook cisco/playbooks/10_ucs_validation.yml

# Phase 3: Security
ansible-playbook cisco/playbooks/04_ucs_phase3_security.yml -e "apply_changes=true"
ansible-playbook cisco/playbooks/11_ucs_compliance_audit.yml

# Phase 4: Monitoring
ansible-playbook cisco/playbooks/05_ucs_phase4_monitoring.yml -e "apply_changes=true"

# Phase 5: Backup/DR
ansible-playbook cisco/playbooks/06_ucs_phase5_backup_dr.yml -e "apply_changes=true"

# Final validation
ansible-playbook cisco/playbooks/10_ucs_validation.yml
ansible-playbook cisco/playbooks/11_ucs_compliance_audit.yml
```

**Alternative:** Use full deployment for faster setup

```bash
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml -e "apply_changes=true"
```

### Scenario 2: Development/Test Environment

```bash
# Quick start (minimal configuration)
ansible-playbook cisco/playbooks/20_ucs_quick_start.yml -e "apply_changes=true"
```

### Scenario 3: Security Hardening Existing System

```bash
# Apply security hardening only
ansible-playbook cisco/playbooks/04_ucs_phase3_security.yml -e "apply_changes=true"

# Audit compliance
ansible-playbook cisco/playbooks/11_ucs_compliance_audit.yml
```

### Scenario 4: Monthly Compliance Audit

```bash
# Run comprehensive compliance audit
ansible-playbook cisco/playbooks/11_ucs_compliance_audit.yml

# Review report
cat /tmp/ucs-compliance-audit-*/compliance_audit_report.txt
```

### Scenario 5: Routine Maintenance Window

```bash
# Pre-maintenance backup and health check
ansible-playbook cisco/playbooks/30_ucs_maintenance.yml -e "apply_changes=true"

# With security policy updates
ansible-playbook cisco/playbooks/30_ucs_maintenance.yml \
  -e "apply_changes=true" \
  -e "update_security_policies=true"
```

## Artifacts

All playbooks generate comprehensive artifacts in the specified directory (default: `/tmp/ucs-*-artifacts/`):

### Deployment Artifacts
- Configuration plans (JSON)
- Deployment reports (TXT)
- Organization structure
- Network topology
- Service profile configurations

### Compliance Artifacts
- STIG remediation reports
- NIST 800-53 control mappings
- Compliance checklists
- Audit findings

### Operational Artifacts
- Health check results
- Fault analysis
- System validation reports
- Backup verification

### Typical Artifacts Structure

```
/tmp/ucs-fourth-estate-artifacts/
├── deployment_metadata.json
├── deployment_report.txt
├── compliance_report.txt
├── stig_cat1_remediation.txt
├── stig_cat2_remediation.txt
├── stig_cat3_remediation.txt
├── nist_800_53_controls.txt
├── health_check_results.json
├── fault_analysis.json
├── backup_verification.txt
└── disaster_recovery_plan.txt
```

## Compliance Frameworks

All playbooks implement comprehensive security controls:

### DoD STIG
- **Category I** (High Severity): 8+ findings
- **Category II** (Medium Severity): 7+ findings
- **Category III** (Low Severity): 6+ findings

### NIST 800-53
- **AC**: Access Control (12 controls)
- **IA**: Identification & Authentication (8 controls)
- **AU**: Audit & Accountability (10 controls)
- **SC**: System & Communications Protection (8 controls)
- **CM**: Configuration Management (4 controls)
- **SI**: System & Information Integrity (3 controls)
- **PE**: Physical & Environmental Protection (1 control)

**Total: 46+ controls implemented**

### Additional Frameworks
- NIST 800-171 (CUI protection)
- FISMA Moderate baseline
- FISMA High baseline

## Best Practices

### 1. Always Dry-Run First
```bash
# Run without apply_changes to validate
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml
```

### 2. Review Artifacts
Check generated reports before production deployment:
```bash
ls -lh /tmp/ucs-*-artifacts/
cat /tmp/ucs-*-artifacts/deployment_report.txt
```

### 3. Use Phased Deployment for Large Environments
Phased deployment provides better control and validation opportunities.

### 4. Regular Health Checks
```bash
# Weekly validation
ansible-playbook cisco/playbooks/10_ucs_validation.yml
```

### 5. Monthly Compliance Audits
```bash
# Monthly compliance review
ansible-playbook cisco/playbooks/11_ucs_compliance_audit.yml
```

### 6. Backup Before Changes
```bash
# Always backup before major changes
ansible-playbook cisco/playbooks/06_ucs_phase5_backup_dr.yml \
  -e "apply_changes=true" \
  -e "backup_trigger_immediate=true"
```

### 7. Test in Lab First
Always test playbooks in a lab environment before production use.

### 8. Use Ansible Vault
Never store credentials in plain text. Always use Ansible Vault.

### 9. Monitor During Deployment
Watch UCS Manager for faults during deployment.

### 10. Document Changes
Maintain change logs and document any deviations from baseline.

## Troubleshooting

### Connection Issues

```bash
# Verify UCS Manager reachability
ping ucs-manager.example.com

# Test with validation playbook
ansible-playbook cisco/playbooks/10_ucs_validation.yml
```

### Playbook Fails

1. **Check prerequisites**: Ensure Ansible, cisco.ucs collection, and ucsmsdk are installed
2. **Verify credentials**: Check vault variables
3. **Review logs**: Check Ansible output for specific errors
4. **Check artifacts**: Review generated artifacts for details
5. **UCS faults**: Check UCS Manager for system faults

### Dry-Run Shows No Changes

This is expected behavior. Set `apply_changes=true` to apply configurations.

### STIG Findings Not Remediated

1. Verify STIG variables are enabled (stig_cat1_enabled, etc.)
2. Check UCS firmware version compatibility
3. Review playbook output for skipped tasks
4. Consult STIG documentation for manual steps

### Compliance Audit Failures

1. Ensure all deployment phases are complete
2. Run validation playbook first
3. Check that security role has been applied
4. Review audit artifacts for specific issues

## Support

For detailed playbook documentation, see:
- **[PLAYBOOK_INDEX.md](PLAYBOOK_INDEX.md)** - Complete playbook catalog

For role documentation, see:
- `../roles/ucs_prod_infrastructure/README.md`
- `../roles/ucs_security_hardening/README.md`
- `../roles/ucs_prod_networking/README.md`
- `../roles/ucs_prod_monitoring/README.md`
- `../roles/ucs_prod_backup_dr/README.md`

For main documentation:
- `../README.md` - Main Cisco automation documentation

## Contributing

When creating new playbooks:

1. Follow existing naming conventions
2. Include comprehensive pre_tasks, tasks, and post_tasks
3. Generate meaningful artifacts
4. Support dry-run mode (apply_changes=false)
5. Add playbook to PLAYBOOK_INDEX.md
6. Test in lab environment
7. Document all variables and tags

## License

MIT

## Author

Created for Fourth Estate production UCS deployments.

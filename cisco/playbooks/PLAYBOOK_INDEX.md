# Cisco UCS Playbook Index

Complete guide to all available playbooks for Fourth Estate UCS deployment.

## Production Deployment Playbooks

### 01_ucs_full_deployment.yml
**Purpose:** Complete end-to-end production deployment
**Use Case:** Greenfield deployments, complete infrastructure setup
**Duration:** 30-60 minutes (varies by configuration)
**Features:**
- All 5 deployment phases in sequence
- Complete infrastructure, networking, security, monitoring, backup
- DoD STIG and NIST 800-53 compliance
- Comprehensive artifact generation

**Usage:**
```bash
# Dry run
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml

# Production deployment
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml -e "apply_changes=true"
```

---

## Phased Deployment Playbooks

Use these for controlled, incremental deployments with validation between phases.

### 02_ucs_phase1_infrastructure.yml
**Purpose:** Deploy base infrastructure
**Includes:**
- UCS Manager configuration
- Organizations and hierarchy
- Service profiles and templates
- Server pools
- Address pools (UUID, MAC, WWN, IQN)
- High availability

**Usage:**
```bash
ansible-playbook cisco/playbooks/02_ucs_phase1_infrastructure.yml -e "apply_changes=true"
```

### 03_ucs_phase2_networking.yml
**Purpose:** Configure networking
**Includes:**
- VLANs (Management, Production, Development, DMZ)
- VSANs for SAN connectivity
- QoS policies
- Network control policies (CDP/LLDP)
- Multicast policies

**Prerequisites:** Phase 1 must be complete
**Usage:**
```bash
ansible-playbook cisco/playbooks/03_ucs_phase2_networking.yml -e "apply_changes=true"
```

### 04_ucs_phase3_security.yml
**Purpose:** Apply security hardening
**Includes:**
- DoD STIG Category I/II/III (21+ findings)
- NIST 800-53 controls (46+ controls)
- Password policies
- Access control and RBAC
- Authentication hardening
- Audit logging
- Cryptographic controls
- DoD banner

**Prerequisites:** Phases 1-2 must be complete
**Usage:**
```bash
ansible-playbook cisco/playbooks/04_ucs_phase3_security.yml -e "apply_changes=true"
```

### 05_ucs_phase4_monitoring.yml
**Purpose:** Configure monitoring
**Includes:**
- SNMP v2c/v3
- SNMP trap destinations
- Call Home
- Health monitoring
- Power/thermal monitoring
- Compliance checklists

**Prerequisites:** Phases 1-3 must be complete
**Usage:**
```bash
ansible-playbook cisco/playbooks/05_ucs_phase4_monitoring.yml -e "apply_changes=true"
```

### 06_ucs_phase5_backup_dr.yml
**Purpose:** Configure backup and disaster recovery
**Includes:**
- Full-state backups
- Configuration backups
- Scheduled backup jobs
- DR procedures documentation
- RTO/RPO targets
- Backup verification scripts

**Prerequisites:** Phases 1-4 must be complete
**Usage:**
```bash
ansible-playbook cisco/playbooks/06_ucs_phase5_backup_dr.yml -e "apply_changes=true"
```

---

## Operational Playbooks

### 10_ucs_validation.yml
**Purpose:** Validate deployment and system health
**Use Case:** Post-deployment validation, routine health checks
**Checks:**
- System connectivity
- Configuration status
- Service profile associations
- System faults (critical, major, minor)
- Hardware health
- Firmware versions
- Network connectivity

**Usage:**
```bash
ansible-playbook cisco/playbooks/10_ucs_validation.yml
```

### 11_ucs_compliance_audit.yml
**Purpose:** Audit compliance with security standards
**Use Case:** Regular compliance audits, security reviews
**Audits:**
- DoD STIG findings
- NIST 800-53 controls
- Password policies
- Session management
- Audit logging
- Cryptographic settings
- Network security
- Access controls

**Frequency:** Monthly recommended
**Usage:**
```bash
ansible-playbook cisco/playbooks/11_ucs_compliance_audit.yml
```

---

## Development/Testing Playbooks

### 20_ucs_quick_start.yml
**Purpose:** Minimal deployment for dev/test
**⚠ WARNING:** NOT for production use
**Includes:**
- Basic infrastructure
- Minimal networking (LAN only, no SAN)
- Essential security (STIG Cat I only)
- Basic monitoring
- NO backup/DR

**Usage:**
```bash
ansible-playbook cisco/playbooks/20_ucs_quick_start.yml -e "apply_changes=true"
```

---

## Maintenance Playbooks

### 30_ucs_maintenance.yml
**Purpose:** Routine maintenance and configuration updates
**Use Case:** Scheduled maintenance windows, configuration updates
**Tasks:**
- Pre-maintenance backup
- Health checks
- Firmware updates (optional)
- Security policy updates (optional)
- Network configuration updates (optional)
- Post-maintenance validation

**Usage:**
```bash
# Backup and health check only
ansible-playbook cisco/playbooks/30_ucs_maintenance.yml -e "apply_changes=true"

# With security policy updates
ansible-playbook cisco/playbooks/30_ucs_maintenance.yml \
  -e "apply_changes=true" \
  -e "update_security_policies=true"

# With firmware updates (requires careful planning)
ansible-playbook cisco/playbooks/30_ucs_maintenance.yml \
  -e "apply_changes=true" \
  -e "update_firmware=true"
```

---

## Playbook Selection Guide

### For New Deployments

**Option 1: Full Deployment (Fastest)**
```bash
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml -e "apply_changes=true"
```

**Option 2: Phased Deployment (Most Control)**
```bash
ansible-playbook cisco/playbooks/02_ucs_phase1_infrastructure.yml -e "apply_changes=true"
# Validate Phase 1
ansible-playbook cisco/playbooks/10_ucs_validation.yml

ansible-playbook cisco/playbooks/03_ucs_phase2_networking.yml -e "apply_changes=true"
# Validate Phase 2
ansible-playbook cisco/playbooks/10_ucs_validation.yml

ansible-playbook cisco/playbooks/04_ucs_phase3_security.yml -e "apply_changes=true"
# Continue with phases 4 and 5...
```

### For Existing Deployments

**Health Check:**
```bash
ansible-playbook cisco/playbooks/10_ucs_validation.yml
```

**Compliance Audit:**
```bash
ansible-playbook cisco/playbooks/11_ucs_compliance_audit.yml
```

**Configuration Updates:**
```bash
ansible-playbook cisco/playbooks/30_ucs_maintenance.yml \
  -e "apply_changes=true" \
  -e "update_security_policies=true"
```

### For Development/Testing

**Quick Start:**
```bash
ansible-playbook cisco/playbooks/20_ucs_quick_start.yml -e "apply_changes=true"
```

---

## Common Parameters

All playbooks support these common parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `apply_changes` | `false` | Set to `true` to apply changes (dry-run by default) |
| `ucs_hostname` | vault | UCS Manager hostname/IP |
| `ucs_username` | vault | Administrative username |
| `ucs_password` | vault | Administrative password |
| `fourth_estate_org_name` | "FourthEstate" | Organization name |
| `ucs_artifacts_dir` | `/tmp/ucs-*` | Artifacts output directory |

---

## Tags

All playbooks support selective execution using tags:

| Tag | Description |
|-----|-------------|
| `infrastructure` | Infrastructure deployment tasks |
| `networking` | Networking configuration tasks |
| `security` | Security hardening tasks |
| `compliance` | Compliance-related tasks |
| `monitoring` | Monitoring setup tasks |
| `backup` | Backup configuration tasks |
| `phase1`, `phase2`, etc. | Specific deployment phases |

**Example:**
```bash
# Run only security tasks
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml --tags security

# Run only infrastructure and networking
ansible-playbook cisco/playbooks/01_ucs_full_deployment.yml --tags infrastructure,networking
```

---

## Artifacts

All playbooks generate artifacts in the specified directory:

- Configuration plans (JSON)
- Deployment reports (TXT)
- Compliance reports (TXT/JSON)
- Health check results (JSON)
- Fault analysis (JSON)
- Deployment metadata

Default location: `/tmp/ucs-fourth-estate-artifacts/`

---

## Best Practices

1. **Always dry-run first:** Run without `apply_changes=true` to validate
2. **Review artifacts:** Check generated reports before production deployment
3. **Use phased deployment:** For large environments, use phases 2-6
4. **Validate between phases:** Run validation playbook after each phase
5. **Regular audits:** Run compliance audit monthly
6. **Maintenance windows:** Use maintenance playbook for updates
7. **Backup before changes:** Always perform backup before major changes
8. **Test in lab:** Test playbooks in lab environment first

---

## Troubleshooting

### Connection Issues
```bash
# Test connectivity
ansible-playbook cisco/playbooks/10_ucs_validation.yml
```

### Configuration Issues
Check artifacts directory for detailed error messages and reports.

### Compliance Issues
```bash
# Run compliance audit for detailed findings
ansible-playbook cisco/playbooks/11_ucs_compliance_audit.yml
```

---

## Support

For issues or questions:
1. Review playbook artifacts for detailed information
2. Check role README files in `cisco/roles/*/README.md`
3. Review main documentation: `cisco/README.md`
4. Check test results: `cisco/TEST_RESULTS.txt`

---

**Document Version:** 1.0
**Last Updated:** 2026-01-14
**Maintained By:** Fourth Estate DevOps Team

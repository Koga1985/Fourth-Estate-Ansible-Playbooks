# ucs_prod_backup_dr

Cisco UCS production backup and disaster recovery role for Fourth Estate deployments.

## Description

This role configures automated backups and disaster recovery procedures for Cisco UCS production infrastructure. It provides full-state backups, configuration backups, scheduled backup jobs, DR documentation, and recovery procedures for fourth estate organizations to ensure business continuity and rapid recovery from disasters.

## Features

- **Full-State Backups**: Complete system state including all configuration and operational data
- **Configuration Backups**: Logical and system configuration backups
- **Scheduled Backups**: Automated daily/weekly backup jobs
- **Immediate Backups**: On-demand backup triggering
- **Multiple Protocols**: SCP, FTP, TFTP, SFTP support
- **Backup Verification**: Automated backup integrity checks
- **DR Documentation**: Disaster recovery procedures and runbooks
- **RTO/RPO Tracking**: Recovery Time Objective and Recovery Point Objective management
- **Backup Retention**: Configurable retention policies
- **Notification**: Backup status alerts and reporting

## Requirements

- Ansible >= 2.9
- Cisco UCS Python SDK (`pip install ucsmsdk`)
- Cisco UCS Ansible collection (`ansible-galaxy collection install cisco.ucs`)
- Administrative access to UCS Manager
- Remote backup server with SCP/FTP/TFTP/SFTP access
- Sufficient storage space for backups (recommend 3x full-state size)
- Network connectivity to backup server

## Role Variables

### Connection Variables (Required)
```yaml
ucs_hostname: "ucs-manager.example.com"
ucs_username: "admin"
ucs_password: "secure_password"
```

### Deployment Control
```yaml
apply_changes: false                    # Set to true to apply changes
ucs_artifacts_dir: "/tmp/ucs-artifacts" # Artifacts output directory
```

### Backup Configuration
```yaml
backup_type: "full-state"               # Backup type
backup_protocol: "scp"                  # Transfer protocol (scp, ftp, tftp, sftp)
backup_server: "backup.example.com"     # Backup server hostname/IP
backup_username: "backup_user"          # Backup server username
backup_password: "secure_password"      # Backup server password
backup_remote_path: "/backups/ucs/fourth-estate"  # Remote path
```

**Backup Types:**
- **full-state**: Complete system backup (all configuration, operational state)
- **config-all**: All configuration (logical + system)
- **config-logical**: Logical configuration only
- **config-system**: System configuration only

**Protocols:**
- **scp**: Secure Copy (recommended, encrypted)
- **sftp**: SSH File Transfer Protocol (encrypted)
- **ftp**: File Transfer Protocol (not recommended, unencrypted)
- **tftp**: Trivial File Transfer Protocol (not recommended, unencrypted)

### Backup Schedule
```yaml
backup_schedule: "daily"                # Schedule (daily, weekly, manual)
backup_retention_days: 30               # Retention period in days
```

**Schedule Options:**
- **daily**: Daily automated backups (recommended)
- **weekly**: Weekly automated backups
- **manual**: Manual backups only (scheduled job disabled)

### Immediate Backup
```yaml
backup_trigger_immediate: false         # Trigger immediate backup
backup_immediate_types:                 # Types to backup immediately
  - "full-state"
  - "config-all"
```

### Disaster Recovery Objectives
```yaml
dr_rto_hours: 4                         # Recovery Time Objective (hours)
dr_rpo_hours: 24                        # Recovery Point Objective (hours)
```

**RTO/RPO Guidelines:**
- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
  - Tier 1/Critical: 4 hours
  - Tier 2/Important: 8 hours
  - Tier 3/Normal: 24 hours
- **RPO (Recovery Point Objective)**: Maximum acceptable data loss
  - Tier 1/Critical: 1-4 hours
  - Tier 2/Important: 8-12 hours
  - Tier 3/Normal: 24 hours

### Contact Information
```yaml
dr_primary_contact: "DR Team Lead"
dr_secondary_contact: "Backup Admin"
dr_emergency_phone: "+1-555-0911"
backup_admin_contact: "backup-admin@example.com"
```

See `defaults/main.yml` for complete variable documentation.

## Dependencies

None

## Example Playbook

### Basic Backup Configuration
```yaml
---
- name: Configure UCS Backup and DR
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    backup_type: "full-state"
    backup_schedule: "daily"
    backup_protocol: "scp"

  roles:
    - role: ucs_prod_backup_dr
```

### Immediate Full Backup
```yaml
---
- name: Trigger Immediate UCS Backup
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    backup_trigger_immediate: true
    backup_immediate_types:
      - "full-state"

  roles:
    - role: ucs_prod_backup_dr
```

### Multiple Backup Types
```yaml
---
- name: Configure Multiple Backup Types
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    backup_schedule: "daily"
    backup_immediate_types:
      - "full-state"          # Complete system backup
      - "config-all"          # All configuration
      - "config-logical"      # Logical config only

  roles:
    - role: ucs_prod_backup_dr
```

### High-Availability DR Configuration
```yaml
---
- name: Configure High-Availability DR
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    backup_schedule: "daily"
    backup_retention_days: 90
    dr_rto_hours: 2               # 2-hour RTO
    dr_rpo_hours: 4               # 4-hour RPO

  roles:
    - role: ucs_prod_backup_dr
```

## Usage

### Dry Run (Validation Only)
```bash
ansible-playbook playbooks/deploy_backup_dr.yml
```

### Apply Changes
```bash
ansible-playbook playbooks/deploy_backup_dr.yml -e "apply_changes=true"
```

### Trigger Immediate Backup
```bash
ansible-playbook playbooks/deploy_backup_dr.yml \
  -e "apply_changes=true" \
  -e "backup_trigger_immediate=true"
```

### Weekly Backup Schedule
```bash
ansible-playbook playbooks/deploy_backup_dr.yml \
  -e "apply_changes=true" \
  -e "backup_schedule=weekly"
```

## Backup Architecture

### Fourth Estate Backup and DR Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     Cisco UCS Manager                       │
│            (Source System - Production Data)                │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Scheduled/Immediate
                              │ Backup Trigger
                              │
                    ┌─────────▼─────────┐
                    │  Backup Process   │
                    │   (Full-State,    │
                    │  Config-All, etc) │
                    └─────────┬─────────┘
                              │
                              │ SCP/SFTP
                              │ (Encrypted)
                              │
┌─────────────────────────────▼─────────────────────────────┐
│              Remote Backup Server                         │
│                                                            │
│  /backups/ucs/fourth-estate/                              │
│    ├── full-state-YYYY-MM-DD-HHMMSS.tar.gz               │
│    ├── config-all-YYYY-MM-DD-HHMMSS.xml                  │
│    └── config-logical-YYYY-MM-DD-HHMMSS.xml              │
│                                                            │
│  Retention: 30 days (configurable)                        │
└───────────────────────────────────────────────────────────┘
                              │
                              │ In case of disaster
                              │
                    ┌─────────▼─────────┐
                    │  DR Recovery      │
                    │  Procedures       │
                    │  RTO: 4 hours     │
                    │  RPO: 24 hours    │
                    └───────────────────┘
```

## Backup Types and Sizes

### Full-State Backup
- **Contents**: Complete system state, all configuration, operational data
- **Size**: 50-500 MB (varies by deployment size)
- **Restore**: Complete system recovery
- **Use Case**: Disaster recovery, system migration
- **Frequency**: Daily recommended

### Config-All Backup
- **Contents**: All configuration (logical + system)
- **Size**: 5-50 MB
- **Restore**: Configuration recovery
- **Use Case**: Configuration rollback, replication
- **Frequency**: After configuration changes

### Config-Logical Backup
- **Contents**: Service profiles, policies, pools
- **Size**: 1-10 MB
- **Restore**: Logical configuration only
- **Use Case**: Quick rollback, testing
- **Frequency**: After logical config changes

### Config-System Backup
- **Contents**: System-level configuration
- **Size**: 1-5 MB
- **Restore**: System configuration only
- **Use Case**: System-level rollback
- **Frequency**: After system changes

## Disaster Recovery Procedures

### Pre-Disaster Preparation
1. Configure automated daily backups
2. Verify backup completion and integrity
3. Test restoration procedures quarterly
4. Document recovery procedures
5. Maintain current contact lists
6. Store backups offsite or in cloud
7. Keep recovery media accessible

### During Disaster
1. Assess damage and data loss extent
2. Contact DR team (primary/secondary contacts)
3. Locate most recent valid backup
4. Prepare replacement hardware if needed
5. Initiate recovery procedures
6. Follow documented runbooks

### Recovery Steps
1. **Verify Backup Integrity**
   - Validate backup file checksums
   - Verify backup is not corrupted
   - Confirm backup version compatibility

2. **Prepare Target System**
   - Install/configure replacement UCS Manager
   - Verify network connectivity
   - Configure initial management access

3. **Restore Backup**
   - Transfer backup to UCS Manager
   - Initiate restore operation
   - Monitor restore progress

4. **Validate Recovery**
   - Verify all service profiles
   - Check server associations
   - Validate network connectivity
   - Run health checks
   - Test critical applications

5. **Post-Recovery**
   - Document recovery actions
   - Update DR documentation
   - Conduct post-mortem analysis
   - Implement improvements

### Recovery Time Estimates
- **Full-State Restore**: 30-60 minutes (RTO: 4 hours)
- **Config-All Restore**: 15-30 minutes
- **Config-Logical Restore**: 10-20 minutes

## Compliance

This role supports backup and DR requirements from:
- **NIST 800-53**: CP-9 (System Backup), CP-10 (System Recovery)
- **DoD STIG**: Backup and recovery requirements
- **NIST 800-171**: Backup controls for CUI
- **FISMA**: Contingency planning requirements

## Security Considerations

### Backup Security
- **Encryption**: Use SCP or SFTP for encrypted transfers
- **Access Control**: Restrict backup server access
- **Credentials**: Store in Ansible Vault, rotate regularly
- **Integrity**: Verify backup checksums
- **Offsite Storage**: Maintain offsite backup copies
- **Data Classification**: Protect backups as production data

### Backup Server Hardening
- Dedicated backup server (isolated from production)
- SSH key-based authentication (preferred over passwords)
- Firewall rules limiting access
- Regular security updates
- Audit logging enabled
- Intrusion detection/prevention

### Data Protection
- Encrypt backups at rest on backup server
- Implement backup retention policies
- Secure deletion of expired backups
- Regular backup restoration tests
- Document backup locations in secure location

## Troubleshooting

### Backup Fails to Complete
- **Check Network Connectivity**: `ping backup_server`
- **Verify Credentials**: Test SSH/FTP login manually
- **Check Disk Space**: Ensure backup server has sufficient space
- **Review UCS Faults**: Check UCS Manager for backup-related faults
- **Protocol Issues**: Try alternative protocol (SCP vs FTP)
- **Firewall Rules**: Verify required ports are open

### Backup File Corruption
- **Verify Transfer**: Check backup file size matches expected
- **MD5 Checksum**: Validate backup integrity
- **Network Issues**: Poor network may cause corruption
- **Retry Backup**: Trigger new backup immediately
- **Multiple Copies**: Maintain redundant backups

### Restoration Failures
- **Version Mismatch**: Ensure backup version matches target UCS version
- **Incomplete Backup**: Verify backup completed successfully
- **Target Preparation**: Ensure target system is properly initialized
- **Network Issues**: Verify network connectivity during restore
- **Consult TAC**: Contact Cisco TAC for critical recovery issues

### Schedule Not Running
- **Verify Policy**: Check backup policy configuration in UCS Manager
- **Check Scheduler**: Verify UCS Manager scheduler is enabled
- **Review Logs**: Check UCS Manager logs for backup job execution
- **Manual Trigger**: Test with immediate backup
- **Time Sync**: Ensure NTP is configured correctly

## Best Practices

### Backup Strategy
1. **3-2-1 Rule**: 3 copies, 2 different media, 1 offsite
2. **Test Restores**: Quarterly restoration tests
3. **Verify Integrity**: Automated backup verification
4. **Document Procedures**: Maintain recovery runbooks
5. **Monitor Backups**: Alert on backup failures
6. **Retention Policy**: Balance storage cost vs recovery needs

### Operational Practices
1. **Pre-Change Backups**: Always backup before major changes
2. **Post-Change Verification**: Verify backup after configuration changes
3. **Regular Schedule**: Daily backups for production systems
4. **Offsite Storage**: Store backups in separate physical location
5. **Encryption**: Always use encrypted protocols (SCP/SFTP)
6. **Access Control**: Limit backup server access to authorized personnel

### DR Testing
1. **Annual Full DR Test**: Complete disaster recovery exercise
2. **Quarterly Restore Test**: Partial restoration verification
3. **Monthly Backup Validation**: Verify backup completion and integrity
4. **Document Results**: Record all test results and issues
5. **Update Procedures**: Improve procedures based on test findings
6. **Train Personnel**: Ensure DR team is trained on procedures

## Artifacts Generated

The role creates the following artifacts in `ucs_artifacts_dir`:
- `backup_plan.json`: Planned backup configuration
- `backup_schedule.txt`: Backup schedule details
- `dr_procedures.txt`: Disaster recovery runbook
- `backup_verification.txt`: Backup integrity verification results
- `rto_rpo_targets.txt`: Recovery objectives documentation
- `backup_report.txt`: Complete deployment report
- `recovery_procedures.md`: Step-by-step recovery guide

## Tags

Available tags for selective execution:
- `backup_config`: Configure backup policies only
- `immediate_backup`: Trigger immediate backup only
- `dr_docs`: Generate DR documentation only
- `verification`: Run backup verification only

**Example:**
```bash
ansible-playbook playbooks/deploy_backup_dr.yml --tags immediate_backup
```

## Monitoring Backup Jobs

### Verify Backup Completion
```bash
# Check UCS Manager backup status
ansible-playbook playbooks/verify_backup.yml

# View backup files on remote server
ssh backup_user@backup_server "ls -lh /backups/ucs/fourth-estate/"
```

### Backup Alerting
- Configure SNMP traps for backup failures
- Set up email notifications for backup completion
- Monitor backup job logs in UCS Manager
- Alert on backup file size anomalies

## Storage Requirements

### Estimate Storage Needs
```
Daily backups × Retention days × Backup size = Total storage

Example:
- Full-state backup: 200 MB
- Daily backups
- 30-day retention
- Total: 200 MB × 30 = 6 GB

Recommendation: Provision 3x calculated storage for growth
Example total: 6 GB × 3 = 18 GB
```

### Storage Best Practices
- Monitor backup server disk space (alert at 80%)
- Implement automated retention cleanup
- Archive old backups to long-term storage
- Use compression to reduce storage requirements
- Plan for backup growth (10-20% annually)

## License

MIT

## Author Information

Created for Fourth Estate production backup and disaster recovery deployments.

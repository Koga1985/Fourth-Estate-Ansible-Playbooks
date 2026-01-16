# Tenable Security Center

This directory contains **8 Ansible roles** for automating **Tenable Security Center** (formerly SecurityCenter) including installation, scan configuration, vulnerability management, compliance checks, and reporting automation.

## 📋 Roles

### Installation & Configuration (2 roles)
- **tenable_security_center_install** - Security Center installation and setup
- **tenable_security_center_config** - System configuration and licensing

### Scanning Infrastructure (3 roles)
- **tenable_scan_zones** - Scan zone configuration
- **tenable_scan_policies** - Scan policy management
- **tenable_scan_schedules** - Automated scan scheduling

### Vulnerability & Compliance (2 roles)
- **tenable_vulnerability_management** - Vulnerability tracking and remediation
- **tenable_compliance_checks** - NIST 800-53, STIG, CIS compliance

### Reporting (1 role)
- **tenable_reporting** - Automated report generation and distribution

## 🚀 Quick Start

```bash
# Install Security Center
ansible-playbook playbooks/tenable_install.yml \
  -e "tenable_version=5.23.0" \
  -e "tenable_license_file=license.key"

# Configure scan policies
ansible-playbook playbooks/tenable_scan_config.yml \
  -e "scan_zone=corporate-network" \
  -e "scan_frequency=weekly"
```

## ⚙️ Configuration

### Security Center Connection

```yaml
# Tenable Security Center connection
tenable_host: "sc.example.com"
tenable_port: 443
tenable_username: "admin"
tenable_password: "{{ vault_tenable_password }}"
tenable_access_key: "{{ vault_tenable_access_key }}"
tenable_secret_key: "{{ vault_tenable_secret_key }}"
```

### Installation Configuration

```yaml
# Security Center installation
tenable_version: "5.23.0"
tenable_install_dir: "/opt/sc"
tenable_data_dir: "/opt/sc/data"
tenable_license_file: "{{ vault_tenable_license }}"

# Database settings
tenable_db_type: "postgresql"  # or mysql
tenable_db_host: "localhost"
tenable_db_port: 5432
tenable_db_name: "securitycenter"
```

### Scan Zone Configuration

```yaml
# Scan zones (network segments)
scan_zones:
  - name: "corporate-network"
    description: "Corporate internal network"
    ip_ranges:
      - "10.0.0.0/8"
      - "172.16.0.0/12"
      - "192.168.0.0/16"
    scanners:
      - "scanner01"
      - "scanner02"

  - name: "dmz"
    description: "DMZ network segment"
    ip_ranges:
      - "203.0.113.0/24"
    scanners:
      - "scanner03"
```

### Scan Policy Configuration

```yaml
# Scan policies
scan_policies:
  - name: "Full Network Scan"
    description: "Comprehensive vulnerability scan"
    template: "advanced"
    plugin_family:
      - "Port scanners"
      - "Service detection"
      - "General"
      - "Web Servers"
      - "Databases"
    safe_checks: true
    optimize: true

  - name: "Authenticated Scan"
    description: "Credentialed vulnerability scan"
    template: "advanced"
    credentials:
      ssh:
        username: "scanner"
        password: "{{ vault_scanner_ssh_password }}"
      windows:
        username: "scanner"
        password: "{{ vault_scanner_windows_password }}"
        domain: "EXAMPLE"

  - name: "Web Application Scan"
    description: "OWASP Top 10 vulnerability scan"
    template: "web_app"
    plugins:
      - "CGI abuses"
      - "Web Servers"
      - "CGI abuses : XSS"
      - "Web application abuses"
```

### Scan Schedule Configuration

```yaml
# Automated scan schedules
scan_schedules:
  - name: "Weekly Full Scan"
    policy: "Full Network Scan"
    scan_zone: "corporate-network"
    schedule:
      frequency: "weekly"
      day_of_week: "sunday"
      time: "02:00"
    email_notification:
      - "security-team@example.com"

  - name: "Daily Web Scan"
    policy: "Web Application Scan"
    scan_zone: "dmz"
    schedule:
      frequency: "daily"
      time: "03:00"

  - name: "Monthly Compliance Scan"
    policy: "NIST 800-53 Audit"
    scan_zone: "all-zones"
    schedule:
      frequency: "monthly"
      day_of_month: 1
      time: "00:00"
```

### Compliance Check Configuration

```yaml
# Compliance checks
compliance_policies:
  - name: "NIST 800-53 Rev 5"
    framework: "nist_800_53_r5"
    audit_files:
      - "NIST_800-53_Rev5_Level_1_Windows_Server_2019.audit"
      - "NIST_800-53_Rev5_Level_1_Linux.audit"

  - name: "DISA STIG"
    framework: "disa_stig"
    audit_files:
      - "RHEL_8_STIG.audit"
      - "Windows_Server_2019_STIG.audit"

  - name: "CIS Benchmarks"
    framework: "cis"
    audit_files:
      - "CIS_RedHat_Enterprise_Linux_8_v2.0.0.audit"
      - "CIS_Microsoft_Windows_Server_2019_v1.3.0.audit"
```

### Vulnerability Management

```yaml
# Vulnerability management
vulnerability_settings:
  risk_scoring: "cvss_v3"
  severity_thresholds:
    critical: 9.0
    high: 7.0
    medium: 4.0
    low: 0.1

  # Auto-accept risk for specific plugins
  accepted_risks:
    - plugin_id: "19506"  # Nessus scan information
      reason: "Informational only"
    - plugin_id: "11219"  # Nessus SYN scanner
      reason: "False positive"

  # Recast severity
  recast_rules:
    - plugin_id: "98765"
      from_severity: "high"
      to_severity: "medium"
      reason: "Mitigated by compensating controls"
```

### Reporting Configuration

```yaml
# Automated reports
reports:
  - name: "Executive Summary"
    type: "executive_summary"
    format: "pdf"
    schedule: "weekly"
    recipients:
      - "ciso@example.com"
      - "security-director@example.com"

  - name: "Vulnerability Details"
    type: "vulnerability"
    format: "csv"
    filters:
      severity: ["critical", "high"]
      exploitability: "exploitable"
    schedule: "daily"
    recipients:
      - "security-team@example.com"

  - name: "Compliance Posture"
    type: "compliance"
    format: "pdf"
    frameworks:
      - "nist_800_53_r5"
      - "disa_stig"
    schedule: "monthly"
    recipients:
      - "compliance-team@example.com"

  - name: "Trend Analysis"
    type: "trend"
    format: "pdf"
    timeframe: "90_days"
    metrics:
      - "vulnerability_count"
      - "risk_score"
      - "patch_compliance"
    schedule: "monthly"
```

## 📖 Common Use Cases

### Use Case 1: Deploy Security Center

```yaml
---
# playbooks/tenable_deploy.yml
- name: Deploy Tenable Security Center
  hosts: security_center
  become: true

  roles:
    - role: tenable_security_center_install
      vars:
        tenable_version: "5.23.0"
        tenable_license_file: "{{ vault_license }}"

    - role: tenable_security_center_config
      vars:
        tenable_admin_email: "admin@example.com"
        tenable_smtp_server: "smtp.example.com"
```

### Use Case 2: Configure Vulnerability Scanning

```bash
ansible-playbook playbooks/tenable_scan_setup.yml \
  -e "scan_zone=production" \
  -e "scan_policy=authenticated" \
  -e "schedule=weekly"
```

### Use Case 3: Generate Compliance Report

```bash
ansible-playbook playbooks/tenable_compliance_report.yml \
  -e "framework=nist_800_53" \
  -e "report_format=pdf" \
  -e "email=compliance@example.com"
```

### Use Case 4: Automated Remediation Workflow

```bash
ansible-playbook playbooks/tenable_remediation.yml \
  -e "severity=critical" \
  -e "create_tickets=true" \
  -e "servicenow_instance=prod"
```

## 🛡️ Security Best Practices

1. **Secure Access** - Use TLS/SSL for all communications
2. **API Key Rotation** - Rotate API keys regularly
3. **Least Privilege** - Grant minimal permissions to scan accounts
4. **Credential Management** - Use Ansible Vault for scan credentials
5. **Network Segmentation** - Deploy scanners in appropriate network zones
6. **Safe Checks** - Enable safe checks to prevent service disruption
7. **Scan Throttling** - Configure scan speed to avoid network impact
8. **Audit Logging** - Enable comprehensive audit logs
9. **Regular Updates** - Keep Security Center and plugins updated
10. **Data Retention** - Configure appropriate data retention policies

## 🔧 Troubleshooting

### Issue: Scan Failing to Start

**Symptoms:** Scans remain in "pending" status

**Resolution:**
```bash
# Check scanner connectivity
/opt/sc/support/bin/sc_status.sh

# Verify scan zone configuration
curl -k -X GET https://sc.example.com/rest/scanZone \
  -H "X-SecurityCenter: $TOKEN"

# Check scanner logs
tail -f /opt/sc/logs/scanner.log
```

### Issue: False Positives

**Symptoms:** Vulnerabilities reported incorrectly

**Resolution:**
- Enable "safe checks" in scan policy
- Use authenticated scanning with credentials
- Recast severity or accept risk for known false positives
- Update to latest plugin feed

### Issue: Performance Issues

**Symptoms:** Scans running slowly or timing out

**Resolution:**
```bash
# Optimize scan policy
- Disable unnecessary plugin families
- Enable "Optimize scan" option
- Reduce scan parallelism
- Increase scan timeout values

# Add more scanners
- Deploy additional Nessus scanners
- Distribute scans across multiple scanners
```

## 📚 Additional Resources

- [Tenable Security Center Documentation](https://docs.tenable.com/security-center/)
- [Nessus Plugin Documentation](https://www.tenable.com/plugins/)
- [Tenable API Documentation](https://docs.tenable.com/security-center/api/index.html)
- [NIST National Vulnerability Database](https://nvd.nist.gov/)
- [CVE Details](https://www.cvedetails.com/)
- [Tenable Community](https://community.tenable.com/)

## 🤝 Contributing

When contributing to Tenable automation:
- Test scan policies in non-production first
- Document custom audit files
- Include sample reports
- Validate API credentials
- Test notification workflows
- Include rollback procedures

---

**Last Updated:** 2026-01-16
**Maintained By:** Fourth Estate Infrastructure Team
**Tenable Versions Supported:** Security Center 5.20+, Nessus 10.x+

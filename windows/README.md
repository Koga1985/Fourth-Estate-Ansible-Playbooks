# Windows Server Automation

This directory contains **20+ Ansible roles** for automating **Microsoft Windows Server** infrastructure with emphasis on security hardening (DoD STIG), Active Directory, Group Policy, and Fourth Estate requirements.

## Overview

Comprehensive Windows Server automation covering STIG hardening, Active Directory domain services, DHCP/DNS, Group Policy management, WSUS patch management, IIS web server, firewall configuration, backup automation, and user lifecycle management.

## 📋 Role Categories

### Security & Compliance (3 roles)
- **win_stig_hardening** - DoD STIG compliance automation for Windows Server
- **win_firewall** - Windows Firewall advanced configuration
- **win_updates** - Windows Update and patch management

### Active Directory (3 roles)
- **win_active_directory** - AD DS installation, domain/forest configuration
- **win_group_policy** - GPO creation, linking, and enforcement
- **win_user_management** - User/group lifecycle automation

### Infrastructure Services (4 roles)
- **win_dhcp_dns** - DHCP and DNS server configuration
- **win_wsus** - Windows Server Update Services deployment
- **win_backup** - Windows Server Backup automation
- **win_iis** - IIS web server and application pool management

## 🚀 Quick Start

### Prerequisites

- Ansible 2.12.0+ with WinRM support
- `ansible.windows` collection (version 1.11.0+)
- `community.windows` collection (version 1.11.0+)
- PowerShell 5.1+ on target Windows servers
- WinRM configured on Windows targets

### Installation

```bash
# Install required collections
ansible-galaxy collection install ansible.windows
ansible-galaxy collection install community.windows

# Install Python WinRM library
pip install pywinrm
```

### Windows Target Configuration

**Enable WinRM on Windows Server:**
```powershell
# Run on Windows Server (as Administrator)
Enable-PSRemoting -Force
Set-Item WSMan:\localhost\Service\Auth\Basic -Value $true
Set-Item WSMan:\localhost\Service\AllowUnencrypted -Value $true  # Dev only!

# For production, use HTTPS/Kerberos
New-SelfSignedCertificate -DnsName "server.example.com" -CertStoreLocation Cert:\LocalMachine\My
$cert = Get-ChildItem Cert:\LocalMachine\My | Where-Object {$_.Subject -like "*server.example.com*"}
New-Item -Path WSMan:\localhost\Listener -Transport HTTPS -Address * -CertificateThumbPrint $cert.Thumbprint -Force
```

### Ansible Inventory Configuration

```ini
# inventory/windows.ini
[windows_servers]
win-dc-01.example.com
win-file-01.example.com
win-web-01.example.com

[windows_servers:vars]
ansible_user=administrator
ansible_password={{ vault_win_admin_password }}
ansible_connection=winrm
ansible_winrm_transport=ntlm  # or kerberos for domain-joined
ansible_winrm_server_cert_validation=ignore  # Use 'validate' in production
ansible_port=5986  # HTTPS WinRM (5985 for HTTP)
```

## 📖 Common Use Cases

### Use Case 1: Apply Windows Server STIG Hardening

```yaml
---
# playbooks/windows_stig_hardening.yml
- name: Apply DoD STIG to Windows Servers
  hosts: windows_servers
  gather_facts: true

  roles:
    - role: win_stig_hardening
      vars:
        stig_profile: "high"  # low, moderate, high
        stig_cat1_enabled: true
        stig_cat2_enabled: true
        stig_cat3_enabled: false
```

```bash
ansible-playbook playbooks/windows_stig_hardening.yml \
  -i inventory/windows.ini \
  --ask-vault-pass
```

### Use Case 2: Deploy Active Directory Domain Controller

```bash
ansible-playbook playbooks/windows_ad_deploy.yml \
  -i inventory/windows.ini \
  -e "domain_name=fourth-estate.local" \
  -e "domain_netbios_name=FOURTHESTATE" \
  -e "forest_mode=WinThreshold" \
  --ask-vault-pass
```

### Use Case 3: Configure DHCP and DNS Services

```bash
ansible-playbook playbooks/windows_dhcp_dns.yml \
  -i inventory/windows.ini \
  -e "dhcp_scope_name=Servers" \
  -e "dhcp_scope_start=10.0.1.10" \
  -e "dhcp_scope_end=10.0.1.250" \
  -e "dns_forwarders=8.8.8.8,8.8.4.4"
```

### Use Case 4: Deploy IIS Web Server

```bash
ansible-playbook playbooks/windows_iis_deploy.yml \
  -i inventory/windows.ini \
  -e "iis_site_name=Fourth Estate Portal" \
  -e "iis_site_port=443" \
  -e "iis_site_path=C:\\inetpub\\wwwroot"
```

### Use Case 5: Configure Windows Server Backup

```bash
ansible-playbook playbooks/windows_backup_config.yml \
  -i inventory/windows.ini \
  -e "backup_target=E:\\" \
  -e "backup_schedule=daily" \
  -e "backup_time=02:00"
```

## ⚙️ Configuration Variables

### STIG Hardening Configuration

```yaml
# Windows Server STIG
win_stig_profile: "moderate"  # low, moderate, high
win_stig_cat1_enabled: true
win_stig_cat2_enabled: true
win_stig_cat3_enabled: false

# Specific findings to skip (exceptions)
win_stig_exceptions:
  - "V-1072"  # Example: Interactive logon banner
  - "V-1127"  # Example: Specific audit policy

# Audit policy
win_audit_account_logon: true
win_audit_logon_events: true
win_audit_object_access: true
win_audit_privilege_use: true
```

### Active Directory Configuration

```yaml
# Domain configuration
win_ad_domain_name: "fourth-estate.local"
win_ad_netbios_name: "FOURTHESTATE"
win_ad_forest_mode: "WinThreshold"  # Win2012R2, Win2016, WinThreshold
win_ad_domain_mode: "WinThreshold"

# DSRM password (recovery mode)
win_ad_safe_mode_password: "{{ vault_ad_safe_mode_password }}"

# AD site configuration
win_ad_sites:
  - name: "HQ"
    description: "Headquarters Site"
  - name: "DR"
    description: "Disaster Recovery Site"

# Organizational Units
win_ad_ous:
  - name: "Fourth Estate"
    path: "DC=fourth-estate,DC=local"
  - name: "Servers"
    path: "OU=Fourth Estate,DC=fourth-estate,DC=local"
  - name: "Workstations"
    path: "OU=Fourth Estate,DC=fourth-estate,DC=local"
  - name: "Users"
    path: "OU=Fourth Estate,DC=fourth-estate,DC=local"
```

### Group Policy Configuration

```yaml
# GPO settings
win_gpo_name: "Fourth Estate Security Policy"
win_gpo_link_path: "DC=fourth-estate,DC=local"
win_gpo_link_enabled: true

# Password policy
win_gpo_password_history: 24
win_gpo_max_password_age: 60
win_gpo_min_password_age: 1
win_gpo_min_password_length: 15
win_gpo_password_complexity: true
win_gpo_reversible_encryption: false

# Account lockout
win_gpo_lockout_duration: 15
win_gpo_lockout_threshold: 3
win_gpo_lockout_window: 15
```

### DHCP/DNS Configuration

```yaml
# DHCP configuration
win_dhcp_scopes:
  - name: "Servers"
    start_ip: "10.0.1.10"
    end_ip: "10.0.1.250"
    subnet_mask: "255.255.255.0"
    gateway: "10.0.1.1"
    dns_servers:
      - "10.0.1.10"
      - "10.0.1.11"
    lease_duration: "8.00:00:00"  # 8 days

# DNS configuration
win_dns_forwarders:
  - "8.8.8.8"
  - "8.8.4.4"

win_dns_zones:
  - name: "fourth-estate.local"
    type: "primary"
    dynamic_update: "secure"
```

## 🛡️ Security & Compliance

### DoD STIG Findings Coverage

| STIG Category | Total Findings | Automated | Manual | N/A |
|---------------|----------------|-----------|--------|-----|
| **Cat I (High)** | 58 | 45 | 10 | 3 |
| **Cat II (Medium)** | 142 | 115 | 20 | 7 |
| **Cat III (Low)** | 38 | 30 | 5 | 3 |
| **Total** | 238 | 190 | 35 | 13 |

### NIST 800-53 Controls

Implemented controls for Windows Server:
- **AC-2** - Account Management
- **AC-7** - Unsuccessful Logon Attempts
- **AU-2** - Audit Events
- **IA-2** - Identification and Authentication
- **IA-5** - Authenticator Management
- **SC-8** - Transmission Confidentiality
- **SI-2** - Flaw Remediation

### CIS Benchmarks

Windows Server roles implement CIS Benchmark recommendations:
- Level 1 (basic hardening)
- Level 2 (advanced hardening for high-security environments)

## 🔧 Troubleshooting

### Issue: WinRM Connection Failures

**Symptoms:** "Connection timeout" or "Authentication failed"

**Resolution:**
```bash
# Test WinRM from Ansible control node
ansible windows_servers -i inventory/windows.ini -m win_ping

# Check WinRM listener on Windows Server
winrm enumerate winrm/config/Listener

# Enable detailed logging
ansible-playbook playbook.yml -vvv
```

### Issue: PowerShell Execution Policy

**Symptoms:** "Execution of scripts is disabled"

**Resolution:**
```powershell
# On Windows Server
Set-ExecutionPolicy RemoteSigned -Scope LocalMachine -Force
```

### Issue: STIG Compliance Breaks Functionality

**Symptoms:** Applications fail after STIG hardening

**Resolution:**
```yaml
# Add exceptions to STIG configuration
win_stig_exceptions:
  - "V-XXXXX"  # Document why this exception is needed

# Or adjust STIG profile to moderate
win_stig_profile: "moderate"
```

## 📚 Additional Resources

- [Windows Server Documentation](https://docs.microsoft.com/en-us/windows-server/)
- [DoD Windows Server STIG](https://public.cyber.mil/stigs/)
- [Ansible Windows Modules](https://docs.ansible.com/ansible/latest/collections/ansible/windows/)
- [CIS Windows Server Benchmarks](https://www.cisecurity.org/cis-benchmarks/)
- [Active Directory Best Practices](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/)

## 🤝 Contributing

When contributing to Windows automation:
- Test in lab environment first (never production)
- Document required PowerShell modules
- Include rollback procedures for AD/GPO changes
- Test with both local and domain-joined scenarios
- Document STIG/NIST control mappings
- Include WinRM configuration requirements

---

**Last Updated:** 2026-01-15
**Maintained By:** Fourth Estate Infrastructure Team
**Windows Versions Supported:** Windows Server 2016, 2019, 2022

# Compliance Mapping: DISA STIG & NIST 800-53 Rev 5

This document maps every technology platform and Ansible role in this repository to the
applicable **DISA Security Technical Implementation Guide (STIG)** findings and
**NIST SP 800-53 Rev 5** control families.

**Classification:** UNCLASSIFIED
**Frameworks Covered:** DISA STIG, NIST 800-53 Rev 5, NIST 800-171, FedRAMP
**Last Updated:** 2026-03-16

---

## Table of Contents

1. [How to Use This Document](#how-to-use-this-document)
2. [NIST 800-53 Rev 5 — Control Family Mapping](#nist-800-53-rev-5--control-family-mapping)
   - [AC — Access Control](#ac--access-control)
   - [AU — Audit and Accountability](#au--audit-and-accountability)
   - [CA — Assessment, Authorization, and Monitoring](#ca--assessment-authorization-and-monitoring)
   - [CM — Configuration Management](#cm--configuration-management)
   - [CP — Contingency Planning](#cp--contingency-planning)
   - [IA — Identification and Authentication](#ia--identification-and-authentication)
   - [IR — Incident Response](#ir--incident-response)
   - [RA — Risk Assessment](#ra--risk-assessment)
   - [SA — System and Services Acquisition](#sa--system-and-services-acquisition)
   - [SC — System and Communications Protection](#sc--system-and-communications-protection)
   - [SI — System and Information Integrity](#si--system-and-information-integrity)
3. [DISA STIG Mapping — By Platform](#disa-stig-mapping--by-platform)
   - [VMware ESXi STIG V1R1](#vmware-esxi-stig-v1r1)
   - [VMware vSphere VM STIG](#vmware-vsphere-vm-stig)
   - [Kubernetes STIG V1R11](#kubernetes-stig-v1r11)
   - [Red Hat Enterprise Linux 8 STIG V1R14](#red-hat-enterprise-linux-8-stig-v1r14)
   - [Microsoft Windows Server STIG V2R8](#microsoft-windows-server-stig-v2r8)
   - [Cisco IOS/NX-OS Network Infrastructure STIG V2R7](#cisco-iosnx-os-network-infrastructure-stig-v2r7)
   - [Cisco ACI STIG (APIC STIG / Network Infrastructure STIG)](#cisco-aci-stig-apic-stig--network-infrastructure-stig)
   - [Arista EOS Network Device STIG](#arista-eos-network-device-stig)
   - [Palo Alto Networks STIG V2R2](#palo-alto-networks-stig-v2r2)
   - [PostgreSQL STIG V2R1](#postgresql-stig-v2r1)
   - [MySQL/MariaDB STIG V2R2](#mysqlmariadb-stig-v2r2)
   - [Oracle Database STIG V2R4](#oracle-database-stig-v2r4)
   - [Ansible Automation Platform / RHEL Application STIG](#ansible-automation-platform--rhel-application-stig)
   - [OT/ICS Systems STIG](#otics-systems-stig)
4. [Per-Platform Quick Reference](#per-platform-quick-reference)

---

## How to Use This Document

- **Auditors:** Use the NIST control family tables to identify which playbooks provide
  evidence of a given control implementation.
- **Engineers:** Use the Per-Platform Quick Reference table to find the exact role path
  and associated controls before modifying a role.
- **Operators:** Run a role with `--check --diff` to produce dry-run artifacts, then
  reference the control IDs in this document when submitting to your Authorizing Official.
- **Policy as Code:** The `policy_as_code/` directory executes controls as Ansible tasks.
  Each policy file maps directly to the NIST control listed in the corresponding table row.

---

## NIST 800-53 Rev 5 — Control Family Mapping

### AC — Access Control

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| AC-2 | Account Management | `ansible/roles/ans_access_sso_directory` | AAP |
| AC-2 | Account Management | `ansible_tower/roles/ansible_tower_organizations`, `ansible_tower_rbac` | Ansible Tower |
| AC-2 | Account Management | `windows/roles/win_active_directory`, `win_user_management` | Windows Server |
| AC-2 | Account Management | `vmware/tasks/add_vsphere_users.yml`, `enforce_vsphere_rbac.yml` | VMware |
| AC-2 | Account Management | `ansible/tasks/ans_ctrl__orgs_teams.yml`, `ans_ctrl__rbac_baseline.yml` | AAP |
| AC-3 | Access Enforcement | `ansible/tasks/ans_ctrl__rbac_baseline.yml` | AAP |
| AC-3 | Access Enforcement | `ansible_tower/roles/ansible_tower_rbac` | Ansible Tower |
| AC-3 | Access Enforcement | `vmware/tasks/enforce_vsphere_rbac.yml`, `import_vsphere_permissions.yml` | VMware |
| AC-5 | Separation of Duties | `ansible/roles/ans_ctrl_policy_guardrails` | AAP |
| AC-5 | Separation of Duties | `ansible/tasks/ans_ctrl__approvals.yml` | AAP |
| AC-6 | Least Privilege | `ansible/roles/ans_access_sso_directory` (team-scoped RBAC) | AAP |
| AC-6 | Least Privilege | `ansible/tasks/ans_ctrl__rbac_baseline.yml` | AAP |
| AC-6 | Least Privilege | `vmware/tasks/enforce_vsphere_rbac.yml` | VMware |
| AC-12 | Session Termination | `policy_as_code/policies/access_control/session_timeout.yml` | Policy as Code |
| AC-12 | Session Termination | STIG findings V-230286, V-230287 | RHEL 8 |
| AC-17 | Remote Access | `vmware/roles/vsphere_esxi_stig_hardening` (SSH/ESXi shell lockdown) | VMware ESXi |
| AC-17 | Remote Access | `arista/roles/arista_backup_restore` (management plane hardening) | Arista |
| AC-17 | Remote Access | `cisco/roles/aci_security_hardening` (out-of-band management access control) | Cisco ACI |
| AC-18 | Wireless Access Control | `cisco/roles/ise_policy__*` (ISE wireless policy sets) | Cisco ISE |
| AC-19 | Access Control for Mobile | `cisco/roles/ise_byod__workflow`, `ise_posture__*` (ISE MDM/BYOD integration) | Cisco ISE |
| AC-20 | Use of External Systems | `illumio/roles` (micro-segmentation boundary) | Illumio |

---

### AU — Audit and Accountability

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| AU-2 | Event Logging | `ansible/roles/ans_ctrl_backup_and_audit` | AAP |
| AU-2 | Event Logging | `ansible/tasks/ans_ctrl__audit_export.yml` | AAP |
| AU-2 | Event Logging | `vmware/roles/vsphere_esxi_stig_hardening` (remote syslog) | VMware ESXi |
| AU-2 | Event Logging | `cisco/roles/aci_monitoring` (syslog remote destinations, fault management) | Cisco ACI |
| AU-2 | Event Logging | `cisco/roles/aci_security_hardening` (audit logging, syslog forwarding) | Cisco ACI |
| AU-2 | Event Logging | `cisco/roles/ise_audit__config_changes` (ISE configuration change audit) | Cisco ISE |
| AU-2 | Event Logging | `cisco/roles/ise_integration__logging` (remote syslog / SIEM integration) | Cisco ISE |
| AU-2 | Event Logging | `splunk/roles` | Splunk |
| AU-2 | Event Logging | `elk_stack/roles` | ELK Stack |
| AU-2 | Event Logging | `sciencelogic/roles` | ScienceLogic |
| AU-2 | Event Logging | `policy_as_code/policies/audit_accountability/audit_logging.yml` | Policy as Code |
| AU-3 | Content of Audit Records | `ansible/tasks/ans_ctrl__audit_export.yml` | AAP |
| AU-3 | Content of Audit Records | `splunk/roles` | Splunk |
| AU-3 | Content of Audit Records | STIG findings V-230315, V-230316, V-230317, V-230318 | RHEL 8 |
| AU-4 | Audit Log Storage Capacity | `ansible/roles/ans_ops_artifacts_retention` | AAP |
| AU-5 | Response to Audit Processing Failures | `sciencelogic/roles` (alerting on log gaps) | ScienceLogic |
| AU-6 | Audit Record Review | `ansible/tasks/ans_ctrl__analytics_usage.yml` | AAP |
| AU-6 | Audit Record Review | `sciencelogic/roles` | ScienceLogic |
| AU-9 | Protection of Audit Information | `ansible/roles/ans_ctrl_backup_and_audit` (0640 mode, read-only export) | AAP |
| AU-11 | Audit Record Retention | `ansible/roles/ans_ops_artifacts_retention` | AAP |
| AU-11 | Audit Record Retention | `ansible/tasks/ans_ops__artifacts_retention.yml` | AAP |
| AU-12 | Audit Record Generation | `policy_as_code/policies/audit_accountability/audit_logging.yml` | Policy as Code |
| AU-12 | Audit Record Generation | `vmware/roles/vsphere_esxi_stig_hardening` (syslog, logDirUnique) | VMware ESXi |
| AU-12 | Audit Record Generation | `cisco/roles/aci_monitoring` (Call Home, fault severity reporting) | Cisco ACI |
| AU-12 | Audit Record Generation | `cisco/roles/ise_report__auth_failures`, `ise_report__endpoint_catalog` | Cisco ISE |

---

### CA — Assessment, Authorization, and Monitoring

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| CA-2 | Control Assessments | `policy_as_code/` (automated compliance checks) | Policy as Code |
| CA-7 | Continuous Monitoring | `tenable/roles` | Tenable |
| CA-7 | Continuous Monitoring | `sciencelogic/roles` | ScienceLogic |
| CA-7 | Continuous Monitoring | `prometheus_grafana/roles` | Prometheus/Grafana |
| CA-7 | Continuous Monitoring | `dragos/roles` (OT-specific monitoring) | Dragos |
| CA-7 | Continuous Monitoring | `claroty/roles` (OT asset monitoring) | Claroty |
| CA-8 | Penetration Testing | `tenable/roles` (vulnerability scanning) | Tenable |
| CA-9 | Internal System Connections | `illumio/roles` (micro-segmentation) | Illumio |

---

### CM — Configuration Management

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| CM-2 | Baseline Configuration | `ansible/roles/ans_core_runtime_baseline` | AAP |
| CM-2 | Baseline Configuration | `vmware/roles/cluster_baseline` | VMware |
| CM-2 | Baseline Configuration | `arista/roles/arista_baseline_config` | Arista |
| CM-2 | Baseline Configuration | `rhel/roles` | RHEL |
| CM-2 | Baseline Configuration | `windows/roles/win_group_policy` | Windows |
| CM-2 | Baseline Configuration | `kubernetes/playbook-cluster-hardening.yml` | Kubernetes |
| CM-3 | Configuration Change Control | `ansible/tasks/ans_ctrl__approvals.yml` | AAP |
| CM-3 | Configuration Change Control | `ansible/roles/ans_content_qa_ci` | AAP |
| CM-3 | Configuration Change Control | `vmware/roles/drift_report` | VMware |
| CM-3 | Configuration Change Control | `servicenow/roles` (change ticket integration) | ServiceNow |
| CM-5 | Access Restrictions for Change | `ansible/roles/ans_ctrl_policy_guardrails` | AAP |
| CM-5 | Access Restrictions for Change | `ansible/tasks/ans_ctrl__approvals.yml` | AAP |
| CM-6 | Configuration Settings | `vmware/roles/vsphere_esxi_stig_hardening` | VMware ESXi |
| CM-6 | Configuration Settings | `vmware/roles/vsphere_vm_stig_hardening` | VMware VM |
| CM-6 | Configuration Settings | `cisco/roles/aci_security_hardening` (STIG Cat I/II/III, password/TLS/RBAC) | Cisco ACI |
| CM-6 | Configuration Settings | `cisco/roles/ucs_security_hardening` (STIG Cat I/II/III) | Cisco UCS |
| CM-6 | Configuration Settings | `rhel/roles` (hardening baseline) | RHEL |
| CM-6 | Configuration Settings | `windows/roles/win_stig_hardening` | Windows |
| CM-6 | Configuration Settings | `kubernetes/playbook-cluster-hardening.yml` | Kubernetes |
| CM-6 | Configuration Settings | `ansible/tasks/ans_core__ansible_cfg_enforce.yml` | AAP |
| CM-7 | Least Functionality | `vmware/roles/vsphere_esxi_stig_hardening` (disable TSM/TSM-SSH) | VMware ESXi |
| CM-7 | Least Functionality | `windows/roles/win_stig_hardening` | Windows |
| CM-7 | Least Functionality | `rhel/roles` (disable unused services) | RHEL |
| CM-7 | Least Functionality | `arista/roles/arista_acl_qos_security` (ACL hardening) | Arista |
| CM-8 | System Component Inventory | `servicenow/roles` (CMDB integration) | ServiceNow |
| CM-8 | System Component Inventory | `ansible/roles/ans_core_inventory_hygiene` | AAP |
| CM-8 | System Component Inventory | `vmware/tasks/vsphere_vm_info.yml` | VMware |
| CM-8 | System Component Inventory | `vmware/roles/vcenter_tags` | VMware |
| CM-9 | Configuration Management Plan | `policy_as_code/` | Policy as Code |
| CM-10 | Software Usage Restrictions | `ansible/roles/ans_content_trust_and_lock` (collection signing/lock) | AAP |
| CM-11 | User-Installed Software | `ansible/tasks/ans_content__allowlist.yml` | AAP |

---

### CP — Contingency Planning

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| CP-6 | Alternate Storage Site | `veeam/roles` (off-site cloud tier) | Veeam |
| CP-6 | Alternate Storage Site | `cohesity/roles` (cloud archive) | Cohesity |
| CP-6 | Alternate Storage Site | `netapp/roles` (SnapMirror/SnapVault) | NetApp |
| CP-7 | Alternate Processing Site | `vmware/roles/vsan_cluster` (HA/FT) | VMware |
| CP-7 | Alternate Processing Site | `cohesity/roles` (DR failover) | Cohesity |
| CP-9 | System Backup | `ansible/roles/ans_ctrl_backup_and_audit` | AAP |
| CP-9 | System Backup | `veeam/roles` | Veeam |
| CP-9 | System Backup | `cohesity/roles` | Cohesity |
| CP-9 | System Backup | `arista/roles/arista_backup_restore` | Arista |
| CP-9 | System Backup | `netapp/roles` (SnapVault) | NetApp |
| CP-9 | System Backup | `pure_storage/roles` (snapshots/protection) | Pure Storage |
| CP-9 | System Backup | `vast/roles` (snapshot policies) | VAST Data |
| CP-9 | System Backup | `windows/roles/win_backup` | Windows |
| CP-10 | System Recovery | `veeam/roles` (SureBackup, instant recovery) | Veeam |
| CP-10 | System Recovery | `cohesity/roles` (instant recovery) | Cohesity |
| CP-10 | System Recovery | `ansible/tasks/ans_ctrl__restore_sandbox.yml` | AAP |
| CP-10 | System Recovery | `vmware/roles/vsphere_snapshots_role` | VMware |

---

### IA — Identification and Authentication

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| IA-2 | Identification and Authentication (Users) | `ansible/roles/ans_access_sso_directory` (LDAP/SAML/OIDC) | AAP |
| IA-2 | Identification and Authentication (Users) | `windows/roles/win_active_directory` | Windows |
| IA-2 | Identification and Authentication (Users) | `cisco/roles` (ISE identity policy) | Cisco ISE |
| IA-2(1) | MFA for Privileged Accounts | `ansible/roles/ans_ctrl_policy_guardrails` (`fourth_estate_mandatory_mfa`) | AAP |
| IA-2(1) | MFA for Privileged Accounts | `cisco/roles` (ISE MFA) | Cisco ISE |
| IA-3 | Device Identification | `cisco/roles` (ISE device profiling) | Cisco ISE |
| IA-3 | Device Identification | `infoblox/roles` (DHCP/DNS device identity) | Infoblox |
| IA-5 | Authenticator Management | `policy_as_code/policies/identification_auth/password_policy.yml` | Policy as Code |
| IA-5 | Authenticator Management | STIG findings V-230502, V-230503, V-230505, V-230507, V-230509 | RHEL 8 |
| IA-5 | Authenticator Management | `ansible/roles/ans_core_secrets_identity` | AAP |
| IA-5 | Authenticator Management | `hashicorp_vault/roles` (dynamic credentials) | HashiCorp Vault |
| IA-5(1) | Password-Based Authentication | `policy_as_code/policies/identification_auth/password_policy.yml` | Policy as Code |
| IA-7 | Cryptographic Module Authentication | `ansible/roles/ans_core_runtime_baseline` (FIPS mode) | AAP |
| IA-8 | Non-Organizational Users | `ansible/roles/ans_access_sso_directory` (SSO federation) | AAP |
| IA-11 | Re-Authentication | `policy_as_code/policies/access_control/session_timeout.yml` | Policy as Code |

---

### IR — Incident Response

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| IR-4 | Incident Handling | `sciencelogic/roles` (automated alerting/escalation) | ScienceLogic |
| IR-4 | Incident Handling | `dragos/roles` (OT threat detection) | Dragos |
| IR-4 | Incident Handling | `claroty/roles` (OT incident visibility) | Claroty |
| IR-4 | Incident Handling | `palo_alto/roles` (threat prevention) | Palo Alto |
| IR-4 | Incident Handling | `servicenow/roles` (incident management) | ServiceNow |
| IR-5 | Incident Monitoring | `sciencelogic/roles` | ScienceLogic |
| IR-5 | Incident Monitoring | `tenable/roles` | Tenable |
| IR-5 | Incident Monitoring | `elk_stack/roles` | ELK Stack |
| IR-5 | Incident Monitoring | `prometheus_grafana/roles` | Prometheus/Grafana |
| IR-5 | Incident Monitoring | `splunk/roles` | Splunk |
| IR-6 | Incident Reporting | `servicenow/roles` (incident ticket creation) | ServiceNow |
| IR-6 | Incident Reporting | `ansible/tasks/ans_ctrl__notifications.yml` | AAP |
| IR-7 | Incident Response Assistance | `servicenow/roles` | ServiceNow |

---

### RA — Risk Assessment

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| RA-5 | Vulnerability Monitoring and Scanning | `tenable/roles` | Tenable |
| RA-5 | Vulnerability Monitoring and Scanning | `ansible/tasks/ans_content__sbom_vuln_scan.yml` (Syft + Grype) | AAP |
| RA-5 | Vulnerability Monitoring and Scanning | `crowdstrike/roles` | CrowdStrike |
| RA-5 | Vulnerability Monitoring and Scanning | `sentinelone/roles` | SentinelOne |
| RA-5(2) | Update Vulnerabilities to Be Scanned | `tenable/roles` (feed updates) | Tenable |
| RA-7 | Risk Response | `servicenow/roles` (risk ticket tracking) | ServiceNow |

---

### SA — System and Services Acquisition

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| SA-10 | Developer Configuration Management | `ansible/roles/ans_ci_pipelines` | AAP |
| SA-10 | Developer Configuration Management | `ansible/roles/ans_content_qa_ci` | AAP |
| SA-10 | Developer Configuration Management | `ansible/tasks/ans_ci__pipeline_scaffold.yml` | AAP |
| SA-10 | Developer Configuration Management | `ansible/tasks/ans_ci__precommit.yml` | AAP |
| SA-11 | Developer Testing and Evaluation | `ansible/roles/ans_content_qa_ci` (molecule/lint) | AAP |
| SA-12 | Supply Chain Protection | `ansible/roles/ans_content_trust_and_lock` (GPG signing, sig verify) | AAP |
| SA-12 | Supply Chain Protection | `ansible/tasks/ans_content__sync_and_sign.yml` | AAP |
| SA-12 | Supply Chain Protection | `ansible/tasks/ans_ctrl__content_signed_only.yml` | AAP |
| SA-12 | Supply Chain Protection | `ansible/tasks/ans_content__mirror_lock.yml` | AAP |
| SA-15 | Development Process, Standards, and Tools | `ansible/roles/ans_ci_pipelines` | AAP |

---

### SC — System and Communications Protection

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| SC-5 | Denial-of-Service Protection | `arista/roles/arista_acl_qos_security` | Arista |
| SC-5 | Denial-of-Service Protection | `palo_alto/roles` | Palo Alto |
| SC-5 | Denial-of-Service Protection | `f5_bigip/roles` | F5 BIG-IP |
| SC-7 | Boundary Protection | `palo_alto/roles` | Palo Alto |
| SC-7 | Boundary Protection | `checkpoint/roles` | Check Point |
| SC-7 | Boundary Protection | `fortinet/roles` | Fortinet |
| SC-7 | Boundary Protection | `illumio/roles` (micro-segmentation) | Illumio |
| SC-7 | Boundary Protection | `vmware/roles/nsx_t_security` | VMware NSX-T |
| SC-7 | Boundary Protection | `arista/roles/arista_acl_qos_security` | Arista |
| SC-7 | Boundary Protection | `f5_bigip/roles` (WAF/virtual servers) | F5 BIG-IP |
| SC-7 | Boundary Protection | `cisco/roles/aci_security_hardening` (contract enforcement, EPG isolation) | Cisco ACI |
| SC-7 | Boundary Protection | `cisco/roles/aci_tenant_config` (intra-EPG isolation, contracts) | Cisco ACI |
| SC-7 | Boundary Protection | `cisco/roles/ise_anc__quarantine_rules` (adaptive network quarantine) | Cisco ISE |
| SC-7 | Boundary Protection | `windows/roles/win_firewall` | Windows |
| SC-7 | Boundary Protection | `vmware/roles/vsphere_esxi_stig_hardening` (firewall rulesets) | VMware ESXi |
| SC-8 | Transmission Confidentiality and Integrity | `policy_as_code/policies/system_communications/cryptographic_protection.yml` | Policy as Code |
| SC-8 | Transmission Confidentiality and Integrity | STIG findings V-230273, V-230274, V-230275, V-230276, V-230277 | RHEL 8 |
| SC-8 | Transmission Confidentiality and Integrity | `cisco/roles/aci_security_hardening` (TLS 1.2+ enforcement, FIPS-mode) | Cisco ACI |
| SC-8 | Transmission Confidentiality and Integrity | `cisco/roles/ucs_security_hardening` (TLS 1.2+ enforcement) | Cisco UCS |
| SC-8 | Transmission Confidentiality and Integrity | `vmware/roles/vsphere_vm_stig_hardening` | VMware VM |
| SC-8 | Transmission Confidentiality and Integrity | `arista/roles/arista_acl_qos_security` | Arista |
| SC-12 | Cryptographic Key Establishment and Management | `hashicorp_vault/roles` (PKI, key management) | HashiCorp Vault |
| SC-12 | Cryptographic Key Establishment and Management | `vmware/roles/vcenter_kms` | VMware |
| SC-12 | Cryptographic Key Establishment and Management | `ansible/tasks/ans_secrets__vault_rotate.yml` | AAP |
| SC-13 | Cryptographic Protection | `policy_as_code/policies/system_communications/cryptographic_protection.yml` | Policy as Code |
| SC-13 | Cryptographic Protection | `ansible/roles/ans_core_runtime_baseline` (FIPS mode) | AAP |
| SC-13 | Cryptographic Protection | `hashicorp_vault/roles` | HashiCorp Vault |
| SC-17 | Public Key Infrastructure Certificates | `vmware/roles/vcenter_certificates` | VMware |
| SC-17 | Public Key Infrastructure Certificates | `hashicorp_vault/roles` (PKI) | HashiCorp Vault |
| SC-28 | Protection of Information at Rest | `vmware/tasks/enforce_vm_encryption.yml` | VMware |
| SC-28 | Protection of Information at Rest | `vmware/roles/vcenter_kms` | VMware |
| SC-28 | Protection of Information at Rest | `hashicorp_vault/roles` | HashiCorp Vault |
| SC-28 | Protection of Information at Rest | `pure_storage/roles` (array-level encryption) | Pure Storage |
| SC-28 | Protection of Information at Rest | `netapp/roles` (volume encryption) | NetApp |
| SC-28 | Protection of Information at Rest | `databases/postgresql`, `databases/mysql`, `databases/oracle` (TDE) | Databases |

---

### SI — System and Information Integrity

| Control | Title | Implementing Roles / Task Files | Platform |
|---------|-------|--------------------------------|----------|
| SI-2 | Flaw Remediation | `rhel/roles` (patching) | RHEL |
| SI-2 | Flaw Remediation | `windows/roles/win_updates`, `win_wsus` | Windows |
| SI-2 | Flaw Remediation | `vmware/roles/cluster_lifecycle_vlcm` | VMware |
| SI-2 | Flaw Remediation | `openshift/roles` (patch management) | OpenShift |
| SI-2 | Flaw Remediation | `ansible/roles/ans_ops_upgrade_window` | AAP |
| SI-3 | Malicious Code Protection | `crowdstrike/roles` (EDR deployment) | CrowdStrike |
| SI-3 | Malicious Code Protection | `sentinelone/roles` (EDR deployment) | SentinelOne |
| SI-3 | Malicious Code Protection | `palo_alto/roles` (AV/WildFire) | Palo Alto |
| SI-3 | Malicious Code Protection | `fortinet/roles` (AV/IPS) | Fortinet |
| SI-4 | System Monitoring | `sciencelogic/roles` | ScienceLogic |
| SI-4 | System Monitoring | `prometheus_grafana/roles` | Prometheus/Grafana |
| SI-4 | System Monitoring | `elk_stack/roles` | ELK Stack |
| SI-4 | System Monitoring | `splunk/roles` | Splunk |
| SI-4 | System Monitoring | `dragos/roles` (OT monitoring) | Dragos |
| SI-4 | System Monitoring | `claroty/roles` (OT monitoring) | Claroty |
| SI-4 | System Monitoring | `tenable/roles` | Tenable |
| SI-7 | Software, Firmware, and Information Integrity | `ansible/roles/ans_content_trust_and_lock` (collection signing/verify) | AAP |
| SI-7 | Software, Firmware, and Information Integrity | `ansible/tasks/ans_content__sbom_vuln_scan.yml` (SBOM + SHA-256) | AAP |
| SI-7 | Software, Firmware, and Information Integrity | `ansible/tasks/ans_content__sync_and_sign.yml` | AAP |
| SI-7 | Software, Firmware, and Information Integrity | `ansible/tasks/ans_ctrl__content_signed_only.yml` | AAP |
| SI-10 | Information Input Validation | `ansible/roles/ans_content_qa_ci` | AAP |
| SI-10 | Information Input Validation | `policy_as_code/` | Policy as Code |
| SI-12 | Information Management and Retention | `ansible/roles/ans_ops_artifacts_retention` | AAP |

---

## DISA STIG Mapping — By Platform

### VMware ESXi STIG V1R1

Role: `vmware/roles/vsphere_esxi_stig_hardening`

| STIG Finding | Severity | Description | Implemented Task |
|-------------|----------|-------------|-----------------|
| ESXI-67-000001 | Cat I | Enable lockdown mode | `Set Lockdown mode` |
| ESXI-67-000002 | Cat II | Restrict SSH access | `Set SSH service policy` |
| ESXI-67-000003 | Cat II | Disable ESXi Shell | `Set ESXi Shell service policy` |
| ESXI-67-000004 | Cat II | Configure NTP | `Configure NTP servers`, `Ensure NTP service policy/state` |
| ESXI-67-000005 | Cat II | Configure remote syslog | `Configure remote syslog`, `Set Syslog.global.logDirUnique` |
| ESXI-67-000006 | Cat II | Set host acceptance level | `Set acceptance level on each host` |
| ESXI-67-000007 | Cat II | Configure firewall rulesets | `Configure firewall rulesets` |
| ESXI-67-000008 | Cat II | Apply advanced host configuration | `Apply advanced host configuration (bulk)` |

Role: `vmware/roles/vcenter_certificates`
- Implements certificate rotation, PKI trust chain enforcement.

Role: `vmware/roles/vcenter_kms`
- Implements KMS-based encryption key management for vSAN and VM encryption.

---

### VMware vSphere VM STIG

Role: `vmware/roles/vsphere_vm_stig_hardening`

| STIG Finding | Severity | Description |
|-------------|----------|-------------|
| VMCH-06-000001 | Cat I | Disable copy/paste between VM and client |
| VMCH-06-000003 | Cat I | Disable disk shrink |
| VMCH-06-000004 | Cat II | Limit console connections |
| VMCH-06-000007 | Cat II | Disable logging to host |
| VMCH-06-000009 | Cat II | Restrict VM-to-host communication |
| VMCH-06-000010 | Cat II | Enable VM encryption (with vcenter_kms) |

Supporting roles: `vmware/tasks/enforce_vm_encryption.yml`

---

### Kubernetes STIG V1R11

Role: `kubernetes/playbook-cluster-hardening.yml`

| STIG Finding | Severity | Description |
|-------------|----------|-------------|
| V-242376 | Cat I | Pod security policies / admission control |
| V-242381 | Cat I | RBAC authorization mode |
| V-242383 | Cat I | Disable anonymous API access |
| V-242386 | Cat II | API server audit logging |
| V-242390 | Cat II | Etcd data encryption at rest |
| V-242395 | Cat II | Kubelet authentication |
| V-242400 | Cat II | Network policies enforced |
| V-242410 | Cat III | Node authorization mode |

Supporting roles: `openshift/roles` (OpenShift adds Red Hat OpenShift Container Platform STIG V1R2 controls on top of base Kubernetes STIG).

---

### Red Hat Enterprise Linux 8 STIG V1R14

Role: `rhel/roles`
Policy as Code: `policy_as_code/policies/`

| STIG Finding | Severity | NIST Control | Description |
|-------------|----------|--------------|-------------|
| V-230502 | Cat I | IA-5 | Password complexity minimum length |
| V-230503 | Cat I | IA-5 | Password contains uppercase |
| V-230505 | Cat I | IA-5 | Password contains lowercase |
| V-230507 | Cat I | IA-5 | Password contains numeric character |
| V-230509 | Cat I | IA-5 | Password contains special character |
| V-230273 | Cat I | SC-8 | Protect data in transit (TLS 1.2+) |
| V-230274 | Cat I | SC-8/SC-13 | Cryptographic algorithms (FIPS 140-2) |
| V-230275 | Cat I | SC-13 | Disallow non-FIPS ciphers |
| V-230276 | Cat II | SC-8 | SSH protocol settings |
| V-230277 | Cat II | SC-13 | Crypto module selection |
| V-230286 | Cat II | AC-12 | Session idle timeout |
| V-230287 | Cat II | AC-12 | Session lock after inactivity |
| V-230315 | Cat II | AU-2/AU-12 | Audit all login/logout events |
| V-230316 | Cat II | AU-2/AU-12 | Audit privileged command use |
| V-230317 | Cat II | AU-2/AU-12 | Audit account creation/modification |
| V-230318 | Cat II | AU-2 | Audit file access failures |

---

### Microsoft Windows Server STIG V2R8

Role: `windows/roles/win_stig_hardening`
Supporting roles: `win_group_policy`, `win_active_directory`, `win_firewall`, `win_user_management`

| STIG Finding | Severity | Description |
|-------------|----------|-------------|
| WN19-000010 | Cat II | Inactive accounts disabled after 35 days |
| WN19-000020 | Cat II | Local accounts with blank passwords disabled |
| WN19-AC-000010 | Cat I | Administrator account renamed |
| WN19-AC-000020 | Cat I | Guest account disabled |
| WN19-AU-000010 | Cat II | Audit policy: Account Logon events |
| WN19-AU-000020 | Cat II | Audit policy: Account Management |
| WN19-AU-000030 | Cat II | Audit policy: Logon/Logoff |
| WN19-CC-000010 | Cat II | Windows Firewall enabled (all profiles) |
| WN19-CC-000020 | Cat II | SMBv1 disabled |
| WN19-CC-000030 | Cat II | LLMNR disabled |
| WN19-SO-000010 | Cat I | LAN Manager hash storage disabled |
| WN19-SO-000020 | Cat I | NTLMv1 disabled |
| WN19-UR-000010 | Cat II | Deny access to this computer from the network |

---

### Cisco IOS/NX-OS Network Infrastructure STIG V2R7

Role: `cisco/roles`

| STIG Finding | Severity | Description |
|-------------|----------|-------------|
| NET-IPV6-001 | Cat I | Disable IPv6 on interfaces not required |
| NET0400 | Cat II | Enable AAA for access control |
| NET0470 | Cat II | Enable logging to syslog server |
| NET0480 | Cat II | Timestamps on log entries |
| NET0600 | Cat II | Restrict SNMP community strings |
| NET0700 | Cat II | Restrict management access by ACL |
| NET0800 | Cat II | SSH enabled, Telnet disabled |
| NET1028 | Cat I | Disable unused services (CDP, BOOTP, etc.) |
| CISC-ND-000010 | Cat I | Authentication for management access |

---

### Cisco ACI STIG (APIC STIG / Network Infrastructure STIG)

Roles: `cisco/roles/aci_fabric_deploy`, `cisco/roles/aci_security_hardening`, `cisco/roles/aci_monitoring`

| STIG Finding | Severity | Description | Implementing Role |
|-------------|----------|-------------|------------------|
| NET0400 | Cat II | Enable AAA for APIC management access | `aci_security_hardening` |
| NET0470 | Cat II | Enable syslog to remote server | `aci_monitoring` |
| NET0480 | Cat II | Timestamps on log entries | `aci_monitoring` |
| NET0600 | Cat II | Restrict SNMP — SNMPv3 only, disable v1/v2c | `aci_security_hardening` |
| NET0700 | Cat II | Restrict management access by OOB ACL | `aci_fabric_deploy`, `aci_security_hardening` |
| NET0800 | Cat II | SSH enabled; Telnet disabled on APIC | `aci_security_hardening` |
| NET1028 | Cat I | Disable unused services | `aci_security_hardening` |
| CISC-ND-000010 | Cat I | Authentication required for all management access | `aci_security_hardening` |
| CISC-ND-000020 | Cat II | Session timeout enforcement (15 min) | `aci_security_hardening` |
| CISC-ND-000030 | Cat I | Password complexity minimum requirements | `aci_security_hardening` |
| CISC-ND-000040 | Cat II | RBAC — privilege separation for operators/admins | `aci_security_hardening` |
| CISC-ND-000050 | Cat II | TLS 1.2+ enforced; TLS 1.0/1.1 disabled | `aci_security_hardening` |
| CISC-ND-000060 | Cat II | Call Home notification configured | `aci_monitoring` |
| CISC-ND-000070 | Cat I | Rogue endpoint detection enabled | `aci_fabric_deploy` |
| CISC-ND-000080 | Cat II | Loop protection enabled on leaf nodes | `aci_fabric_deploy` |

---

### Arista EOS Network Device STIG

Roles: `arista/roles/arista_acl_qos_security`, `arista/roles/arista_baseline_config`, `arista/roles/arista_backup_restore`

| STIG Finding | Severity | Description | Implementing Role |
|-------------|----------|-------------|------------------|
| NET0400 | Cat II | AAA authentication | `arista_baseline_config` |
| NET0470 | Cat II | Syslog to remote server | `arista_baseline_config` |
| NET0600 | Cat II | SNMPv3 only | `arista_acl_qos_security` |
| NET0700 | Cat II | Management ACL | `arista_acl_qos_security` |
| NET0800 | Cat II | SSH only, Telnet disabled | `arista_baseline_config` |
| NET1028 | Cat I | Disable unused protocols | `arista_baseline_config` |
| — | Cat II | Configuration backup | `arista_backup_restore` |

---

### Palo Alto Networks STIG V2R2

Roles: `palo_alto/roles`

| STIG Finding | Severity | Description |
|-------------|----------|-------------|
| PANW-AG-000001 | Cat I | Application identification enabled |
| PANW-AG-000010 | Cat II | Threat prevention profiles applied |
| PANW-AG-000015 | Cat II | URL filtering applied |
| PANW-AG-000020 | Cat I | Deny-all default policy |
| PANW-IP-000001 | Cat II | NTP configured |
| PANW-IP-000010 | Cat II | Syslog to remote server |
| PANW-IP-000015 | Cat II | Admin authentication via RADIUS/LDAP |
| PANW-IP-000020 | Cat II | SSH only management access |
| PANW-IP-000025 | Cat II | Audit logging of admin actions |
| PANW-NM-000001 | Cat I | WildFire threat intelligence enabled |

---

### PostgreSQL STIG V2R1

Roles: `databases/postgresql/roles`

| STIG Finding | Severity | Description |
|-------------|----------|-------------|
| PGS9-00-000100 | Cat II | Enable pgaudit for audit logging |
| PGS9-00-000200 | Cat I | Use SCRAM-SHA-256 authentication |
| PGS9-00-000300 | Cat I | Disable trust authentication |
| PGS9-00-000400 | Cat II | Restrict superuser access |
| PGS9-00-000500 | Cat II | Encrypt connections (SSL required) |
| PGS9-00-000600 | Cat II | Set log_connections, log_disconnections |
| PGS9-00-000700 | Cat II | Set log_line_prefix |
| PGS9-00-000800 | Cat II | Restrict pg_hba.conf access |

---

### MySQL/MariaDB STIG V2R2

Roles: `databases/mysql/roles`

| STIG Finding | Severity | Description |
|-------------|----------|-------------|
| MYS8-00-000100 | Cat II | Enable audit log plugin |
| MYS8-00-000200 | Cat I | Disable anonymous user |
| MYS8-00-000300 | Cat I | Remove test database |
| MYS8-00-000400 | Cat II | Require SSL for connections |
| MYS8-00-000500 | Cat II | Restrict FILE privilege |
| MYS8-00-000600 | Cat II | Disable LOCAL INFILE |
| MYS8-00-000700 | Cat II | Set appropriate password policy |

---

### Oracle Database STIG V2R4

Roles: `databases/oracle/roles`

| STIG Finding | Severity | Description |
|-------------|----------|-------------|
| O112-C2-019000 | Cat I | Enable Oracle Unified Auditing |
| O112-C2-019100 | Cat II | Audit privileged account use |
| O112-C2-016700 | Cat I | Restrict DBA role assignment |
| O112-C2-016800 | Cat II | Revoke PUBLIC execute privileges |
| O112-C2-012400 | Cat II | Enable Transparent Data Encryption |
| O112-C2-012500 | Cat II | Enforce SSL for remote connections |
| O112-C2-013600 | Cat II | Set FAILED_LOGIN_ATTEMPTS |
| O112-C2-013700 | Cat II | Set PASSWORD_LIFE_TIME profile |

---

### Ansible Automation Platform / RHEL Application STIG

Roles under `ansible/` and `ansible_tower/`

| STIG / Control | Severity | Description | Implementing Role / Task |
|---------------|----------|-------------|-------------------------|
| RHEL-08-010550 | Cat I | Privileged account auditing | `ans_ctrl__audit_export.yml` |
| RHEL-08-020230 | Cat II | No shared credentials | `ans_core_secrets_identity` |
| AC-2 | — | Account lifecycle management | `ans_access_sso_directory`, `ans_ctrl__orgs_teams.yml` |
| AC-3 | — | Role-based access enforcement | `ans_ctrl__rbac_baseline.yml`, `ansible_tower_rbac` |
| AC-5 | — | Separation of duties | `ans_ctrl__approvals.yml`, `ans_ctrl_policy_guardrails` |
| AU-2 | — | Audit log collection | `ans_ctrl_backup_and_audit`, `ans_ctrl__audit_export.yml` |
| CM-3 | — | Change control with approvals | `ans_ctrl__approvals.yml` |
| CM-10 | — | Signed content only | `ans_content_trust_and_lock`, `ans_ctrl__content_signed_only.yml` |
| IA-5 | — | Vault credential rotation | `ans_core_secrets_identity`, `ans_secrets__vault_rotate.yml` |
| SC-13 | — | FIPS 140-2 mode | `ans_core_runtime_baseline` |
| SI-7 | — | SBOM + vulnerability scan | `ans_content__sbom_vuln_scan.yml` |

---

### OT/ICS Systems STIG

Roles: `operational_technology/roles`, `dragos/roles`, `claroty/roles`

| STIG / Control | Severity | Description | Platform |
|---------------|----------|-------------|---------|
| ICS-001 | Cat I | Network segmentation (IT/OT DMZ) | `operational_technology` |
| ICS-002 | Cat I | Firewall rules at OT boundary | `operational_technology` |
| ICS-003 | Cat II | OT asset inventory | `claroty`, `dragos` |
| ICS-004 | Cat II | Continuous threat monitoring | `dragos` |
| ICS-005 | Cat II | Secure remote access to OT | `claroty` |
| ICS-006 | Cat II | Firmware integrity verification | `operational_technology` |
| ICS-007 | Cat II | OT-specific audit logging | `operational_technology` |
| ICS-008 | Cat II | Patch/firmware management | `operational_technology` |
| NERC CIP-007 | — | Ports and services management | `operational_technology` |
| NERC CIP-010 | — | Configuration change management | `operational_technology` |

---

## Per-Platform Quick Reference

The table below maps every top-level directory to its primary DISA STIG(s) and NIST 800-53
control families for rapid lookup.

| Platform Directory | Primary DISA STIG | NIST 800-53 Families | Key Roles / Task Files |
|--------------------|-------------------|---------------------|------------------------|
| `ansible/` | RHEL 8 App STIG | AC, AU, CM, IA, SA, SC, SI | `ans_access_sso_directory`, `ans_ctrl_backup_and_audit`, `ans_ctrl_policy_guardrails`, `ans_core_secrets_identity`, `ans_content_trust_and_lock`, `ans_core_runtime_baseline` |
| `ansible_tower/` | RHEL 8 App STIG | AC, AU, CM, IA | `ansible_tower_rbac`, `ansible_tower_organizations`, `ansible_tower_config` |
| `arista/` | Network Device STIG | AU, CM, CP, SC | `arista_acl_qos_security`, `arista_baseline_config`, `arista_backup_restore` |
| `aws/` | DoD CC SRG / FedRAMP | AC, AU, CM, IA, SC, SI | IAM, VPC, EC2, EKS, S3 roles |
| `azure/` | DoD CC SRG / FedRAMP | AC, AU, CM, IA, SC, SI | Azure AD, AKS, Key Vault, Sentinel roles |
| `checkpoint/` | Firewall STIG | AC, AU, SC, SI | Access policy, threat prevention roles |
| `cisco/` | ACI STIG (APIC), IOS STIG V2R7, UCS STIG | AC, AU, CM, IA, SC, SI | `aci_security_hardening`, `aci_monitoring`, `aci_fabric_deploy`, ISE identity/policy/profiling/posture/reporting (28 roles), `ucs_security_hardening`, `ucs_prod_monitoring` |
| `claroty/` | ICS STIG | AU, CM, IA, SC, SI | OT asset mgmt, secure remote access roles |
| `cohesity/` | General App STIG | CP, SC | Cluster config, protection, recovery roles |
| `crowdstrike/` | Endpoint Security | RA, SI | EDR deployment, policy management |
| `databases/postgresql/` | PostgreSQL STIG V2R1 | AC, AU, IA, SC | Install, replication, audit, security roles |
| `databases/mysql/` | MySQL STIG V2R2 | AC, AU, IA, SC | Install, Galera, backup, security roles |
| `databases/oracle/` | Oracle STIG V2R4 | AC, AU, IA, SC | Install, Data Guard, RMAN, security roles |
| `dragos/` | ICS STIG | AU, IR, RA, SI | Threat detection, inventory, topology roles |
| `elk_stack/` | General App STIG | AU, IR, SI | Elasticsearch, Logstash, Kibana, Filebeat |
| `f5_bigip/` | F5 BIG-IP STIG | AC, AU, SC, SI | Load balancing, SSL, WAF, HA roles |
| `fortinet/` | FortiGate STIG | AC, AU, SC, SI | Firewall, VPN, IPS/AV, HA roles |
| `google_cloud_platform/` | DoD CC SRG / FedRAMP | AC, AU, CM, IA, SC, SI | GCP IAM, VPC, GKE, BigQuery roles |
| `hashicorp_vault/` | General App STIG | IA, SC | PKI, dynamic credentials, audit, secrets roles |
| `illumio/` | Network Security STIG | AC, SC | Micro-segmentation, VEN management roles |
| `infoblox/` | DNS/DHCP STIG | CM, IA, SC | DNS, DHCP, RPZ, grid management roles |
| `kubernetes/` | Kubernetes STIG V1R11 | AC, AU, CM, IA, SC, SI | Cluster hardening, RBAC, network policy |
| `netapp/` | Storage STIG | CP, SC | ONTAP cluster, SVM, SnapMirror, SnapVault |
| `openshift/` | Kubernetes STIG + OCP STIG V1R2 | AC, AU, CM, IA, SC, SI | OCP lifecycle, operators, GitOps, monitoring |
| `operational_technology/` | ICS STIG, NERC CIP | AU, CM, IR, SC, SI | Firewall, IDPS, logging, firmware roles |
| `palo_alto/` | PAN-OS STIG V2R2 | AC, AU, CM, SC, SI | Security rules, threat prevention, VPN roles |
| `policy_as_code/` | RHEL 8 STIG (direct) | AC, AU, CM, IA, SC, SI | Password policy, session timeout, audit, crypto |
| `prometheus_grafana/` | General App STIG | AU, CA, IR, SI | Metrics, alerting, dashboarding roles |
| `pure_storage/` | Storage STIG | CP, SC | FlashArray/FlashBlade provisioning, protection |
| `rhel/` | RHEL 8 STIG V1R14 | AC, AU, CM, IA, SC, SI | Hardening, patching, audit, firewall, SELinux |
| `sciencelogic/` | General App STIG | AU, CA, IR, SI | Monitoring, RBA, powerflow, governance roles |
| `sentinelone/` | Endpoint Security | RA, SI | EDR deployment, policy management |
| `servicenow/` | General App STIG | CM, IR | CMDB, incident/change management, asset tracking |
| `splunk/` | General App STIG | AU, IR, SI | Log aggregation, forwarder, security monitoring |
| `tenable/` | General App STIG | CA, RA, SI | Vulnerability scanning, compliance, reporting |
| `vast/` | Storage STIG | CP, SC | All-flash NAS, monitoring, security hardening |
| `veeam/` | General App STIG | CP | Backup, replication, SureBackup, cloud tier |
| `vmware/` | ESXi STIG V1R1, VM STIG | AC, AU, CM, CP, SC, SI | ESXi hardening, VM hardening, vCenter, NSX-T, vSAN |
| `windows/` | Windows Server STIG V2R8 | AC, AU, CM, CP, IA, SC, SI | STIG hardening, AD, GPO, firewall, WSUS |

---

## Policy as Code — Direct Control Implementations

The `policy_as_code/` directory executes NIST and STIG controls directly as Ansible tasks.
Each file below is an executable compliance check and remediation playbook.

| Policy File | NIST Control | STIG Finding(s) | Severity |
|-------------|-------------|-----------------|----------|
| `policies/identification_auth/password_policy.yml` | IA-5, IA-5(1) | V-230502, V-230503, V-230505, V-230507, V-230509 | Cat I |
| `policies/access_control/session_timeout.yml` | AC-12, IA-11 | V-230286, V-230287 | Cat II |
| `policies/audit_accountability/audit_logging.yml` | AU-2, AU-12 | V-230315, V-230316, V-230317, V-230318 | Cat II |
| `policies/system_communications/cryptographic_protection.yml` | SC-8, SC-13 | V-230273, V-230274, V-230275, V-230276, V-230277 | Cat I |

**Running individual policy checks:**

```bash
# IA-5 — Password Policy (dry run)
ansible-playbook policy_as_code/site.yml -i inventory/prod.yml --tags nist_ia_5

# AC-12 — Session Timeout (dry run)
ansible-playbook policy_as_code/site.yml -i inventory/prod.yml --tags nist_ac_12

# AU-2 — Audit Logging (apply)
ansible-playbook policy_as_code/site.yml -i inventory/prod.yml -e "apply_changes=true" --tags nist_au_2

# SC-13 — Cryptographic Protection (Cat I findings only)
ansible-playbook policy_as_code/site.yml -i inventory/prod.yml -e "apply_changes=true" --tags stig_cat1
```

---

## NIST 800-171 — CUI Control Mapping

For Fourth Estate organizations handling **Controlled Unclassified Information (CUI)**,
the following NIST 800-171 requirements are addressed:

| 800-171 Requirement | Description | Implementing Component |
|---------------------|-------------|----------------------|
| 3.1.1 | Limit system access to authorized users | `ans_access_sso_directory`, `ans_ctrl__rbac_baseline.yml` |
| 3.1.2 | Limit system access to authorized transactions | `ans_ctrl_policy_guardrails`, `ans_ctrl__approvals.yml` |
| 3.1.3 | Control CUI flow | `illumio/roles`, `palo_alto/roles`, `vmware/roles/nsx_t_security` |
| 3.3.1 | Create and retain audit logs | `ans_ctrl_backup_and_audit`, `splunk/roles`, `elk_stack/roles` |
| 3.3.2 | Ensure individual actions are traceable | `ans_ctrl__audit_export.yml`, `sciencelogic/roles` |
| 3.5.2 | Authenticate organizational users | `ans_access_sso_directory`, `windows/roles/win_active_directory` |
| 3.5.3 | MFA for local/network access to privileged accounts | `ans_ctrl_policy_guardrails` (mandatory MFA flag) |
| 3.13.1 | Monitor, control, and protect communications | `palo_alto/roles`, `checkpoint/roles`, `fortinet/roles` |
| 3.13.2 | Employ architectural designs for security | `vmware/roles/nsx_t_networking`, `illumio/roles` |
| 3.13.8 | Protect CUI in transit | `policy_as_code/policies/system_communications/cryptographic_protection.yml` |
| 3.13.10 | Establish/manage cryptographic keys | `hashicorp_vault/roles`, `vmware/roles/vcenter_kms` |
| 3.14.1 | Identify, report, and correct information flaws | `tenable/roles`, `rhel/roles`, `windows/roles/win_updates` |
| 3.14.2 | Protect against malicious code | `crowdstrike/roles`, `sentinelone/roles` |
| 3.14.6 | Monitor systems for security alerts | `sciencelogic/roles`, `splunk/roles`, `dragos/roles` |

---

## FedRAMP Baseline Alignment

Cloud platform roles align to FedRAMP control baselines:

| Cloud Platform | FedRAMP Baseline | Key Control Areas |
|---------------|-----------------|-------------------|
| `aws/` | FedRAMP Moderate / High | AC, AU, CA, CM, IA, IR, RA, SA, SC, SI |
| `azure/` | FedRAMP Moderate / High (Azure Gov) | AC, AU, CA, CM, IA, IR, RA, SA, SC, SI |
| `google_cloud_platform/` | FedRAMP Moderate | AC, AU, CM, IA, SC, SI |
| `openshift/` | FedRAMP Moderate | AC, AU, CM, IA, SC, SI |

---

*This document is generated from manual analysis of role and task implementations.*
*Re-validate control mappings after each major release or when STIG versions are updated.*
*Reference: [DISA STIG Library](https://public.cyber.mil/stigs/) | [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)*

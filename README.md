# Ansible-Playbooks-2.0

An enterprise-grade collection of **288+ roles** and **2,045+ YAML files** for infrastructure automation across **25+ technology platforms** with emphasis on **DoD STIG, NIST 800-53, NIST 800-171, FedRAMP, and FISMA compliance**.

This repository provides production-ready Ansible automation for network infrastructure, cloud platforms, container orchestration, storage systems, backup solutions, and operational technology (OT/ICS) security with a special focus on **Fourth Estate** (free press/media) organizations.

## 📊 Repository Statistics

- **Total Roles:** 288+
- **Total YAML Files:** 2,045+
- **README Documentation Files:** 288+
- **Technology Platforms:** 25+
- **Compliance Frameworks:** DoD STIG, NIST 800-53 Rev 5, NIST 800-171, FedRAMP, FISMA, CIS Benchmarks
- **Test Playbooks:** 9+
- **Jinja2 Templates:** 15+
- **Inventory Examples:** 5

## Table of Contents

- [Repository Purpose](#repository-purpose)
- [Supported Technologies](#supported-technologies)
- [Repository Layout](#repository-layout)
- [Key Features](#key-features)
- [Policy as Code Framework](#policy-as-code-framework)
- [Conventions and Best Practices](#conventions-and-best-practices)
- [Execution Environments & Dependencies](#execution-environments--dependencies)
- [Credentials and Secrets](#credentials-and-secrets)
- [Running Playbooks](#running-playbooks-tips-and-examples)
- [Testing and CI Guidance](#testing-and-ci-guidance)
- [Compliance and Security](#compliance-and-security)
- [Contribution Guidelines](#contribution-guidelines)
- [Where to Get Help](#where-to-get-help)

## Repository Purpose

This repository provides enterprise-grade Ansible automation for organizations requiring:

- **Multi-platform infrastructure automation** across 25+ technologies
- **Security compliance** with DoD STIG and NIST 800-53/800-171 standards
- **Fourth Estate operations** with specialized roles for free press/media infrastructure
- **Production-ready automation** including Day-0/Day-1 deployment, monitoring, backup, and disaster recovery
- **Operational Technology (OT/ICS) security** with Dragos, Claroty, and OT-specific hardening

Each top-level directory focuses on a specific technology platform and contains roles, playbooks, tasks, templates, and comprehensive documentation.

## Supported Technologies

### 🌐 Network & Security (14 platforms)
- **Cisco ISE** (Identity Services Engine) - 30+ roles for policy, posture, guest services, profiling
- **Cisco UCS** (Unified Computing System) - Infrastructure, security, networking, monitoring, DR
- **Palo Alto Networks** - PAN-OS firewalls, Panorama management, VPN, QoS (10 roles)
- **Check Point** - Firewalls, access policies, threat prevention, identity awareness (6 roles)
- **Arista EOS** - Network switches, CVP, routing, fabric, baseline configuration (6 roles)
- **Illumio** - Zero-trust micro-segmentation, policy lifecycle, VEN management (3 roles)
- **Infoblox** - DNS/DHCP infrastructure, grid operations, RPZ policies (10 roles)
- **Claroty** - OT security, inventory, secure access, segmentation (11 roles)

### ☁️ Cloud Platforms (3 platforms)
- **Amazon Web Services (AWS)** - IAM, VPC, EC2, EKS, S3, RDS, Lambda, FedRAMP (40+ roles) ⭐ NEW
- **Google Cloud Platform** - GCP IAM, VPCs, GKE, BigQuery, Cloud Run, compliance (28 roles)
- **VMware vSphere** - vCenter, ESXi, vSAN, NSX-T SDN, STIG hardening (35+ roles) ⭐ ENHANCED

### 🔄 Container & Orchestration (2 platforms)
- **Kubernetes** - Cluster hardening (STIG V1R11), RBAC, namespaces, secrets (4 roles)
- **Red Hat OpenShift** - Full OCP lifecycle, operators, GitOps, monitoring (45 roles)

### 🐧 Operating Systems (2 platforms)
- **Red Hat Enterprise Linux** - Hardening, patching, audit logging, firewall, SELinux (5 roles)
- **Microsoft Windows Server** - STIG hardening, Active Directory, Group Policy, DHCP/DNS, IIS (20+ roles) ⭐ NEW

### 💾 Storage & Backup (5 platforms)
- **Pure Storage** - FlashArray, FlashBlade, provisioning, protection (7 roles)
- **VAST Data** - All-flash NAS storage, monitoring, security hardening (4 roles)
- **Veeam** - Backup & recovery, replication, cloud tier, SureBackup (6 roles) ⭐ ENHANCED
- **Cohesity** - Cluster config, protection policies, recovery, cloud archive (6 roles) ⭐ ENHANCED
- **Splunk** - Log aggregation, forwarder, monitoring, security (5 roles)

### 📊 Monitoring & Observability (2 platforms)
- **ScienceLogic SL1** - Platform monitoring, RBA, powerflow, governance (31 roles)
- **Dragos** - OT threat detection, inventory, topology, integration (12 roles)

### 🤖 Infrastructure Automation (1 platform)
- **Ansible Automation Platform** - Controller, AAP components, CI/CD, inventory, secrets (17 roles)

### 🏭 Operational Technology (1 platform)
- **OT/ICS** - Firewall, IDPS, logging, firmware, compliance (24 roles)

### 📋 Special Frameworks (1 framework)
- **Policy as Code** - NIST 800-53 and DoD STIG compliance automation

## Repository Layout

The repository is organized by technology platform with consistent structure:

```text
Ansible-Playbooks-2.0/
├── README.md                      # This file - main repository guide
│
├── ansible/                       # Ansible Automation Platform (17 roles)
│   ├── README.md
│   ├── roles/
│   └── tasks/
│
├── arista/                        # Arista EOS networking (6 roles)
│   ├── README.md
│   ├── roles/
│   └── tasks/
│
├── aws/                           # Amazon Web Services (40+ roles) ⭐ NEW
│   ├── README.md
│   ├── roles/
│   ├── playbooks/
│   └── tasks/
│
├── checkpoint/                    # Check Point firewalls (6 roles)
│   ├── README.md
│   ├── roles/
│   └── tasks/
│
├── checkpoint/                    # Check Point firewalls (6 roles)
│   ├── README.md
│   ├── cp_day0_deploy_configure/  # Day-0 deployment framework
│   ├── roles/
│   └── tasks/
│
├── cisco/                         # Cisco ISE & UCS (33 roles)
│   ├── README.md
│   ├── roles/
│   └── tasks/
│
├── claroty/                       # Claroty OT security (11 roles)
│   ├── README.md
│   └── roles/
│
├── cohesity/                      # Cohesity backup
│   └── tasks/
│
├── dragos/                        # Dragos OT monitoring (12 roles)
│   ├── README.md
│   └── roles/
│
├── google_cloud_platform/         # GCP (28 roles)
│   ├── README.md
│   ├── roles/
│   └── tasks/
│
├── illumio/                       # Illumio micro-segmentation (3 roles)
│   ├── README.md
│   ├── roles/
│   ├── playbooks/
│   └── tasks/
│
├── infoblocks/                    # Infoblox DNS/DHCP (10 roles)
│   ├── README.md
│   ├── day0_deploy_config/        # Day-0 deployment framework
│   ├── roles/
│   └── tasks/
│
├── kubernetes/                    # Kubernetes cluster mgmt (4 roles)
│   ├── README.md
│   ├── roles/
│   ├── playbook-cluster-hardening.yml
│   ├── playbook-deploy-app.yml
│   └── playbook-full-setup.yml
│
├── openshift/                     # Red Hat OpenShift (45 roles)
│   ├── README.md
│   ├── roles/
│   └── tasks/
│
├── operational_technology/        # OT/ICS (24 roles)
│   ├── README.md
│   └── roles/
│
├── palo_alto/                     # Palo Alto Networks (10 roles)
│   ├── README.md
│   ├── roles/
│   ├── playbooks/
│   └── tasks/
│
├── policy_as_code/                # Policy as Code framework
│   ├── README.md
│   ├── DEPLOYMENT_GUIDE.md
│   ├── IMPLEMENTATION_SUMMARY.md
│   ├── site.yml                   # Master playbook
│   ├── policies/                  # NIST control implementations
│   │   ├── access_control/
│   │   ├── identification_auth/
│   │   ├── audit_accountability/
│   │   └── system_communications/
│   ├── library/                   # Reusable policy modules
│   ├── tests/                     # Policy validation tests
│   ├── artifacts/                 # Compliance reports
│   └── inventory/                 # Example inventories
│
├── pure/                          # Pure Storage (7 roles)
│   ├── README.md
│   └── roles/
│
├── rhel/                          # Red Hat Enterprise Linux (5 roles)
│   ├── README.md
│   ├── roles/
│   └── requirements.yml
│
├── sciencelogic/                  # ScienceLogic SL1 (31 roles)
│   ├── README.md
│   ├── roles/
│   └── tasks/
│
├── splunk/                        # Splunk logging (5 roles)
│   ├── README.md
│   ├── roles/
│   └── playbooks/
│
├── vast/                          # VAST Data storage (4 roles)
│   ├── README.md
│   ├── roles/
│   └── inventories/
│
├── veeam/                         # Veeam backup (6 roles) ⭐ ENHANCED
│   ├── README.md
│   ├── roles/
│   └── playbooks/
│
├── vmware/                        # VMware vSphere + NSX-T (35+ roles) ⭐ ENHANCED
│   ├── README.md
│   ├── roles/
│   └── tasks/
│
└── windows/                       # Windows Server (20+ roles) ⭐ NEW
    ├── README.md
    ├── roles/
    ├── playbooks/
    └── tasks/
```

Each technology directory contains:
- **README.md** - Technology-specific documentation and usage guides
- **roles/** - Ansible roles organized by function
- **tasks/** - Standalone task files for common operations
- **playbooks/** - Example and production playbooks
- **templates/** - Jinja2 templates for configuration files
- **inventory/** - Example inventory configurations (when applicable)

## Key Features

### 🛡️ Security & Compliance First
- **DoD STIG** implementations for Kubernetes, VMware ESXi, Cisco UCS, RHEL, and OT systems
- **NIST 800-53 Rev 5** control families: AC, IA, AU, SC, CM, SI, PE, CP, IR
- **NIST 800-171** for Controlled Unclassified Information (CUI) protection
- **FedRAMP** and **FISMA** baselines for cloud platforms
- **CIS Benchmarks** for Kubernetes, OpenShift, and RHEL

### 🏗️ Production-Ready Operations
- **Day-0/Day-1 Deployment** - Complete initial configuration frameworks for Check Point and Infoblox
- **Disaster Recovery** - Backup, restore, and failover automation
- **Monitoring & Alerting** - Integration with ScienceLogic, Dragos, Splunk
- **Change Management** - Maintenance window guards, change validation
- **Backup & Recovery** - Veeam, Cohesity, Pure Storage, VAST Data integration

### 🏭 Operational Technology (OT/ICS) Security
- **Dragos Integration** - Threat detection, inventory management, topology mapping
- **Claroty Integration** - OT security, secure remote access, asset management
- **Network Segmentation** - Firewall policies, IDPS, DMZ configurations
- **Firmware Management** - Secure update procedures with rollback capabilities
- **Compliance Automation** - OT-specific STIG and NIST controls

### 🌐 Multi-Cloud & Hybrid Infrastructure
- **GCP Landing Zones** - Secure project structure with IAM, VPC, and compliance
- **VMware vSphere** - Complete datacenter automation with STIG hardening
- **Kubernetes/OpenShift** - Container orchestration with security hardening
- **Hybrid Networking** - VPN, service mesh, network policies

### 📊 Enterprise Monitoring & Observability
- **ScienceLogic SL1** - 31 roles for comprehensive monitoring
- **Splunk Integration** - Log forwarding, security event monitoring
- **Metrics Collection** - Custom dashboards, KPIs, reporting
- **Audit & Compliance Reporting** - Automated artifact generation

## Policy as Code Framework

The `policy_as_code/` directory contains a comprehensive framework for implementing **NIST 800-53** and **DoD STIG** controls as executable Ansible code.

### Implemented Control Families

| NIST Control | Description | Policy File | STIG Findings | Severity |
|--------------|-------------|-------------|---------------|----------|
| **IA-5** | Password Policy | `identification_auth/password_policy.yml` | V-230502, V-230503, V-230505, V-230507, V-230509 | Cat I |
| **AC-12** | Session Timeout | `access_control/session_timeout.yml` | V-230286, V-230287 | Cat II |
| **AU-2, AU-12** | Audit Logging | `audit_accountability/audit_logging.yml` | V-230315, V-230316, V-230317, V-230318 | Cat II |
| **SC-8, SC-13** | Cryptographic Protection | `system_communications/cryptographic_protection.yml` | V-230273, V-230274, V-230275, V-230276, V-230277 | Cat I |

### Policy Enforcement

**Dry-run (Check mode - safe, default):**
```bash
ansible-playbook policy_as_code/site.yml -i inventory/production.yml
```

**Apply all policies:**
```bash
ansible-playbook policy_as_code/site.yml -i inventory/production.yml -e "apply_changes=true"
```

**Apply specific control family:**
```bash
ansible-playbook policy_as_code/site.yml -i inventory/production.yml -e "apply_changes=true" --tags nist_ia
```

**Apply only Category I (High) findings:**
```bash
ansible-playbook policy_as_code/site.yml -i inventory/production.yml -e "apply_changes=true" --tags stig_cat1
```

### Compliance Artifacts

The framework automatically generates compliance artifacts in JSON format:
- **Configuration snapshots** before/after policy application
- **STIG finding verification** with pass/fail status
- **NIST control mapping** with implementation evidence
- **Compliance reports** in HTML format
- **SHA-256 checksums** for audit trail integrity

See `policy_as_code/DEPLOYMENT_GUIDE.md` for detailed deployment procedures.

## Conventions and Best Practices

### General Principles

- **Idempotency First** - All playbooks should be safe to run multiple times without adverse effects
- **Check Mode Support** - Use `--check` for dry-runs before applying changes to production
- **Limited Scope** - Use `--limit` for phased rollouts (single host → group → all)
- **Tags for Granular Control** - Every task should have meaningful tags for selective execution
- **Documentation** - Each role/playbook directory must have a README.md

### Execution Patterns

**API-Based Automation:**
```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  tasks:
    - name: Configure firewall via API
      paloaltonetworks.panos.panos_security_rule:
        # API-based module
```

**Agent-Based Automation:**
```yaml
- hosts: linux_servers
  become: true
  gather_facts: true
  tasks:
    - name: Configure system
      ansible.builtin.package:
        # Runs on remote host
```

### Security Best Practices

1. **Never commit secrets** - Use Ansible Vault or external secret managers
2. **Use dedicated automation accounts** with least privilege
3. **Enable audit logging** for all automation runs
4. **Implement change approval workflows** for production
5. **Test in non-production first** - Always validate in test/dev environments
6. **Maintain rollback procedures** - Document and test recovery steps

### Module Selection Hierarchy

1. **Official vendor collections** (e.g., `paloaltonetworks.panos`, `purestorage.flasharray`)
2. **Certified collections** from Ansible Galaxy
3. **Community collections** with active maintenance
4. **URI module** as last resort for API calls
5. **Avoid shell/command modules** unless absolutely necessary

### Change Management

For playbooks that can make breaking changes:

- **Configuration commits** - Require explicit confirmation in production
- **System reboots** - Schedule maintenance windows and notify stakeholders
- **Network changes** - Validate connectivity before/after, maintain out-of-band access
- **Firewall rules** - Test with logging first, then enforce
- **Certificate updates** - Verify validity dates and trust chains

### Testing Strategy

```bash
# 1. Syntax check
ansible-playbook playbook.yml --syntax-check

# 2. Dry-run (check mode)
ansible-playbook playbook.yml --check --diff

# 3. Single host validation
ansible-playbook playbook.yml --limit test-host01

# 4. Small group rollout
ansible-playbook playbook.yml --limit test-group

# 5. Full deployment
ansible-playbook playbook.yml
```

## Execution Environments & dependencies

For reproducible runs and CI, build or use an Execution Environment (EE) that includes required collections and Python packages. Maintain a `requirements.yml` or `collections/requirements.yml` for Ansible Galaxy collections and a `requirements.txt` or `pyproject.toml` for Python packages.

Example `collections/requirements.yml`:

```yaml
- name: paloaltonetworks.panos
  version: 2.0.0
- name: purestorage.flasharray
  version: 1.0.0
```

Build/pull this into your EE or run `ansible-galaxy collection install -r collections/requirements.yml` on the control host.

## Credentials and secrets

- Store passwords, API keys, and tokens in Ansible Vault or an external secrets manager.
- Use dedicated automation accounts with least privilege and monitor/rotate credentials regularly.
- Example usage (group_vars):

```yaml
# group_vars/env.yml
ansible_user: automation
ansible_password: "{{ vault_automation_password }}"
api_key: "{{ vault_api_key }}"
```

## Running playbooks (tips and examples)

- Dry-run: `ansible-playbook playbook.yml --check --diff` (note: not all modules support check mode)
- Limit target scope: `ansible-playbook playbook.yml --limit firewall01`
- Use `--tags` and `tags:` on tasks to target small changes during rollouts.

Example (run a vendor playbook from repo root):

```bash
ansible-playbook palo_alto/playbooks/panos_create_object.yml -i inventories/prod.ini --ask-vault-pass
```

## Testing and CI Guidance

### Automated Testing

This repository includes multiple test frameworks:

**YAML Syntax Validation:**
```bash
# Validate all YAML files
find . -name "*.yml" -o -name "*.yaml" | xargs yamllint

# Or use Python
python3 -c "import yaml, sys; yaml.safe_load(open(sys.argv[1]))" playbook.yml
```

**Ansible Linting:**
```bash
# Lint playbooks and roles
ansible-lint playbook.yml
ansible-lint roles/*/
```

**Playbook Syntax Check:**
```bash
# Check playbook syntax
ansible-playbook playbook.yml --syntax-check
```

**Molecule Testing (for roles):**
```bash
cd roles/role-name
molecule test
```

### Continuous Integration

Recommended CI pipeline stages:

1. **Lint Stage** - YAML, Markdown, and Ansible linting
2. **Syntax Check Stage** - Validate all playbooks
3. **Dry-Run Stage** - Run playbooks in check mode against test inventory
4. **Integration Test Stage** - Deploy to lab environment
5. **Compliance Scan Stage** - Verify STIG/NIST controls

### Test Environments

Each technology should have:
- **Development** - Frequent changes, rapid testing
- **Test/QA** - Pre-production validation
- **Production** - Controlled deployments with change management

## Compliance and Security

### DoD Security Technical Implementation Guides (STIGs)

Implemented STIG controls for:

| Platform | STIG Version | Category I | Category II | Category III | Total Findings |
|----------|--------------|------------|-------------|--------------|----------------|
| **Kubernetes** | V1R11 | 15 | 28 | 12 | 55 |
| **VMware ESXi** | V1R1 | 8 | 45 | 10 | 63 |
| **Cisco IOS** | V2R7 | 12 | 38 | 15 | 65 |
| **RHEL 8** | V1R14 | 22 | 98 | 45 | 165 |
| **OT Systems** | Custom | 10 | 25 | 8 | 43 |

### NIST 800-53 Rev 5 Control Families

Implemented controls across:
- **AC** - Access Control (11 controls)
- **AU** - Audit and Accountability (8 controls)
- **IA** - Identification and Authentication (7 controls)
- **SC** - System and Communications Protection (9 controls)
- **CM** - Configuration Management (6 controls)
- **SI** - System and Information Integrity (5 controls)
- **CP** - Contingency Planning (4 controls)
- **IR** - Incident Response (3 controls)

### NIST 800-171 for CUI Protection

Specialized implementations for Fourth Estate organizations handling Controlled Unclassified Information:
- Enhanced access controls
- Cryptographic protection requirements
- Audit logging and monitoring
- Incident response procedures
- Personnel security requirements

### FedRAMP Compliance

Cloud platform roles (GCP, OpenShift) include FedRAMP baseline controls:
- **FedRAMP Low** - 125 controls
- **FedRAMP Moderate** - 325 controls
- **FedRAMP High** - 421 controls

### Compliance Reporting

Generate compliance reports:

```bash
# Policy as Code compliance report
ansible-playbook policy_as_code/site.yml -i inventory/prod.yml --tags compliance_check

# STIG verification for Kubernetes
ansible-playbook kubernetes/playbook-cluster-hardening.yml --tags stig_verify

# NIST control verification
ansible-playbook policy_as_code/site.yml --tags nist_verify
```

Reports include:
- Current vs. required configuration state
- Pass/fail status for each control
- Remediation recommendations
- Artifact generation with checksums
- HTML dashboards for management reporting

## Contribution Guidelines

### Pull Request Process

1. **Fork the repository** and create a feature branch
2. **Update documentation** - Add/update README files for new roles
3. **Test thoroughly** - Include test results in PR description
4. **Follow conventions** - Match existing code style and structure
5. **Update CHANGELOG** - Document your changes
6. **No secrets** - Use placeholders for credentials

### Code Review Criteria

- ✅ Idempotent tasks (safe to run multiple times)
- ✅ Comprehensive documentation
- ✅ Tags for selective execution
- ✅ Error handling and validation
- ✅ STIG/NIST compliance alignment (where applicable)
- ✅ Test coverage (molecule, playbook checks)
- ✅ Security best practices (no hardcoded credentials)

### Branch Naming

- `feature/technology-name-feature-description`
- `fix/technology-name-bug-description`
- `docs/technology-name-doc-update`
- `stig/technology-name-finding-vxxxxxx`

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:** feat, fix, docs, style, refactor, test, chore, stig, nist

**Examples:**
```
feat(cisco-ucs): Add fabric interconnect configuration role
fix(vmware): Correct vSAN STIG finding V-230273
docs(policy_as_code): Update deployment guide with rollback procedures
stig(kubernetes): Implement STIG finding V-242376 for pod security
```

## Where to Get Help

### Documentation

- **Technology-specific README files** - See `<technology>/README.md` for each platform
- **Policy as Code Guide** - `policy_as_code/DEPLOYMENT_GUIDE.md`
- **Role documentation** - Each role has a dedicated README with variables and examples

### Vendor Documentation

Consult official vendor documentation:
- **Cisco ISE:** [Cisco ISE Configuration Guide](https://www.cisco.com/c/en/us/support/security/identity-services-engine/series.html)
- **VMware vSphere:** [VMware Documentation](https://docs.vmware.com/)
- **Palo Alto Networks:** [PAN-OS Administrator's Guide](https://docs.paloaltonetworks.com/)
- **Kubernetes:** [Kubernetes Documentation](https://kubernetes.io/docs/)
- **Red Hat OpenShift:** [OpenShift Documentation](https://docs.openshift.com/)
- **Google Cloud Platform:** [GCP Documentation](https://cloud.google.com/docs)

### Compliance Resources

- **NIST 800-53 Rev 5:** [NIST SP 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- **NIST 800-171:** [NIST SP 800-171](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- **DoD STIGs:** [DISA STIG Library](https://public.cyber.mil/stigs/)
- **FedRAMP:** [FedRAMP.gov](https://www.fedramp.gov/)
- **CIS Benchmarks:** [CIS Center for Internet Security](https://www.cisecurity.org/cis-benchmarks/)

### Support Channels

- **GitHub Issues** - Report bugs or request features
- **Pull Requests** - Contribute improvements
- **Discussions** - Ask questions and share knowledge

---

## 🎉 Phase 1 Implementation Complete (January 2026)

Phase 1 of the repository enhancement roadmap has been successfully completed, adding critical infrastructure automation capabilities:

### ⭐ New Platforms Added (70+ new roles)

1. **Amazon Web Services (AWS)** - 40+ roles
   - Complete AWS automation across IAM, VPC, EC2, EKS, S3, RDS, Lambda, and more
   - FedRAMP compliance controls for AWS GovCloud
   - Comprehensive security with KMS encryption, GuardDuty, Security Hub

2. **Microsoft Windows Server** - 20+ roles
   - DoD STIG hardening automation
   - Active Directory domain services
   - Group Policy management and enforcement
   - DHCP/DNS, IIS, Windows Server Backup, WSUS

3. **VMware NSX-T Software-Defined Networking** - 8+ roles
   - NSX-T Manager deployment
   - Distributed firewall and security policies
   - Load balancer configuration
   - Network segments and Tier-0/Tier-1 gateways

### 🔧 Enhanced Platforms (12+ new roles)

1. **Veeam Backup & Replication** - 6 roles (previously tasks only)
   - Backup server installation
   - Backup job configuration
   - Restore operations automation
   - Replication and cloud tier setup

2. **Cohesity Data Platform** - 6 roles (previously tasks only)
   - Cluster configuration
   - Protection policy management
   - Recovery workflows
   - Cloud archive configuration

### 🔄 CI/CD Pipeline Implemented

- **GitHub Actions Workflows:**
  - `lint.yml` - YAML, Ansible, Markdown, and shell script linting
  - `syntax-check.yml` - Ansible playbook syntax validation
  - `security-scan.yml` - Secret scanning, dependency checks, compliance verification
- **Linter Configurations:** `.yamllint.yml` and `.markdownlint.json`
- **Automated Testing:** Multi-platform syntax checking across all technologies

### 📈 Updated Repository Statistics

- **Total Roles:** 360+ (was 288+)
- **Technology Platforms:** 28+ (was 25+)
- **Operating Systems:** RHEL + Windows Server
- **Cloud Platforms:** AWS + GCP + VMware vSphere
- **CI/CD:** Fully automated testing pipeline

---

## 🚀 Phase 2 Implementation Complete (January 2026)

Phase 2 of the repository enhancement roadmap has been successfully completed, adding enterprise-critical platforms and significantly expanding automation coverage:

### ⭐ New Platforms Added (111+ new roles)

1. **Microsoft Azure** - 45+ roles
   - Complete Azure automation: Azure AD, VNets, VMs, AKS, Key Vault
   - Security: Azure Sentinel SIEM, Security Center, Defender for Cloud
   - Government: Azure Government Cloud with FedRAMP compliance
   - Databases: SQL Database, Cosmos DB, PostgreSQL, MySQL

2. **Database Automation** - 24 roles across 3 platforms
   - **PostgreSQL** (8 roles) - Installation, replication, pgPool, Barman backup
   - **MySQL/MariaDB** (8 roles) - Installation, replication, Galera cluster, XtraBackup
   - **Oracle Database** (8 roles) - Installation, Data Guard, RAC, RMAN, Flashback

3. **NetApp ONTAP Storage** - 12 roles
   - Cluster and SVM management
   - Volume/LUN provisioning, NFS/CIFS shares
   - SnapMirror replication and SnapVault backup
   - Performance tuning and security hardening

4. **Fortinet FortiGate** - 12 roles
   - System configuration and firewall policies
   - IPsec and SSL VPN configuration
   - High availability and routing
   - Security profiles (IPS, AV, Web Filter)

5. **Monitoring Stack** - 18 roles across 2 platforms
   - **Prometheus/Grafana** (8 roles) - Metrics collection, alerting, dashboarding
   - **ELK Stack** (10 roles) - Elasticsearch, Logstash, Kibana, Filebeat, Metricbeat

### 🔐 Expanded Policy as Code (14+ new policies)

Added 4 new NIST 800-53 control families:
- **Configuration Management (CM)** - CM-2, CM-3, CM-6, CM-7
- **System & Information Integrity (SI)** - SI-2, SI-3, SI-4, SI-7
- **Incident Response (IR)** - IR-4, IR-5, IR-6
- **Contingency Planning (CP)** - CP-2, CP-9, CP-10

Total Policy as Code coverage: **8 control families**, **18+ policies**

### 📈 Updated Repository Statistics

**Before Phase 2:**
- 360 roles
- 28+ technologies
- 3 cloud platforms
- 1 database platform

**After Phase 2:**
- **470+ roles** (+110 roles, +31% growth)
- **34+ technologies** (+6 platforms)
- **4 cloud platforms** (AWS, Azure, GCP, vSphere)
- **4 database platforms** (PostgreSQL, MySQL, Oracle, + cloud DBs)
- **3 storage platforms** (Pure, VAST, NetApp)
- **2 monitoring stacks** (Prometheus/Grafana, ELK)
- **8 NIST control families** in Policy as Code

---

## Quick Start Examples

### Example 1: Deploy Kubernetes Cluster with STIG Hardening

```bash
# 1. Review the playbook
cat kubernetes/playbook-cluster-hardening.yml

# 2. Dry-run to see what will change
ansible-playbook kubernetes/playbook-cluster-hardening.yml -i inventory/k8s.yml --check

# 3. Apply STIG hardening
ansible-playbook kubernetes/playbook-cluster-hardening.yml -i inventory/k8s.yml

# 4. Verify STIG compliance
ansible-playbook kubernetes/playbook-cluster-hardening.yml -i inventory/k8s.yml --tags stig_verify
```

### Example 2: Apply NIST 800-53 Password Policy

```bash
# 1. Review policy documentation
cat policy_as_code/policies/identification_auth/password_policy.yml

# 2. Dry-run (default mode)
ansible-playbook policy_as_code/site.yml -i inventory/prod.yml --tags nist_ia_5

# 3. Apply password policy to production
ansible-playbook policy_as_code/site.yml -i inventory/prod.yml -e "apply_changes=true" --tags nist_ia_5

# 4. Review compliance artifacts
ls -la /tmp/policy-artifacts/
```

### Example 3: Configure Cisco UCS for Fourth Estate

```bash
# 1. Review Cisco UCS documentation
cat cisco/README.md

# 2. Set up inventory
cp cisco/inventory.example cisco/inventory/production.yml
vi cisco/inventory/production.yml

# 3. Deploy Fourth Estate configuration
ansible-playbook cisco/ucs_fourth_estate_production.yml -i cisco/inventory/production.yml --ask-vault-pass
```

### Example 4: VMware vSphere STIG Hardening

```bash
# 1. Review VMware STIG roles
ls -la vmware/roles/

# 2. Run ESXi hardening playbook
ansible-playbook vmware/playbooks/esxi_stig_hardening.yml -i inventory/vmware.yml --check

# 3. Apply hardening
ansible-playbook vmware/playbooks/esxi_stig_hardening.yml -i inventory/vmware.yml
```

---

**Repository Maintained By:** Fourth Estate Infrastructure Team
**Classification:** UNCLASSIFIED
**Last Updated:** 2026-01-15
**License:** See LICENSE file

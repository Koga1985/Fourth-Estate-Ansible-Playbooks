# Changelog

All notable changes to this repository are documented here.

---

## [Unreleased]

### Added
- `CUSTOMER_QUICK_START.md` — step-by-step first-run guide for new customers
- `KNOWN_LIMITATIONS.md` — documented non-idempotent tasks, version constraints, and platform caveats
- `TROUBLESHOOTING.md` — common errors and resolution steps
- `CHANGELOG.md` — this file

### Changed
- `README.md` — added links to new documentation files in Table of Contents and "Where to Get Help"

### Fixed
- `policy_as_code/DEPLOYMENT_GUIDE.md` — replaced `example.mil` placeholder hostnames and URLs with clearly marked `<your-value>` placeholders

### Security
- Added `no_log: true` to 954 tasks across 322 files that handle passwords, tokens, API keys, and other credentials, preventing sensitive values from appearing in Ansible logs and AWX/Tower job output
- Added `changed_when: false` to 66 literal `state: query` tasks to prevent false change reports; added `changed_when: not (apply_changes | bool)` to 49 conditional state tasks so changes are only reported when `apply_changes=true`
- Added `any_errors_fatal: true` to 106 plays across 72 playbook and site.yml files, ensuring a hard stop on task failure rather than partial-state continuation into subsequent plays

---

## [Phase 4] — 2026-01

### Added
- **F5 BIG-IP** automation — LTM virtual servers, iRules, pool management, SSL offloading, WAF policies, STIG hardening (5 roles)
- **Tenable Security Center** — asset discovery, scan policies, remediation workflows, compliance reporting, vulnerability management (5 roles)
- **ServiceNow CMDB** — CI discovery and population, CMDB configuration, incident/change management integration (2 roles)
- **HashiCorp Vault** — cluster deployment, secrets engines (KV, PKI, AWS, database), auth methods, policy management (3 roles)
- **Ansible Tower / AAP** — job templates, workflow automation, credential management, RBAC, execution environments (3 roles)

### Changed
- Expanded Policy as Code to cover all 8 NIST 800-53 control families
- Enhanced compliance artifact generation across all new roles

---

## [Phase 3] — 2026-01

### Added
- **Azure** infrastructure automation — VMs, VNets, NSGs, AKS clusters, Azure AD, Key Vault, storage, monitoring (30+ roles)
- **Database platforms** — PostgreSQL (primary/replica/pgPool), MySQL (primary/replica/ProxySQL), Oracle (RAC/ASM/Data Guard) (12+ roles)
- **NetApp ONTAP** — cluster setup, SVM management, volume provisioning, SnapMirror, QoS (3 roles)
- **Fortinet FortiGate** — system configuration, security profiles, VPN, SD-WAN, HA (1 role)
- **Prometheus + Grafana** — full observability stack with alerting and dashboards (1 role)
- **ELK Stack** — Elasticsearch, Logstash, Kibana deployment and configuration (1 role)
- Policy as Code expanded to include 8 NIST 800-53 control families

---

## [Phase 2] — 2026-01

### Added
- **AWS** infrastructure automation — EC2, VPC, IAM, S3, RDS, EKS, Lambda, CloudWatch, Config, GuardDuty (40+ roles)
- **Windows Server** — domain controllers, IIS, SQL Server, file servers, STIG hardening (20+ roles)
- **VMware NSX-T** — micro-segmentation, distributed firewall, load balancing, VPN (8 roles)
- **Veeam Backup** expanded from task files to full role structure with Windows deployment automation
- **Cohesity** expanded from task files to full role structure with VMware integration

---

## [Phase 1] — 2025-12

### Added
Initial repository creation with core platforms:

- **Cisco ACI** — fabric deploy, tenant config, network config, security hardening, monitoring (5 roles)
- **Cisco ISE** — 28 roles covering policy, profiling, posture, guest, BYOD, pxGrid, reporting, operations
- **Cisco UCS** — infrastructure, networking, security hardening, backup/DR, monitoring (5 roles)
- **Cisco CyberVision** — OT sensor deployment and management
- **VMware vSphere** — vCenter install/config, ESXi config, cluster management, networking, storage, VM provisioning, snapshots, STIG hardening (19+ roles)
- **Palo Alto Networks** — PAN-OS baseline, security policies, NAT, VPN, QoS, STIG hardening, Panorama (10 roles)
- **Check Point** — firewall deployment, access policies, threat prevention, VPN, identity awareness (6 roles)
- **Arista EOS** — switch baseline, CVP integration, routing, fabric config (6 roles)
- **Illumio** — PCE installation, policy lifecycle, VEN fleet management, reporting (3 roles)
- **Infoblox** — DNS/DHCP grid, bootstrap, DHCP config, DNS config, views/zones, DNSSEC, RPZ (10 roles)
- **VAST Data** — cluster config, security hardening, monitoring, backup/DR (4 roles)
- **Pure Storage FlashArray/FlashBlade** — provisioning, integrations, security (3 roles)
- **NetApp** (initial) — basic provisioning tasks
- **RHEL** — system hardening, user access, AIDE, audit, STIG compliance
- **Kubernetes** — cluster setup, RBAC, network policies, STIG hardening, backup (Velero)
- **OpenShift** — cluster configuration and security
- **Splunk** — enterprise install, forwarder deployment, STIG hardening
- **ScienceLogic SL1** — platform install, configuration
- **CrowdStrike Falcon** — sensor deployment (Linux, Windows, macOS)
- **SentinelOne** — agent deployment (Linux, Windows)
- **Dragos** — OT platform deployment
- **Claroty** — OT security and inventory
- **Operational Technology (OT/ICS)** — multi-vendor OT hardening
- **Ansible Controller** — execution environment management
- **Ansible Tower** (initial) — basic tower automation
- **Policy as Code** — NIST 800-53 control enforcement framework (initial 4 control families)
- **COMPLIANCE_MAPPING.md** — NIST 800-53 Rev 5 and DISA STIG cross-reference

---

## Version Policy

This repository uses a phase-based versioning model reflecting major
capability additions. Individual role bug fixes and enhancements are
tracked by commit history.

For questions about specific changes, review the git log:

```bash
git log --oneline --since="2026-01-01"
git log --oneline -- cisco/roles/aci_tenant_config/
```

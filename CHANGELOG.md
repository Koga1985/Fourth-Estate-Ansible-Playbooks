# Changelog

All notable changes to the Fourth Estate Ansible Playbooks are documented here.
The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [2026-06-30] — Dynatrace platform expansion (Tier C)

Grew the `dynatrace/` platform from 12 to **17 roles** (operational lifecycle,
DR, and remaining tenant-config surfaces):

- `dynatrace_oneagent_lifecycle` — fleet lifecycle for installed OneAgents:
  version assessment, host-group/network-zone/monitoring-mode reconfigure via
  `oneagentctl`, service restart, and a **double-gated** decommission/uninstall
  (requires `apply_changes=true` **and** `oneagent_decommission=true`).
- `dynatrace_config_backup` — read-only export of tenant Config API + Settings 2.0
  objects to timestamped JSON (DR / change-audit) with a manifest artifact.
- `dynatrace_synthetic_locations` — manage private synthetic locations (ActiveGate
  synthetic capability), assess + data-driven apply.
- `dynatrace_cloud_integrations` — manage AWS/Azure/GCP monitoring connectors,
  assess + data-driven apply.
- `dynatrace_extensions` — Extension Framework 2.0 install/activate, assess +
  data-driven apply.
- `dynatrace/site.yml` extended: opt-in `dynatrace_oneagent_lifecycle` and
  `dynatrace_config_backup` plays (gated via `enabled_components`), and the three
  new config roles added to the tenant-config play.

All safe-by-default (`apply_changes=false` assesses/reports; tokens `no_log`).
Repository totals updated: **619 roles**, **3,920 YAML files**, **44 platforms**.

## [2026-06-30] — Dynatrace platform expansion (Tier A + B)

Grew the `dynatrace/` platform from 4 to **12 roles** + a master `site.yml`:

- **Tier A** — `dynatrace_kubernetes` (DynaKube on K8s/OpenShift), `dynatrace_iam`
  (Account Management groups/users/policies, NIST AC-2/AC-6), `dynatrace_monitoring_as_code`
  (SLOs/synthetic monitors/dashboards), `dynatrace_notifications` (ServiceNow/Slack/etc.).
- **Tier B** — `dynatrace_data_privacy` (PII/IP masking, SC-28/SI-12),
  `dynatrace_log_monitoring` (log masking/storage, AU-9/SC-28), `dynatrace_appsec`
  (runtime vulnerability + attack protection, SA-11/RA-5), `dynatrace_audit_export`
  (audit log → NDJSON evidence + SIEM forward, AU-6/AU-9/AU-11).
- `dynatrace/site.yml` sequences deploy → config → security/compliance → IAM.

Repository totals updated: **607 roles**, **3,895 YAML files**, **44 platforms**.

## [2026-06-30] — Dynatrace platform

Added the **`dynatrace/`** observability platform (4 roles), following the
monitoring-platform deployment + NIST-aligned security pattern (no DISA STIG
exists for Dynatrace):

- `dynatrace/roles/dynatrace_oneagent` — deploy/configure OneAgent (Linux/Windows), idempotent via `oneagentctl`.
- `dynatrace/roles/dynatrace_activegate` — deploy ActiveGate (group / network zone).
- `dynatrace/roles/dynatrace_tenant_config` — tenant config via Config/Settings 2.0 APIs (assessment + data-driven apply).
- `dynatrace/roles/dynatrace_security_hardening` — NIST 800-53 (AC/AU/IA/SC) posture assessment + hardening (token hygiene, audit-log access, IP restrictions).

All safe-by-default (`apply_changes=false` assesses/reports; tokens `no_log`).
Repository totals updated: **599 roles**, **3,854 YAML files**, **44 platforms**.

## [2026-06-29] — Tier 3 STIG expansion (network / endpoint / database)

Added 6 more dedicated STIG roles (1 new platform: `juniper/`, plus `databases/mongodb/`):

- `juniper/roles/junos_stig` — Juniper Junos STIG (NDM `JUNI-ND-*` + Router `JUNI-RT-*`) via `junipernetworks.junos`.
- `cisco/roles/cisco_ios_xe_router_stig` — Cisco IOS XE Router STIG (`CISC-RT-*`) via `cisco.ios`.
- `splunk/roles/splunk_enterprise_stig` — Splunk Enterprise STIG (`SPLK-CL-*`) via `community.general.ini_file`.
- `windows/roles/win11_stig` — Windows 11 STIG (`WN11-*`) via `ansible.windows`.
- `windows/roles/win_browsers_stig` — Edge/Chrome/Firefox STIGs (`EDGE-00-*`, `DTBC-*`, `DTBF-*`) via `win_regedit`.
- `databases/mongodb/roles/mongodb_stig` — MongoDB Enterprise STIG (`mongod.conf`).

Repository totals updated: **595 roles**, **3,830 YAML files**, **43 platforms**, **39 dedicated STIG/SRG roles**.

## [2026-06-28] — Tier 2 STIG expansion (operating systems & databases)

Added 7 more dedicated STIG roles (1 new platform: `ubuntu/`, plus `databases/mssql/`):

- `rhel/roles/rhel8_stig` — RHEL 8 STIG (`RHEL-08-*`) via `ansible.builtin`/`ansible.posix`.
- `ubuntu/roles/ubuntu2204_stig` — Ubuntu 22.04 LTS STIG (`UBTU-22-*`) via apt/ufw/apparmor/faillock/sysctl.
- `windows/roles/win_server2019_stig` — Windows Server 2019 STIG (`WN19-*`) via `ansible.windows`.
- `databases/postgresql/roles/postgresql_stig` — PostgreSQL STIG (`PGS9-00-*`) via `community.postgresql`.
- `databases/mysql/roles/mysql80_stig` — MySQL 8.0 STIG via `community.mysql`.
- `databases/oracle/roles/oracle_db_stig` — Oracle Database STIG (`O121-*`) via sqlplus.
- `databases/mssql/roles/mssql_stig` — SQL Server STIG (`SQL6-D0-*`) via `community.general.mssql_script`.

Repository totals updated: **589 roles**, **3,785 YAML files**, **42 platforms**, **33 dedicated STIG/SRG roles**.

## [2026-06-27] — Tier 1 STIG expansion (network/web/virtualization)

Added 5 more dedicated STIG roles on top of existing vendor platforms, same
safe-by-default contract (assessment/dry-run first, per-host JSON artifact):

- `palo_alto/roles/panos_stig` — Palo Alto PAN-OS NDM STIG (`PANW-NM-*`) via `paloaltonetworks.panos`.
- `fortinet/roles/fortigate_stig` — FortiGate Firewall STIG (`FGFW-ND-*`) via `fortinet.fortios`.
- `f5_bigip/roles/f5_bigip_stig` — F5 BIG-IP Device Management STIG (`F5BI-DM-*`) via `f5networks.f5_modules`.
- `windows/roles/win_iis10_stig` — Microsoft IIS 10.0 Server + Site STIG (`IISW-SV-*`, `IISW-SI-*`) via `ansible.windows`.
- `vmware/roles/vsphere8_stig` — VMware vSphere 8 STIG, ESXi 8 (`ESXI-80-*`) + vCenter 8 (`VCSA-80-*`) via `community.vmware`.

Repository totals updated: **582 roles**, **3,734 YAML files**, **26 dedicated STIG/SRG roles**.

## [2026-06-26] — DoD STIG / SRG expansion

Added **21 dedicated DoD STIG / SRG roles** across **5 new platform areas**. Every
runnable role is **safe by default** (`apply_changes=false` / assessment mode runs
in check mode and writes a per-host JSON evidence artifact; pass
`-e apply_changes=true` to enforce). See
[STIG_COVERAGE_MATRIX.md](./STIG_COVERAGE_MATRIX.md) for the full mapping of every
requested benchmark to its role/status.

### Added — Cisco network device STIGs (`cisco/roles/`)
- `cisco_ios_xe_l2_stig` — IOS XE Catalyst as a Layer-2 device (L2S `CISC-L2-*` + NDM `CISC-ND-*`), `cisco.ios`.
- `cisco_nxos_stig` — Nexus NX-OS Switch STIG (NDM + L2), `cisco.nxos`.
- `cisco_asa_stig` — ASA NDM (`CASA-ND-*`) + Firewall (`CASA-FW-*`), `cisco.asa`.
- `cisco_ftd_stig` — Firepower Threat Defense via the FMC REST API (assess + data-driven enforce).
- `cisco_aci_router_stig` — ACI L3Out routing-plane STIG (`CISC-RT-*`) via `cisco.aci`.
- `cisco_ise_stig` — ISE NDM (`CISC-ND-*`) assess + OpenAPI enforce via `uri`.

### Added — Operating systems & containers
- `rhel/roles/rhel9_stig` — RHEL 9 STIG (`RHEL-09-*`, V2R6), `ansible.builtin`/`ansible.posix`.
- `windows/roles/win_server2022_stig` — Windows Server 2022 STIG (`WN22-*`, V2R6) with optional Active Directory Domain (`AD.*`) and Windows DNS (`WDNS-*`) controls.
- `openshift/roles/ocp_stig_profile` — OpenShift Container Platform 4.x STIG (`CNTR-OS-*`, V2R4) via `kubernetes.core`.

### Added — Database
- `databases/db2/roles/db2_stig` — IBM DB2 V10.5 STIG (`DB2X-00-*`, V2R1) via the DB2 CLP, `db2audit`, and SQL (drift-aware).

### Added — Application / Web (`app_web_server/`)
- `tomcat_app_server_srg` — Application Server SRG V4R4 (`SRG-APP-*-AS-*`) via idempotent XML edits.
- `apache_web_server_srg` — Web Server SRG (`SRG-APP-*-WSR-*`), `apachectl`-validated drop-in.

### Added — Policy / SRG assessments
- `policy_as_code/roles/app_sec_dev_stig` — Application Security & Development STIG V6R4 (`APSC-DV-*`) CI/CD gate (gitleaks/semgrep/grype/checkov → evidence; optional build-fail).
- `network_policy/roles/ndm_srg_assessment` — Network Device Management SRG (V5R3) + Network Infrastructure Policy STIG (V10R7) evidence rollup.
- `cloud_policy/roles/cloud_computing_srg_assessment` — DoD Cloud Computing SRG (IL2–IL6) + SaaS shared-responsibility mapping onto the AWS/Azure/GCP roles.

### Added — IBM z/OS family (`ibm_zos/`, read-only assessment skeletons)
- `zos_racf_stig`, `zos_tss_stig`, `zos_cics_tss_stig`, `zos_netview_tss_stig`,
  `zos_tdmf_tss_stig`, `zos_zsecure_stig`. Each generates a STIG checklist +
  command reference (runs anywhere) and can run read-only verify commands against
  a live LPAR via `ibm.ibm_zos_core` (`zos_live_assessment=true`). **No blind
  enforcement** — remediation is documented for the z/OS systems programmer.

### Added — Documentation
- `STIG_COVERAGE_MATRIX.md` — full request-to-role traceability matrix.
- Per-platform and per-role READMEs for all new areas; `CHANGELOG.md` (this file).

### Notes
- Repository totals updated: **577 roles**, **3,684 YAML files**, **41 platforms**.
- All new YAML passes the CI gate (`scripts/check_yaml.py` + `yamllint`). The
  localhost-executable assessment roles (`ndm_srg_assessment`,
  `cloud_computing_srg_assessment`, `app_sec_dev_stig`, the six `ibm_zos/*`
  checklist generators) were additionally run end-to-end during development.

## [2026-03-16] — Production readiness / security hardening
- Added `no_log: true` to credential-handling tasks, `changed_when` correctness
  to query tasks, `any_errors_fatal: true` to plays, and the customer docs
  (CUSTOMER_QUICK_START, KNOWN_LIMITATIONS, TROUBLESHOOTING).

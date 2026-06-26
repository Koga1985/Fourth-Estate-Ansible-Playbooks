# Changelog

All notable changes to the Fourth Estate Ansible Playbooks are documented here.
The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

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

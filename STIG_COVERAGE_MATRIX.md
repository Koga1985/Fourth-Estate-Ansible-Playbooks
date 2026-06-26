# STIG / SRG Coverage Matrix

This matrix tracks the DISA STIGs and SRGs requested for "grab-and-go,
production-ready" Ansible playbooks against what exists in this repository.

**Status legend**

| Status | Meaning |
|--------|---------|
| ✅ Delivered | New, self-contained, runnable role added in this effort (dry-run safe, real STIG rule IDs, certified-collection or `uri` modules, README + runnable playbook + inventory/vars examples + JSON artifact). |
| 🟡 Existing | The platform already has hardening/automation roles in the repo that cover most of the control family; may need a STIG-version refresh. |
| 🛣️ Roadmap | Not yet built. Scoped below with the intended collection/approach. |

> Every ✅ role is **safe by default**: `apply_changes=false` runs in check/assessment
> mode and writes a per-host JSON findings artifact. Pass `-e apply_changes=true` to enforce.

---

## Requested items

| # | Requested STIG / SRG | Status | Location / Notes |
|---|----------------------|--------|------------------|
| 1 | **Cisco IOS XE — Catalyst as a Layer-2 device** | ✅ Delivered | `cisco/roles/cisco_ios_xe_l2_stig` — L2S (`CISC-L2-*`) + NDM (`CISC-ND-*`). |
| 2 | **Cisco NX-OS Switch STIG** | ✅ Delivered | `cisco/roles/cisco_nxos_stig` — NDM + L2 via `cisco.nxos`. |
| 3 | **Cisco ASA STIG** | ✅ Delivered | `cisco/roles/cisco_asa_stig` — NDM (`CASA-ND-*`) + Firewall (`CASA-FW-*`) via `cisco.asa`. |
| 4 | **Cisco FTD STIG** | ✅ Delivered | `cisco/roles/cisco_ftd_stig` — FMC REST API assess + enforce. |
| 5 | **Cisco ACI / ACI Router STIG** | ✅ Delivered | ACI fabric/NDM: `cisco/roles/aci_security_hardening`. ACI **Router** `CISC-RT-*` (BGP/OSPF auth, GTSM, route control): `cisco/roles/cisco_aci_router_stig`. |
| 6 | **Cisco ISE STIG** | ✅ Delivered | `cisco/roles/cisco_ise_stig` — ISE NDM (`CISC-ND-*`) assess + OpenAPI enforce, plus the 28 functional `ise_*` roles. |
| 7 | **Cisco UCS** | 🟡 Existing | `cisco/roles/ucs_security_hardening` — DoD STIG CAT I/II/III. |
| 8 | **Network Device Management SRG (V5R3)** | ✅ Delivered | `network_policy/roles/ndm_srg_assessment` — consolidated evidence/checklist mapping `SRG-APP-*-NDM-*` to the device STIG artifacts. |
| 9 | **Red Hat Enterprise Linux 9 STIG (V2R6)** | ✅ Delivered | `rhel/roles/rhel9_stig` — `RHEL-09-*` CAT I/II/III via `ansible.builtin`/`ansible.posix`. (Existing `rhel-hardening` targets RHEL 8.) |
| 10 | **Red Hat OpenShift Container Platform 4.x STIG (V2R4)** | ✅ Delivered | `openshift/roles/ocp_stig_profile` — consolidated `CNTR-OS-*` profile (audit, encryption-at-rest, TLS profile, OAuth tokens, self-provisioner, PSA restricted, default-deny netpol). Complemented by existing `ocp_audit_config`, `ocp_psa_enforce`, `ocp_rbac_baseline`, `ocp_scc_legacy_mgmt`, `ocp_network_policies_baseline`. |
| 11 | **Microsoft Windows Server 2022 STIG (V2R6)** | ✅ Delivered | `windows/roles/win_server2022_stig` — `WN22-*` account/audit/registry via `ansible.windows`. (Legacy `win_stig_hardening` retained.) |
| 12 | **Active Directory Domain STIG** | ✅ Delivered | `windows/roles/win_server2022_stig` (AD controls, `win_is_domain_controller=true`) + existing `win_active_directory`. |
| 13 | **Microsoft Windows Server DNS STIG** | ✅ Delivered | `windows/roles/win_server2022_stig` (DNS controls, `win_is_dns_server=true`, `WDNS-*`) + existing `win_dhcp_dns`. |
| 14 | **Application Server SRG (V4R4)** | ✅ Delivered | `app_web_server/roles/tomcat_app_server_srg` — `SRG-APP-*-AS-*` (Tomcat; fork for JBoss/WebLogic). |
| 15 | **Web Server SRG** | ✅ Delivered | `app_web_server/roles/apache_web_server_srg` — `SRG-APP-*-WSR-*` (Apache; IIS via `windows/roles/win_iis`). |
| 16 | **Application Security & Development STIG (V6R4)** | ✅ Delivered | `policy_as_code/roles/app_sec_dev_stig` — `APSC-DV-*` CI/CD gate (secret/SAST/SCA/IaC scanners → evidence, optional build-fail). |
| 17 | **Network Infrastructure Policy STIG (V10R7)** | ✅ Delivered | `network_policy/roles/ndm_srg_assessment` — `NET-*` architecture controls + evidence rollup. |
| 18 | **Cloud Computing SRG** | ✅ Delivered | `cloud_policy/roles/cloud_computing_srg_assessment` — CC SRG/FedRAMP families mapped to `aws_*`/`azure_*`/`gcp_*` roles + IL2–IL6 + evidence. |
| 19 | **SaaS** | ✅ Delivered | `cloud_policy/roles/cloud_computing_srg_assessment` — SaaS shared-responsibility checklist (FedRAMP auth, CRM, SSO/MFA, SIEM, encryption, DLP). |
| 20 | **IBM DB2 V10.5 STIG (V2R1)** | ✅ Delivered | `databases/db2/roles/db2_stig` — `DB2X-00-*` via DB2 CLP, `db2audit`, SQL (drift-aware, assessment-safe). |
| 21 | **IBM z/OS STIG (RACF / ACF2 / TSS products)** | 🛣️ Roadmap | R11 — z/OS family; see note below. |
| 22 | **z/OS RACF Products** | 🛣️ Roadmap | R11 |
| 23 | **IBM z/OS — NetView for TSS V7R2** | 🛣️ Roadmap | R11 |
| 24 | **IBM z/OS — TDMF for TSS V7R2** | 🛣️ Roadmap | R11 |
| 25 | **IBM z/OS — CICS Transaction Server (TSS) V7R2** | 🛣️ Roadmap | R11 |
| 26 | **IBM zSecure Suite STIG (V1R3)** | 🛣️ Roadmap | R11 |

---

## Roadmap detail

| ID | Scope | Intended approach |
|----|-------|-------------------|
| R1 | ✅ Done — Cisco ACI **Router** STIG (`CISC-RT-*`) | Delivered as `cisco/roles/cisco_aci_router_stig`. |
| R2 | ✅ Done — Cisco ISE NDM STIG mapping | Delivered as `cisco/roles/cisco_ise_stig`. |
| R3 | ✅ Done — Network Device Management SRG / Network Infrastructure Policy STIG | Delivered as `network_policy/roles/ndm_srg_assessment`. |
| R4 | ✅ Done — OpenShift 4.x STIG consolidated profile | Delivered as `openshift/roles/ocp_stig_profile` (`CNTR-OS-*`). |
| R5 | ✅ Done — Windows Server 2022 STIG V2R6 | Delivered as `windows/roles/win_server2022_stig` (`WN22-*`). |
| R6 | ✅ Done — AD Domain STIG + Windows DNS STIG | Delivered in `windows/roles/win_server2022_stig` (DC/DNS toggles, `AD.*` / `WDNS-*`). |
| R7 | ✅ Done — Application Server SRG (V4R4) + Web Server SRG | Delivered as `app_web_server/roles/{tomcat_app_server_srg,apache_web_server_srg}`. |
| R8 | ✅ Done — Application Security & Development STIG (V6R4) | Delivered as `policy_as_code/roles/app_sec_dev_stig` (`APSC-DV-*` CI/CD gate). |
| R9 | ✅ Done — Cloud Computing SRG / SaaS | Delivered as `cloud_policy/roles/cloud_computing_srg_assessment`. |
| R10 | ✅ Done — IBM DB2 V10.5 STIG (V2R1) | Delivered as `databases/db2/roles/db2_stig`. |
| R11 | IBM z/OS family (RACF, ACF2/TSS, CICS, NetView, TDMF, zSecure) | z/OS automation requires `ibm.ibm_zos_core` (Ansible for z/OS) running against a USS-enabled LPAR with SSH; controls applied via TSO/RACF commands and JCL. This is **environment-specific** and not "grab-and-go" without a z/OS managed node — delivered as documented role skeletons with the command sets, not blind enforcement. |

---

## How to run a delivered role

```bash
cd cisco/roles/<role>/playbooks
ansible-galaxy collection install <collection>     # see role meta/main.yml
cp inventory.example inventory && $EDITOR inventory # vault your credentials

ansible-playbook -i inventory run.yml                       # DRY-RUN (report)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE
```

Artifacts are written to `/tmp/<platform>-artifacts/<host>_*.json`.

_Last updated: 2026-06-26._

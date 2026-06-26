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
| 5 | **Cisco ACI / ACI Router STIG** | 🟡 Existing | `cisco/roles/aci_security_hardening` (+ `aci_*`) implement APIC/NDM hardening (`CISC-ND-*`). ACI **Router**-specific `CISC-RT-*` controls tracked in roadmap row R1. |
| 6 | **Cisco ISE STIG** | 🟡 Existing | `cisco/roles/ise_*` (28 roles) implement ISE policy/admin hardening. Dedicated ISE-NDM STIG mapping tracked in roadmap row R2. |
| 7 | **Cisco UCS** | 🟡 Existing | `cisco/roles/ucs_security_hardening` — DoD STIG CAT I/II/III. |
| 8 | **Network Device Management SRG (V5R3)** | 🟡 Existing | Implemented transitively by every `CISC-ND-*` / `CASA-ND-*` control in the four delivered Cisco roles (the SRG is the parent of those STIGs). Cross-reference doc tracked in R3. |
| 9 | **Red Hat Enterprise Linux 9 STIG (V2R6)** | ✅ Delivered | `rhel/roles/rhel9_stig` — `RHEL-09-*` CAT I/II/III via `ansible.builtin`/`ansible.posix`. (Existing `rhel-hardening` targets RHEL 8.) |
| 10 | **Red Hat OpenShift Container Platform 4.x STIG (V2R4)** | ✅ Delivered | `openshift/roles/ocp_stig_profile` — consolidated `CNTR-OS-*` profile (audit, encryption-at-rest, TLS profile, OAuth tokens, self-provisioner, PSA restricted, default-deny netpol). Complemented by existing `ocp_audit_config`, `ocp_psa_enforce`, `ocp_rbac_baseline`, `ocp_scc_legacy_mgmt`, `ocp_network_policies_baseline`. |
| 11 | **Microsoft Windows Server 2022 STIG (V2R6)** | 🟡 Existing | `windows/roles/win_stig_hardening` + `win_group_policy`. Version refresh to V2R6 tracked in R5. |
| 12 | **Active Directory Domain STIG** | 🟡 Existing | `windows/roles/win_active_directory`. AD-Domain-STIG control mapping tracked in R6. |
| 13 | **Microsoft Windows Server DNS STIG** | 🟡 Existing | `windows/roles/win_dhcp_dns`. DNS-STIG control mapping tracked in R6. |
| 14 | **Application Server SRG (V4R4)** | 🛣️ Roadmap | R7 — generic Jakarta EE/Tomcat/JBoss app-server hardening. |
| 15 | **Web Server SRG** | 🛣️ Roadmap | R7 — generic web-server controls; partially covered by existing `windows/roles/win_iis`. |
| 16 | **Application Security & Development STIG (V6R4)** | 🛣️ Roadmap | R8 — pipeline/policy-as-code checks (not a host config STIG). |
| 17 | **Network Infrastructure Policy STIG (V10R7)** | 🛣️ Roadmap | R3 — policy/architecture STIG; assessment-checklist role. |
| 18 | **Cloud Computing SRG** | 🛣️ Roadmap | R9 — policy SRG; maps to existing AWS/Azure/GCP FedRAMP roles. |
| 19 | **SaaS** | 🛣️ Roadmap | R9 — covered under Cloud Computing SRG / DoD Cloud guidance. |
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
| R1 | Cisco ACI **Router** STIG (`CISC-RT-*`) | Extend `cisco/roles/aci_security_hardening` with an `aci_router_stig` task set via `cisco.aci`/`aci_rest` (BGP/OSPF auth, uRPF, control-plane). |
| R2 | Cisco ISE NDM STIG mapping | Add `CISC-ND-*` cross-map to existing `ise_admin__*` roles (banner, AAA, syslog, NTP, SNMPv3, session timeout). |
| R3 | Network Device Management SRG / Network Infrastructure Policy STIG | Assessment-checklist role producing a control-by-control evidence artifact across managed network devices. |
| R4 | ✅ Done — OpenShift 4.x STIG consolidated profile | Delivered as `openshift/roles/ocp_stig_profile` (`CNTR-OS-*`). |
| R5 | Windows Server 2022 STIG V2R6 refresh | Refresh `win_stig_hardening` rule IDs (`WN22-*`) and add a registry/secpol audit report. |
| R6 | AD Domain STIG + Windows DNS STIG | Map `win_active_directory` / `win_dhcp_dns` tasks to `AD.*` and `WDNS-*` rule IDs; add assessment. |
| R7 | Application Server SRG (V4R4) + Web Server SRG | `app_server/` roles for Tomcat/JBoss + generic web-server controls (TLS, logging, account mgmt). |
| R8 | Application Security & Development STIG (V6R4) | Policy-as-code gate (SAST/DAST/dependency/secret scanning evidence) under `policy_as_code/`. |
| R9 | Cloud Computing SRG / SaaS | Control-mapping doc + assessment tying existing `aws/`, `azure/`, `google_cloud_platform/` FedRAMP roles to the SRG. |
| R10 | IBM DB2 V10.5 STIG (V2R1) | `databases/db2/` role applying `DB2*-*` SQL/parameter controls via authenticated SQL. |
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

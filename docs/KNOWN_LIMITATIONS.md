# Known Limitations

This document describes known limitations, operational constraints, and caveats for the Fourth Estate Ansible Playbooks. **Customers assume all risk when running these playbooks.** Review this document fully before executing any playbook in production.

---

## Table of Contents

1. [General Operational Safeguards](#1-general-operational-safeguards)
2. [Unimplemented Platforms](#2-unimplemented-platforms)
3. [Non-Idempotent Operations](#3-non-idempotent-operations)
4. [Destructive Operations](#4-destructive-operations)
5. [Mandatory Dry-Run Requirement](#5-mandatory-dry-run-requirement)
6. [Reboot and Service Restart Requirements](#6-reboot-and-service-restart-requirements)
7. [Operational Technology (OT/ICS) Environments](#7-operational-technology-otics-environments)
8. [Platform-Specific Limitations](#8-platform-specific-limitations)
9. [Version and Compatibility Constraints](#9-version-and-compatibility-constraints)
10. [Air-Gapped and Offline Deployment Constraints](#10-air-gapped-and-offline-deployment-constraints)
11. [STIG and Compliance Caveats](#11-stig-and-compliance-caveats)
12. [Python and Collection Dependencies](#12-python-and-collection-dependencies)
13. [Network and Connectivity Requirements](#13-network-and-connectivity-requirements)
14. [Advanced Features Not Yet Implemented](#14-advanced-features-not-yet-implemented)
15. [Templates Requiring Site Review](#15-templates-requiring-site-review)
16. [Credentials on a Command Line](#16-credentials-on-a-command-line)

---

## 1. General Operational Safeguards

These safeguards apply to all platforms and roles.

- **Dry-run before production.** All playbooks default to `apply_changes: false`. Never skip the dry-run step.
- **Maintenance windows.** Any role that restarts services or reboots systems must be scheduled during a maintenance window.
- **Out-of-band access.** Maintain out-of-band management access to critical infrastructure before running playbooks.
- **Idempotency is not guaranteed.** Not all roles are idempotent. See [Section 2](#2-non-idempotent-operations) for details. Running a playbook multiple times may produce unintended duplicate actions.
- **STIG exceptions.** Some STIG findings may not apply to all environments. Document exceptions using the format `"V-XXXXX": "<reason>"` before applying hardening.

---

## 2. Unimplemented Platforms

155 roles in this repository contained no tasks at all. They had the complete
role layout -- `README.md`, `defaults/main.yml`, `meta/main.yml`, sometimes
handlers and templates -- but an empty `tasks/main.yml`. 114 of them were
invoked by playbooks, so a "phase" such as `Phase 1 - Tower Installation` ran,
reported success, and changed nothing.

Those roles and the 120 playbook invocations that called them have been
removed, so no playbook now claims a phase it does not perform. The
consequence is that several platforms have little or no automation:

| Platform | Roles remaining | Status |
|----------|-----------------|--------|
| Ansible Tower / AAP | 5 | controller configuration as code; does not install AAP itself |
| Windows Server | 1 | only `win_server2022_stig`, which `site.yml` does not invoke -- run it directly |
| Fortinet FortiGate | 1 | |
| Cohesity, ServiceNow, Prometheus/Grafana | 2 each | |
| NetApp ONTAP, Veeam, ELK Stack | 3 each | |
| Tenable, HashiCorp Vault, F5 BIG-IP | 4 each | |
| Microsoft Azure | 7 | reduced from a claimed 46 |

MySQL / MariaDB and Oracle Database are no longer listed because the
directories have been removed. Each held a `site.yml` that announced "NO
AUTOMATION IMPLEMENTED" and changed nothing, and `COMPLIANCE_MAPPING.md`
listed STIG findings against `roles/` directories they never had. No customer
ran either.

Do not assume a platform directory implies working automation. Check the
platform README and the roles that actually exist before planning work around
it. The repository statistics in the top-level README now count only roles
that do something.

---

## 3. Non-Idempotent Operations

The following roles or platforms have operations that are **not idempotent**. Running them more than once may cause duplicate or unintended actions.

| Platform | Role / Area | Detail |
|----------|-------------|--------|
| **Veeam** | All roles | Some Veeam API calls are inherently imperative. Review each playbook's variable list before running in production. Running tasks multiple times may result in duplicate backup jobs or policies. |
| **VMware** | `vcenter_certificates` | Custom solution-user certificate rotation is not fully idempotent. Environment-specific `expect` prompt sequences may vary. Only VMCA-based solution-user rotation is fully automated. |

**Recommendation:** Run all playbooks twice in a test environment before production to verify expected idempotency behavior.

---

## 4. Destructive Operations

Roles that can delete or permanently alter data are gated behind explicit flags. These flags are `false` by default. Enabling them without review may cause irreversible damage.

### Palo Alto — Object Pruning
- **Role:** `pa_objects_catalog`
- **Files:** `tasks/prune.yml`
- Two conditions must both be explicitly set to enable deletion:
  - `prune.dry_run: false`
  - `prune.allow_delete: true`
- A preview report is always generated. Review it before enabling deletion.

### Operational Technology — Asset Disposal
- **Role:** `ot_asset_lifecycle`
- **Files:** `tasks/includes/dispose.yml`
- Asset disposal requires `dry_run: false` plus a valid disposal method (`recycle`, `destroy`, `return_to_vendor`, `archive`).
- `asset_id` and `disposal_method` must be explicitly defined. Missing values will fail validation.

### Pure Storage — SafeMode Snapshot Retention
- **Role:** `pure_flasharray_protection`
- Snapshots cannot be deleted before a 24-hour minimum retention period (`flasharray_safemode_retention_minimum: 24`).
- This is enforced by the array. Playbooks that attempt deletion before this window will fail.

### UCS — Quick Start Playbook
- **Playbook:** `cisco/playbooks/20_ucs_quick_start.yml`
- **WARNING: NOT for production use.** This playbook is a minimal deployment for development and testing only. It includes basic infrastructure and LAN-only networking with no SAN configuration.

---

## 5. Mandatory Dry-Run Requirement

All playbooks default to `apply_changes: false` (dry-run mode). This is intentional.

**Before applying any changes to production:**

1. Run with `apply_changes=false` and review all `changed` results.
2. Confirm expected vs. actual changes.
3. Run again with `apply_changes=true` only after validation.

Skipping the dry-run step is the leading cause of unintended configuration changes.

---

## 6. Reboot and Service Restart Requirements

The following operations require a system reboot or cause service restarts. Schedule accordingly.

| Platform | Operation | Impact |
|----------|-----------|--------|
| **RHEL** | FIPS mode enablement (`rhel-hardening`, `fips.yml`) | **Full system reboot required.** Service downtime is unavoidable. Run only during maintenance windows. The playbook emits: `WARNING: System reboot required to complete FIPS enablement`. |
| **VMware** | vCenter certificate rotation (`vcenter_certificates`) | vCenter services will restart during rotation. Lab testing is strongly recommended before production. Run only during maintenance windows. |

---

## 7. Operational Technology (OT/ICS) Environments

OT environments require additional precautions beyond standard IT deployments.

### Safety Instrumented Systems (SIS)
- **Never automate changes to Safety Instrumented Systems.** SIS changes require manual validation and approval by qualified personnel. No playbook in this repository is designed or validated for SIS use.

### Active Network Discovery
- **Role:** `cybervision_asset_management`
- Active discovery sends ARP and ICMP probes that can cause PLCs, RTUs, and other OT devices to malfunction or crash.
- **Coordinate with OT engineers before enabling active discovery.**
- Default discovery rate is `low` to minimize risk. Do not increase discovery rate in production OT environments without explicit OT engineer approval.
- Set `cv_active_discovery_rate: "low"` in all production OT environments.

### Legacy Systems
- Legacy OT systems cannot be patched or upgraded via automation. These systems must be handled manually or with vendor support.
- Compliance automation capabilities are limited for legacy OT endpoints. Document these as exceptions.

### Change Control
- All OT changes require change control approval and must operate within approved maintenance windows.
- OT environments prioritize availability over confidentiality. Security automations may need environment-specific tuning.

---

## 8. Platform-Specific Limitations

### Cisco — ACI Fabric Health Blocking
- **Role:** `aci_monitoring`
- Deployment is blocked if the fabric health score drops below `aci_health_critical_threshold: 50`.
- Health scores below `aci_health_warn_threshold: 75` emit warnings but do not block.
- To override the block: `aci_fault_fail_on_critical: false` (not recommended for production).

### Infoblox — Version-Agnostic Best-Effort Roles

| Role | Limitation |
|------|-----------|
| `infoblox_grid_bootstrap` | Some fields differ by NIOS release. The role logs warnings where an attribute is not accepted. Join token generation writes a helper file; member joining still requires manual CLI steps on the appliance. |
| `infoblox_grid_upgrade` | Upload and activation are best-effort and vary by NIOS version. Default is `dry_run: true`. Always test upgrades in a lab environment first. |
| `infoblox_capacity_reports` | DNS query statistics are best-effort and may be incomplete or unavailable on some NIOS releases. |

### VMware — Device Removal During Hardening
- **Role:** `vsphere_vm_stig_hardening`
- This role removes CD-ROM and floppy devices and disconnects serial/parallel ports from VMs as part of STIG compliance.
- Verify that no workloads depend on these devices before applying to production VMs.

### VAST — SNMP Version Constraint
- Only SNMPv3 is supported for DoD compliance. SNMPv1 and SNMPv2 are not supported.

### Dedicated STIG / SRG roles (June 2026 expansion)

| Role(s) | Limitation |
|---------|-----------|
| `ibm_zos/roles/*` (RACF, TSS, CICS, NetView, TDMF, zSecure) | **Assessment skeletons — no enforcement.** They generate a STIG checklist + read-only command reference and, in live mode (`zos_live_assessment=true`), run only read-only verify commands via `ibm.ibm_zos_core`. Remediation is performed by the z/OS systems programmer. Control-area IDs must be reconciled with the exact V-/rule-IDs in your STIG release. Live mode requires z/OS Python + ZOAU + SSH on the LPAR. |
| `cisco/roles/cisco_ftd_stig`, `cisco/roles/cisco_ise_stig` | Enforcement is **data-driven** (`ftd_stig_operations` / `ise_stig_operations`). Because FMC/ISE OpenAPI request bodies vary by version, the enforcement list ships empty — validate each operation against your platform's API explorer before enabling. Assessment is fully functional out of the box. |
| `cisco/roles/cisco_aci_router_stig` | You must supply the exact APIC managed-object DNs (`bgpPeerP`, `ospfIfP`, `l3extOut`); discover them first. `enforceRtctrl=import,export` makes an L3Out default-deny — confirm route-control profiles permit required prefixes. |
| `policy_as_code/roles/app_sec_dev_stig` | The CI/CD gate depends on external scanners (gitleaks/semgrep/grype/checkov) being on `PATH`. Missing scanners are reported as `tool-not-available` (attach manual evidence), not failed. Several `APSC-DV-*` controls are procedural (`manual-review`). |
| `network_policy/roles/ndm_srg_assessment`, `cloud_policy/roles/cloud_computing_srg_assessment` | Evidence rollups: run the underlying device/provider roles first so their artifacts exist. Coverage reflects implemented roles; DoD-specific and SaaS items are procedural checklists. |
| `windows/roles/win_server2022_stig` | AD Domain and Windows DNS controls run only on hosts flagged `win_is_domain_controller` / `win_is_dns_server` and require the `ActiveDirectory` / `DnsServer` PowerShell modules. Account-policy changes on a DC apply to the whole domain. |
| `app_web_server/roles/apache_web_server_srg` | Path defaults assume RHEL/EL (`/etc/httpd`); set the `apache_*` path vars for Debian/Ubuntu. |
| `databases/db2/roles/db2_stig` | Several `dbm cfg` and SSL changes require a DB2 instance restart; native encryption (`ENCRLIB`) requires the instance to be licensed and a keystore configured. |

> **CI note:** the repository enforces four required gates — YAML parse,
> `yamllint`, `ansible-lint` (offline, pinned toolchain, baseline-ratcheted),
> and `ansible-playbook --syntax-check` for the core-only playbooks. A **full**
> `ansible-lint`/`--syntax-check` with every vendor collection resolved requires
> the per-role collections from Ansible Galaxy (run as an informational,
> non-blocking job); install them in your execution environment to reproduce
> those checks locally.

---

## 9. Version and Compatibility Constraints

### Minimum Requirements

| Requirement | Minimum Version |
|-------------|-----------------|
| Ansible Core | 2.15+ |
| Python | 3.10+ |

### Key Collection Minimums

| Collection | Minimum Version |
|------------|----------------|
| `cisco.aci` | 2.9.0 |
| `infoblox.nios_modules` | 1.5.0 |
| `community.general` | 7.0.0 |
| `ansible.windows` | 1.14.0 |
| `fortinet.fortios` | 2.3.0 |
| `fortinet.fortimanager` | 2.4.0 |

### Platform Version Support
- **VMware vSphere:** Versions 7 and 8 only.
- **Kubernetes STIG:** V1R11 compliance requires specific API versions. Verify API compatibility before applying.

### STIG Version Drift
- STIG control mappings must be re-validated after each major release of this repository. STIG version updates may change control applicability. Reference the DISA STIG Library and NIST SP 800-53 Rev 5 for current control definitions.

---

## 10. Air-Gapped and Offline Deployment Constraints

For environments without internet access, agent/sensor installers cannot be automatically downloaded.

| Platform | Requirement |
|----------|-------------|
| **CrowdStrike Falcon** | Set `falcon_sensor_download_url` to a pre-staged internal URL. Sensors must be downloaded and hosted internally before running the playbook. |
| **SentinelOne** | Set `s1_agent_download_url` to a pre-staged internal URL. Same requirement as CrowdStrike. |

Both roles will fail if the download URL is unreachable and no local URL is provided.

---

## 11. STIG and Compliance Caveats

- **Not all STIG findings apply to all environments.** Review each finding for applicability before applying hardening.
- **Policy-as-Code compliance controls may impact service availability.** Review `policy_as_code/DEPLOYMENT_GUIDE.md` for pre-deployment warnings.
- **Compliance mappings are point-in-time.** The `COMPLIANCE_MAPPING.md` file reflects a specific STIG and NIST version. Validate mappings are current before using for audit purposes.
- **STIG exceptions must be documented.** Use the format `"V-XXXXX": "<justification>"` and maintain an exception register for your environment.

---

## 12. Python and Collection Dependencies

Missing Python packages or Ansible collections will cause playbook failures. The following Python libraries are required per platform and must be installed on the Ansible control node.

| Platform | Required Python Packages |
|----------|--------------------------|
| Cisco ACI | `acicobra`, `acimodel` |
| Cisco ISE | `ciscoisesdk` |
| Cisco UCS | `ucsmsdk` |
| Infoblox | `infoblox-client` |
| Fortinet | `fortiosapi` |
| Palo Alto | `pan-python`, `pandevice` |
| All platforms | `requests` |

Refer to each platform's `requirements.txt` or `requirements.yml` for the complete list. A `ModuleNotFoundError` at runtime typically indicates a missing Python dependency, not a missing Ansible collection.

---

## 13. Network and Connectivity Requirements

- The Ansible control host must have network access to each target system's management API endpoint.
- Verify connectivity before running: `curl -k https://<management-ip>/api/`
- Firewall rules, proxies, and routing must allow API traffic from the control host.
- **TLS certificate verification:** The control host must trust the target system's TLS certificate. Add CA certificates to the control host CA bundle for environments using internal or self-signed certificates.
- **Out-of-band management access** is strongly recommended for critical infrastructure before executing any playbook.

---

## 14. Advanced Features Not Yet Implemented

The following optional/advanced workflows ship as **fail-fast placeholders**: the role
loads and the default path runs, but enabling the feature stops with a clear, actionable
message rather than executing unverified automation against critical systems. Provide a
site-specific implementation (validated in a non-production environment) before enabling
them.

| Role | Feature (placeholder) | Enabled by |
|------|----------------------|------------|
| `operational_technology/ot_firmware_register` | register / verify / baseline / update_plan / rollback workflows | `ot_firmware_operation` |
| `illumio/illumio_pce_install` | PCE database cluster, PgBouncer, load balancer | `illumio_pce_cluster_mode`, `illumio_pce_use_pgbouncer`, `illumio_pce_use_loadbalancer` |
| `sciencelogic/sl1_platform_install` | database cluster, high availability, data/message collector install | `sl1_db_cluster.enabled`, `sl1_ha.enabled`, collector `install: true` |

> **SentinelOne / CrowdStrike Windows** install tasks and **Kubernetes control-plane/worker
> join, metrics-server, validation, and Fourth Estate namespace** tasks were implemented
> following standard vendor / `kubeadm` procedures and the existing sibling tasks in each
> role. They are not yet validated against live hosts — test in a non-production
> environment and confirm installer versions/arguments for your environment first.

## 15. Templates Requiring Site Review

Most previously-missing templates were implemented with working, variable-driven content
(postgres backup/restore scripts, splunk `.conf` files, report/inventory artifacts, kubelet
args, ELK role mappings, SL1 network config). The following **security/clustering** templates
were added as **valid standard schemas but must be reviewed and populated for your site
before production** — several require secrets/URLs that have *no default* and will fail-fast
at render time if unset, rather than deploying an incomplete configuration:

| Role | Template | Provide before enabling |
|------|----------|------------------------|
| `kubernetes/k8s-cluster-hardening` | `encryption-config-rotated.yaml` | `k8s_encryption_key` (from Vault) |
| `kubernetes/k8s-cluster-hardening` | `audit-webhook-config.yaml` | `k8s_audit_webhook_url` |
| `kubernetes/k8s-cluster-hardening` | `kube-apiserver-flags.yaml` | `k8s_apiserver_extra_flags` |
| `kubernetes/k8s-cluster-hardening` | `security-context-admission.yaml` | PSA defaults (`k8s_psa_*`) |
| `kubernetes/k8s-cluster-hardening` | `rsyslog-kubernetes.conf` | `k8s_rsyslog_remote` (optional) |
| `illumio/illumio_pce_install` | `cluster_peers.yml`, `pce_environment`, `illumio_cli_config`, `pce-ctl` wrapper | PCE topology / FQDN / install paths |
| `sciencelogic/sl1_platform_install` | `install_config_db` | `sl1_db_server.*` |

---

## 16. Credentials on a Command Line

`no_log: true` covers credentials passed to a module as arguments — the whole
`uri` header class this repository swept. It does **not** cover two cases that
still exist here. Both are documented rather than silently patched, because the
fix in each case depends on a vendor interface this repository cannot verify.

### What was measured

A secret was passed three ways to a task on a live run, and every process on the
box was inspected while it executed:

| How the secret is passed | Visible in a process command line | Visible in a process environment | Suppressed by `no_log` |
|---|---|---|---|
| Interpolated into the command | 1 process | — | Result only, not the command |
| Ansible `environment:` keyword | 2 processes | 3 processes | **No** |
| `args: stdin:` | none | none | n/a |

Two results are worth reading twice.

**`environment:` is worse than the command line, not better.** Ansible
implements it by prefixing the remote command with `VAR=value python3
AnsiballZ_….py`, so the secret lands on two shell command lines *and* in the
environment of three descendant processes.

**`no_log` does not protect a secret passed via `environment:`.** At `-vvv` the
connection plugin prints its `EXEC /bin/sh -c 'VAR=value …'` line before the
module runs, and `no_log` suppresses only the module's result. Verified: a task
with `no_log: true` and an `environment:` secret still prints it at `-vvv`.

`stdin` is the only one of the three that keeps a secret off every command line,
but it works only when the invoked program reads the secret from stdin. It is
not a fix for a vendor CLI that accepts the secret only as a flag.

### Case 1 — vendor CLIs that take a secret only as a flag

| Location | Credential | Runs on |
|---|---|---|
| `sciencelogic/sl1_platform_install` `40_database_server.yml`, `50_all_in_one.yml` | `--db-root-password`, `--admin-password` | the SL1 server |
| `crowdstrike/falcon_sensor_install` `install_linux.yml` | `falconctl --provisioning-token=` | each managed node |
| `vmware/` — 13 PowerCLI tasks | `Connect-VIServer -Password` | the control node / execution environment |

All carry `no_log: true`, so nothing reaches the job output or the Automation
Platform job record. The command line remains readable through `ps` on the host
running the command for as long as the command runs.

The 13 vmware tasks run under `hosts: localhost`, so that host is the execution
environment container — created for one job and destroyed with it. The
ScienceLogic and CrowdStrike tasks run on managed nodes, where the process table
is shared with whoever else is on the box. Treat those two as the ones that
matter.

`no_log` costs diagnostics on these tasks, and the vmware PowerCLI ones are the
expensive case: a failure now prints only the censored placeholder instead of the
PowerShell error. Registered results are unaffected — `cap_cmd.stdout` and its
equivalents still reach the tasks that parse them — so reports still build. To
debug a failing PowerCLI task, set `no_log: false` on that one task in a
non-production run, and set it back.

Fixes, none applied here:

- **ScienceLogic.** Both installers already receive the same passwords through
  their `--config` file, which is written at mode `0600` — the flags duplicate a
  secret that is already delivered safely. Drop the flags once the installer's
  config format is confirmed against the real package. That format is not
  verified today (see the header of `templates/install_config_db.j2`), which is
  why the duplication has not been removed on assumption.
- **CrowdStrike.** `falconctl` accepts the provisioning token only as a flag.
  There is no fix short of a vendor change.
- **vmware.** This repository authors the PowerShell, so the password can be
  read from stdin: add `$pw = [Console]::In.ReadLine();` at the top of the
  `-Command` body, use `-Password $pw`, and pass `stdin: "{{ vcenter_password }}"`
  under `args:`. It needs testing against a live vCenter, which CI here cannot do.

### Case 2 — secrets passed through `environment:`

| Location | Credential | Has `no_log` |
|---|---|---|
| `databases/postgresql/postgresql_replication` `main.yml` | `PGPASSWORD` for `pg_basebackup` | yes — and it does not help |
| `illumio/illumio_pce_install` `install_pce.yml` | `ILLUMIO_PCE_ADMIN_PASSWORD` for `install.sh` | no |

`PGPASSWORD` is the idiomatic way to drive `pg_basebackup`, and the idiomatic
fix is a `.pgpass` file at mode `0600` in the `postgres` user's home, which the
client reads with no environment variable and no flag.

For the Illumio PCE installer, the admin password is not among the keys its
`install_config.json` carries, so the environment variable is currently the only
channel. Whether `install.sh` will read it from stdin instead is a question for
the vendor's documentation. No `no_log` was added there deliberately: it would
not close the `-vvv` exposure, and a `no_log` that does not protect what a reader
assumes it protects is worse than none.

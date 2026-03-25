# Known Limitations

This document describes known limitations, operational constraints, and caveats for the Fourth Estate Ansible Playbooks. **Customers assume all risk when running these playbooks.** Review this document fully before executing any playbook in production.

---

## Table of Contents

1. [General Operational Safeguards](#1-general-operational-safeguards)
2. [Non-Idempotent Operations](#2-non-idempotent-operations)
3. [Destructive Operations](#3-destructive-operations)
4. [Mandatory Dry-Run Requirement](#4-mandatory-dry-run-requirement)
5. [Reboot and Service Restart Requirements](#5-reboot-and-service-restart-requirements)
6. [Operational Technology (OT/ICS) Environments](#6-operational-technology-otics-environments)
7. [Platform-Specific Limitations](#7-platform-specific-limitations)
8. [Version and Compatibility Constraints](#8-version-and-compatibility-constraints)
9. [Air-Gapped and Offline Deployment Constraints](#9-air-gapped-and-offline-deployment-constraints)
10. [STIG and Compliance Caveats](#10-stig-and-compliance-caveats)
11. [Python and Collection Dependencies](#11-python-and-collection-dependencies)
12. [Network and Connectivity Requirements](#12-network-and-connectivity-requirements)

---

## 1. General Operational Safeguards

These safeguards apply to all platforms and roles.

- **Dry-run before production.** All playbooks default to `apply_changes: false`. Never skip the dry-run step.
- **Maintenance windows.** Any role that restarts services or reboots systems must be scheduled during a maintenance window.
- **Out-of-band access.** Maintain out-of-band management access to critical infrastructure before running playbooks.
- **Idempotency is not guaranteed.** Not all roles are idempotent. See [Section 2](#2-non-idempotent-operations) for details. Running a playbook multiple times may produce unintended duplicate actions.
- **STIG exceptions.** Some STIG findings may not apply to all environments. Document exceptions using the format `"V-XXXXX": "<reason>"` before applying hardening.

---

## 2. Non-Idempotent Operations

The following roles or platforms have operations that are **not idempotent**. Running them more than once may cause duplicate or unintended actions.

| Platform | Role / Area | Detail |
|----------|-------------|--------|
| **Veeam** | All roles | Some Veeam API calls are inherently imperative. Review each playbook's variable list before running in production. Running tasks multiple times may result in duplicate backup jobs or policies. |
| **VMware** | `vcenter_certificates` | Custom solution-user certificate rotation is not fully idempotent. Environment-specific `expect` prompt sequences may vary. Only VMCA-based solution-user rotation is fully automated. |

**Recommendation:** Run all playbooks twice in a test environment before production to verify expected idempotency behavior.

---

## 3. Destructive Operations

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

## 4. Mandatory Dry-Run Requirement

All playbooks default to `apply_changes: false` (dry-run mode). This is intentional.

**Before applying any changes to production:**

1. Run with `apply_changes=false` and review all `changed` results.
2. Confirm expected vs. actual changes.
3. Run again with `apply_changes=true` only after validation.

Skipping the dry-run step is the leading cause of unintended configuration changes.

---

## 5. Reboot and Service Restart Requirements

The following operations require a system reboot or cause service restarts. Schedule accordingly.

| Platform | Operation | Impact |
|----------|-----------|--------|
| **RHEL** | FIPS mode enablement (`rhel-hardening`, `fips.yml`) | **Full system reboot required.** Service downtime is unavoidable. Run only during maintenance windows. The playbook emits: `WARNING: System reboot required to complete FIPS enablement`. |
| **VMware** | vCenter certificate rotation (`vcenter_certificates`) | vCenter services will restart during rotation. Lab testing is strongly recommended before production. Run only during maintenance windows. |

---

## 6. Operational Technology (OT/ICS) Environments

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

## 7. Platform-Specific Limitations

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

---

## 8. Version and Compatibility Constraints

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

## 9. Air-Gapped and Offline Deployment Constraints

For environments without internet access, agent/sensor installers cannot be automatically downloaded.

| Platform | Requirement |
|----------|-------------|
| **CrowdStrike Falcon** | Set `falcon_sensor_download_url` to a pre-staged internal URL. Sensors must be downloaded and hosted internally before running the playbook. |
| **SentinelOne** | Set `s1_agent_download_url` to a pre-staged internal URL. Same requirement as CrowdStrike. |

Both roles will fail if the download URL is unreachable and no local URL is provided.

---

## 10. STIG and Compliance Caveats

- **Not all STIG findings apply to all environments.** Review each finding for applicability before applying hardening.
- **Policy-as-Code compliance controls may impact service availability.** Review `policy_as_code/DEPLOYMENT_GUIDE.md` for pre-deployment warnings.
- **Compliance mappings are point-in-time.** The `COMPLIANCE_MAPPING.md` file reflects a specific STIG and NIST version. Validate mappings are current before using for audit purposes.
- **STIG exceptions must be documented.** Use the format `"V-XXXXX": "<justification>"` and maintain an exception register for your environment.

---

## 11. Python and Collection Dependencies

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

## 12. Network and Connectivity Requirements

- The Ansible control host must have network access to each target system's management API endpoint.
- Verify connectivity before running: `curl -k https://<management-ip>/api/`
- Firewall rules, proxies, and routing must allow API traffic from the control host.
- **TLS certificate verification:** The control host must trust the target system's TLS certificate. Add CA certificates to the control host CA bundle for environments using internal or self-signed certificates.
- **Out-of-band management access** is strongly recommended for critical infrastructure before executing any playbook.

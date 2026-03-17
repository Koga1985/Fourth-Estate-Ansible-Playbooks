# Operational Technology Tasks

This directory contains **50+ standalone task files** for Operational Technology (OT) environment management. These files target OT security platforms (Claroty, Dragos, Nozomi, etc.), OT network devices, SCADA historians, and cross-platform OT workflows. They can be included in any playbook with `ansible.builtin.include_tasks`.

## Task Files by Category

### Alerts and Incident Response
| File | Description |
|------|-------------|
| `ot_alerts__forward_splunk_hec.yml` | Forwards normalized OT alerts to a Splunk HEC endpoint. |
| `ot_alerts__forward_syslog.yml` | Forwards OT alerts to a remote syslog/SIEM target. |
| `ot_alerts__hooks_raise_incident.yml` | Opens an incident ticket in ServiceNow or Jira for high-severity OT alerts. |
| `ot_alerts__hooks_tag_asset.yml` | Tags the originating asset in the OT security platform with the alert severity. |
| `ot_alerts__pull_normalize.yml` | Pulls alerts from an OT platform API and normalizes them to a common schema. |

### Change Window and Change Control
| File | Description |
|------|-------------|
| `ot_change_window_guard__assert.yml` | Asserts that the current time falls within an approved change window; fails the play otherwise. |
| `ot_emergency_freeze__check.yml` | Reads an emergency freeze flag from a SoT file or variable and blocks downstream changes if active. |
| `ot_drift__preflight_report.yml` | Generates a pre-change drift report comparing current device state to the golden baseline. |
| `ot_whatif__capture.yml` | Captures a what-if (dry-run) summary and writes it to an artifact file for review. |

### Compliance
| File | Description |
|------|-------------|
| `ot_compliance_62443__bundle.yml` | Assembles an ISA/IEC-62443 compliance evidence bundle including audit events, role reviews, and rule diffs compressed into a ZIP archive. |

### DNS
| File | Description |
|------|-------------|
| `ot_dns__zones_forwarders_audit.yml` | Audits DNS zone configurations and forwarder settings on OT network infrastructure. |

### Firmware
| File | Description |
|------|-------------|
| `ot_firmware_register__delta_report.yml` | Compares the current firmware ledger to the previous run and reports new or changed firmware versions. |
| `ot_firmware_register__ledger_import.yml` | Imports a firmware inventory snapshot from an OT platform into the local ledger. |

### Flow Analysis and Segmentation
| File | Description |
|------|-------------|
| `ot_flows__drift_compare.yml` | Compares current network flows against an approved baseline and reports deviations. |
| `ot_flows__exceptions.yml` | Applies or removes flow exceptions for approved cross-zone communications. |
| `ot_flows__reduce_to_allowlist.yml` | Reduces observed flows to a minimum allowlist for firewall rule generation. |

### IDPS (Intrusion Detection/Prevention)
| File | Description |
|------|-------------|
| `ot_idps__exceptions_apply.yml` | Applies IDS/IPS rule exceptions for known-safe OT protocol behaviors. |
| `ot_idps__profile_baseline.yml` | Applies the baseline IDPS detection profile to OT network sensors. |

### Inventory
| File | Description |
|------|-------------|
| `ot_inventory__cmdb_sync.yml` | Pushes the normalized OT asset inventory to a CMDB (ServiceNow or similar). |
| `ot_inventory__coverage_report.yml` | Reports on OT asset visibility coverage and gaps by zone. |
| `ot_inventory__dedupe_merge.yml` | Deduplicates and merges asset records from multiple OT platform sources. |
| `ot_inventory__discover_from_platform.yml` | Pulls the current asset list from an OT security platform API. |
| `ot_inventory__normalize_labels.yml` | Normalizes site, zone, and criticality labels across the OT asset inventory. |
| `ot_inventory__ownership_map.yml` | Assigns system-owner metadata to OT assets from a mapping definition. |

### Metrics and Reporting
| File | Description |
|------|-------------|
| `ot_metrics__daily_digest.yml` | Produces a daily operational metrics digest for OT security posture. |
| `ot_metrics__monthly_summary.yml` | Generates a monthly summary report of OT security KPIs. |
| `ot_metrics__scorecards.yml` | Renders per-site or per-zone OT security scorecards. |

### Firewall and Network Policy
| File | Description |
|------|-------------|
| `ot_ngfw_checkpoint__sections_rules.yml` | Applies OT-specific firewall rule sections to a Check Point gateway. |
| `ot_ngfw_panos__sections_rules.yml` | Applies OT-specific firewall rule sections to a Palo Alto Networks NGFW. |

### PKI and Trust
| File | Description |
|------|-------------|
| `ot_pki_trust__distribute_bundles.yml` | Distributes CA trust bundles to OT devices and control systems. |
| `ot_pki_trust__expiry_report.yml` | Reports on certificate expiry dates across OT devices and infrastructure. |

### Time Synchronization
| File | Description |
|------|-------------|
| `ot_timesync__audit.yml` | Audits NTP/PTP time synchronization status across OT network devices. |
| `ot_timesync__configure.yml` | Configures NTP or PTP time synchronization settings on OT devices. |

### Topology
| File | Description |
|------|-------------|
| `ot_topology__diff_golden.yml` | Compares the current OT network topology against a golden reference and reports differences. |
| `ot_topology__export_flows.yml` | Exports OT network topology and flow data for documentation or further analysis. |

### Vulnerability Management
| File | Description |
|------|-------------|
| `ot_vuln__ingest_findings.yml` | Ingests vulnerability findings from OT security platforms into the local findings store. |
| `ot_vuln__tickets_create.yml` | Creates remediation tickets for OT vulnerability findings in a ticketing system. |
| `ot_vuln__tickets_reconcile.yml` | Reconciles open vulnerability tickets against current findings and closes resolved items. |
| `ot_vuln__worklist_build.yml` | Builds a prioritized remediation worklist from OT vulnerability findings. |

### Zone Model
| File | Description |
|------|-------------|
| `ot_zone_model__render_intents.yml` | Renders segmentation intents from the OT zone model for downstream firewall enforcement. |

### Windows HMI Patching
| File | Description |
|------|-------------|
| `ot_windows_hmi__patch_rings.yml` | Applies Windows patches to HMI systems in configured patch rings with pre/post validation. |
| `ot_windows_hmi__prechecks_snapshot.yml` | Takes a VM snapshot and runs pre-check assertions before HMI patching begins. |
| `ot_windows_hmi__rollback_hooks.yml` | Executes rollback procedures by reverting to the pre-patch snapshot on failure. |

## Usage

```yaml
---
- name: OT daily operations
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    artifacts_dir: "/tmp/ot-artifacts"

  tasks:
    - name: Assert change window is open
      ansible.builtin.include_tasks: operational_technology/tasks/ot_change_window_guard__assert.yml

    - name: Check emergency freeze status
      ansible.builtin.include_tasks: operational_technology/tasks/ot_emergency_freeze__check.yml

    - name: Pull and normalize OT inventory
      ansible.builtin.include_tasks: operational_technology/tasks/ot_inventory__discover_from_platform.yml
```

## Requirements

- Ansible 2.12+
- Credentials for the relevant OT security platforms stored in Ansible Vault
- `artifacts_dir` set to a writable local path for report and export output

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

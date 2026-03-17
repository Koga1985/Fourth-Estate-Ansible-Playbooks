# Illumio Tasks

This directory contains **47 standalone task files** for Illumio Core PCE operations. These can be included directly in any playbook for fine-grained control over specific Illumio workflows.

## Task Files by Category

### Administration
| File | Description |
|------|-------------|
| `illumio_admin__api_health.yml` | Checks PCE API health and validates authentication credentials. |
| `illumio_admin__rate_limit_guard.yml` | Inserts adaptive delays to stay within PCE API rate limits during bulk operations. |
| `illumio_org__users_roles.yml` | Manages PCE user accounts and role assignments. |

### Backup and Export
| File | Description |
|------|-------------|
| `illumio_backup__config_export.yml` | Exports PCE configuration objects (labels, services, rule sets) to JSON files. |
| `illumio_backup__policy_versions.yml` | Snapshots the current active policy version with metadata. |
| `illumio_explorer__flows_export.yml` | Exports Explorer traffic flow data for a given time window and workload set. |
| `illumio_explorer__top_talkers.yml` | Produces a top-talkers report from Explorer flow data. |
| `illumio_map__snapshot.yml` | Captures an Illumination Map snapshot for reporting. |

### Labels and Workloads
| File | Description |
|------|-------------|
| `illumio_labels__assign_workloads.yml` | Assigns labels to workloads based on a mapping definition. |
| `illumio_labels__golden_enforce.yml` | Enforces a golden label schema, flagging or correcting workloads that deviate. |
| `illumio_labels__rename_merge.yml` | Renames or merges label values across the PCE. |
| `illumio_labels__schema_apply.yml` | Applies a label type schema (dimensions) to the PCE organization. |
| `illumio_workloads__discover_sync.yml` | Syncs workload discovery results from an external source into the PCE. |
| `illumio_workloads__mode_enforce.yml` | Changes workload enforcement mode (idle/visibility/full enforcement). |
| `illumio_workloads__service_owner.yml` | Sets service-owner label metadata on workloads. |
| `illumio_workloads__ven_pair.yml` | Pairs managed workloads to the PCE using generated pairing keys. |
| `illumio_inventory__coverage_report.yml` | Reports on workload coverage and unmanaged asset counts. |
| `illumio_inventory__prune_stale.yml` | Removes stale or decommissioned workload records from the PCE. |

### Policy
| File | Description |
|------|-------------|
| `illumio_policy__brownout_check.yml` | Validates policy against brownout (potential connectivity disruption) criteria before promotion. |
| `illumio_policy__promote.yml` | Promotes the draft policy to active/provisioned state. |
| `illumio_policy__rollback.yml` | Rolls back the active policy to a previous version. |
| `illumio_policy__ven_test_mode.yml` | Switches selected workloads into test mode for policy validation. |
| `illumio_secpolicy__draft_scope.yml` | Creates or updates a scoped draft policy for a subset of workloads. |

### Rules
| File | Description |
|------|-------------|
| `illumio_rules__allowlist_from_flows.yml` | Generates allowlist rule candidates from Explorer flow data. |
| `illumio_rules__apply.yml` | Applies a defined rule set to the PCE. |
| `illumio_rules__exceptions.yml` | Adds or removes rule exceptions for specific workload pairs. |
| `illumio_rules__hitcount_report.yml` | Reports rule hit counts to identify unused or over-permissive rules. |
| `illumio_rules__shadow_overlaps_report.yml` | Identifies shadowed or overlapping rules in the active policy. |
| `illumio_iplists__manage.yml` | Creates, updates, or deletes IP list objects in the PCE. |
| `illumio_services__catalog.yml` | Manages the PCE service catalog (port/protocol definitions). |
| `illumio_vservices__manage.yml` | Manages Virtual Service objects for application-layer segmentation. |

### VEN Lifecycle
| File | Description |
|------|-------------|
| `illumio_ven__download_installer.yml` | Downloads the VEN installer package from the PCE or a mirror. |
| `illumio_ven__install_linux.yml` | Installs the VEN agent on Linux hosts. |
| `illumio_ven__install_windows.yml` | Installs the VEN agent on Windows hosts via WinRM. |
| `illumio_ven__unpair_decom.yml` | Unpairs and removes VEN from decommissioned workloads. |
| `illumio_ven__upgrade.yml` | Upgrades VEN to a target version with pre/post health checks. |

### Integrations
| File | Description |
|------|-------------|
| `illumio_int__servicenow_change.yml` | Creates or closes ServiceNow change records for policy promotions. |
| `illumio_int__servicenow_cmdb.yml` | Pushes workload and label data to the ServiceNow CMDB. |
| `illumio_int__soar_webhook.yml` | Sends policy or alert events to a SOAR platform webhook. |
| `illumio_int__splunk_hec.yml` | Forwards flow and audit event data to a Splunk HEC endpoint. |
| `illumio_int__syslog_forward.yml` | Configures PCE syslog forwarding to a remote SIEM. |

### Reporting
| File | Description |
|------|-------------|
| `illumio_report__app_scorecards.yml` | Generates per-application segmentation scorecard reports. |
| `illumio_report__audit_events.yml` | Exports PCE audit events for a defined time window. |
| `illumio_report__daily_digest.yml` | Produces a daily operational digest of policy, VEN, and alert activity. |
| `illumio_report__segmentation_score.yml` | Calculates an aggregate segmentation coverage score for the environment. |

### MSP/Multi-Tenant
| File | Description |
|------|-------------|
| `illumio_msp__baseline_labels.yml` | Applies baseline label schemas across multiple PCE organizations. |
| `illumio_msp__multi_tenant_runner.yml` | Iterates task execution across a list of PCE tenants for MSP scenarios. |

### Change Control
| File | Description |
|------|-------------|
| `illumio_guard__dry_run.yml` | Executes a policy dry-run and records what would change without committing. |
| `illumio_guard__window.yml` | Enforces a change window gate; halts execution outside approved windows. |

## Usage

```yaml
---
- name: Daily Illumio operations
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    illumio_pce_host: "pce.example.com"
    illumio_api_key: "{{ vault_illumio_api_key }}"
    illumio_api_secret: "{{ vault_illumio_api_secret }}"
    illumio_org_id: 1
    artifacts_dir: "/tmp/illumio-artifacts"

  tasks:
    - name: Check PCE health
      ansible.builtin.include_tasks: illumio/tasks/illumio_admin__api_health.yml

    - name: Export daily audit events
      ansible.builtin.include_tasks: illumio/tasks/illumio_report__audit_events.yml
```

## Requirements

- Ansible 2.12+
- Illumio PCE API reachable from the control host
- API credentials in `illumio_api_key` and `illumio_api_secret` (Ansible Vault recommended)

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

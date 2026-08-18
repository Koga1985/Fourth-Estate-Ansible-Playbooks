
# ScienceLogic (SL1) Ansible Tasks Bundle

Production-ready task files for ScienceLogic SL1 platform automation. Each task file addresses a specific operational area and is designed for use as an `include_tasks` target or as a standalone task import within a playbook.

## Artifacts

All tasks write artifacts to `{{ artifacts_dir | default('/tmp/sl1-artifacts') }}`. This directory is created automatically by each task file.

## Authentication

Every task file requires an `sl1` dict with at minimum:

```yaml
sl1:
  url: "https://sl1.example.com"
  token: "{{ vault_sl1_token }}"
  verify_ssl: true
```

## Task Files

### Platform Administration
| File | Description |
|------|-------------|
| `sl1_admin__api_health.yml` | Ping the SL1 REST API (`/api/version`), verify token auth, and write a health artifact to `artifacts_dir/api_health.json`. |
| `sl1_admin__collector_pools.yml` | Manage collector pool assignments and thresholds. |
| `sl1_admin__credential_vault.yml` | Create or update credential records in the SL1 credential vault. |
| `sl1_admin__orgs_and_users.yml` | Manage organizations and user accounts, roles, and group memberships. |

### Discovery & Inventory
| File | Description |
|------|-------------|
| `sl1_discovery__ip_range_jobs.yml` | Create and run IP-range discovery jobs; write results to artifacts. |
| `sl1_discovery__cloud_accounts.yml` | Register and trigger cloud account discovery (AWS, Azure, GCP). |
| `sl1_devices__bulk_onboard.yml` | Load a CSV/JSON source-of-truth (`devices_sot_path`) and write an onboard plan artifact. |
| `sl1_devices__tags_labels.yml` | Apply tags and labels to managed devices in bulk. |
| `sl1_devices__maintenance_windows.yml` | Create and manage maintenance windows for devices or groups. |
| `sl1_devices__prune_stale.yml` | Identify and optionally remove stale device entries. |

### Monitoring Content
| File | Description |
|------|-------------|
| `sl1_content__powerpacks_import.yml` | Import PowerPacks from file or ScienceLogic content server. |
| `sl1_dynapp__attach_policies.yml` | Attach Dynamic Application policies to device classes. |
| `sl1_dynapp__credentials_bind.yml` | Bind credentials to Dynamic Applications on target devices. |

### Automation & Remediation
| File | Description |
|------|-------------|
| `sl1_rba__actions_register.yml` | Register Run Book Automation (RBA) actions in SL1. |
| `sl1_rba__event_bindings.yml` | Map events to RBA actions; write binding plan to `artifacts_dir/rba_event_bindings.json`. |
| `sl1_powerflow__workflows_deploy.yml` | Deploy or update PowerFlow workflows; write workflow manifest to `artifacts_dir/powerflow_workflows.json`. |
| `sl1_powerflow__run_job.yml` | Trigger an existing PowerFlow job and capture run status. |

### ITSM Integration
| File | Description |
|------|-------------|
| `sl1_itsm__create_incidents.yml` | Create or update ITSM incidents from SL1 event selections with deduplication; write incident plan to `artifacts_dir/itsm_incidents_plan.json`. |
| `sl1_itsm__cmdb_sync.yml` | Synchronize SL1 device inventory to a downstream CMDB. |
| `sl1_itsm__servicenow_binding.yml` | Configure the SL1-to-ServiceNow integration binding. |

### Dashboards, KPIs & Reporting
| File | Description |
|------|-------------|
| `sl1_dashboards__deploy.yml` | Deploy or update SL1 dashboards from JSON definitions. |
| `sl1_kpi__slo_sla_export.yml` | Export SLO/SLA metrics to CSV artifacts for reporting. |
| `sl1_reports__schedule.yml` | Create or update scheduled report definitions in SL1. |
| `sl1_coverage__gaps_report.yml` | Generate a coverage gaps report identifying unmonitored or under-monitored devices. |

### Policy & Event Management
| File | Description |
|------|-------------|
| `sl1_policies__event_filters.yml` | Manage event filter policies (suppress, escalate, correlate). |
| `sl1_policies__thresholds_enforce.yml` | Enforce threshold policies across device classes. |
| `sl1_event__noise_reduction.yml` | Apply event deduplication and suppression rules. |
| `sl1_notify__email_webhook.yml` | Configure email and webhook notification templates. |
| `sl1_snmp__oid_tests.yml` | Run SNMP OID test queries and validate device responses. |

### Performance & Hygiene
| File | Description |
|------|-------------|
| `sl1_perf__polling_intervals.yml` | Adjust polling intervals for device classes or individual devices. |
| `sl1_perf__retention_policies.yml` | Configure data retention policies for performance and event data. |
| `sl1_cost__cloud_metering.yml` | Export cloud metering data for cost allocation reporting. |

## Usage Example

```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  vars:
    sl1:
      url: "https://sl1.example.com"
      token: "{{ vault_sl1_token }}"
      verify_ssl: true
    artifacts_dir: "/tmp/sl1-artifacts"
  tasks:
    - name: Check SL1 API health
      ansible.builtin.include_tasks: sl1_admin__api_health.yml

    - name: Run IP range discovery
      ansible.builtin.include_tasks: sl1_discovery__ip_range_jobs.yml
```

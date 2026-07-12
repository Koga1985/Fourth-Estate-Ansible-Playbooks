# ot_asset_lifecycle

Ot Asset Lifecycle role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `operational_technology/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ot_asset_api_url` | `"https://cmdb.agency.gov/api/v1"` | No | API Configuration |
| `ot_asset_api_token` | `""` | No | — |
| `ot_asset_verify_ssl` | `true` | No | — |
| `ot_asset_api_timeout` | `30` | No | — |
| `ot_asset_state` | `present` | No | Asset State Management present, absent, maintenance, retired |
| `ot_asset_operation` | `register` | No | register, update, decommission, dispose |
| `ot_asset_id` | `""` | No | Asset Information |
| `ot_asset_name` | `""` | No | — |
| `ot_asset_type` | `""` | No | plc, hmi, rtu, ied, scada_server, historian, switch, firewall, sensor |
| `ot_asset_vendor` | `""` | No | — |
| `ot_asset_model` | `""` | No | — |
| `ot_asset_serial_number` | `""` | No | — |
| `ot_asset_firmware_version` | `""` | No | — |
| `ot_asset_ip_address` | `""` | No | — |
| `ot_asset_mac_address` | `""` | No | — |
| `ot_asset_criticality` | `medium` | No | Asset Classification critical, high, medium, low |
| `ot_asset_purdue_level` | `""` | No | level_0, level_1, level_2, level_3, level_4, level_5 |
| `ot_asset_zone` | `""` | No | safety, control, supervision, enterprise |
| `ot_asset_function` | `""` | No | Description of asset function |
| `ot_asset_protocols` | `[]` | No | List of industrial protocols (modbus, dnp3, iec61850, opc, profinet) |
| `ot_asset_owner` | `""` | No | Asset Ownership Primary owner/responsible party |
| `ot_asset_custodian` | `""` | No | Day-to-day custodian |
| `ot_asset_support_contact` | `""` | No | — |
| `ot_asset_vendor_contact` | `""` | No | — |
| `ot_asset_facility` | `""` | No | Asset Location |
| `ot_asset_building` | `""` | No | — |
| `ot_asset_room` | `""` | No | — |
| `ot_asset_rack` | `""` | No | — |
| `ot_asset_rack_position` | `""` | No | — |
| `ot_asset_coordinates` | `""` | No | GPS coordinates if applicable |
| `ot_asset_purchase_date` | `""` | No | Lifecycle Tracking |
| `ot_asset_install_date` | `""` | No | — |
| `ot_asset_commission_date` | `""` | No | — |
| `ot_asset_warranty_expiry` | `""` | No | — |
| `ot_asset_support_contract_number` | `""` | No | — |
| `ot_asset_support_expiry` | `""` | No | — |
| `ot_asset_eol_date` | `""` | No | End of Life date |
| `ot_asset_eosl_date` | `""` | No | End of Service Life date |
| `ot_asset_maintenance_schedule` | `""` | No | Maintenance Scheduling cron format or description |
| `ot_asset_maintenance_window` | `""` | No | — |
| `ot_asset_last_maintenance` | `""` | No | — |
| `ot_asset_next_maintenance` | `""` | No | — |
| `ot_asset_maintenance_contact` | `""` | No | — |
| `ot_asset_change_control_required` | `true` | No | Change Control Integration |
| `ot_asset_change_freeze_exempt` | `false` | No | — |
| `ot_asset_emergency_change_authorized` | `false` | No | — |
| `ot_asset_compliance_frameworks` | `[]` | No | Compliance and Security nerc_cip, iec_62443, nist_800_82 |
| `ot_asset_security_classification` | `moderate` | No | high, moderate, low |
| `ot_asset_encryption_required` | `false` | No | — |
| `ot_asset_audit_logging_enabled` | `true` | No | — |
| `ot_asset_parent_id` | `""` | No | Asset Relationships Parent asset (e.g., parent system) |
| `ot_asset_dependencies` | `[]` | No | List of dependent asset IDs |
| `ot_asset_connections` | `[]` | No | Network connections to other assets |
| `ot_asset_baseline_config` | `""` | No | Asset Configuration Path to baseline configuration |
| `ot_asset_current_config` | `""` | No | Path to current configuration |
| `ot_asset_config_backup_enabled` | `true` | No | — |
| `ot_asset_config_backup_schedule` | `"0 2 * * *"` | No | Daily at 2 AM |
| `ot_asset_documentation_url` | `""` | No | Documentation |
| `ot_asset_manuals` | `[]` | No | — |
| `ot_asset_diagrams` | `[]` | No | — |
| `ot_asset_procedures` | `[]` | No | — |
| `ot_asset_monitoring_enabled` | `true` | No | Monitoring Integration |
| `ot_asset_snmp_community` | `""` | No | — |
| `ot_asset_syslog_enabled` | `true` | No | — |
| `ot_asset_metrics_collection` | `true` | No | — |
| `ot_asset_decommission_reason` | `""` | No | Decommissioning |
| `ot_asset_decommission_date` | `""` | No | — |
| `ot_asset_data_sanitization_required` | `true` | No | — |
| `ot_asset_disposal_method` | `""` | No | recycle, destroy, return_to_vendor, archive |
| `ot_asset_approval_required` | `true` | No | Workflow Configuration |
| `ot_asset_approvers` | `[]` | No | — |
| `ot_asset_notification_recipients` | `[]` | No | — |
| `ot_asset_artifacts_dir` | `/var/lib/ot-asset-lifecycle` | No | Local Configuration |
| `ot_asset_log_dir` | `/var/log/ot-asset-lifecycle` | No | — |
| `ot_asset_backup_dir` | `/var/backups/ot-assets` | No | — |
| `ot_asset_dry_run` | `false` | No | — |
| `ot_asset_require_serial_number` | `true` | No | Validation Rules |
| `ot_asset_require_ip_address` | `true` | No | — |
| `ot_asset_require_purdue_level` | `true` | No | — |
| `ot_asset_require_criticality` | `true` | No | — |
| `ot_asset_cmdb_sync` | `true` | No | Integration Settings |
| `ot_asset_siem_integration` | `true` | No | — |
| `ot_asset_ticketing_integration` | `false` | No | — |
| `ot_asset_ticketing_system` | `""` | No | servicenow, jira, remedy |
| `ot_asset_generate_reports` | `true` | No | Reporting |
| `ot_asset_report_format` | `json` | No | json, yaml, html, pdf |
| `ot_asset_report_destination` | `"{{ ot_asset_artifacts_dir }}/reports"` | No | — |

## Example Playbook

```yaml
---
- name: Ot Asset Lifecycle
  hosts: localhost
  gather_facts: false
  roles:
    - role: operational_technology/roles/ot_asset_lifecycle
```

## License

MIT

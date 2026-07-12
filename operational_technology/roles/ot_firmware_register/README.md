# ot_firmware_register
Governance ledger for firmware versions and signature checks.

## Requirements

- Ansible 2.14+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ot_firmware_api_url` | `"https://firmware-registry.agency.gov/api/v1"` | No | API Configuration |
| `ot_firmware_api_token` | `""` | No | — |
| `ot_firmware_verify_ssl` | `true` | No | — |
| `ot_firmware_api_timeout` | `60` | No | — |
| `ot_firmware_operation` | `register` | No | Operation Mode register, verify, baseline, update_plan, rollback |
| `ot_firmware_dry_run` | `false` | No | — |
| `ot_firmware_id` | `""` | No | Firmware Information |
| `ot_firmware_vendor` | `""` | No | — |
| `ot_firmware_device_type` | `""` | No | plc, hmi, rtu, ied, switch, firewall |
| `ot_firmware_device_model` | `""` | No | — |
| `ot_firmware_version` | `""` | No | — |
| `ot_firmware_release_date` | `""` | No | — |
| `ot_firmware_file_path` | `""` | No | — |
| `ot_firmware_file_url` | `""` | No | — |
| `ot_firmware_hash_algorithm` | `sha256` | No | Hash Verification md5, sha1, sha256, sha512 |
| `ot_firmware_hash_value` | `""` | No | — |
| `ot_firmware_verify_hash` | `true` | No | — |
| `ot_firmware_vendor_signature` | `""` | No | — |
| `ot_firmware_signature_verified` | `false` | No | — |
| `ot_firmware_golden_image` | `false` | No | Golden Image Repository |
| `ot_firmware_golden_image_path` | `/var/lib/ot-firmware/golden` | No | — |
| `ot_firmware_approved` | `false` | No | — |
| `ot_firmware_approval_date` | `""` | No | — |
| `ot_firmware_approved_by` | `""` | No | — |
| `ot_firmware_baseline_version` | `""` | No | Baseline Management |
| `ot_firmware_is_baseline` | `false` | No | — |
| `ot_firmware_baseline_date` | `""` | No | — |
| `ot_firmware_baseline_assets` | `[]` | No | List of asset IDs using this baseline |
| `ot_firmware_cve_ids` | `[]` | No | Vulnerability Mapping |
| `ot_firmware_vulnerability_score` | `0.0` | No | — |
| `ot_firmware_vulnerability_severity` | `none` | No | none, low, medium, high, critical |
| `ot_firmware_patches_included` | `[]` | No | — |
| `ot_firmware_security_advisories` | `[]` | No | — |
| `ot_firmware_update_window` | `""` | No | Update Planning |
| `ot_firmware_update_priority` | `medium` | No | low, medium, high, critical |
| `ot_firmware_update_impact` | `""` | No | — |
| `ot_firmware_update_prerequisites` | `[]` | No | — |
| `ot_firmware_update_dependencies` | `[]` | No | — |
| `ot_firmware_estimated_update_time` | `""` | No | — |
| `ot_firmware_rollback_supported` | `true` | No | Rollback Information |
| `ot_firmware_rollback_procedure` | `""` | No | — |
| `ot_firmware_rollback_time_estimate` | `""` | No | — |
| `ot_firmware_previous_version` | `""` | No | — |
| `ot_firmware_change_request_id` | `""` | No | Change Control Integration |
| `ot_firmware_change_approved` | `false` | No | — |
| `ot_firmware_change_freeze_exempt` | `false` | No | — |
| `ot_firmware_emergency_update` | `false` | No | — |
| `ot_firmware_testing_required` | `true` | No | Testing and Validation |
| `ot_firmware_test_environment` | `""` | No | — |
| `ot_firmware_test_results` | `""` | No | — |
| `ot_firmware_validation_status` | `pending` | No | pending, passed, failed |
| `ot_firmware_validated_by` | `""` | No | — |
| `ot_firmware_validation_date` | `""` | No | — |
| `ot_firmware_deployed_assets` | `[]` | No | Deployment Tracking |
| `ot_firmware_deployment_date` | `""` | No | — |
| `ot_firmware_deployment_method` | `""` | No | manual, automated |
| `ot_firmware_deployment_success_rate` | `100` | No | — |
| `ot_firmware_compliance_verified` | `false` | No | Compliance |
| `ot_firmware_compliance_frameworks` | `[]` | No | nerc_cip, iec_62443, nist_800_82 |
| `ot_firmware_regulatory_approval` | `false` | No | — |
| `ot_firmware_release_notes_url` | `""` | No | Documentation |
| `ot_firmware_installation_guide` | `""` | No | — |
| `ot_firmware_known_issues` | `[]` | No | — |
| `ot_firmware_compatibility_matrix` | `[]` | No | — |
| `ot_firmware_vendor_contact` | `""` | No | Metadata |
| `ot_firmware_support_url` | `""` | No | — |
| `ot_firmware_eol_date` | `""` | No | — |
| `ot_firmware_tags` | `[]` | No | — |
| `ot_firmware_notes` | `""` | No | — |
| `ot_firmware_artifacts_dir` | `/var/lib/ot-firmware` | No | Local Configuration |
| `ot_firmware_log_dir` | `/var/log/ot-firmware` | No | — |
| `ot_firmware_backup_dir` | `/var/backups/ot-firmware` | No | — |
| `ot_firmware_repository_dir` | `/var/lib/ot-firmware/repository` | No | — |
| `ot_firmware_cmdb_sync` | `true` | No | Integration Settings |
| `ot_firmware_vulnerability_scan` | `true` | No | — |
| `ot_firmware_notify_on_new` | `true` | No | — |
| `ot_firmware_notification_recipients` | `[]` | No | — |
| `ot_firmware_generate_reports` | `true` | No | Reporting |
| `ot_firmware_report_format` | `json` | No | json, yaml, html |
| `ot_firmware_report_destination` | `"{{ ot_firmware_artifacts_dir }}/reports"` | No | — |
| `ot_firmware_binary_analysis` | `false` | No | Advanced Features |
| `ot_firmware_malware_scan` | `false` | No | — |
| `ot_firmware_code_signing_required` | `true` | No | — |
| `ot_firmware_integrity_monitoring` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ot_firmware_register
  hosts: all
  gather_facts: false
  roles:
    - role: ot_firmware_register
```

## License

MIT

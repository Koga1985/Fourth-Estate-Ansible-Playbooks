# claroty_xdome_secure_access_audit_export

Exports Secure Remote Access audit logs from Claroty xDome with configurable filters, time ranges, and log types. Writes results to CSV/JSON locally and optionally forwards to a SIEM (Splunk, QRadar, ArcSight, Azure Sentinel), creates ServiceNow incidents for violations, and generates compliance reports for NERC CIP, IEC 62443, and NIST 800-82.

## Requirements

- Ansible 2.15+
- `CLAROTY_API_TOKEN` environment variable set (or override via `claroty.token`)
- Network access to the Claroty xDome API endpoint
- Python `requests` library on the Ansible control node

## Role Variables

### Core

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/claroty-artifacts"` | No | Local directory for exported log files |
| `log_dir` | `"/var/log/claroty"` | No | Directory for role operational logs |

### Claroty API

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `claroty.base_url` | `"https://xdome.claroty.com/api"` | **Yes** | xDome API base URL |
| `claroty.token` | `$CLAROTY_API_TOKEN` | **Yes** | API authentication token (vault-protected) |
| `claroty.verify_ssl` | `true` | No | Verify xDome TLS certificate |
| `claroty.timeout` | `60` | No | API request timeout in seconds |

### Audit Export

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `audit_export.enabled` | `true` | No | Enable audit log export |
| `audit_export.export_formats` | `["csv", "json", "syslog"]` | No | Output formats |
| `audit_export.time_range.mode` | `"relative"` | No | `"relative"` or `"absolute"` |
| `audit_export.time_range.relative_range` | `"24h"` | No | Relative range: `1h`, `24h`, `7d`, `30d` |
| `audit_export.time_range.start_time` | `""` | No | ISO 8601 start time (absolute mode) |
| `audit_export.time_range.end_time` | `""` | No | ISO 8601 end time (absolute mode) |
| `audit_export.log_types` | see defaults | No | List of log type strings to export (session_logs, user_activity, connection_logs, file_transfer_logs, command_execution, failed_access, policy_violations, mfa_events, certificate_events) |
| `audit_export.filters.users` | `[]` | No | Filter by user email addresses |
| `audit_export.filters.user_types` | `[]` | No | Filter by user type: vendor, contractor, employee |
| `audit_export.filters.source_ips` | `[]` | No | Filter by source IP |
| `audit_export.filters.protocols` | `[]` | No | Filter by protocol: rdp, ssh, vnc, https |
| `audit_export.filters.min_severity` | `"info"` | No | Minimum severity: debug, info, warning, error, critical |
| `audit_export.filters.include_successful` | `true` | No | Include successful sessions |
| `audit_export.filters.include_failed` | `true` | No | Include failed access attempts |
| `audit_export.filters.include_policy_violations` | `true` | No | Include policy violation events |
| `audit_export.enrichment.include_user_details` | `true` | No | Enrich records with user profile data |
| `audit_export.enrichment.include_asset_details` | `true` | No | Enrich records with asset metadata |
| `audit_export.enrichment.include_geo_location` | `true` | No | Add geolocation data to records |
| `audit_export.enrichment.include_session_recordings` | `false` | No | Include session recording metadata |

### SIEM Integration

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `siem_integration.enabled` | `false` | No | Forward logs to a SIEM |
| `siem_integration.platform` | `"splunk"` | No | Target SIEM: splunk, qradar, arcsight, sentinel |
| `siem_integration.splunk.hec_url` | `"https://splunk.agency.gov:8088/..."` | No | Splunk HEC endpoint |
| `siem_integration.splunk.hec_token` | `$SPLUNK_HEC_TOKEN` | **Yes if Splunk** | Splunk HEC token (vault-protected) |
| `siem_integration.splunk.index` | `"claroty_audit"` | No | Splunk index |
| `siem_integration.splunk.sourcetype` | `"claroty:xdome:audit"` | No | Splunk sourcetype |

### ServiceNow Integration

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `servicenow_integration.enabled` | `false` | No | Create ServiceNow incidents for violations |
| `servicenow_integration.instance` | `"agency.service-now.com"` | No | ServiceNow instance hostname |
| `servicenow_integration.token` | `$SERVICENOW_TOKEN` | **Yes if enabled** | ServiceNow API token (vault-protected) |
| `servicenow_integration.create_incidents_for` | `["policy_violations", "failed_access", "suspicious_activity"]` | No | Event types that trigger incident creation |
| `servicenow_integration.assignment_group` | `"OT Security Team"` | No | Incident assignment group |
| `servicenow_integration.priority` | `"2"` | No | Incident priority |

### Compliance Reporting

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `compliance.enabled` | `true` | No | Generate compliance reports |
| `compliance.standards` | `["nerc_cip", "iec_62443", "nist_800_82"]` | No | Compliance frameworks to report against |
| `compliance.report_formats` | `["pdf", "csv"]` | No | Report output formats |

### Scheduled Exports

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `scheduled_exports.enabled` | `false` | No | Enable scheduled (cron-driven) exports |
| `scheduled_exports.schedule` | `"0 2 * * *"` | No | Cron expression for export schedule |
| `scheduled_exports.retention_days` | `365` | No | Days to retain exported files |
| `scheduled_exports.compress` | `true` | No | Compress exports with gzip |
| `scheduled_exports.encrypt` | `true` | No | Encrypt exports at rest |

### Export Destinations

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `export_destinations.local_filesystem.enabled` | `true` | No | Write exports to `artifacts_dir` |
| `export_destinations.s3.enabled` | `false` | No | Upload exports to S3 |
| `export_destinations.s3.bucket` | `"agency-claroty-audit-logs"` | No | S3 bucket name |
| `export_destinations.s3.region` | `"us-gov-west-1"` | No | AWS region |
| `export_destinations.sftp.enabled` | `false` | No | Transfer exports via SFTP |

## Example Playbook

```yaml
- name: Export Claroty xDome audit logs (last 24h)
  hosts: localhost
  gather_facts: false
  roles:
    - role: claroty/roles/claroty_xdome_secure_access_audit_export
      vars:
        claroty:
          base_url: "https://xdome.agency.gov/api"
          token: "{{ vault_claroty_token }}"
        audit_export:
          time_range:
            mode: relative
            relative_range: "24h"
          filters:
            min_severity: "warning"
            include_policy_violations: true
        siem_integration:
          enabled: true
          platform: splunk
          splunk:
            hec_url: "https://splunk.agency.gov:8088/services/collector"
            hec_token: "{{ vault_splunk_hec_token }}"
```

## Tags

| Tag | Description |
|-----|-------------|
| `export` | Run audit log export |
| `siem` | Forward logs to SIEM |
| `servicenow` | Create ServiceNow incidents |
| `compliance` | Generate compliance reports |

## Compliance Controls

| Framework | Control ID | Description |
|-----------|-----------|-------------|
| NIST 800-53 | AU-2 | Audit Events |
| NIST 800-53 | AU-9 | Protection of Audit Information |
| NIST 800-53 | AU-12 | Audit Record Generation |
| NIST 800-53 | CA-7 | Continuous Monitoring |
| NIST 800-53 | IR-4 | Incident Handling |
| IEC 62443 | SR 6.1 | Audit Log Accessibility |
| NERC CIP | CIP-007-6 R4 | Security Event Monitoring |

## Notes

- The Claroty API token must have `Audit Log Export` permissions.
- `audit_export.enrichment.include_session_recordings: false` by default — enabling this significantly increases export size and API latency.
- `scheduled_exports.enabled: false` by default; this role is designed for on-demand invocation. Use a cron job or Ansible AWX schedule to automate recurring exports.
- Compliance reports require the compliance module to be licensed on your xDome instance.

## License

MIT

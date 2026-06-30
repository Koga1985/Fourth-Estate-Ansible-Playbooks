# Dynatrace Audit Export (`dynatrace_audit_export`)

Exports the **Dynatrace audit log** to a local **NDJSON evidence file** and
optionally forwards each record to a **SIEM/HTTP collector** (e.g., Splunk HEC).
Supports **NIST 800-53 AU-6 / AU-9 / AU-11** (audit review, protection, retention)
for the ATO/evidence package.

## Why "grab and go"
* Read-only against Dynatrace (`GET /api/v2/auditlogs`); token `no_log`.
* Writes a timestamped NDJSON file + a JSON summary artifact every run — designed
  to run on a **schedule** (cron / AWX / AAP) to retain audit evidence.

## Quick start
```bash
cd dynatrace/roles/dynatrace_audit_export/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml
cat /tmp/dynatrace-artifacts/dynatrace_audit_export.json
```

## Key variables
| Variable | Purpose |
|----------|---------|
| `audit_lookback` | Dynatrace relative window (e.g. `now-24h`) — align to your schedule |
| `audit_filter` | optional server-side filter (eventType/category/...) |
| `audit_output_file` | NDJSON evidence destination |
| `audit_forward_url` / `audit_forward_headers` | optional SIEM forward (e.g. Splunk HEC) |

> If the summary reports `more_pages: true`, shorten the window or run more
> frequently so each run captures a full page. Token scope: `auditLogs.read`.

## Tags
`--tags export`, `forward`, `report`.

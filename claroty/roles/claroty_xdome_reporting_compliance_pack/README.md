# claroty_xdome_reporting_compliance_pack

Builds a CSV-based compliance evidence bundle from Claroty xDome by exporting alerts, secure access session logs, and asset change records. All artifacts are written to `artifacts_dir`.

## What it does

1. **Exports alerts** — POSTs to `/v1/alerts/search` with `alerts_filter`; writes `alerts_csv` with columns: `id`, `severity`, `category`, `asset`, `site`, `detected_at`, `status`.
2. **Exports secure access logs** — POSTs to `/v1/secure-access/logs/search` with `access_logs_filter`; writes `access_csv` with columns: `datetime`, `user`, `vendor`, `asset`, `site`, `action`, `result`, `reason`, `session_id`.
3. **Exports change records** — POSTs to `/v1/changes/search` with `changes_filter`; writes `changes_csv` with columns: `datetime`, `actor`, `entity`, `action`, `details`. The `/v1/changes/search` endpoint availability varies by xDome version; verify the endpoint path against your deployment's API documentation and update `changes_filter` accordingly.

## Variables (see `defaults/main.yml`)

```yaml
artifacts_dir: "/tmp/claroty-artifacts"

# Query filters (all default to last 30 days)
alerts_filter:
  severity: ["high", "critical"]
  since: "30d"
access_logs_filter:
  since: "30d"
changes_filter:
  since: "30d"

# Output filenames
alerts_csv: "compliance_alerts.csv"
access_csv: "compliance_access.csv"
changes_csv: "compliance_changes.csv"
```

Required variable (not in defaults):

```yaml
claroty:
  base_url: "https://xdome.example.com"
  token: "{{ vault_claroty_token }}"
  verify_ssl: true
```

## Example play

```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: claroty_xdome_reporting_compliance_pack
      vars:
        claroty:
          base_url: "https://xdome.example.com"
          token: "{{ vault_claroty_token }}"
        alerts_filter:
          severity: ["medium", "high", "critical"]
          since: "90d"
        access_logs_filter:
          since: "90d"
        changes_filter:
          since: "90d"
```

## Outputs

| File | Description |
|------|-------------|
| `artifacts_dir/compliance_alerts.csv` | Alert records with severity, category, asset, site, detection time, and status |
| `artifacts_dir/compliance_access.csv` | Secure access session logs with user, vendor, asset, action, result, and session ID |
| `artifacts_dir/compliance_changes.csv` | Asset and configuration change records with actor, entity, action, and details |

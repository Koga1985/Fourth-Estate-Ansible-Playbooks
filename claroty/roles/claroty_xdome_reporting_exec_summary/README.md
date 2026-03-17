# claroty_xdome_reporting_exec_summary

Generates executive summary CSV reports from Claroty xDome asset, risk, and alert data. Produces two artifacts: an asset coverage summary and a KPI metrics report.

## What it does

1. **Pulls asset inventory** — POSTs to `/v1/assets/search` with `inventory_filter` and collects asset count, unique sites, and device types.
2. **Pulls open risks** — POSTs to `/v1/risks/search` with `risk_filter` (defaults to open risks with minimum risk score of 1).
3. **Pulls recent alerts** — POSTs to `/v1/alerts/search` with `alerts_filter` (defaults to high/critical severity in the last 30 days).
4. **Writes a coverage CSV** (`coverage_csv`) — Columns: `total_assets`, `sites`, `device_types`.
5. **Writes a KPI CSV** (`kpi_csv`) — Columns: `date`, `open_risks`, `critical_high`, `median_risk`, `mttr_days_est`. The `critical_high` count includes risks with a score of 80 or above. The `median_risk` is computed from sorted risk scores. The `mttr_days_est` field requires closed-ticket data not available from the risks endpoint; it is set to `0` by default and should be populated by integrating with your ITSM system (e.g., ServiceNow) to calculate actual mean time to remediate from ticket open/close timestamps.

## Variables (see `defaults/main.yml`)

```yaml
artifacts_dir: "/tmp/claroty-artifacts"

# Query filters
inventory_filter: {}               # Empty = all assets; filter by site, type, etc.
risk_filter:
  status: ["open"]
  minRisk: 1
alerts_filter:
  severity: ["high", "critical"]
  since: "30d"

# Output filenames
coverage_csv: "exec_coverage.csv"
kpi_csv: "exec_kpi.csv"
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
    - role: claroty_xdome_reporting_exec_summary
      vars:
        claroty:
          base_url: "https://xdome.example.com"
          token: "{{ vault_claroty_token }}"
        inventory_filter:
          site: "Plant-A"
        alerts_filter:
          severity: ["high", "critical"]
          since: "7d"
```

## Outputs

| File | Description |
|------|-------------|
| `artifacts_dir/exec_coverage.csv` | Asset coverage summary: total assets, site count, device type count |
| `artifacts_dir/exec_kpi.csv` | KPI metrics: open risks, critical/high count, median risk score, MTTR estimate |

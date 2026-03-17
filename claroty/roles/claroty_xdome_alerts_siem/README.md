# claroty_xdome_alerts_siem

Polls the Claroty xDome alerts API, writes a CSV artifact, forwards raw alert JSON to an HTTP SIEM endpoint, and optionally tags high/critical assets back in xDome or raises tickets in ServiceNow or Jira.

## Requirements

- Ansible 2.12+
- Network access to the Claroty xDome API (HTTPS)
- A valid xDome bearer token
- For SIEM forwarding: an HTTP/HTTPS ingest endpoint with a valid bearer token
- For ticketing: ServiceNow or Jira instance with REST API access

## Role Variables

### Connection (required)

| Variable | Description |
|----------|-------------|
| `claroty.base_url` | Base URL of the Claroty xDome instance (e.g. `https://xdome.example.com`). |
| `claroty.token` | Bearer token for xDome API authentication. Store in Ansible Vault. |
| `claroty.verify_ssl` | Whether to verify the xDome TLS certificate. Default: `true`. |

### Alert Filtering

| Variable | Default | Description |
|----------|---------|-------------|
| `alert_filter.severity` | `["high","critical"]` | List of severity values to include. |
| `alert_filter.since` | `"24h"` | Time window for alert retrieval (relative string or ISO 8601 timestamp). |
| `alert_filter.limit` | `2000` | Maximum number of alerts to retrieve per run. |

### SIEM Forwarding

| Variable | Default | Description |
|----------|---------|-------------|
| `forward.enabled` | `false` | Enable HTTP forwarding of alert payload to a SIEM endpoint. |
| `forward.type` | `"http"` | Forwarding method. Currently supports `http`. |
| `forward.endpoint` | `"https://siem.example/ingest"` | URL of the SIEM ingest endpoint. |
| `forward.token` | `""` | Bearer token for the SIEM endpoint. Falls back to `SIEM_TOKEN` environment variable. |
| `forward.verify_ssl` | `true` | Whether to verify the SIEM endpoint TLS certificate. |

### Hooks

| Variable | Default | Description |
|----------|---------|-------------|
| `hooks.tag_asset` | `false` | Tag the originating xDome asset with the alert severity for high/critical alerts. |
| `hooks.raise_ticket` | `false` | Create a ticket in the configured ticketing system for high/critical alerts. |
| `hooks.ticketing.system` | `"servicenow"` | Ticketing system to use: `servicenow` or `jira`. |
| `hooks.ticketing.instance` | `null` | ServiceNow instance hostname or Jira base URL. |
| `hooks.ticketing.token` | `""` | Bearer token. Falls back to `TICKET_TOKEN` environment variable. |
| `hooks.ticketing.table` | `"incident"` | ServiceNow table to write tickets to (ServiceNow only). |
| `hooks.ticketing.project_key` | `"SEC"` | Jira project key (Jira only). |

### Output

| Variable | Default | Description |
|----------|---------|-------------|
| `artifacts_dir` | `"/tmp/claroty-artifacts"` | Directory for CSV artifact output. Created if it does not exist. |

## Dependencies

None.

## Example Playbook

```yaml
---
- name: Pull Claroty alerts and forward to Splunk HEC
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    claroty:
      base_url: "https://xdome.example.com"
      token: "{{ vault_claroty_token }}"
      verify_ssl: true
    alert_filter:
      severity: ["high", "critical"]
      since: "6h"
      limit: 500
    forward:
      enabled: true
      type: http
      endpoint: "https://splunk.example.com:8088/services/collector"
      token: "{{ vault_splunk_hec_token }}"
      verify_ssl: true
    hooks:
      tag_asset: true
      raise_ticket: true
      ticketing:
        system: servicenow
        instance: "myorg.service-now.com"
        token: "{{ vault_snow_token }}"
        table: incident
    artifacts_dir: "/opt/claroty/artifacts"

  roles:
    - role: claroty/roles/claroty_xdome_alerts_siem
```

## Output Artifacts

- `{{ artifacts_dir }}/xdome_alerts.csv` — CSV file containing all retrieved alerts with columns: `id`, `severity`, `category`, `asset`, `site`, `detected_at`, `status`, `desc`.

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

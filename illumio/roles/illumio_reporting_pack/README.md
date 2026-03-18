# illumio_reporting_pack

Generates a suite of CSV reports from the Illumio PCE API: an overall segmentation KPI scorecard, per-application workload scorecards, a 24-hour operational digest, and an optional time-windowed audit-event export. Reports are written to `artifacts_dir` on the Ansible controller and are suitable for ingestion into a SIEM, dashboard, or compliance-tracking system.

## Requirements

- Ansible 2.12 or later
- Network connectivity from the Ansible controller to the Illumio PCE API (`pce_url`)
- The following variables must be supplied at runtime:
  - `pce_url` — base URL of the PCE (e.g. `https://pce.example.mil:8443`)
  - `org_id` — PCE organization ID (integer)
  - `api_user` — PCE API username
  - `api_key` — PCE API key (store in Ansible Vault)

## Role Variables

All variables are defined in `defaults/main.yml`.

| Variable | Default | Required | Description |
|---|---|---|
| `verify_ssl` | `true` | No | Verify TLS certificates when calling the PCE API. |
| `artifacts_dir` | `/tmp/illumio-artifacts` | No | Directory on the Ansible controller where CSV report files are written. Created automatically if it does not exist. |
| `start_time` | _(undefined)_ | No | ISO 8601 start timestamp for the audit-event export (e.g. `2026-03-16T00:00:00Z`). When undefined, the audit-events task is skipped. |
| `end_time` | _(undefined)_ | No | ISO 8601 end timestamp for the audit-event export. When undefined, the audit-events task is skipped. |

### Runtime-only variables (no defaults)

| Variable | Description |
|---|---|
| `pce_url` | Base URL of the PCE. |
| `org_id` | PCE organization ID integer. |
| `api_user` | PCE API authentication username. |
| `api_key` | PCE API key. Store in Ansible Vault. |

## Reports Generated

| File | Description |
|---|---|
| `segmentation_score.csv` | Single-row KPI: total workloads, percentage labeled, percentage enforced, active rule-set count. |
| `app_scorecards.csv` | Per-workload rows grouped by application label: labeled and enforced counts and percentages. |
| `daily_digest.csv` | Count of new workloads, policy audit events, and exceptions created within the last 24 hours (or a custom window via `since`/`until`). |
| `audit_events.csv` | _(Optional)_ Raw audit event export for the time window defined by `start_time` and `end_time`. Only generated when both variables are set. |

## Example Playbook

```yaml
- name: Generate Illumio PCE reporting pack
  hosts: localhost
  gather_facts: false
  roles:
    - role: illumio_reporting_pack
      vars:
        pce_url: "https://pce.dc1.example.mil:8443"
        org_id: 1
        api_user: "{{ vault_illumio_api_user }}"
        api_key: "{{ vault_illumio_api_key }}"
        artifacts_dir: /opt/reports/illumio
```

### With audit event export

```yaml
- name: Generate Illumio reporting pack with audit export
  hosts: localhost
  gather_facts: false
  roles:
    - role: illumio_reporting_pack
      vars:
        pce_url: "https://pce.dc1.example.mil:8443"
        org_id: 1
        api_user: "{{ vault_illumio_api_user }}"
        api_key: "{{ vault_illumio_api_key }}"
        start_time: "2026-03-16T00:00:00Z"
        end_time: "2026-03-17T00:00:00Z"
```

## Notes and Dependencies

- All PCE API calls use `no_log: true` to prevent credentials from appearing in Ansible output or logs.
- The daily digest uses a rolling 24-hour window by default. Override the window start and end with the `since` and `until` variables inside the include, or supply `start_time`/`end_time` for the audit-event export.
- The role makes direct HTTPS calls to the PCE API using `ansible.builtin.uri`. No Illumio Ansible collection is required.
- All tasks run on `localhost` (the Ansible controller). No remote hosts are required.
- Report CSV files are overwritten on each run. If historical reports must be retained, configure `artifacts_dir` to a timestamped path or handle archiving externally.

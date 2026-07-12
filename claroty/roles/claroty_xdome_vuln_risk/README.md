# claroty_xdome_vuln_risk
Pulls risks, builds remediation worklists, optional ticketing to ServiceNow/Jira, and writes KPI snapshots.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/claroty-artifacts"` | No | — |
| `risk_filter` | `{ status: ["open"], minRisk: 1, limit: 1000 }` | No | — |
| `ticketing` | `{ enable: false, system: "servicenow", instance: null, token: "{{ l...` | No | — |
| `kpi` | `{ enabled: true, csv_prefix: "xdome_risk_trend" }` | No | — |

## Example Playbook

```yaml
- name: Use claroty_xdome_vuln_risk
  hosts: all
  gather_facts: false
  roles:
    - role: claroty_xdome_vuln_risk
```

## License

MIT

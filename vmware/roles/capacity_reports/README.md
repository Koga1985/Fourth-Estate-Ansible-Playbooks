# capacity_reports

Capacity Reports role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vmware/README.md`

## Requirements

- Ansible 2.15+
- Collection: `community.vmware`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vcenter_hostname` | `""` | No | vCenter connection |
| `vcenter_username` | `""` | No | — |
| `vcenter_password` | `""` | No | — |
| `vcenter_validate_certs` | `false` | No | — |
| `vcenter_datacenter` | `""` | No | Scope Datacenter name to report on |
| `clusters` | `[]` | No | Optional: limit to these clusters; empty = all in DC |
| `include_datastores_regex` | `""` | No | Optional regex to filter datastores (e.g., "^vsan\|^nfs-prod") |
| `out_dir` | `"/tmp"` | No | Output (BI-friendly) |
| `csv_clusters` | `"{{ out_dir }}/capacity_clusters.csv"` | No | — |
| `csv_datastores` | `"{{ out_dir }}/capacity_datastores.csv"` | No | — |
| `json_summary` | `"{{ out_dir }}/capacity_summary.json"` | No | — |
| `history_csv` | `"{{ out_dir }}/capacity_history.csv"` | No | Optional history & trend set to "" to disable history |
| `trend_days` | `90` | No | compute simple linear trend over N days if history present |
| `warn_free_pct` | `20` | No | Headroom thresholds (percent free) |
| `crit_free_pct` | `10` | No | — |

## Example Playbook

```yaml
---
- name: Capacity Reports
  hosts: localhost
  gather_facts: false
  roles:
    - role: vmware/roles/capacity_reports
```

## License

MIT

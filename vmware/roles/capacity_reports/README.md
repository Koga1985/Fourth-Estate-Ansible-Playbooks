# capacity_reports

Capacity Reports role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vmware/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vcenter_hostname` | `""` |  |
| `vcenter_username` | `""` |  |
| `vcenter_password` | `""` |  |
| `vcenter_validate_certs` | `false` |  |
| `vcenter_datacenter` | `""` | No | Datacenter name to report on |
| `clusters` | `[]` | No | Optional: limit to these clusters; empty = all in DC |
| `include_datastores_regex` | `""` | Optional regex to filter datastores (e.g., "^vsan|^nfs-prod") |
| `out_dir` | `"/tmp"` |  |
| `csv_clusters` | `"{{ out_dir }}/capacity_clusters.csv"` |  |
| `csv_datastores` | `"{{ out_dir }}/capacity_datastores.csv"` |  |
| `json_summary` | `"{{ out_dir }}/capacity_summary.json"` |  |
| `history_csv` | `"{{ out_dir }}/capacity_history.csv"` | No | set to "" to disable history |
| `trend_days` | `90` | No | compute simple linear trend over N days if history present |
| `warn_free_pct` | `20` |  |
| `crit_free_pct` | `10` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `community.vmware`
- See platform `requirements.yml` for install instructions

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

# pure_fa_data_protection

Pure Fa Data Protection role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `fa_url` | `"10.0.0.10"` | No | — |
| `api_token` | `"{{ lookup('env','PURE_FA_TOKEN') }}"` | No | — |
| `validate_certs` | `false` | No | — |
| `artifacts_dir` | `"/tmp/pure-artifacts"` | No | — |
| `snap_jobs` | `[]` | No | — |
| `snap_policies` | `[]` | No | — |
| `pgroups` | `[]` | No | — |
| `peers` | `[]` | No | — |
| `pg_links` | `[]` | No | — |
| `ac_pods` | `[]` | No | — |
| `adr_pods` | `[]` | No | — |
| `clones` | `[]` | No | — |

## Example Playbook

```yaml
---
- name: Pure Fa Data Protection
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_fa_data_protection
```

## License

MIT

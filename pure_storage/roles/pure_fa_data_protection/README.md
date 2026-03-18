# pure_fa_data_protection

Pure Fa Data Protection role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `fa_url` | `"10.0.0.10"` |  |
| `api_token` | `"{{ lookup('env','PURE_FA_TOKEN') }}"` |  |
| `validate_certs` | `false` |  |
| `artifacts_dir` | `"/tmp/pure-artifacts"` |  |
| `snap_jobs` | `[]` |  |
| `snap_policies` | `[]` |  |
| `pgroups` | `[]` |  |
| `peers` | `[]` |  |
| `pg_links` | `[]` |  |
| `ac_pods` | `[]` |  |
| `adr_pods` | `[]` |  |
| `clones` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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

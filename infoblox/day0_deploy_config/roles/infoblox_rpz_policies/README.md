# infoblox_rpz_policies

Infoblox Rpz Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/day0_deploy_config/README.md`

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `nios_host` | `""` | No | — |
| `nios_username` | `""` | No | — |
| `nios_password` | `""` | No | — |
| `nios_validate_certs` | `false` | No | — |
| `nios_wapi_version` | `"v2.12"` | No | — |
| `rpz_dns_view` | `"default"` | No | — |
| `rpz_zones` | `[]` | No | — |
| `rpz_enforcement_order` | `[]` | No | — |
| `rpz_sync` | `false` | No | — |
| `artifact_dir` | `"/tmp/infoblox-rpz"` | No | — |

## Example Playbook

```yaml
---
- name: Infoblox Rpz Policies
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/day0_deploy_config/roles/infoblox_rpz_policies
```

## License

MIT

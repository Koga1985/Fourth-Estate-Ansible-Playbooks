# infoblox_tsig_acls

Infoblox Tsig Acls role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/day0_deploy_config/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `nios_host` | `""` |  |
| `nios_username` | `""` |  |
| `nios_password` | `""` |  |
| `nios_validate_certs` | `false` |  |
| `nios_wapi_version` | `"v2.12"` |  |
| `artifact_dir` | `"/tmp/infoblox-tsig-acls"` |  |
| `tsig_keys` | `[]` |  |
| `named_acls` | `[]` |  |
| `dns_view_policies` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Infoblox Tsig Acls
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/day0_deploy_config/roles/infoblox_tsig_acls
```

## License

MIT

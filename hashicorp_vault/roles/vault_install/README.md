# vault_install

Vault Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `hashicorp_vault/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `vault_version` | `"1.15.4"` |  |
| `vault_enterprise` | `false` |  |
| `vault_license_path` | `""` |  |
| `vault_bin_path` | `"/usr/local/bin"` |  |
| `vault_config_path` | `"/etc/vault.d"` |  |
| `vault_data_path` | `"/opt/vault/data"` |  |
| `vault_tls_path` | `"/etc/vault.d/tls"` |  |
| `vault_plugin_path` | `"/etc/vault.d/plugins"` |  |
| `vault_log_path` | `"/var/log/vault"` |  |
| `vault_user` | `"vault"` |  |
| `vault_group` | `"vault"` |  |
| `vault_uid` | `8200` |  |
| `vault_gid` | `8200` |  |
| `vault_address` | `"0.0.0.0"` |  |
| `vault_port` | `8200` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `community.hashi_vault`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Vault Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: hashicorp_vault/roles/vault_install
```

## License

MIT

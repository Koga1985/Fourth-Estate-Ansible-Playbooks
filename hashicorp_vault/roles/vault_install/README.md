# vault_install

Vault Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `hashicorp_vault/README.md`

## Requirements

- Ansible 2.15+
- Collection: `community.hashi_vault`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vault_version` | `"1.15.4"` | No | Vault version |
| `vault_enterprise` | `false` | No | — |
| `vault_license_path` | `""` | No | — |
| `vault_bin_path` | `"/usr/local/bin"` | No | Installation paths |
| `vault_config_path` | `"/etc/vault.d"` | No | — |
| `vault_data_path` | `"/opt/vault/data"` | No | — |
| `vault_tls_path` | `"/etc/vault.d/tls"` | No | — |
| `vault_plugin_path` | `"/etc/vault.d/plugins"` | No | — |
| `vault_log_path` | `"/var/log/vault"` | No | — |
| `vault_user` | `"vault"` | No | User and group |
| `vault_group` | `"vault"` | No | — |
| `vault_uid` | `8200` | No | — |
| `vault_gid` | `8200` | No | — |
| `vault_address` | `"0.0.0.0"` | No | Network configuration |
| `vault_port` | `8200` | No | — |
| `vault_cluster_port` | `8201` | No | — |
| `vault_api_addr` | `"https://{{ ansible_fqdn }}:8200"` | No | — |
| `vault_cluster_addr` | `"https://{{ ansible_default_ipv4.address }}:8201"` | No | — |
| `vault_tls_disable` | `false` | No | TLS configuration |
| `vault_tls_cert_file` | `"{{ vault_tls_path }}/vault-cert.pem"` | No | — |
| `vault_tls_key_file` | `"{{ vault_tls_path }}/vault-key.pem"` | No | — |
| `vault_tls_ca_file` | `"{{ vault_tls_path }}/ca-cert.pem"` | No | — |
| `vault_tls_min_version` | `"tls13"` | No | — |
| `vault_tls_cipher_suites` | `""` | No | — |
| `vault_tls_require_and_verify_client_cert` | `false` | No | — |
| `vault_tls_disable_client_certs` | `false` | No | — |
| `vault_seal_type` | `"awskms"` | No | Auto-unseal configuration Options: awskms, azurekeyvault, gcpckms, shamir |
| `vault_awskms_region` | `"us-gov-west-1"` | No | — |
| `vault_awskms_kms_key_id` | `""` | No | — |
| `vault_awskms_endpoint` | `""` | No | — |
| `vault_azure_tenant_id` | `""` | No | — |
| `vault_azure_client_id` | `""` | No | — |
| `vault_azure_client_secret` | `""` | No | — |
| `vault_azure_vault_name` | `""` | No | — |
| `vault_azure_key_name` | `""` | No | — |
| `vault_storage_type` | `"raft"` | No | Storage backend (default: raft) |
| `vault_raft_node_id` | `"{{ ansible_hostname }}"` | No | — |
| `vault_raft_path` | `"{{ vault_data_path }}/raft"` | No | — |
| `vault_raft_performance_multiplier` | `1` | No | — |
| `vault_raft_trailing_logs` | `10000` | No | — |
| `vault_raft_snapshot_threshold` | `8192` | No | — |
| `vault_raft_max_entry_size` | `1048576` | No | — |
| `vault_disable_mlock` | `false` | No | Performance tuning |
| `vault_disable_cache` | `false` | No | — |
| `vault_max_lease_ttl` | `"768h"` | No | — |
| `vault_default_lease_ttl` | `"768h"` | No | — |
| `vault_disable_clustering` | `false` | No | — |
| `vault_ui` | `true` | No | UI configuration |
| `vault_telemetry_enabled` | `true` | No | Telemetry |
| `vault_telemetry_statsd_address` | `"127.0.0.1:8125"` | No | — |
| `vault_telemetry_disable_hostname` | `false` | No | — |
| `vault_prometheus_retention_time` | `"24h"` | No | — |
| `vault_service_enabled` | `true` | No | Service configuration |
| `vault_service_state` | `"started"` | No | — |
| `vault_log_level` | `"info"` | No | Log configuration trace, debug, info, warn, error |
| `vault_log_format` | `"json"` | No | — |
| `vault_enable_syslog` | `true` | No | — |
| `vault_syslog_facility` | `"LOCAL0"` | No | — |
| `vault_enable_fips` | `false` | No | FIPS 140-2 mode |
| `vault_enable_namespaces` | `false` | No | Namespace configuration (Enterprise) |
| `vault_install_license` | `false` | No | License (Enterprise) |
| `vault_license_content` | `""` | No | — |
| `vault_install_plugins` | `[]` | No | Plugins |
| `vault_nofile_limit` | `65536` | No | System limits |
| `vault_nproc_limit` | `4096` | No | — |
| `vault_configure_firewall` | `true` | No | Firewall configuration |
| `vault_firewall_allowed_ips` | `[]` | No | — |
| `vault_selinux_enabled` | `true` | No | SELinux |
| `vault_enable_backup` | `true` | No | Backup configuration |
| `vault_backup_path` | `"/backup/vault"` | No | — |
| `vault_snapshot_interval` | `"1h"` | No | — |
| `vault_air_gapped` | `false` | No | Air-gapped deployment |
| `vault_local_binary_path` | `""` | No | — |
| `vault_http_proxy` | `""` | No | Proxy configuration |
| `vault_https_proxy` | `""` | No | — |
| `vault_no_proxy` | `"localhost,127.0.0.1"` | No | — |
| `vault_health_check_interval` | `30` | No | Health check configuration |
| `vault_health_check_timeout` | `10` | No | — |
| `vault_extra_config` | `{}` | No | Additional configuration |

## Example Playbook

```yaml
---
- name: Vault Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: hashicorp_vault/roles/vault_install
```

## Tags

| Tag | Description |
|-----|-------------|
| `airgap` | Tasks tagged `airgap` |
| `backup` | Tasks tagged `backup` |
| `binary` | Tasks tagged `binary` |
| `capabilities` | Tasks tagged `capabilities` |
| `cleanup` | Tasks tagged `cleanup` |
| `cli` | Tasks tagged `cli` |
| `config` | Tasks tagged `config` |
| `directories` | Tasks tagged `directories` |
| `download` | Tasks tagged `download` |
| `environment` | Tasks tagged `environment` |
| `firewall` | Tasks tagged `firewall` |
| `health` | Tasks tagged `health` |
| `install` | Tasks tagged `install` |
| `license` | Tasks tagged `license` |
| `limits` | Tasks tagged `limits` |
| `logging` | Tasks tagged `logging` |
| `packages` | Tasks tagged `packages` |
| `plugins` | Tasks tagged `plugins` |
| `selinux` | Tasks tagged `selinux` |
| `service` | Tasks tagged `service` |
| `sysctl` | Tasks tagged `sysctl` |
| `syslog` | Tasks tagged `syslog` |
| `systemd` | Tasks tagged `systemd` |
| `user` | Tasks tagged `user` |
| `validate` | Tasks tagged `validate` |
| `vault` | Tasks tagged `vault` |

## License

MIT

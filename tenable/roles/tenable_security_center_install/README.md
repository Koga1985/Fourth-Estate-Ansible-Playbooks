# tenable_security_center_install

Tenable Security Center Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `tenable/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `tsc_version` | `"6.2.0"` | No | Version and Package |
| `tsc_package_ext` | `"{{ 'rpm' if ansible_os_family == 'RedHat' else 'deb' }}"` | No | — |
| `tsc_download_url` | `"https://downloads.tenable.com/SecurityCenter"` | No | — |
| `tsc_download_enabled` | `false` | No | — |
| `tsc_package_path` | `""` | No | — |
| `tsc_checksum` | `""` | No | — |
| `tsc_cleanup_package` | `true` | No | — |
| `tsc_install_dir` | `"/opt/sc"` | No | Installation Directories |
| `tsc_data_dir` | `"/var/sc"` | No | — |
| `tsc_create_data_dir` | `true` | No | — |
| `tsc_license_file` | `""` | No | License Configuration |
| `tsc_license_content` | `""` | No | — |
| `tsc_admin_username` | `"admin"` | No | Admin Account Configuration |
| `tsc_admin_password` | `"{{ vault_tsc_admin_password }}"` | No | — |
| `tsc_admin_email` | `"security@agency.gov"` | No | — |
| `tsc_admin_firstname` | `"Security"` | No | — |
| `tsc_admin_lastname` | `"Administrator"` | No | — |
| `tsc_hostname` | `"{{ ansible_fqdn }}"` | No | Network Configuration |
| `tsc_https_port` | `443` | No | — |
| `tsc_http_port` | `80` | No | — |
| `tsc_ssl_cert` | `""` | No | SSL/TLS Configuration |
| `tsc_ssl_key` | `""` | No | — |
| `tsc_generate_self_signed` | `true` | No | — |
| `tsc_ssl_state` | `"DC"` | No | — |
| `tsc_ssl_city` | `"Washington"` | No | — |
| `tsc_ssl_org` | `"Fourth Estate Agency"` | No | — |
| `tsc_validate_certs` | `true` | No | — |
| `tsc_db_type` | `"postgresql"` | No | Database Configuration |
| `tsc_db_name` | `"tenable_sc"` | No | — |
| `tsc_db_user` | `"tenable"` | No | — |
| `tsc_db_password` | `"{{ vault_tsc_db_password }}"` | No | — |
| `tsc_db_host` | `"localhost"` | No | — |
| `tsc_db_port` | `5432` | No | — |
| `postgresql_config_dir` | `"{{ '/var/lib/pgsql/data' if ansible_os_family == 'RedHat' else '/e...` | No | PostgreSQL Configuration |
| `tsc_pg_shared_buffers` | `"256MB"` | No | — |
| `tsc_pg_effective_cache_size` | `"1GB"` | No | — |
| `tsc_pg_maintenance_work_mem` | `"128MB"` | No | — |
| `mysql_service_name` | `"{{ 'mysqld' if ansible_os_family == 'RedHat' else 'mysql' }}"` | No | MySQL Configuration |
| `mysql_config_file` | `"{{ '/etc/my.cnf' if ansible_os_family == 'RedHat' else '/etc/mysql...` | No | — |
| `tsc_mysql_root_password` | `"{{ vault_tsc_mysql_root_password }}"` | No | — |
| `tsc_mysql_buffer_pool_size` | `"512M"` | No | — |
| `tsc_auto_plugin_update` | `true` | No | Plugin Feed Configuration |
| `tsc_plugin_update_hour` | `"2"` | No | — |
| `tsc_plugin_update_minute` | `"0"` | No | — |
| `tsc_plugin_feed_url` | `"https://plugins.nessus.org"` | No | — |
| `tsc_configure_firewall` | `true` | No | Firewall Configuration |
| `tsc_configure_selinux` | `true` | No | SELinux Configuration |
| `tsc_min_memory_mb` | `8192` | No | System Requirements |
| `tsc_min_disk_gb` | `100` | No | — |
| `tsc_fourth_estate` | `(see defaults/main.yml)` | No | Fourth Estate Specific Settings |
| `tsc_service_enabled` | `true` | No | Service Configuration |
| `tsc_service_state` | `started` | No | — |
| `tsc_log_level` | `"info"` | No | Log Configuration |
| `tsc_log_retention_days` | `90` | No | — |

## Example Playbook

```yaml
---
- name: Tenable Security Center Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: tenable/roles/tenable_security_center_install
```

## License

MIT

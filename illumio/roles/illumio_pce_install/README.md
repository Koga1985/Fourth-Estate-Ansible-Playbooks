# illumio_pce_install

Illumio Pce Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `illumio/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `illumio_pce_version` | `"22.5.0"` | No | PCE Version and Installation |
| `illumio_pce_package_file` | `"illumio-pce-{{ illumio_pce_version }}.tar.gz"` | No | — |
| `illumio_pce_package_url` | `"https://repo.illum.io/downloads/{{ illumio_pce_package_file }}"` | No | — |
| `illumio_pce_package_local_path` | `""` | No | — |
| `illumio_pce_online_install` | `true` | No | — |
| `illumio_pce_cleanup_install_files` | `true` | No | — |
| `illumio_pce_min_cpu` | `8` | No | System Requirements |
| `illumio_pce_min_memory_mb` | `16384` | No | — |
| `illumio_pce_min_disk_gb` | `500` | No | — |
| `illumio_pce_user` | `illumio-pce` | No | System Configuration |
| `illumio_pce_group` | `illumio-pce` | No | — |
| `illumio_pce_data_dir` | `/var/lib/illumio-pce` | No | — |
| `illumio_pce_config_dir` | `/etc/illumio-pce` | No | — |
| `illumio_pce_cert_dir` | `/etc/illumio-pce/certs` | No | — |
| `illumio_pce_fqdn` | `"{{ ansible_fqdn }}"` | No | Network Configuration |
| `illumio_pce_port` | `8443` | No | — |
| `illumio_pce_required_ports` | `(see defaults/main.yml)` | No | — |
| `illumio_pce_use_iptables` | `false` | No | Firewall Configuration |
| `illumio_pce_firewall_rules` | `[]` | No | — |
| `illumio_pce_install_database` | `true` | No | Database Configuration |
| `illumio_pce_database_host` | `localhost` | No | — |
| `illumio_pce_database_port` | `5432` | No | — |
| `illumio_pce_database_name` | `illumio_pce` | No | — |
| `illumio_pce_database_user` | `illumio_pce` | No | — |
| `illumio_pce_database_password` | `"{{ vault_illumio_pce_database_password \| default('ChangeMe123!') }}"` | **Yes** | — |
| `illumio_pce_postgresql_version` | `13` | No | — |
| `illumio_pce_postgresql_repo_url` | `"https://download.postgresql.org/pub/repos/yum/reporpms/EL-{{ ansib...` | No | — |
| `illumio_pce_postgresql_data_dir` | `"/var/lib/pgsql/{{ illumio_pce_postgresql_version }}/data"` | No | — |
| `illumio_pce_enable_db_backup` | `true` | No | Database Backup |
| `illumio_pce_database_backup_dir` | `/var/backups/illumio-pce` | No | — |
| `illumio_pce_backup_hour` | `2` | No | — |
| `illumio_pce_backup_retention_days` | `30` | No | — |
| `illumio_pce_use_pgbouncer` | `false` | No | — |
| `illumio_pce_cluster_mode` | `false` | No | Cluster Configuration (High Availability) |
| `illumio_pce_cluster_nodes` | `[]` | No | — |
| `illumio_pce_cluster_vip` | `""` | No | — |
| `illumio_pce_ssl_cert_file` | `""` | No | SSL/TLS Configuration |
| `illumio_pce_ssl_key_file` | `""` | No | — |
| `illumio_pce_ssl_ca_file` | `""` | No | — |
| `illumio_pce_generate_selfsigned_cert` | `true` | No | — |
| `illumio_pce_cert_country` | `"US"` | No | — |
| `illumio_pce_cert_state` | `"DC"` | No | — |
| `illumio_pce_cert_locality` | `"Washington"` | No | — |
| `illumio_pce_use_loadbalancer` | `false` | No | Load Balancer |
| `illumio_pce_loadbalancer_vip` | `""` | No | — |
| `illumio_pce_superuser` | `"admin@illumio.com"` | No | PCE Admin Configuration |
| `illumio_pce_superuser_password` | `"{{ vault_illumio_pce_superuser_password \| default('ChangeMe123!') }}"` | **Yes** | — |
| `illumio_pce_admin_user` | `"pce_admin"` | No | — |
| `illumio_pce_admin_password` | `"{{ vault_illumio_pce_admin_password \| default('ChangeMe123!') }}"` | **Yes** | — |
| `illumio_pce_admin_fullname` | `"PCE Administrator"` | No | — |
| `illumio_pce_admin_email` | `""` | No | — |
| `illumio_pce_generate_api_key` | `true` | No | — |
| `illumio_pce_org_name` | `"Fourth Estate"` | No | Organization Configuration |
| `illumio_pce_org_description` | `"Fourth Estate Zero Trust Microsegmentation"` | No | — |
| `illumio_pce_license_file` | `""` | No | License Configuration |
| `illumio_pce_selinux_enforcing` | `false` | No | SELinux Configuration |
| `illumio_pce_repo_url` | `"https://repo.illum.io"` | No | Repository Configuration |
| `illumio_pce_system_packages` | `(see defaults/main.yml)` | No | System Packages |

## Example Playbook

```yaml
---
- name: Illumio Pce Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: illumio/roles/illumio_pce_install
```

## Tags

| Tag | Description |
|-----|-------------|
| `certificates` | Tasks tagged `certificates` |
| `cluster` | Tasks tagged `cluster` |
| `database` | Tasks tagged `database` |
| `firewall` | Tasks tagged `firewall` |
| `illumio` | Tasks tagged `illumio` |
| `initialize` | Tasks tagged `initialize` |
| `install` | Tasks tagged `install` |
| `license` | Tasks tagged `license` |
| `loadbalancer` | Tasks tagged `loadbalancer` |
| `pce` | Tasks tagged `pce` |
| `prerequisites` | Tasks tagged `prerequisites` |
| `selinux` | Tasks tagged `selinux` |
| `system` | Tasks tagged `system` |
| `verify` | Tasks tagged `verify` |

## License

MIT

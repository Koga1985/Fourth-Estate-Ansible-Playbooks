# sl1_platform_install

Production-ready Ansible role for installing ScienceLogic SL1 Platform components for Fourth Estate agencies.

## Requirements

- RHEL/CentOS 7+
- Minimum 8 CPUs, 16GB RAM, 100GB disk
- SL1 installer package
- Valid SL1 license

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sl1_install_mode` | `"all_in_one"` | No | Installation Mode all_in_one, database_server, message_collector, data_collector |
| `sl1_package_path` | `"/tmp/sl1_installer.bin"` | No | SL1 Software Package |
| `sl1_version` | `"12.2.0"` | No | — |
| `sl1_license_file` | `"/tmp/sl1_license.lic"` | No | — |
| `sl1_db_server` | `(see defaults/main.yml)` | No | Database Server Configuration |
| `sl1_aio` | `(see defaults/main.yml)` | No | All-In-One Appliance Configuration |
| `sl1_message_collectors` | `(see defaults/main.yml)` | No | Message Collector Configuration |
| `sl1_data_collectors` | `(see defaults/main.yml)` | No | Data Collector Configuration |
| `sl1_network` | `(see defaults/main.yml)` | No | Network Configuration |
| `sl1_ssl` | `(see defaults/main.yml)` | No | SSL/TLS Configuration |
| `sl1_ha` | `(see defaults/main.yml)` | No | High Availability Configuration |
| `sl1_db_cluster` | `(see defaults/main.yml)` | No | Database Cluster Configuration |
| `sl1_setup_wizard` | `(see defaults/main.yml)` | No | Initial Setup Wizard Configuration |
| `sl1_license` | `(see defaults/main.yml)` | No | License Configuration |
| `sl1_system` | `(see defaults/main.yml)` | No | System Configuration |
| `sl1_install_options` | `(see defaults/main.yml)` | No | Installation Options |
| `sl1_post_install` | `(see defaults/main.yml)` | No | Post-Installation Tasks |
| `sl1_services` | `(see defaults/main.yml)` | No | Service Configuration |
| `fourth_estate` | `(see defaults/main.yml)` | No | Fourth Estate Specific Configuration |
| `artifacts_dir` | `"/tmp/sl1-install-artifacts"` | No | Artifacts and Logging |
| `log_level` | `"info"` | No | debug, info, warn, error |
| `dry_run` | `false` | No | — |

## Example Playbook

```yaml
- hosts: sl1_servers
  roles:
    - role: sl1_platform_install
      sl1_install_mode: "all_in_one"
      sl1_aio:
        hostname: "sl1.example.com"
        ip_address: "10.0.1.20"
```

## Features

- SL1 Database Server installation
- SL1 All-In-One Appliance installation
- Message Collector installation
- Data Collector installation
- High availability configuration
- Database cluster setup
- SSL/TLS certificate installation
- License activation
- Initial setup wizard
- Post-installation configuration

## Dependencies

None

## Author

Fourth Estate Automation Team

## License

MIT

# sl1_platform_install

Production-ready Ansible role for installing ScienceLogic SL1 Platform components for Fourth Estate agencies.

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

## Requirements

- RHEL/CentOS 7+
- Minimum 8 CPUs, 16GB RAM, 100GB disk
- SL1 installer package
- Valid SL1 license

## Role Variables

See `defaults/main.yml` for all configurable variables.

## Dependencies

None

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

## License

MIT

## Author

Fourth Estate Automation Team

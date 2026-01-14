# ucs_prod_networking

Cisco UCS production networking configuration role.

## Description

Configures VLANs, VSANs, QoS policies, and network control policies for Cisco UCS production deployments.

## Features

- VLAN configuration for network segmentation
- VSAN configuration for SAN connectivity
- QoS policy management
- Network control policies (CDP/LLDP)
- Multicast policy configuration
- Uplink port channel configuration

## Requirements

- Ansible >= 2.9
- Cisco UCS Ansible collection
- Administrative access to UCS Manager

## Variables

See `defaults/main.yml` for configuration options.

## Example Playbook

```yaml
- name: Configure UCS Networking
  hosts: localhost
  roles:
    - role: ucs_prod_networking
      vars:
        apply_changes: true
```

## License

MIT

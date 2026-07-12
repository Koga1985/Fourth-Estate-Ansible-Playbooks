# rhel-firewall-selinux

Configures firewalld zones, allowed services and ports, and SELinux mode/policy on RHEL servers. Implements STIG V-204401 (SELinux enforcing) and V-204500 through V-204510 (firewall controls).

## Requirements

- Ansible 2.15+
- `ansible.posix` collection

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `rhel_selinux_state` | `enforcing` | No | SELinux state: enforcing, permissive, disabled STIG V-204401 |
| `rhel_selinux_policy` | `targeted` | No | SELinux policy type: targeted, mls |
| `rhel_selinux_booleans` | `{}` | No | SELinux booleans to configure |
| `rhel_install_selinux_tools` | `true` | No | Install SELinux troubleshooting tools |
| `rhel_firewall_enabled` | `true` | No | Enable firewalld STIG V-204500 |
| `rhel_firewall_default_zone` | `public` | No | Default firewall zone |
| `rhel_firewall_services` | `(see defaults/main.yml)` | No | Firewall services to allow |
| `rhel_firewall_ports` | `[]` | No | Firewall ports to open |
| `rhel_firewall_rich_rules` | `[]` | No | Firewall rich rules |
| `rhel_firewall_zones` | `[]` | No | Firewall zones configuration |
| `rhel_firewall_remove_services` | `[]` | No | Remove services from firewall |
| `rhel_firewall_panic` | `false` | No | Panic mode (block all traffic) |
| `rhel_firewall_direct_rules` | `[]` | No | Direct rules (iptables) |
| `rhel_firewall_block_icmp` | `[]` | No | ICMP block |
| `rhel_firewall_masquerade` | `false` | No | Masquerading |
| `rhel_firewall_port_forward` | `[]` | No | Port forwarding |

## Example Playbook

```yaml
---
- name: Configure RHEL Firewall and SELinux
  hosts: rhel_servers
  become: true
  roles:
    - role: rhel/roles/rhel-firewall-selinux
      vars:
        rhel_selinux_state: enforcing
        rhel_firewall_services:
          - ssh
          - https
        rhel_firewall_ports:
          - "8443/tcp"
```

## Tags

| Tag | Description |
|-----|-------------|
| `firewall` | Tasks tagged `firewall` |
| `packages` | Tasks tagged `packages` |
| `selinux` | Tasks tagged `selinux` |
| `services` | Tasks tagged `services` |
| `validation` | Tasks tagged `validation` |

## License

MIT

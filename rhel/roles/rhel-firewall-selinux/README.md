# rhel-firewall-selinux

Configures firewalld zones, allowed services and ports, and SELinux mode/policy on RHEL servers. Implements STIG V-204401 (SELinux enforcing) and V-204500 through V-204510 (firewall controls).

## Requirements

- Ansible 2.15+
- `ansible.posix` collection

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `rhel_selinux_state` | `"enforcing"` | No | SELinux state: `enforcing`, `permissive`, `disabled` |
| `rhel_selinux_policy` | `"targeted"` | No | SELinux policy type |
| `rhel_selinux_booleans` | `{}` | No | SELinux booleans to set (key: value pairs) |
| `rhel_firewall_enabled` | `true` | No | Enable and start firewalld |
| `rhel_firewall_default_zone` | `"public"` | No | Default firewalld zone |
| `rhel_firewall_services` | `["ssh"]` | No | Services to allow in the default zone |
| `rhel_firewall_ports` | `[]` | No | Ports to allow (e.g. `["8080/tcp"]`) |

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

## License

MIT

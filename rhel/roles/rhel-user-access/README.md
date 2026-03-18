# rhel-user-access

Manages local users, groups, sudo access, and SSH authorized keys on RHEL servers. Implements STIG account management controls including inactive account locking and unauthorized user removal.

## Requirements

- Ansible 2.15+

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `rhel_users` | `[]` | No | List of users to create/manage. Each entry: `name`, `groups`, `ssh_key`, `password`, `state` |
| `rhel_groups` | `[]` | No | List of groups to create. Each entry: `name`, optional `gid` |
| `rhel_sudo_groups` | `["wheel"]` | No | Groups that receive sudo access |
| `rhel_remove_users` | `[]` | No | List of usernames to remove |
| `rhel_lock_inactive` | `true` | No | Lock accounts inactive for `rhel_inactive_days` days |
| `rhel_inactive_days` | `35` | No | Days before locking inactive accounts (STIG V-204425) |

## Example Playbook

```yaml
---
- name: Manage RHEL Users
  hosts: rhel_servers
  become: true
  roles:
    - role: rhel/roles/rhel-user-access
      vars:
        rhel_users:
          - name: ansible_svc
            groups: wheel
            ssh_key: "ssh-rsa AAAA... ansible@control"
            state: present
        rhel_sudo_groups:
          - wheel
        rhel_lock_inactive: true
        rhel_inactive_days: 35
```

## License

MIT

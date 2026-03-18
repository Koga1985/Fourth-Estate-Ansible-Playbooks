# rhel-patch-management

Manages patching for RHEL servers: applies security or all updates via yum/dnf, handles optional automatic reboots, and validates system state post-patch. Implements STIG V-204393 (system currency).

## Requirements

- Ansible 2.15+
- `community.general` collection
- Red Hat subscription (RHSM) active on target hosts, or a configured local/satellite repo

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `rhel_security_updates_only` | `false` | No | Install only security-classified updates |
| `rhel_auto_reboot` | `false` | No | Reboot automatically if kernel was updated |
| `rhel_reboot_delay` | `300` | No | Seconds to wait before rebooting |
| `rhel_update_kernel` | `true` | No | Include kernel packages in updates |
| `rhel_exclude_packages` | `[]` | No | Package names to exclude from updates |
| `rhel_check_only` | `false` | No | List available updates without installing (dry-run) |
| `rhel_clean_cache` | `true` | No | Run `yum clean all` after patching |

## Example Playbook

```yaml
---
# Dry-run: check what would update
- name: Check RHEL Updates
  hosts: rhel_servers
  become: true
  roles:
    - role: rhel/roles/rhel-patch-management
      vars:
        rhel_check_only: true

# Apply security updates with auto-reboot
- name: Apply RHEL Security Patches
  hosts: rhel_servers
  become: true
  roles:
    - role: rhel/roles/rhel-patch-management
      vars:
        rhel_security_updates_only: true
        rhel_auto_reboot: true
```

## License

MIT

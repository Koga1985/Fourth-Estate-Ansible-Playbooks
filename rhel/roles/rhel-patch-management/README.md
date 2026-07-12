# rhel-patch-management

Manages patching for RHEL servers: applies security or all updates via yum/dnf, handles optional automatic reboots, and validates system state post-patch. Implements STIG V-204393 (system currency).

## Requirements

- Ansible 2.15+
- `community.general` collection
- Red Hat subscription (RHSM) active on target hosts, or a configured local/satellite repo

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `rhel_auto_reboot` | `false` | No | Automatic reboot after updates |
| `rhel_reboot_delay` | `300` | No | Reboot delay in seconds |
| `rhel_security_updates_only` | `false` | No | Install security updates only |
| `rhel_exclude_packages` | `[]` | No | Exclude packages from updates |
| `rhel_update_kernel` | `true` | No | Update kernel |
| `rhel_clean_cache` | `true` | No | Clean package cache after updates |
| `rhel_check_only` | `false` | No | Check for available updates without installing |
| `rhel_download_only` | `false` | No | Download updates without installing |
| `rhel_reboot_timeout` | `600` | No | Reboot timeout in seconds |
| `rhel_post_reboot_delay` | `30` | No | Post-reboot delay in seconds |
| `rhel_update_all_packages` | `true` | No | Update all packages |
| `rhel_packages_to_update` | `[]` | No | Specific packages to update (empty means all) |
| `rhel_enable_repos` | `[]` | No | Enable repository during update |
| `rhel_disable_repos` | `[]` | No | Disable repository during update |
| `rhel_subscription_auto_attach` | `false` | No | Subscription manager auto-attach |
| `rhel_update_cache` | `true` | No | Update metadata cache before checking |
| `rhel_generate_update_report` | `true` | No | Generate update report |
| `rhel_update_report_path` | `/tmp/rhel-update-report.txt` | No | Update report path |
| `rhel_create_snapshot` | `false` | No | Pre-update snapshot (requires LVM) |
| `rhel_snapshot_size` | `5G` | No | Snapshot size |

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

## Tags

| Tag | Description |
|-----|-------------|
| `cache` | Tasks tagged `cache` |
| `cleanup` | Tasks tagged `cleanup` |
| `kernel` | Tasks tagged `kernel` |
| `report` | Tasks tagged `report` |
| `security-updates` | Tasks tagged `security-updates` |
| `updates` | Tasks tagged `updates` |
| `validation` | Tasks tagged `validation` |

## License

MIT

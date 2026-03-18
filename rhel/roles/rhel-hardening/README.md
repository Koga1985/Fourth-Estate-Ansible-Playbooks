# rhel-hardening

Applies DoD STIG (RHEL 8 V1R14 / RHEL 9 V1R3) and NIST 800-53 Rev 5 system hardening to Red Hat Enterprise Linux servers. Covers FIPS mode, SSH configuration, kernel parameters, password policy, file permissions, and login banners.

## Requirements

- Ansible 2.15+
- `ansible.posix` collection
- Hosts in the `rhel_servers` inventory group
- `become: true` (sudo access required)

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `rhel_stig_level` | `"high"` | No | Compliance level: `low`, `medium`, `high`, `critical` |
| `rhel_apply_nist_controls` | `true` | No | Apply NIST 800-53 controls |
| `rhel_apply_cis_benchmark` | `true` | No | Apply CIS Benchmark controls |
| `rhel_enable_fips` | `false` | No | Enable FIPS 140-2 mode (**requires reboot**) |
| `rhel_ssh_permit_root_login` | `false` | No | Allow root SSH login (STIG V-230293) |
| `rhel_ssh_password_authentication` | `false` | No | Allow password auth via SSH |
| `rhel_ssh_port` | `22` | No | SSH listening port |
| `rhel_selinux_state` | `"enforcing"` | No | SELinux mode (STIG V-204401) |

> **Note:** Setting `rhel_enable_fips: true` requires a reboot to take effect. The role will reboot the host if `rhel_auto_reboot: true` is set.

## Example Playbook

```yaml
---
- name: RHEL STIG Hardening
  hosts: rhel_servers
  become: true
  roles:
    - role: rhel/roles/rhel-hardening
      vars:
        rhel_stig_level: high
        rhel_enable_fips: false      # set true and reboot for full STIG compliance
        rhel_ssh_permit_root_login: false
```

## Tags

| Tag | Description |
|-----|-------------|
| `hardening` | All hardening tasks |
| `ssh` | SSH configuration (V-230293 through V-230300) |
| `fips` | FIPS 140-2 configuration |
| `kernel` | Kernel parameter hardening |
| `banner` | Login banner configuration |

## License

MIT

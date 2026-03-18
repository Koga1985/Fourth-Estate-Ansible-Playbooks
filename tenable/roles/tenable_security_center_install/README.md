# tenable_security_center_install

Tenable Security Center Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `tenable/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `tsc_version` | `"6.2.0"` |  |
| `tsc_package_ext` | `"{{ 'rpm' if ansible_os_family == 'RedHat' else...` |  |
| `tsc_download_url` | `"https://downloads.tenable.com/SecurityCenter"` |  |
| `tsc_download_enabled` | `false` |  |
| `tsc_package_path` | `""` |  |
| `tsc_checksum` | `""` |  |
| `tsc_cleanup_package` | `true` |  |
| `tsc_install_dir` | `"/opt/sc"` |  |
| `tsc_data_dir` | `"/var/sc"` |  |
| `tsc_create_data_dir` | `true` |  |
| `tsc_license_file` | `""` |  |
| `tsc_license_content` | `""` |  |
| `tsc_admin_username` | `"admin"` |  |
| `tsc_admin_password` | `"{{ vault_tsc_admin_password }}"` |  |
| `tsc_admin_email` | `"security@agency.gov"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Tenable Security Center Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: tenable/roles/tenable_security_center_install
```

## License

MIT

# illumio_pce_install

Illumio Pce Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `illumio/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `illumio_pce_version` | `"22.5.0"` |  |
| `illumio_pce_package_file` | `"illumio-pce-{{ illumio_pce_version }}.tar.gz"` |  |
| `illumio_pce_package_url` | `"https://repo.illum.io/downloads/{{ illumio_pce...` |  |
| `illumio_pce_package_local_path` | `""` |  |
| `illumio_pce_online_install` | `true` |  |
| `illumio_pce_cleanup_install_files` | `true` |  |
| `illumio_pce_min_cpu` | `8` |  |
| `illumio_pce_min_memory_mb` | `16384` |  |
| `illumio_pce_min_disk_gb` | `500` |  |
| `illumio_pce_user` | `illumio-pce` |  |
| `illumio_pce_group` | `illumio-pce` |  |
| `illumio_pce_data_dir` | `/var/lib/illumio-pce` |  |
| `illumio_pce_config_dir` | `/etc/illumio-pce` |  |
| `illumio_pce_cert_dir` | `/etc/illumio-pce/certs` |  |
| `illumio_pce_fqdn` | `"{{ ansible_fqdn }}"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Illumio Pce Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: illumio/roles/illumio_pce_install
```

## License

MIT

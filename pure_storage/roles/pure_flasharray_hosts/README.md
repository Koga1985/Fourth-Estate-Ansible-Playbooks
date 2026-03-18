# pure_flasharray_hosts

Pure Flasharray Hosts role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` |  |
| `flasharray_default_linux_personality` | `"linux"` |  |
| `flasharray_default_esxi_personality` | `"esxi"` |  |
| `flasharray_default_windows_personality` | `"windows"` |  |
| `flasharray_default_aix_personality` | `"aix"` |  |
| `flasharray_default_solaris_personality` | `"solaris"` |  |
| `flasharray_multipath_enabled` | `true` |  |
| `flasharray_recommended_paths_per_host` | `4` | 2 per controller minimum |
| `flasharray_iscsi_mtu` | `9000` | Jumbo frames recommended |
| `flasharray_iscsi_tcp_window` | `131072` |  |
| `flasharray_iscsi_use_chap` | `false` | Set true if CHAP required |
| `flasharray_fc_queue_depth` | `128` |  |
| `flasharray_fc_use_alua` | `true` |  |
| `flasharray_nvme_queue_depth` | `1024` |  |
| `flasharray_nvme_io_queue_size` | `1024` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Pure Flasharray Hosts
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_hosts
```

## License

MIT

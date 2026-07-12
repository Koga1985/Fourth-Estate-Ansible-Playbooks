# pure_flasharray_hosts

Pure Flasharray Hosts role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` | No | Array connection |
| `flasharray_default_linux_personality` | `"linux"` | No | Host personality defaults |
| `flasharray_default_esxi_personality` | `"esxi"` | No | — |
| `flasharray_default_windows_personality` | `"windows"` | No | — |
| `flasharray_default_aix_personality` | `"aix"` | No | — |
| `flasharray_default_solaris_personality` | `"solaris"` | No | — |
| `flasharray_multipath_enabled` | `true` | No | Multipath configuration recommendations |
| `flasharray_recommended_paths_per_host` | `4` | No | 2 per controller minimum |
| `flasharray_iscsi_mtu` | `9000` | No | iSCSI configuration Jumbo frames recommended |
| `flasharray_iscsi_tcp_window` | `131072` | No | — |
| `flasharray_iscsi_use_chap` | `false` | No | Set true if CHAP required |
| `flasharray_fc_queue_depth` | `128` | No | Fibre Channel configuration |
| `flasharray_fc_use_alua` | `true` | No | — |
| `flasharray_nvme_queue_depth` | `1024` | No | NVMe-oF configuration |
| `flasharray_nvme_io_queue_size` | `1024` | No | — |
| `flasharray_editorial_hostgroup` | `"editorial-systems"` | No | Fourth Estate specific host configurations |
| `flasharray_publishing_hostgroup` | `"publishing-platforms"` | No | — |
| `flasharray_cms_hostgroup` | `"cms-cluster"` | No | — |
| `flasharray_archive_hostgroup` | `"archive-systems"` | No | — |
| `flasharray_lun_assignment_strategy` | `"automatic"` | No | LUN assignment strategy or "manual" |
| `flasharray_lun_start_number` | `0` | No | — |
| `flasharray_host_naming_pattern` | `"{{ hostname }}.{{ domain_name }}"` | No | Host naming convention |
| `flasharray_monitor_host_connections` | `true` | No | Connection monitoring |
| `flasharray_connection_alert_threshold` | `2` | No | Alert if less than 2 paths |
| `flasharray_enable_queue_depth_tuning` | `true` | No | Performance tuning |
| `flasharray_enable_io_scheduler_tuning` | `true` | No | — |

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

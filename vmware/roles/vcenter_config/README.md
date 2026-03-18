# vcenter_config

Vcenter Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vmware/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vcenter_hostname` | `"vcsa.example.mil"` |  |
| `vcenter_username` | `"administrator@vsphere.local"` |  |
| `vcenter_password` | `""` |  |
| `vcenter_validate_certs` | `false` |  |
| `vcenter_server_name` | `"Production vCenter"` |  |
| `vcenter_instance_id` | `""` |  |
| `vcenter_db_max_connections` | `100` |  |
| `vcenter_task_retention_days` | `30` |  |
| `vcenter_event_retention_days` | `30` |  |
| `vcenter_timeout_normal` | `30` |  |
| `vcenter_timeout_long` | `120` |  |
| `vcenter_log_level` | `"info"` | verbose|info|warning|error |
| `vcenter_smtp_server` | `""` |  |
| `vcenter_smtp_port` | `25` |  |
| `vcenter_smtp_sender` | `"vcenter@example.mil"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `community.vmware`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Vcenter Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: vmware/roles/vcenter_config
```

## License

MIT

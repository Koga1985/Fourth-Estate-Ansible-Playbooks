# arista_cvp_inventory_model

Manages the full CloudVision Portal (CVP) inventory model for Arista networks: container topology, configlets, device registration, configlet-to-device assignment, change-control creation, and compliance validation. The role is the authoritative source of truth for how devices are organized and configured within CVP, and it exposes a dry-run gate so that changes are staged before any active policy is modified.

## Requirements

- Ansible 2.12 or later
- `arista.cvp` collection (`ansible-galaxy collection install arista.cvp`)
- Network connectivity to the CloudVision Portal instance (`cvp_host`)
- CVP user with sufficient privileges to create containers, upload configlets, register devices, and manage change controls
- All tasks delegate to `localhost`; the play does not require direct SSH/eAPI access to the EOS devices themselves

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `arista_apply_changes` | `false` | No | Control whether changes are applied or just planned |
| `arista_artifacts_dir` | `"/tmp/arista-artifacts"` | No | Artifacts directory |
| `cvp_host` | `"{{ lookup('env', 'CVP_HOST') \| default('cvp.example.mil') }}"` | No | CVP connection parameters (should be overridden in inventory/vault) |
| `cvp_username` | `"{{ lookup('env', 'CVP_USERNAME') \| default('cvpadmin') }}"` | No | — |
| `cvp_password` | `"{{ lookup('env', 'CVP_PASSWORD') \| default('') }}"` | No | — |
| `cvp_protocol` | `"https"` | No | — |
| `cvp_port` | `443` | No | — |
| `cvp_validate_certs` | `true` | No | — |
| `cvp_apply_mode` | `"strict"` | No | CVP operation settings Options: strict, loose |
| `cvp_search_key` | `"hostname"` | No | Options: hostname, fqdn, serialNumber |
| `cvp_containers` | `(see defaults/main.yml)` | No | CVP container topology Containers organize devices in CVP hierarchically |
| `cvp_configlets` | `(see defaults/main.yml)` | No | CVP configlets Configlets are configuration snippets applied to devices |
| `cvp_devices` | `[]` | No | CVP device inventory Maps physical devices to containers and configlets |
| `cvp_device_configlets` | `[]` | No | CVP device configlet mappings |
| `cvp_change_control` | `(see defaults/main.yml)` | No | CVP change control settings |
| `cvp_collect_facts` | `true` | No | CVP facts collection |
| `cvp_facts_filter` | `".*"` | No | Regex filter for facts collection |
| `cvp_validate_compliance` | `true` | No | CVP compliance validation |
| `cvp_validation_mode` | `"stop_on_error"` | No | Options: stop_on_error, stop_on_warning, valid |
| `cvp_validation_type` | `"valid"` | No | Options: valid, time, stop_on_error, stop_on_warning |
| `cvp_inventory` | `(see defaults/main.yml)` | No | CVP inventory structure for fabric deployment |
| `cvp_task_ids` | `[]` | No | CVP task management List of task IDs for change control |
| `cvp_task_timeout` | `300` | No | Timeout in seconds for task execution |
| `cvp_task_retries` | `3` | No | Number of retries for failed tasks |
| `cvp_backup_enabled` | `true` | No | CVP backup settings |
| `cvp_backup_location` | `"{{ arista_artifacts_dir }}/cvp_backups"` | No | — |
| `cvp_backup_retention_days` | `30` | No | — |

## Example Playbook

```yaml
- name: Synchronise CVP inventory model
  hosts: localhost
  gather_facts: false
  roles:
    - role: arista_cvp_inventory_model
      vars:
        arista_apply_changes: true
        cvp_host: cvp.dc1.example.mil
        cvp_username: "{{ vault_cvp_username }}"
        cvp_password: "{{ vault_cvp_password }}"
        cvp_devices:
          - fqdn: "spine1.dc1.example.mil"
            parentContainerName: "DC1_Spines"
            configlets:
              - "GLOBAL_BASELINE"
              - "SECURITY_BASELINE"
              - "AAA_CONFIG"
            systemMacAddress: "00:1c:73:00:00:01"
          - fqdn: "leaf1.dc1.example.mil"
            parentContainerName: "DC1_Leafs"
            configlets:
              - "GLOBAL_BASELINE"
              - "SECURITY_BASELINE"
```

## Notes and Dependencies

- `arista_apply_changes` defaults to `false`. A JSON inventory plan (`cvp_inventory_plan.json`) is always written to `arista_artifacts_dir`; CVP is not modified until the gate is explicitly opened.
- All tasks delegate to `localhost` and connect to CVP over HTTPS. No direct connection to EOS devices is required.
- CVP credentials (`cvp_username`, `cvp_password`) must be provided at runtime and should never be stored in plaintext. Use Ansible Vault or environment variables (`CVP_HOST`, `CVP_USERNAME`, `CVP_PASSWORD`).
- `cvp_change_control.auto_execute: false` (default) means that generated change controls must be reviewed and approved manually in the CVP UI before they execute against devices.
- An HTML deployment report is rendered from `cvp_deployment_report.j2`; this template must be present in the role's `templates/` directory.
- The role depends on `arista.cvp` collection modules: `cv_container_v3`, `cv_configlet_v3`, `cv_device_v3`, `cv_change_control_v3`, `cv_facts_v3`, and `cv_validate_v3`.

## License

MIT

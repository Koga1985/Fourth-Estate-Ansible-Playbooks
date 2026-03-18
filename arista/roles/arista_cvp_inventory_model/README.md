# arista_cvp_inventory_model

Manages the full CloudVision Portal (CVP) inventory model for Arista networks: container topology, configlets, device registration, configlet-to-device assignment, change-control creation, and compliance validation. The role is the authoritative source of truth for how devices are organized and configured within CVP, and it exposes a dry-run gate so that changes are staged before any active policy is modified.

## Requirements

- Ansible 2.12 or later
- `arista.cvp` collection (`ansible-galaxy collection install arista.cvp`)
- Network connectivity to the CloudVision Portal instance (`cvp_host`)
- CVP user with sufficient privileges to create containers, upload configlets, register devices, and manage change controls
- All tasks delegate to `localhost`; the play does not require direct SSH/eAPI access to the EOS devices themselves

## Role Variables

All variables are defined in `defaults/main.yml`.

| Variable | Default | Required | Description |
|---|---|---|
| `arista_apply_changes` | `false` | No | Safety gate. Set to `true` to push configuration to CVP; otherwise only a plan artifact is written. |
| `arista_artifacts_dir` | `/tmp/arista-artifacts` | No | Directory on the Ansible controller where plan files and CVP facts are written. |
| `cvp_host` | `$CVP_HOST` env / `cvp.example.mil` | No | Hostname or IP of the CVP server. Prefer the environment variable or Vault. |
| `cvp_username` | `$CVP_USERNAME` env / `cvpadmin` | No | CVP API username. |
| `cvp_password` | `$CVP_PASSWORD` env | No | CVP API password. Should be stored in Ansible Vault. |
| `cvp_protocol` | `https` | No | Protocol used to connect to CVP. |
| `cvp_port` | `443` | No | TCP port for CVP API. |
| `cvp_validate_certs` | `true` | No | Verify TLS certificates when connecting to CVP. |
| `cvp_apply_mode` | `strict` | No | Container/device apply mode. `strict` removes objects not in the desired state; `loose` only adds. |
| `cvp_search_key` | `hostname` | No | Key used to search for devices in CVP. Valid values: `hostname`, `fqdn`, `serialNumber`. |
| `cvp_containers` | See defaults | No | List of container definitions (`name`, `parent`) representing the device hierarchy. Defaults to a Fourth Estate / DC1 / DC2 topology. |
| `cvp_configlets` | See defaults | No | List of configlets (`name`, `content`) to upload. Defaults include `GLOBAL_BASELINE`, `SECURITY_BASELINE`, `AAA_CONFIG`, and `SYSLOG_CONFIG`. |
| `cvp_devices` | `[]` | No | List of device entries mapping FQDNs to parent containers and configlets. Should be defined in `host_vars` or `group_vars`. |
| `cvp_device_configlets` | `[]` | No | Per-device configlet assignments (`device`, `configlets`). |
| `cvp_change_control.enabled` | `true` | No | Creates a CVP change control for pending tasks. |
| `cvp_change_control.auto_execute` | `false` | No | Automatically approves and executes the change control. Leave `false` for manual review. |
| `cvp_collect_facts` | `true` | No | Collects CVP facts (devices, containers, configlets, tasks) and saves them to `arista_artifacts_dir`. |
| `cvp_validate_compliance` | `true` | No | Runs CVP compliance validation after applying changes. |
| `cvp_task_timeout` | `300` | No | Timeout in seconds to wait for CVP tasks to complete. |
| `cvp_backup_retention_days` | `30` | No | Retention period for CVP backup artifacts. |

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

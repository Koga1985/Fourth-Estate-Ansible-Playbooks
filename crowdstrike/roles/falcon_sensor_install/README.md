# falcon_sensor_install

Installs, configures, and verifies the CrowdStrike Falcon sensor on Linux and Windows endpoints with DoD STIG compliance. Supports API-based download, local installer, and air-gapped deployments. Also supports Kubernetes container sensor deployment.

## Requirements

- Ansible 2.15+
- `crowdstrike.falcon` collection: `ansible-galaxy collection install crowdstrike.falcon`
- `ansible.posix` collection (Linux)
- `ansible.windows` collection (Windows)
- Hosts must reach `api.crowdstrike.com:443` (or configured proxy) for API install method

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `falcon_cid` | `"{{ vault_falcon_cid }}"` | No | Falcon Configuration REQUIRED — Customer ID from Falcon console |
| `falcon_installation_token` | `"{{ vault_falcon_installation_token \| default('') }}"` | No | Optional provisioning token |
| `falcon_cloud` | `"us-1"` | No | Options: us-1, us-2, eu-1, us-gov-1 |
| `falcon_sensor_version` | `"latest"` | No | Sensor Version |
| `falcon_sensor_version_decrement` | `"0"` | No | N-x versioning for stability |
| `falcon_install_method` | `"api"` | No | Installation Method Options: api, local, repo |
| `falcon_sensor_download_path` | `"/tmp"` | No | — |
| `falcon_local_installer_path` | `""` | No | — |
| `falcon_api_client_id` | `"{{ vault_falcon_api_client_id }}"` | No | API Configuration (store credentials in vault.yml) REQUIRED for api install method |
| `falcon_api_client_secret` | `"{{ vault_falcon_api_client_secret }}"` | No | REQUIRED for api install method |
| `falcon_api_base_url` | `"https://api.crowdstrike.com"` | No | — |
| `falcon_api_timeout` | `300` | No | — |
| `falcon_sensor_backend` | `"auto"` | No | Sensor Configuration Options: auto, kernel, bpf |
| `falcon_provisioning_wait` | `true` | No | — |
| `falcon_provisioning_timeout` | `300` | No | — |
| `falcon_sensor_tags` | `"Fourth-Estate,Managed-by-Ansible"` | No | — |
| `falcon_sensor_apd` | `false` | No | Application Control/Protocol Detection |
| `falcon_sensor_aph` | `false` | No | Application Protocol Handling |
| `falcon_sensor_trace` | `"none"` | No | Trace level: none, err, warn, info, debug |
| `falcon_proxy_enabled` | `false` | No | Network Configuration |
| `falcon_proxy_host` | `""` | No | — |
| `falcon_proxy_port` | `8080` | No | — |
| `falcon_proxy_disable_ssl` | `false` | No | — |
| `falcon_billing` | `""` | No | Billing tag |
| `falcon_air_gapped` | `false` | No | Air-gapped Configuration |
| `falcon_sensor_download_url` | `""` | No | — |
| `falcon_sensor_remove_hash` | `false` | No | — |
| `falcon_service_enable` | `true` | No | Service Configuration |
| `falcon_service_start` | `true` | No | — |
| `falcon_restart_on_change` | `true` | No | — |
| `falcon_linux_install_method` | `"rpm"` | No | Linux Specific Options: rpm, deb, tar |
| `falcon_linux_package_name` | `"falcon-sensor"` | No | — |
| `falcon_linux_service_name` | `"falcon-sensor"` | No | — |
| `falcon_linux_uninstall_cleanup` | `true` | No | — |
| `falcon_windows_install_method` | `"exe"` | No | Windows Specific Options: exe, msi |
| `falcon_windows_service_name` | `"CSFalconService"` | No | — |
| `falcon_windows_install_path` | `"C:\\Program Files\\CrowdStrike"` | No | — |
| `falcon_windows_maintenance_token` | `""` | No | — |
| `falcon_container_enabled` | `false` | No | Container/Kubernetes |
| `falcon_container_runtime` | `"docker"` | No | Options: docker, containerd, cri-o |
| `falcon_k8s_enabled` | `false` | No | — |
| `falcon_k8s_namespace` | `"falcon-system"` | No | — |
| `falcon_k8s_cluster_name` | `""` | No | — |
| `falcon_tamper_protection` | `true` | No | Security Configuration |
| `falcon_remove_host_on_uninstall` | `false` | No | — |
| `falcon_sensor_grouping_tags` | `[]` | No | — |
| `falcon_fourth_estate_enabled` | `true` | No | Fourth Estate Specific |
| `falcon_source_protection` | `true` | No | — |
| `falcon_journalist_protection` | `true` | No | — |
| `falcon_secure_drop_monitoring` | `true` | No | — |
| `falcon_enhanced_logging` | `true` | No | — |
| `falcon_fips_enabled` | `false` | No | FIPS Configuration |
| `falcon_sensor_update_policy` | `"enabled"` | No | Update Configuration |
| `falcon_prevent_uninstall` | `true` | No | — |
| `falcon_enable_sensor_monitoring` | `true` | No | Monitoring |
| `falcon_health_check_interval` | `3600` | No | 1 hour |
| `falcon_stig_mode` | `true` | No | Compliance |
| `falcon_audit_mode` | `false` | No | — |

## Example Playbook

```yaml
---
- name: Deploy CrowdStrike Falcon Sensor
  hosts: falcon_targets
  become: true
  roles:
    - role: crowdstrike/roles/falcon_sensor_install
      vars:
        falcon_cloud: "us-gov-1"
        falcon_sensor_version: "latest"
        falcon_sensor_tags: "Fourth-Estate,Production"
```

## Tags

| Tag | Description |
|-----|-------------|
| `install` | Sensor download and installation |
| `configure` | Sensor configuration (CID, proxy, tags) |
| `verify` | Post-install verification |
| `monitoring` | Health check configuration |
| `security` | Tamper protection and STIG controls |

## License

MIT

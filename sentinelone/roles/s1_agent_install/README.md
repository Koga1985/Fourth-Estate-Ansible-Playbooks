# s1_agent_install

Installs, configures, and verifies the SentinelOne agent on Linux and Windows endpoints with DoD STIG compliance. Supports API-based download, local installer, and air-gapped deployments. Also supports Kubernetes deployment.

## Requirements

- Ansible 2.15+
- `ansible.posix` collection (Linux)
- `ansible.windows` collection (Windows)
- Hosts must reach your SentinelOne console (default: `usgoveast1.sentinelone.net:443`) for API install method

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `s1_site_token` | `"{{ vault_s1_site_token }}"` | No | SentinelOne Configuration REQUIRED — from console: Settings > Sites |
| `s1_console_url` | `"https://usgoveast1.sentinelone.net"` | No | US GovCloud |
| `s1_management_url` | `"{{ s1_console_url }}"` | No | — |
| `s1_agent_version` | `"latest"` | No | Agent Version |
| `s1_agent_version_specific` | `""` | No | Specify exact version if needed |
| `s1_install_method` | `"api"` | No | Installation Method Options: api, local, url |
| `s1_agent_download_path` | `"/tmp"` | No | — |
| `s1_local_installer_path` | `""` | No | — |
| `s1_agent_download_url` | `""` | No | — |
| `s1_api_token` | `"{{ vault_s1_api_token }}"` | No | API Configuration (store credentials in vault.yml) REQUIRED for api install method |
| `s1_api_timeout` | `300` | No | — |
| `s1_account_id` | `""` | No | Optional: specific account |
| `s1_site_id` | `""` | No | Optional: specific site |
| `s1_group_name` | `"Default"` | No | Agent Configuration |
| `s1_tags` | `"Fourth-Estate,Managed-by-Ansible"` | No | — |
| `s1_agent_log_level` | `"info"` | No | Options: off, error, warning, info, debug, trace |
| `s1_customer_id` | `""` | No | — |
| `s1_proxy_enabled` | `false` | No | Network Configuration |
| `s1_proxy_host` | `""` | No | — |
| `s1_proxy_port` | `8080` | No | — |
| `s1_proxy_username` | `""` | No | — |
| `s1_proxy_password` | `""` | No | — |
| `s1_air_gapped` | `false` | No | Air-gapped Configuration |
| `s1_update_server` | `""` | No | — |
| `s1_service_enable` | `true` | No | Service Configuration |
| `s1_service_start` | `true` | No | — |
| `s1_restart_on_change` | `true` | No | — |
| `s1_linux_install_method` | `"rpm"` | No | Linux Specific Options: rpm, deb |
| `s1_linux_package_name` | `"SentinelAgent"` | No | — |
| `s1_linux_service_name` | `"sentinelone"` | No | — |
| `s1_linux_install_path` | `"/opt/sentinelone"` | No | — |
| `s1_windows_install_method` | `"exe"` | No | Windows Specific Options: exe, msi |
| `s1_windows_service_name` | `"SentinelAgent"` | No | — |
| `s1_windows_install_path` | `"C:\\Program Files\\SentinelOne"` | No | — |
| `s1_container_enabled` | `false` | No | Container/Kubernetes |
| `s1_container_runtime` | `"docker"` | No | Options: docker, containerd, cri-o |
| `s1_k8s_enabled` | `false` | No | — |
| `s1_k8s_namespace` | `"sentinelone"` | No | — |
| `s1_k8s_cluster_name` | `""` | No | — |
| `s1_tamper_protection` | `true` | No | Security Configuration |
| `s1_uninstall_protection` | `true` | No | — |
| `s1_self_protection` | `true` | No | — |
| `s1_remove_agent_on_uninstall` | `false` | No | — |
| `s1_enable_network_quarantine` | `true` | No | Agent Features |
| `s1_enable_auto_mitigation` | `true` | No | — |
| `s1_enable_auto_remediation` | `true` | No | — |
| `s1_suspicious_activity_action` | `"detect"` | No | Options: detect, protect |
| `s1_malicious_activity_action` | `"protect"` | No | Options: detect, protect |
| `s1_fourth_estate_enabled` | `true` | No | Fourth Estate Specific |
| `s1_source_protection` | `true` | No | — |
| `s1_journalist_protection` | `true` | No | — |
| `s1_secure_drop_monitoring` | `true` | No | — |
| `s1_enhanced_logging` | `true` | No | — |
| `s1_enable_deep_visibility` | `true` | No | Deep Visibility |
| `s1_dv_retention_days` | `90` | No | — |
| `s1_enable_agent_monitoring` | `true` | No | Monitoring |
| `s1_health_check_interval` | `3600` | No | 1 hour |
| `s1_syslog_enabled` | `false` | No | — |
| `s1_syslog_server` | `""` | No | — |
| `s1_syslog_port` | `514` | No | — |
| `s1_stig_mode` | `true` | No | Compliance |
| `s1_fips_mode` | `false` | No | — |
| `s1_audit_mode` | `false` | No | — |
| `s1_auto_update_enabled` | `true` | No | Update Configuration |
| `s1_update_window_start` | `"02:00"` | No | — |
| `s1_update_window_end` | `"06:00"` | No | — |

## Example Playbook

```yaml
---
- name: Deploy SentinelOne Agent
  hosts: s1_targets
  become: true
  roles:
    - role: sentinelone/roles/s1_agent_install
      vars:
        s1_console_url: "https://usgoveast1.sentinelone.net"
        s1_group_name: "Production-Linux"
        s1_tags: "Fourth-Estate,Production"
```

## Tags

| Tag | Description |
|-----|-------------|
| `install` | Agent download and installation |
| `configure` | Agent configuration (site token, groups, tags) |
| `verify` | Post-install verification |
| `monitoring` | Health check configuration |
| `security` | Tamper protection and STIG controls |

## License

MIT

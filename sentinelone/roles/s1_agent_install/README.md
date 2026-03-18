# s1_agent_install

Installs, configures, and verifies the SentinelOne agent on Linux and Windows endpoints with DoD STIG compliance. Supports API-based download, local installer, and air-gapped deployments. Also supports Kubernetes deployment.

## Requirements

- Ansible 2.15+
- `ansible.posix` collection (Linux)
- `ansible.windows` collection (Windows)
- Hosts must reach your SentinelOne console (default: `usgoveast1.sentinelone.net:443`) for API install method

## Role Variables

### Required

| Variable | Description |
|----------|-------------|
| `vault_s1_site_token` | Site token — from SentinelOne console > Settings > Sites > click site > Site Token |
| `vault_s1_api_token` | API token — from SentinelOne console > Settings > Users > click user > API Token |

### Key Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `s1_site_token` | `{{ vault_s1_site_token }}` | **Yes** | Site registration token |
| `s1_console_url` | `"https://usgoveast1.sentinelone.net"` | No | SentinelOne console URL |
| `s1_install_method` | `"api"` | No | Install method: `api` (download from console), `local` (use local file) |
| `s1_agent_version` | `"latest"` | No | Agent version — pin for stability |
| `s1_group_name` | `"Default"` | No | Agent group in SentinelOne console |
| `s1_tags` | `"Fourth-Estate,Managed-by-Ansible"` | No | Tags visible in SentinelOne console |
| `s1_tamper_protection` | `true` | No | Prevent unauthorized agent removal |
| `s1_enable_auto_mitigation` | `true` | No | Automatically mitigate detected threats |
| `s1_air_gapped` | `false` | No | Enable air-gapped mode (requires `s1_agent_download_url`) |

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

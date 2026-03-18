# falcon_sensor_install

Installs, configures, and verifies the CrowdStrike Falcon sensor on Linux and Windows endpoints with DoD STIG compliance. Supports API-based download, local installer, and air-gapped deployments. Also supports Kubernetes container sensor deployment.

## Requirements

- Ansible 2.15+
- `crowdstrike.falcon` collection: `ansible-galaxy collection install crowdstrike.falcon`
- `ansible.posix` collection (Linux)
- `ansible.windows` collection (Windows)
- Hosts must reach `api.crowdstrike.com:443` (or configured proxy) for API install method

## Role Variables

### Required

| Variable | Description |
|----------|-------------|
| `vault_falcon_cid` | CrowdStrike Customer ID — from Falcon console > Hosts > Sensor Downloads |
| `vault_falcon_api_client_id` | OAuth2 client ID (required for `api` install method) |
| `vault_falcon_api_client_secret` | OAuth2 client secret (required for `api` install method) |

### Key Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `falcon_cid` | `{{ vault_falcon_cid }}` | **Yes** | Customer ID |
| `falcon_cloud` | `"us-1"` | No | Cloud region: `us-1`, `us-2`, `eu-1`, `us-gov-1` |
| `falcon_install_method` | `"api"` | No | Install method: `api` (download from CrowdStrike), `local` (use local file) |
| `falcon_sensor_version` | `"latest"` | No | Sensor version — pin to a specific version for stability |
| `falcon_sensor_tags` | `"Fourth-Estate,Managed-by-Ansible"` | No | Tags visible in Falcon console |
| `falcon_air_gapped` | `false` | No | Enable air-gapped mode (requires `falcon_sensor_download_url`) |
| `falcon_proxy_enabled` | `false` | No | Route sensor traffic through a proxy |
| `falcon_tamper_protection` | `true` | No | Prevent unauthorized sensor removal |

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

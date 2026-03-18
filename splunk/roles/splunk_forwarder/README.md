# splunk_forwarder

Deploys and configures Splunk Universal Forwarder on Linux endpoints with DoD STIG-compliant TLS, FIPS mode, and audit log forwarding.

## Requirements

- Ansible 2.15+
- `ansible.posix` collection
- Target: RHEL/CentOS/Rocky/Ubuntu/Debian
- Splunk indexers must be reachable on port 9997 (or configured port)

## Role Variables

### Required

| Variable | Description |
|----------|-------------|
| `splunk_indexers` | List of indexer endpoints (`host:port`). See example below. |

### Key Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `splunk_indexers` | `["indexer1.example.com:9997"]` | **Yes** | List of indexer addresses |
| `splunk_forwarder_version` | `"9.2.1"` | No | Forwarder version |
| `splunk_forwarder_home` | `"/opt/splunkforwarder"` | No | Installation path |
| `splunk_forwarder_enable_ssl` | `true` | No | Enable TLS for forwarding |
| `splunk_forwarder_fips_mode` | `true` | No | Enable FIPS 140-2 |
| `splunk_monitor_paths` | `/var/log/messages`, `/var/log/secure`, `/var/log/audit/audit.log` | No | Log paths to monitor |
| `splunk_deployment_server` | `""` | No | Deployment server address for centralized config |

## Example Playbook

```yaml
---
- name: Deploy Splunk Forwarder
  hosts: all_linux_servers
  become: true
  roles:
    - role: splunk/roles/splunk_forwarder
      vars:
        splunk_indexers:
          - "splunk-idx-01.example.com:9997"
          - "splunk-idx-02.example.com:9997"
        splunk_monitor_paths:
          - "/var/log/messages"
          - "/var/log/secure"
          - "/var/log/audit/audit.log"
          - "/var/log/httpd"
```

## License

MIT

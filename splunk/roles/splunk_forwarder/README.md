# splunk_forwarder

Deploys and configures Splunk Universal Forwarder on Linux endpoints with DoD STIG-compliant TLS, FIPS mode, and audit log forwarding.

## Requirements

- Ansible 2.15+
- `ansible.posix` collection
- Target: RHEL/CentOS/Rocky/Ubuntu/Debian
- Splunk indexers must be reachable on port 9997 (or configured port)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `splunk_forwarder_version` | `"9.2.1"` | No | — |
| `splunk_forwarder_build` | `"78803f08aabb"` | No | — |
| `splunk_forwarder_home` | `"/opt/splunkforwarder"` | No | — |
| `splunk_forwarder_user` | `"splunk"` | No | — |
| `splunk_forwarder_group` | `"splunk"` | No | — |
| `splunk_indexers` | `(see defaults/main.yml)` | No | Deployment Configuration |
| `splunk_deployment_server` | `""` | No | — |
| `splunk_forwarder_enable_ssl` | `true` | No | TLS Configuration (STIG V-258080) |
| `splunk_forwarder_ssl_verify` | `true` | No | — |
| `splunk_forwarder_tls_min_version` | `"tls1.2"` | No | — |
| `splunk_forwarder_cipher_suite` | `"ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256"` | No | — |
| `splunk_monitor_paths` | `(see defaults/main.yml)` | No | Data Collection |
| `splunk_forwarder_max_kbps` | `1024` | No | Performance and Resource Limits |
| `splunk_forwarder_queue_size` | `"10MB"` | No | — |
| `splunk_forwarder_fips_mode` | `true` | No | Security |
| `splunk_forwarder_enable_boot_start` | `true` | No | — |

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

## Tags

| Tag | Description |
|-----|-------------|
| `config` | Tasks tagged `config` |
| `forwarder` | Tasks tagged `forwarder` |
| `inputs` | Tasks tagged `inputs` |
| `install` | Tasks tagged `install` |
| `outputs` | Tasks tagged `outputs` |
| `security` | Tasks tagged `security` |

## License

MIT

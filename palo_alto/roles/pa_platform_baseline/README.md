# pa_platform_baseline

Applies system and management plane hardening, PKI certificate deployment, dynamic content update schedules, and running-config backup for Palo Alto Networks firewalls. Supports both standalone devices and Panorama-managed deployments.

## Requirements

- Ansible 2.15+
- Collection: `paloaltonetworks.panos` (`ansible-galaxy collection install paloaltonetworks.panos`)
- PAN-OS 10.1 or higher (tested on 10.x and 11.x)
- API key or admin credentials for the target device or Panorama
- `become: false` (PAN-OS modules handle authentication directly)

## Role Variables

### Connection / Panorama

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `pa_use_panorama` | `false` | No | When `true`, targets Panorama rather than a direct device |
| `device_group` | `null` | No | Panorama device group (required when `pa_use_panorama: true`) |
| `vsys` | `"vsys1"` | No | Virtual system to target on the device |
| `template` | `null` | No | Panorama template name |
| `template_stack` | `null` | No | Panorama template stack name |
| `artifacts_dir` | `"/tmp/pan-artifacts"` | No | Local directory for exported configs and reports |
| `commit_after_changes` | `true` | No | Commit the candidate config after all changes |
| `commit_description` | `"Apply platform baseline via Ansible"` | No | Commit description string |

### System Settings

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `system.hostname` | `null` | No | Device hostname |
| `system.timezone` | `"UTC"` | No | System timezone (e.g. `"US/Eastern"`) |
| `system.dns_primary` | `null` | No | Primary DNS server IP |
| `system.dns_secondary` | `null` | No | Secondary DNS server IP |
| `system.login_banner` | `null` | No | Login banner text (DoD STIG required) |

### Management Plane Hardening

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `mgmt_hardening.https` | `true` | No | Allow HTTPS management access |
| `mgmt_hardening.http` | `false` | No | Allow HTTP management access (disable per STIG) |
| `mgmt_hardening.ssh` | `true` | No | Allow SSH management access |
| `mgmt_hardening.telnet` | `false` | No | Allow Telnet access (disable per STIG) |
| `mgmt_hardening.ping` | `true` | No | Allow ICMP ping to management interface |
| `mgmt_hardening.permitted_ips` | `[]` | No | List of CIDRs permitted to reach the management interface |

### NTP

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ntp_servers` | `[]` | No | List of NTP server IPs or hostnames |

### Certificates / PKI

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `certificates` | `[]` | No | List of certificate objects to import (see structure below) |

Each certificate entry:

```yaml
certificates:
  - name: "my-ca-cert"
    certificate_file: "/path/to/cert.pem"
    private_key_file: "/path/to/key.pem"   # optional
    passphrase: "{{ vault_cert_passphrase }}"  # optional
    ca: true
```

### Dynamic Updates

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `du_schedule.content.recurring` | `"daily"` | No | Content update schedule (`"daily"`, `"weekly"`, etc.) |
| `du_schedule.content.at` | `"03:30"` | No | Time for daily content updates |
| `du_schedule.antivirus.recurring` | `"hourly"` | No | Antivirus update frequency |
| `du_schedule.wildfire.recurring` | `"every-15-min"` | No | WildFire update frequency |
| `du_schedule.url_filtering.recurring` | `"daily"` | No | URL filtering update schedule |
| `du_schedule.url_filtering.at` | `"04:10"` | No | Time for daily URL filtering updates |
| `run_updates_now` | `false` | No | Trigger an immediate update check on all content types |

### Backup

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `backup.running_config.enabled` | `true` | No | Export the running config |
| `backup.running_config.scp.enabled` | `false` | No | SCP the running config to a remote server |
| `backup.running_config.scp.server` | `"scp.example.com"` | No | SCP destination hostname |
| `backup.running_config.scp.username` | `"backup"` | No | SCP username |
| `backup.running_config.scp.password` | `$BACKUP_SCP_PASSWORD` | **Yes if SCP enabled** | SCP password (vault-protected) |
| `backup.running_config.scp.path` | `"/incoming/{{ inventory_hostname }}-running.xml"` | No | Remote SCP path |
| `backup.tech_support.enabled` | `false` | No | Export a tech support bundle |

## Example Playbook

```yaml
- name: Apply Palo Alto platform baseline
  hosts: palo_alto_firewalls
  gather_facts: false
  roles:
    - role: palo_alto/roles/pa_platform_baseline
      vars:
        commit_after_changes: true
        system:
          hostname: "fw-prod-01"
          timezone: "US/Eastern"
          dns_primary: "10.0.0.53"
          login_banner: |
            WARNING: This system is for authorized use only.
        mgmt_hardening:
          https: true
          http: false
          ssh: true
          telnet: false
          permitted_ips:
            - "10.10.0.0/24"
        ntp_servers:
          - "10.0.0.123"
        run_updates_now: false
```

## Tags

| Tag | Description |
|-----|-------------|
| `system` | System settings (hostname, DNS, timezone, banner) |
| `mgmt-hardening` | Management plane access controls |
| `ntp` | NTP server configuration |
| `certificates` | PKI certificate import |
| `dynamic-updates` | Content update schedules |
| `backup` | Running config and tech support export |

## Compliance Controls

| Framework | Control ID | Description |
|-----------|-----------|-------------|
| NIST 800-53 | AC-17 | Remote Access — restrict management plane access |
| NIST 800-53 | CM-6 | Configuration Settings — disable insecure protocols |
| NIST 800-53 | CM-7 | Least Functionality — disable HTTP, Telnet |
| NIST 800-53 | SC-8 | Transmission Confidentiality — HTTPS/SSH only |
| NIST 800-53 | SC-17 | PKI certificates |

## Notes

- `commit_after_changes: true` is the default; set to `false` to stage changes without committing (useful for batching multiple roles).
- `mgmt_hardening.permitted_ips: []` means no IP restrictions are applied. Always populate this in production.
- SCP backup requires a reachable SCP server and vault-protected credentials.

## License

MIT

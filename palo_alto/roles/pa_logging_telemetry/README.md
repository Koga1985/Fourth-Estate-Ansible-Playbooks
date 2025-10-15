# pa_logging_telemetry

Production role for Palo Alto Networks to manage **log forwarding** and **telemetry**:
- SYSLOG & HTTP server profiles (e.g., SIEM, Splunk HEC)
- Log Forwarding Profiles (match-lists & actions: panorama/syslog/http/etc.)
- Optional binding of a log profile to rules by tag
- Device telemetry enablement (local firewall)
- Tech-support bundle creation (optional SCP offload)

> Works for **firewalls** and **Panorama** (via `pa_use_panorama: true` + `device_group`).

## Requirements
- Collection: `paloaltonetworks.panos`
- `httpapi` connection to firewall or Panorama

## Key Variables
See `defaults/main.yml`. Common snippets:

```yaml
pa_syslog_profiles:
  - name: "SIEM"
    description: "Primary SIEM"
    servers:
      - { name: "siem1", ip_address: "192.0.2.50", transport: "UDP", port: 514, format: "BSD" }

pa_http_profiles:
  - name: "Splunk-HEC"
    servers:
      - name: "hec1"
        address: "splunk.example"
        http_port: 8088
        https: true
        uri_format: "/services/collector"
        http_method: "POST"
        tls_verify: false
        http_headers:
          - "Authorization: Splunk <token>"

pa_log_forwarding_profiles:
  - name: "Default-Forward"
    match_list:
      - name: "threats"
        log_type: "THREAT"
        actions:
          - { type: "syslog", syslog_profile: "SIEM" }
          - { type: "panorama" }

pa_bind_log_profile:
  enabled: true
  profile_name: "Default-Forward"
  rule_tags: ["owner:secops"]

telemetry:
  enabled: true
  applications: true
  threats: true
  url: true
  wildfire: true

techsupport:
  enabled: true
  exclude_logs: false
  scp:
    enabled: false
```

## Example Play (firewalls)
```yaml
- hosts: pan_firewalls
  gather_facts: false
  roles:
    - role: pa_logging_telemetry
      vars:
        pa_syslog_profiles:
          - name: "SIEM"
            servers:
              - { name: "siem1", ip_address: "192.0.2.50" }
        pa_log_forwarding_profiles:
          - name: "Default-Forward"
            match_list:
              - name: "Threats"
                log_type: "THREAT"
                actions:
                  - { type: "syslog", syslog_profile: "SIEM" }
        pa_bind_log_profile:
          enabled: true
          profile_name: "Default-Forward"
          rule_tags: ["owner:secops"]
        telemetry:
          enabled: true
```

## Example Play (Panorama)
```yaml
- hosts: panorama
  gather_facts: false
  roles:
    - role: pa_logging_telemetry
      vars:
        pa_use_panorama: true
        device_group: "Shared-Services"
        pa_syslog_profiles:
          - name: "SIEM"
            servers:
              - { name: "siem1", ip_address: "192.0.2.50" }
        pa_log_forwarding_profiles:
          - name: "Default-Forward"
            match_list:
              - name: "Threats"
                log_type: "THREAT"
                actions:
                  - { type: "syslog", syslog_profile: "SIEM" }
```

## Notes
- Cortex Data Lake (CDL): Use actions `panorama` or appropriate logging service in the match_list depending on your design.
- Binding to rules by tag uses a fact query; ensure Ansible control host has collection version that provides rule facts helper.
- Tech-support SCP offload runs **on the device**; provide reachable SCP server and credentials if you enable it.

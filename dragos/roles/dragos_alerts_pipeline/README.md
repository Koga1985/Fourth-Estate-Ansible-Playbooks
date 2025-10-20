
# Role: dragos_alerts_pipeline

**Purpose:** alert intake → normalize → distribute.

## Includes
- `dragos_alerts__pull_filtered.yml`
- `dragos_alerts__export_csv.yml`
- `dragos_alerts__forward_http.yml`
- `dragos_alerts__forward_syslog.yml`

## Defaults (see `defaults/main.yml`)
```yaml
alert_filter:
  severity: ["high","critical"]
  category: []
  since_iso: null
siem: {}                      # { url: "...", token: "..." }
syslog:
  use_logger: false
  facility: "user"
  priority: "info"
  cef_vendor: "Dragos"
  cef_product: "xDome"
artifacts_dir: "/tmp/dragos-artifacts"
dragos_base_url: "https://tenant.dragos.com"
dragos_token: "{{ lookup('env','DRAGOS_TOKEN') }}"
dragos_verify_ssl: true
page_size: 500
dry_run: true
```

## Example
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: dragos_alerts_pipeline
      vars:
        alert_filter:
          severity: ["high","critical"]
          since_iso: "2025-01-01T00:00:00Z"
        siem:
          url: "https://siem.example/intake"
          token: "{{ lookup('env','SIEM_TOKEN') }}"
        syslog:
          use_logger: true
```
Artifacts saved under `{{ artifacts_dir }}`:
- `alerts_filtered.json`
- `alerts_filtered.csv`
- (optional) `alerts.cef`

# infoblox_capacity_reports

Generate BI-friendly **capacity reports** from Infoblox (NIOS). The role collects:
- **Address utilization** per network (and aggregates by **Site EA** and optional **container CIDRs**)
- **DHCP utilization** per range
- **DNS query stats** per DNS member (best-effort; varies by NIOS)
- Outputs **CSV** + **JSON** artifacts in `report_dir`

## Requirements
- Ansible collection: `infoblox.nios_modules`
- A WAPI user with read permissions

## Variables (defaults)
```yaml
nios_host: ""
nios_username: ""
nios_password: ""
nios_validate_certs: false
nios_wapi_version: "v2.12"

report_dir: "/tmp/infoblox-capacity"
dns_view: "default"
site_ea_key: "Site"
group_by_container_cidrs: []
```

## Example Playbook
```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: infoblox_capacity_reports
      vars:
        nios_host: "nios.example.local"
        nios_username: "{{ lookup('env','NIOS_USER') }}"
        nios_password: "{{ lookup('env','NIOS_PASS') }}"
        nios_validate_certs: false
        group_by_container_cidrs: ["10.10.0.0/16","10.20.0.0/16"]
        report_dir: "/tmp/infoblox-capacity"
```
## Outputs
- `capacity_raw.json` — raw API responses to help troubleshooting
- `capacity_rollup.json` — structured arrays for networks/site/container/DHCP
- CSVs:
  - `address_utilization_per_network.csv`
  - `address_utilization_by_site.csv`
  - `address_utilization_by_container.csv` (if grouping configured)
  - `dhcp_utilization.csv`

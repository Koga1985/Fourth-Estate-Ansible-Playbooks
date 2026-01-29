# infoblox_audit_compliance

Read-only **drift checks** for Infoblox vs your **desired YAML**. No changes are made—results are exported as **JSON + CSV** for BI.

## What it compares
- **Network Views** (comment, EAs)
- **DNS Views** (comment, EAs)
- **VLANs** (id, parent, description, EAs)
- **Network Containers** IPv4/IPv6 (comment, EAs)
- **Authoritative Zones** (ns_group, EAs)

Tune the fields in `defaults/main.yml` under `cmp_fields:` to widen/narrow the comparison.

## Requirements
- Ansible collection: `infoblox.nios_modules`
- Read-only WAPI credentials

## Desired YAML schema (example)
```yaml
network_views:
  - { name: "Corp-NV", comment: "Corporate networks", extattrs: { Environment: { value: "prod" } } }

dns_views:
  - { name: "Corp-View", comment: "Split-horizon corporate DNS" }

vlans:
  - { name: "VLAN10-Users", id: 10, parent: "default", description: "User access", extattrs: { Environment: { value: "prod" } } }

network_containers_v4:
  - { cidr: "10.0.0.0/8",  comment: "All corp space", extattrs: { Environment: { value: "prod" } } }
network_containers_v6:
  - { cidr: "2001:db8::/32", comment: "Global v6" }

zones_auth:
  - { fqdn: "corp.example.com", view: "default", ns_group: "Grid Primary" }
```

## Example Playbook
```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: infoblox_audit_compliance
      vars:
        nios_host: "nios.example.local"
        nios_username: "{{ lookup('env','NIOS_USER') }}"
        nios_password: "{{ lookup('env','NIOS_PASS') }}"
        desired_files:
          - "group_vars/desired-inventory.yml"
        report_dir: "/tmp/infoblox-audit"
```
## Outputs
- `infoblox_audit_drift.json`
- CSVs for each object type:
  - `network_views_drift.csv`
  - `dns_views_drift.csv`
  - `vlans_drift.csv`
  - `network_containers_v4_drift.csv`
  - `network_containers_v6_drift.csv`
  - `zones_auth_drift.csv`

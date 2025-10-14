# Role: cp_services_catalog

Manage Check Point service catalog separately from objects: L4 (TCP/UDP) services and L7 (Application/URL) definitions.

## Requirements
- Connection: `httpapi` to the Management Server
- Collection: `check_point.mgmt`

## Defaults
```yaml
publish_changes: false

# L4
cp_services_tcp: []
cp_services_udp: []

# L7
cp_app_sites: []
cp_app_categories: []
```

## Usage
```yaml
- hosts: checkpoint_mgmt
  gather_facts: false
  roles:
    - role: cp_services_catalog
      vars:
        publish_changes: true
        cp_services_tcp:
          - { name: http-8080, port: 8080, comment: "HTTP alt" }
        cp_services_udp:
          - { name: syslog-514, port: 514, comment: "Syslog" }
        cp_app_categories:
          - { name: "Business-Apps", color: green }
        cp_app_sites:
          - name: "GitHub"
            primary_category: "Developer Tools"
            url_list: ["github.com","*.githubusercontent.com"]
            risk: 2
```

## Tags
- `services`, `l4`, `l7`, `publish`

# vcenter_inventory_model (role)

Creates and maintains a clean **vCenter inventory model**:
- VM & Host folders
- Optional app-tier subfolders (`web/app/db`, etc.)
- Resource pools under clusters or nested pools

## Requirements
- Ansible >= 2.15
- Collection: `community.vmware` (see `requirements.yml`)
- pyvmomi on the control node

## Usage
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vcenter_inventory_model
      vars:
        vcenter_hostname: "vcenter.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false
        vcenter_datacenter: "DC1"

        vm_folders:
          - "/DC1/vm/Production"
          - "/DC1/vm/NonProd"

        create_app_tier_subfolders: true
        app_tiers: ["web","app","db"]

        resource_pools:
          - { path: "/DC1/host/Cluster01", name: "App" }
          - { path: "/DC1/host/Cluster01/Resources/DB", name: "DB-Heavy" }
```

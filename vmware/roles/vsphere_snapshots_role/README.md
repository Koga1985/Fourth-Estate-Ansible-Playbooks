# vsphere_snapshots (role)

Find and/or delete VMware vSphere snapshots at scale.

## Requirements
- Ansible >= 2.15
- Python pyvmomi on the controller
- Collection: community.vmware

## Variables
See defaults/main.yml for all tunables.

## Usage examples

### Find snapshots
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vsphere_snapshots
      vars:
        vcenter_hostname: "vcenter.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false
        vcenter_datacenter: "DC1"
        vsphere_snapshots_action: "find"
```

### Delete snapshots (dry run)
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vsphere_snapshots
      vars:
        vcenter_hostname: "vcenter.example.local"
        vcenter_username: "{{ vault_vcenter_username }}"
        vcenter_password: "{{ vault_vcenter_password }}"
        vcenter_validate_certs: false
        vcenter_datacenter: "DC1"
        vsphere_snapshots_action: "delete"
        vsphere_snapshots_precheck_only: true
```

### Delete snapshots (confirmed)
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vsphere_snapshots
      vars:
        vcenter_hostname: "vcenter.example.local"
        vcenter_username: "{{ vault_vcenter_username }}"
        vcenter_password: "{{ vault_vcenter_password }}"
        vcenter_validate_certs: false
        vcenter_datacenter: "DC1"
        vsphere_snapshots_action: "delete"
        vsphere_snapshots_confirm_delete: true
        vsphere_snapshots_delete_concurrency: 2
```

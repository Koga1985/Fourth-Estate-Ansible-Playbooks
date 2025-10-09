# vds_fabric (role)

Create and maintain **vSphere Distributed Switches (VDS)**:
- Switch creation/version, **MTU**
- Uplink profile (**quantity/prefix**)
- **LLDP/CDP** discovery (advertise/listen/both)
- **NIOC** toggle (enable/disable, if licensed)
- Optional **host membership** (attach vmnics to VDS)

> Portgroup definitions/policies can live in a separate role (e.g. `vds_portgroups`).

## Requirements
- Ansible >= 2.15
- Collection: `community.vmware`
- vSphere Enterprise Plus for NIOC

## Variables (see `defaults/main.yml`)
```yaml
vcenter_hostname: "vcenter.example.local"
vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
vcenter_validate_certs: false
vcenter_datacenter: "DC1"

dvswitches:
  - name: "VDS-Prod"
    version: "8.0.0"
    mtu: 9000
    uplink_quantity: 4
    uplink_prefix: "Uplink"
    lldp: { protocol: lldp, operation: both }
    nioc: { enabled: true }

host_membership:
  - { dvs_name: "VDS-Prod", esxi_hostname: "esxi01.example.local", vmnics: ["vmnic0","vmnic1"] }
  - { dvs_name: "VDS-Prod", esxi_hostname: "esxi02.example.local", vmnics: ["vmnic0","vmnic1"] }
```

## Example Play
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vds_fabric
      vars:
        vcenter_hostname: "vcenter.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false
        vcenter_datacenter: "DC1"
        dvswitches:
          - name: "VDS-Prod"
            version: "8.0.0"
            mtu: 9000
            uplink_quantity: 4
            uplink_prefix: "Uplink"
            lldp: { protocol: lldp, operation: both }
            nioc: { enabled: true }
        host_membership:
          - { dvs_name: "VDS-Prod", esxi_hostname: "esxi01.example.local", vmnics: ["vmnic0","vmnic1"] }
```

### Notes
- Changing **uplink_quantity/prefix** impacts host migration—plan carefully.
- Enabling **NIOC** requires a compatible license and VDS version.
- Use a separate role to define **dvPortGroups** with VLAN/security policies.

# vmware_esxi_config (role)

Configure an ESXi host in **standalone** mode (direct) or via **vCenter** (and optionally add it to DC/Cluster).
Covers maintenance mode, acceptance level, DNS/NTP/syslog, service policies, and vSwitch/portgroup creation.

## Requirements
- Ansible >= 2.15
- Collection: community.vmware
- Control node Python: pyvmomi

## Examples
See `defaults/main.yml` and below.

### Standalone
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vmware_esxi_config
      vars:
        esxi_mode: standalone
        esxi_hostname: "esxi01.example.local"
        esxi_username: "root"
        esxi_password: "{{ vault_esxi_root_password }}"
        esxi_dns_servers: ["192.0.2.53","192.0.2.54"]
        esxi_ntp_servers: ["time1.example.local","time2.example.local"]
        esxi_syslog_remote: "udp://10.0.0.5:514"
        esxi_vswitches:
          - { name: vSwitch1, mtu: 1500, nics: ["vmnic1","vmnic2"] }
        esxi_portgroups:
          - { name: "Mgmt-PG", vswitch: "vSwitch1", vlan_id: 0 }
        exit_maintenance_mode: true
```

### Via vCenter + Add to Cluster
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vmware_esxi_config
      vars:
        esxi_mode: vcenter
        esxi_hostname: "esxi02.example.local"
        esxi_username: "root"
        esxi_password: "{{ vault_esxi_root_password }}"
        vcenter_hostname: "vcenter.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false
        vcenter_datacenter: "DC1"
        vcenter_cluster: "Compute-Cluster"
        esxi_ntp_servers: ["time1.example.local","time2.example.local"]
        exit_maintenance_mode: true
```

## Notes
- The role assumes ESXi is **already installed and reachable**.
- Adjust service policies to your security baseline (e.g., SSH).

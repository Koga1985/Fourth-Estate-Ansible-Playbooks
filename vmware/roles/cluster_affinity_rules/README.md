# cluster_affinity_rules (role)

Enforce **DRS rules** in a vSphere cluster:
- **VM/VM** affinity & anti-affinity
- **VM/Host** affinity via DRS groups
- Optional **drift enforcement** (delete undeclared rules)

## Requirements
- Ansible >= 2.15
- Collection: `community.vmware`

## Variables
See `defaults/main.yml`. Minimal example:
```yaml
vcenter_hostname: "vcenter.example.local"
vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
vcenter_validate_certs: false
vcenter_datacenter: "DC1"
cluster_name: "Compute-Cluster"

vm_vm_rules:
  - name: "Keep web VMs apart"
    enabled: true
    mandatory: false
    affinity: false
    vms: ["web01","web02","web03"]

vm_host_rules:
  - name: "DBs on DB hosts"
    enabled: true
    mandatory: true
    vm_group: "DB-VMs"
    host_group: "DB-Hosts"
    vms:  ["db01","db02"]
    hosts: ["esxi01.lab.local","esxi02.lab.local"]

remove_undeclared_rules: false
```

## Example Play
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: cluster_affinity_rules
      vars:
        vcenter_hostname: "vcenter.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false
        vcenter_datacenter: "DC1"
        cluster_name: "Compute-Cluster"
        vm_vm_rules:
          - { name: "Keep web VMs apart", enabled: true, mandatory: false, affinity: false, vms: ["web01","web02","web03"] }
        vm_host_rules:
          - { name: "DBs on DB hosts", enabled: true, mandatory: true, vm_group: "DB-VMs", host_group: "DB-Hosts", vms: ["db01","db02"], hosts: ["esxi01.lab.local","esxi02.lab.local"] }
```

> Drift enforcement is name-based. Turn on `remove_undeclared_rules: true` only if you want strict control over rules in the cluster.

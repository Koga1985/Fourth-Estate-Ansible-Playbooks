# drift_report (role)

Produce a **drift report** by comparing **actual vSphere state** against your **desired**
inputs. Supports:
- **cluster_baseline** (DRS/HA/EVC)
- **vds_portgroups** (VLAN, trunk ranges, security policies)

Outputs a compact **JSON** file.

## Variables (essentials)
See `defaults/main.yml` for full list.
```yaml
vcenter_hostname: "vcsa.example.local"
vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
cluster_name: "Compute-Cluster"
dvs_name: "VDS-Prod"

desired_cluster_baseline:
  drs: { enabled: true, mode: fullyAutomated, vmotion_rate: 3 }
  ha:
    enabled: true
    admission_control: { policy: percentage, cpu_failover_percent: 25, mem_failover_percent: 25 }
    host_isolation_response: restartHost
    vm_monitoring: vmAndAppMonitoring
    default_vm_restart_priority: medium
  evc: { mode: intel-broadwell }

desired_vds_portgroups:
  - { name: "PG-Prod-10", port_binding: "static", num_ports: 128,
      vlan: { mode: access, id: 10 },
      security: { allow_promiscuous: false, mac_changes: false, forged_transmits: false } }

report_path: "/tmp/Compute-Cluster-drift-report.json"
fail_when_drift: false
```

## Example
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: drift_report
      vars: { ... as above ... }
```

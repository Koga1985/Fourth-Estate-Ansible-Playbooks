# vsan_cluster (role)

Enable and configure **vSAN** on a cluster (**OSA** or **ESA**), manage **fault
domains**, and run **health checks** with a JSON report.

## Requirements
- PowerShell Core (`pwsh`) and **VMware PowerCLI** on the controller
- vCenter permissions for vSAN configuration and health APIs
- vSAN **Encryption** needs a configured **KMS** (see your KMS role)

## Variables (see `defaults/main.yml`)
```yaml
vcenter_hostname: "vcsa.example.local"
vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
cluster_name: "Compute-Cluster"

vsan:
  enabled: true
  architecture: "osa"       # or "esa" (vSAN 8+)
  auto_claim: false
  data_reduction: disabled  # disabled | compress_only | dedup_compress (OSA only)
  encryption: false
  verbose: false

fault_domains:
  - name: "FD-AZ1"
    hosts: ["esxi01.lab.local","esxi02.lab.local"]
  - name: "FD-AZ2"
    hosts: ["esxi03.lab.local","esxi04.lab.local"]

run_health_checks: true
health_report_path: "/tmp/Compute-Cluster-vsan-health.json"
```

## Example Play
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vsan_cluster
      vars:
        vcenter_hostname: "vcsa.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        cluster_name: "Compute-Cluster"
        vsan:
          enabled: true
          architecture: "osa"
          auto_claim: false
          data_reduction: "dedup_compress"
          encryption: false
        fault_domains:
          - { name: "FD-AZ1", hosts: ["esxi01.lab.local","esxi02.lab.local"] }
          - { name: "FD-AZ2", hosts: ["esxi03.lab.local","esxi04.lab.local"] }
        run_health_checks: true
        health_report_path: "/tmp/Compute-Cluster-vsan-health.json"
```

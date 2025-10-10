# vm_tools_config (role)

Enforce **VMware Tools** settings (time sync, Tools scripts, upgrade policy) and emit a
JSON **stale tools** report. Uses **PowerCLI** via `pwsh` for consistent API coverage.

## What it enforces
- **Time sync**: synchronize guest time with host (`ToolsConfigInfo.SyncTimeWithHost`)
- **Scripts**: after power-on / after resume / before standby / before guest shutdown
- **Upgrade policy**: e.g., `UpgradeAtPowerCycle` (optional)
- **App-consistent snapshots helper**: set `disk.EnableUUID=TRUE`

## What it reports
- Per-VM **ToolsStatus**, **ToolsVersionStatus2**, **ToolsRunningStatus**, version
- Rollup count of **stale** tools (needs upgrade / not running)
- Written to `report_path` as JSON

## Requirements
- PowerShell Core (`pwsh`) and **VMware PowerCLI** on the controller/jump host
- vCenter privileges to reconfigure VMs

## Variables (see `defaults/main.yml`)
```yaml
vcenter_hostname: "vcsa.example.local"
vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
vcenter_validate_certs: false

# Target selection (choose one or combine)
vm_names: []          # explicit list of VM names
cluster_name: ""      # all VMs in a cluster
folder_name: ""       # all VMs in a folder
tag_name: ""          # VMs with this Tag (name)

tools:
  time_sync: true
  upgrade_policy: "UpgradeAtPowerCycle"   # or ""
  scripts:
    after_power_on: true
    after_resume: true
    before_guest_standby: true
    before_guest_shutdown: true
  set_disk_enable_uuid: true

report_path: "/tmp/vmtools-report.json"
```

## Example Play
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vm_tools_config
      vars:
        vcenter_hostname: "vcsa.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false

        cluster_name: "Compute-Cluster"
        tools:
          time_sync: true
          upgrade_policy: "UpgradeAtPowerCycle"
          scripts:
            after_power_on: true
            after_resume: true
            before_guest_standby: true
            before_guest_shutdown: true
          set_disk_enable_uuid: true

        report_path: "/tmp/vmtools-report.json"
```

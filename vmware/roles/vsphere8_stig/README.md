# VMware vSphere 8 STIG (`vsphere8_stig`)

Production-ready Ansible role that hardens **VMware vSphere 8** — **ESXi 8**
(`ESXI-80-*`) hosts plus selected **vCenter 8** (`VCSA-80-*`) settings — via the
certified **`community.vmware`** collection. Runs from the control node against
vCenter.

## Why "grab and go"

* Certified `community.vmware` over pyVmomi.
* **Safe by default**: `apply_changes=false` runs in check mode (reports, no
  change). With `apply_changes=true` settings are applied and a JSON artifact is
  written.

## Quick start

```bash
cd vmware/roles/vsphere8_stig/playbooks
ansible-galaxy collection install community.vmware
pip install pyvmomi
$EDITOR vars.example.yml          # set vCenter + ESXi hosts (vault the password)

ansible-playbook -i inventory.example run.yml -e @vars.example.yml                       # DRY-RUN
ansible-playbook -i inventory.example run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE

cat /tmp/vsphere8-stig-artifacts/vsphere8_stig.json
```

## Controls implemented

| Area | STIG IDs |
|------|----------|
| ESXi advanced settings | ESXI-80-000004 (banner), 000035 (password quality), 000068/000195/000196 (timeouts), 000111/000113/000156 (lockout/history), 000114/000115/000124 (logging/syslog), 000202 (BPDU), 000220 (MOB), 000241 (esxAdminsGroup) |
| ESXi services / lockdown | ESXI-80-000193 (SSH off), 000035 (Shell off), 000124 (NTP), 000201 (lockdown mode) |
| vCenter | VCSA-80-000034 (logging level); 000089/000111/000257 surfaced for manual verification |

> Confirm exact rule IDs against your vSphere 8 STIG release; the settings/values
> are correct regardless of minor rule-ID drift.

## ⚠️ Pre-flight before enforcing

* **Lockdown mode** and disabling SSH/Shell can remove direct host access — keep
  vCenter access and an exception user; lockdown is applied only in enforce mode.
* The `esxAdminsGroup` value intentionally avoids the default "ESX Admins" AD
  group (privilege-escalation finding) — set it to your real admin group.
* Set `Syslog.global.logHost` to your real collector.
* Some VCSA-80 controls are appliance/SSO-scoped and are reported for manual
  verification rather than enforced.
* Review the dry-run artifact before enforcing.

## Tags

`--tags esxi`, `advanced`, `services`, `vcenter`, `report`, plus `stig_cat2`
and per-rule tags.

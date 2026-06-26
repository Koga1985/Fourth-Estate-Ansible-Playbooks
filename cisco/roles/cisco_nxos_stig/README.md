# Cisco NX-OS Switch STIG (`cisco_nxos_stig`)

Production-ready Ansible role that hardens a **Cisco Nexus (NX-OS) switch** to
the DISA **Cisco NX-OS Switch STIG**. It covers the management-plane (NDM,
`CISC-ND-XXXXXX`) and Layer-2 (`CISC-L2-XXXXXX`) control families using the
certified **`cisco.nxos`** collection over `network_cli`.

> Confirm the benchmark release in `defaults/main.yml` (`stig_version`) against
> the [DISA STIG library](https://public.cyber.mil/stigs/).

## Why "grab and go"

* Certified `cisco.nxos` modules — no SDK beyond the collection.
* **Safe by default**: `apply_changes=false` runs in check mode and emits a
  per-host JSON findings report; nothing is written until `-e apply_changes=true`.
* Idempotent, `no_log` on secrets, `copy run start` handler on change only.

## Quick start

```bash
cd cisco/roles/cisco_nxos_stig/playbooks
ansible-galaxy collection install cisco.nxos ansible.netcommon ansible.utils
cp inventory.example inventory && $EDITOR inventory

# DRY-RUN (report only)
ansible-playbook -i inventory run.yml
# ENFORCE
ansible-playbook -i inventory run.yml -e apply_changes=true

cat /tmp/cisco-nxos-artifacts/nexus-01_nxos_stig.json
```

## Controls implemented

| Area | STIG IDs |
|------|----------|
| Feature hygiene | CISC-ND-001000 (SSH/SCP), 001310 (Telnet off), 001440 (unused services) |
| AAA / access | CISC-ND-000160 (TACACS+), 000280 (idle timeout), 000380 (password strength), 000490 (mgmt ACL), 000550 (accounting) |
| Banner | CISC-ND-000010 |
| Logging / time | CISC-ND-000090/000100/000110 (syslog), 000470 (authenticated NTP) |
| SNMP | CISC-ND-000150/000160 (SNMPv3 only, communities removed) |
| SSH | CISC-ND-001000/001210 (key strength) |
| Control plane | CISC-ND-001220 (CoPP) |
| Layer-2 | CISC-L2-000020 (BPDU Guard), 000030 (Loop Guard), 000050 (DHCP snooping), 000070 (DAI) |

## ⚠️ Pre-flight before enforcing

* Confirm `nxos_user_vlans`, `nxos_management_subnets`, and TACACS keys match
  your environment — defaults are placeholders.
* Keep console/out-of-band access during the window; `feature` and ACL changes
  affect the control plane.
* `feature dhcp` is required for DHCP snooping/DAI and is enabled by the role.

## Tags

`--tags ndm`, `aaa`, `features`, `logging`, `ntp`, `snmp`, `l2`, `report`, plus
`stig_cat2` / `stig_cat3` and per-rule tags (e.g. `--tags CISC-ND-000470`).

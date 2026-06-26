# Cisco ASA STIG (`cisco_asa_stig`)

Production-ready Ansible role that hardens a **Cisco ASA** appliance to the DISA
**Cisco ASA NDM STIG** (`CASA-ND-XXXXXX`) and **Cisco ASA Firewall STIG**
(`CASA-FW-XXXXXX`) using the certified **`cisco.asa`** collection over
`network_cli`.

> Confirm the benchmark release in `defaults/main.yml` (`stig_version`) against
> the [DISA STIG library](https://public.cyber.mil/stigs/). The ASA VPN STIG
> (`CASA-VN-*`) is environment-specific and is intentionally left to a separate
> per-tunnel configuration role.

## Why "grab and go"

* Certified `cisco.asa` modules over SSH — no SDK to install.
* **Safe by default**: `apply_changes=false` runs in check mode and emits a
  per-host JSON findings report. Nothing is written until `-e apply_changes=true`.
* Idempotent, `no_log` on secrets, `write memory` handler on change only.

## Quick start

```bash
cd cisco/roles/cisco_asa_stig/playbooks
ansible-galaxy collection install cisco.asa ansible.netcommon ansible.utils
cp inventory.example inventory && $EDITOR inventory

ansible-playbook -i inventory run.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE

cat /tmp/cisco-asa-artifacts/asa-01_asa_stig.json
```

## Controls implemented

| Area | STIG IDs |
|------|----------|
| AAA / fallback | CASA-ND-000190, 000550 |
| Banner | CASA-ND-000100 |
| Password policy | CASA-ND-001440 |
| Idle timeout / sessions | CASA-ND-000160, 000140 |
| SSH / keys | CASA-ND-001130, 001150 |
| Management ACL | CASA-ND-001550 |
| HTTP server | CASA-ND-001310 |
| Logging | CASA-ND-000610, 000620 |
| NTP | CASA-ND-001200 |
| SNMPv3 only | CASA-ND-001210 |
| Firewall | CASA-FW-000010 (threat detection), 000070 (ACL deny logging) |

## ⚠️ Pre-flight before enforcing

* `crypto key generate rsa` regenerates the SSH host key — existing SSH sessions
  must re-trust the host. Only runs when `apply_changes=true`.
* `no http server enable` disables ASDM/HTTP. Re-enable on a restricted
  interface if you manage via ASDM.
* The `asa_logged_acls` deny-any-any is **appended**; confirm those ACLs already
  contain the required permits before enforcing so you don't black-hole traffic.
* Keep console access during the change window.

## Tags

`--tags ndm`, `auth`, `ssh`, `logging`, `ntp`, `snmp`, `firewall`, `report`,
plus `stig_cat2` / `stig_cat3` and per-rule tags (e.g. `--tags CASA-ND-001210`).

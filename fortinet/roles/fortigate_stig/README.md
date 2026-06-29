# Fortinet FortiGate Firewall STIG (`fortigate_stig`)

Production-ready Ansible role that hardens a **Fortinet FortiGate** firewall to
the DISA **FortiGate Firewall STIG** (`FGFW-ND-*`) via the certified
**`fortinet.fortios`** collection (FortiOS REST API over `httpapi`).

## Why "grab and go"

* Certified `fortinet.fortios` over `httpapi` — supply an API token or admin
  credentials (vaulted).
* **Safe by default**: `apply_changes=false` runs in check mode (reports, no
  change). With `apply_changes=true` the FortiOS config is updated (FortiOS
  persists immediately — no separate commit) and a per-host JSON artifact is
  written.

## Quick start

```bash
cd fortinet/roles/fortigate_stig/playbooks
ansible-galaxy collection install fortinet.fortios
cp inventory.example inventory && $EDITOR inventory

ansible-playbook -i inventory run.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE

cat /tmp/fortigate-stig-artifacts/fgt-01_fortigate_stig.json
```

## Controls implemented

| STIG ID | Control |
|---------|---------|
| FGFW-ND-000026 | Pre/post login DoD banner |
| FGFW-ND-000136 | Admin idle timeout |
| FGFW-ND-000330 | Admin lockout threshold + duration |
| FGFW-ND-000139 | Administrator password policy |
| FGFW-ND-000125 | Admin access restricted by trusted hosts |
| FGFW-ND-000113 / 000150 | Telnet disabled, strong crypto + TLS 1.2 floor |
| FGFW-ND-000114 | Management interface allowed-access restricted |
| FGFW-ND-000350 | NTP configured |
| FGFW-ND-000098 / 000099 | Remote syslog + event logging |
| FGFW-ND-000200 | SNMPv3 only (auth SHA + priv AES) |

## ⚠️ Pre-flight before enforcing

* **Trusted hosts** and the management-interface `allowaccess` restrict admin
  reachability — include the control node's subnet or you can lock yourself out.
* Set `fgt_mgmt_interface` to your real management interface name.
* Use a dedicated VDOM via `fortios_vdom` if not `root`.
* Review the dry-run first.

## Tags

`--tags admin`, `services`, `logging`, `ntp`, `snmp`, `report`, plus
`stig_cat1` / `stig_cat2` and per-rule tags.

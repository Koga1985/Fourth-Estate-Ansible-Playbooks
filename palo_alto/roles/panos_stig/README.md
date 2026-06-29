# Palo Alto PAN-OS NDM STIG (`panos_stig`)

Production-ready Ansible role that hardens a **Palo Alto Networks PAN-OS**
firewall to the DISA **PAN-OS NDM STIG** (`PANW-NM-*`) via the certified
**`paloaltonetworks.panos`** collection (PAN-OS XML API).

## Why "grab and go"

* Certified `paloaltonetworks.panos` over the XML API — supply an API key or
  admin credentials (vaulted).
* **Safe by default**: `apply_changes=false` runs in check mode and makes **no**
  candidate-config change or commit. With `apply_changes=true` the candidate
  config is edited and a commit is issued (commit handler), and a per-host JSON
  artifact is written.

## Quick start

```bash
cd palo_alto/roles/panos_stig/playbooks
ansible-galaxy collection install paloaltonetworks.panos
pip install pan-os-python
cp inventory.example inventory && $EDITOR inventory

ansible-playbook -i inventory run.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE + commit

cat /tmp/panos-stig-artifacts/fw-01_panos_stig.json
```

## Controls implemented

| STIG ID | Control |
|---------|---------|
| PANW-NM-000026 | DoD login banner |
| PANW-NM-000136 / 000330 | Idle timeout + admin lockout |
| PANW-NM-000139 | Administrator password complexity/history/expiration |
| PANW-NM-000113 / 000114 | Telnet and HTTP management disabled |
| PANW-NM-000125 | Management access restricted to authorized subnets (permitted-ip) |
| PANW-NM-000350 | NTP servers configured |
| PANW-NM-000098 / 000099 | Remote syslog profile + config/system log forwarding |
| PANW-NM-000200 | SNMPv3 only (auth SHA + priv AES-128) |

## ⚠️ Pre-flight before enforcing

* `permitted-ip` restricts management access — **include the control node's
  subnet** or you will lock yourself out.
* External AAA (TACACS+/RADIUS) authentication profile (`panos_auth_profile`)
  should already exist; assign it to admins after enforcing.
* Enforcement issues a **commit** — schedule a change window.
* In dry-run, API write tasks are skipped (check mode) so nothing is staged;
  use enforce mode to apply and review the artifact.

## Tags

`--tags admin`, `services`, `logging`, `ntp`, `snmp`, `report`, plus
`stig_cat1` / `stig_cat2` / `stig_cat3` and per-rule tags.

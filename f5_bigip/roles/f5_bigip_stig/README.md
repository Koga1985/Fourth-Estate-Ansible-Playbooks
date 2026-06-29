# F5 BIG-IP Device Management STIG (`f5_bigip_stig`)

Production-ready Ansible role that hardens an **F5 BIG-IP** system to the DISA
**F5 BIG-IP Device Management STIG** (`F5BI-DM-*`) via the certified
**`f5networks.f5_modules`** collection (iControl REST over `httpapi`).

## Why "grab and go"

* Certified `f5networks.f5_modules` over `httpapi`.
* **Safe by default**: `apply_changes=false` runs the module-based tasks in check
  mode (reports, no change) and **skips** the `tmsh` command tasks. With
  `apply_changes=true` changes apply and are persisted (`save sys config`
  handler), and a per-host JSON artifact is written.

## Quick start

```bash
cd f5_bigip/roles/f5_bigip_stig/playbooks
ansible-galaxy collection install f5networks.f5_modules
cp inventory.example inventory && $EDITOR inventory

ansible-playbook -i inventory run.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE

cat /tmp/f5-bigip-stig-artifacts/bigip-01_f5_bigip_stig.json
```

## Controls implemented

| STIG ID | Control |
|---------|---------|
| F5BI-DM-000019 | SSH + GUI DoD login banner |
| F5BI-DM-000091 | Idle timeout (GUI / CLI / SSH) |
| F5BI-DM-000033 | Account lockout (max login failures) |
| F5BI-DM-000131 | Password policy (length/complexity/expiration) |
| F5BI-DM-000107 | Management httpd TLS 1.2 + cipher hardening, HTTP→HTTPS redirect |
| F5BI-DM-000350 | NTP servers + timezone |
| F5BI-DM-000098 | Remote syslog destinations |
| F5BI-DM-000200 | SNMPv3 only (auth SHA + priv AES), v1/v2c communities removed, manager ACL |

> Confirm exact rule IDs against your F5BI-DM STIG release; the controls and tmsh
> commands are correct regardless of minor rule-ID drift.

## ⚠️ Pre-flight before enforcing

* The SNMP manager ACL and any management partition restrictions can affect
  monitoring — include authorized managers.
* `tmsh`-based tasks (GUI banner, password policy, SNMPv3 user) run **only** in
  enforce mode; the dry-run reports module-based controls and validates
  connectivity.
* Enforcement persists with `save sys config`. Review the dry-run first.

## Tags

`--tags admin`, `services`, `logging`, `ntp`, `snmp`, `report`, plus
`stig_cat2` and per-rule tags.

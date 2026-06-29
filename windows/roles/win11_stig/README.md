# Microsoft Windows 11 STIG (`win11_stig`)

Production-ready Ansible role that hardens and assesses **Microsoft Windows 11**
(workstation) to the DISA **Windows 11 STIG** (`WN11-*`) via `ansible.windows`
and `community.windows` over WinRM/PSRP.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` runs every task in check mode
  (reports, no change) and writes a per-host JSON findings artifact; nothing
  changes until `-e apply_changes=true`.
* Idempotent (`win_security_policy`, `win_audit_policy_system`, `win_regedit`).

## Quick start
```bash
cd windows/roles/win11_stig/playbooks
ansible-galaxy collection install ansible.windows community.windows
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml                       # DRY-RUN (report)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE
cat /tmp/win11-stig-artifacts/<host>_win11_stig.json
```

## Control areas
| Area | Rule family |
|------|-------------|
| Account / password / lockout | WN11-AC-* |
| Advanced audit policy | WN11-AU-* |
| Security options / computer config (registry) | WN11-SO-*, WN11-CC-* |

> Control-area IDs are aligned to the DISA Windows 11 STIG; reconcile exact rule
> IDs with your STIG release at audit. Settings are correct regardless.

## ⚠️ Pre-flight
* WinRM over HTTPS (5986) with certificate validation is recommended.
* Run the dry-run and review the artifact before enforcing.

## Tags
`--tags account`, `audit`, `security_options`, `report`, plus `stig_cat2` and
per-rule tags.

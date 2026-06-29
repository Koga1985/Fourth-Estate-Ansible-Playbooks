# Windows Server 2019 STIG (`win_server2019_stig`)

Production-ready Ansible role that hardens and assesses **Microsoft Windows
Server 2019** to the DISA **Windows Server 2019 STIG (Ver 3, Rel 2)** (`WN19-*`),
with optional **Active Directory Domain STIG** (`AD.*`) and **Windows DNS STIG**
(`WDNS-*`) controls for hosts that are domain controllers / DNS servers.

Uses the certified `ansible.windows`, `community.windows`, and `microsoft.ad`
collections over WinRM/PSRP.

## Why "grab and go"

* **Safe by default**: `apply_changes=false` runs every task in check mode (and
  the PowerShell-based AD/DNS tasks report drift without changing anything) and
  writes a per-host JSON findings artifact. `-e apply_changes=true` enforces.
* Role-aware: AD and DNS controls run only on hosts flagged
  `win_is_domain_controller` / `win_is_dns_server`.
* Idempotent (`win_security_policy`, `win_audit_policy_system`, `win_regedit`).

## Quick start

```bash
cd windows/roles/win_server2019_stig/playbooks
ansible-galaxy collection install ansible.windows community.windows microsoft.ad
cp inventory.example inventory && $EDITOR inventory   # flag DC/DNS hosts, vault creds

ansible-playbook -i inventory run.yml                       # DRY-RUN (report)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE

cat /tmp/win2019-stig-artifacts/member-01_win2019_stig.json
```

## Control areas

| Area | Rule family |
|------|-------------|
| Account / password / lockout | WN19-AC-000010 … 000100 |
| Advanced audit policy | WN19-AU-000050 … 000440 |
| Security options / computer config | WN19-SO-*, WN19-CC-* |
| Active Directory Domain (DC only) | AD.* (functional level, privileged group review, AD Recycle Bin) |
| Windows DNS (DNS server only) | WDNS-* (secure dynamic updates, event logging, recursion) |

## ⚠️ Pre-flight before enforcing

* WinRM with HTTPS (`5986`) and certificate validation is strongly recommended.
* Account-policy changes on a **domain controller** apply to the **domain**
  password policy — verify values match your domain standard first.
* `win_dns_disable_recursion: true` only on **authoritative-only** servers; it
  will break resolvers used as forwarders.
* AD/DNS tasks require the `ActiveDirectory` / `DnsServer` PowerShell modules
  (present on DC/DNS roles by default).
* Run the dry-run and review the artifact before enforcing.

## Tags

`--tags account`, `audit`, `security_options`, `ad`, `dns`, `report`, plus
`stig_cat2` and per-rule tags (e.g. `--tags WN19-AC-000080`).

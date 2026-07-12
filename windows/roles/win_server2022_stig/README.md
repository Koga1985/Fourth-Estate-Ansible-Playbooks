# Windows Server 2022 STIG (`win_server2022_stig`)

Production-ready Ansible role that hardens and assesses **Microsoft Windows
Server 2022** to the DISA **Windows Server 2022 STIG (Ver 2, Rel 6)** (`WN22-*`),
with optional **Active Directory Domain STIG** (`AD.*`) and **Windows DNS STIG**
(`WDNS-*`) controls for hosts that are domain controllers / DNS servers.

Uses the certified `ansible.windows`, `community.windows`, and `microsoft.ad`
collections over WinRM/PSRP.

## Requirements

- Ansible 2.15+
- Collection: `ansible.windows` (`ansible-galaxy collection install ansible.windows`)
- Collection: `community.windows` (`ansible-galaxy collection install community.windows`)
- Collection: `microsoft.ad` (`ansible-galaxy collection install microsoft.ad`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | Deployment control |
| `artifacts_dir` | `"/tmp/win2022-stig-artifacts"` | No | on the Ansible control node |
| `win_is_domain_controller` | `false` | No | Role flags - set true on the appropriate hosts (use group_vars). |
| `win_is_dns_server` | `false` | No | — |
| `stig_account_policy` | `true` | No | Control-area toggles |
| `stig_audit_policy` | `true` | No | — |
| `stig_security_options` | `true` | No | — |
| `stig_ad_domain` | `"{{ win_is_domain_controller }}"` | No | — |
| `stig_dns_server` | `"{{ win_is_dns_server }}"` | No | — |
| `stig_compliance_report` | `true` | No | — |
| `win_account_policy` | `(see defaults/main.yml)` | No | WN22-AC-* - Account / password / lockout policy (secedit) |
| `win_audit_subcategories` | `(see defaults/main.yml)` | No | WN22-AU-* - Advanced audit policy subcategories (auditpol) Each becomes: AuditPol /set /subcategory:"<name>" /success:enable /failure:enable |
| `win_registry_settings` | `(see defaults/main.yml)` | No | WN22-SO-* / WN22-CC-* - Security options / computer config (registry) |
| `win_legal_notice_text` | `(multi-line text — see defaults/main.yml)` | No | DoD logon legal notice text (WN22-SO-000050) |
| `win_ad_functional_level_min` | `"Win2016"` | No | Active Directory Domain STIG (domain controllers only) AD domain/forest functional level floor |
| `win_dns_secure_dynamic_updates` | `true` | No | Windows DNS STIG (WDNS-*) - DNS servers only WDNS - secure-only dynamic updates |
| `win_dns_log_level_events` | `true` | No | WDNS - event logging |
| `win_dns_disable_recursion` | `false` | No | set true on authoritative-only servers |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Microsoft Windows Server 2022 STIG"` | No | — |
| `stig_version` | `"V2R6"` | No | — |

## Example Playbook

```yaml
- name: Use win_server2022_stig
  hosts: all
  gather_facts: false
  roles:
    - role: win_server2022_stig
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags account`, `audit`, `security_options`, `ad`, `dns`, `report`, plus
`stig_cat2` and per-rule tags (e.g. `--tags WN22-AC-000080`).

## Why "grab and go"

* **Safe by default**: `apply_changes=false` runs every task in check mode (and
  the PowerShell-based AD/DNS tasks report drift without changing anything) and
  writes a per-host JSON findings artifact. `-e apply_changes=true` enforces.
* Role-aware: AD and DNS controls run only on hosts flagged
  `win_is_domain_controller` / `win_is_dns_server`.
* Idempotent (`win_security_policy`, `win_audit_policy_system`, `win_regedit`).

## Quick start

```bash
cd windows/roles/win_server2022_stig/playbooks
ansible-galaxy collection install ansible.windows community.windows microsoft.ad
cp inventory.example inventory && $EDITOR inventory   # flag DC/DNS hosts, vault creds

ansible-playbook -i inventory run.yml                       # DRY-RUN (report)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE

cat /tmp/win2022-stig-artifacts/member-01_win2022_stig.json
```

## Control areas

| Area | Rule family |
|------|-------------|
| Account / password / lockout | WN22-AC-000010 … 000100 |
| Advanced audit policy | WN22-AU-000050 … 000440 |
| Security options / computer config | WN22-SO-*, WN22-CC-* |
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

## License

MIT

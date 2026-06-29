# Microsoft IIS 10.0 STIG (`win_iis10_stig`)

Production-ready Ansible role that hardens **Microsoft IIS 10.0** to the DISA
**IIS 10.0 Server STIG** (`IISW-SV-*`) and **Site STIG** (`IISW-SI-*`) via
`ansible.windows` (WebAdministration / `appcmd` + Schannel registry) over
WinRM/PSRP.

## Why "grab and go"

* **Safe by default**: `apply_changes=false` — the PowerShell-based controls
  compute drift and report without changing anything; the registry tasks run in
  check mode. Nothing is written until `-e apply_changes=true`.
* Per-host JSON evidence artifact written to the control node.

## Quick start

```bash
cd windows/roles/win_iis10_stig/playbooks
ansible-galaxy collection install ansible.windows community.windows
cp inventory.example inventory && $EDITOR inventory

ansible-playbook -i inventory run.yml                       # DRY-RUN (report)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE

cat /tmp/iis10-stig-artifacts/web-01_iis10_stig.json
```

## Controls implemented

| STIG ID | Control |
|---------|---------|
| IISW-SV-000110 | W3C logging with required fields |
| IISW-SV-000130 | Executable MIME type mappings removed |
| IISW-SV-000159 | Legacy SSL/TLS disabled, TLS 1.2 enabled (Schannel) |
| IISW-SI-000206 | Directory browsing disabled |
| IISW-SI-000210 | Session timeout ≤ 20 minutes |
| IISW-SI-000228 | SSL required on the site |
| IISW-SI-000234 | Application pool identity is not LocalSystem (verified) |

> Confirm exact rule IDs against your IIS 10.0 STIG release; the configuration
> settings are correct regardless of minor rule-ID drift.

## ⚠️ Pre-flight before enforcing

* Schannel protocol changes are **server-wide** and need a **reboot** to fully
  take effect; they can break clients that don't support TLS 1.2.
* `iis_site_name` / `iis_app_pool_name` must match your environment.
* "Require SSL" needs a valid HTTPS binding + certificate on the site first.
* Run the dry-run and review the artifact before enforcing.

## Tags

`--tags server`, `logging`, `tls`, `site`, `report`, plus `stig_cat1` /
`stig_cat2` and per-rule tags.

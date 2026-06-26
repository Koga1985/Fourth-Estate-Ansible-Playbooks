# Apache HTTP Server — Web Server SRG (`apache_web_server_srg`)

Production-ready Ansible role that hardens **Apache HTTP Server** to the DISA
**Web Server SRG** (`SRG-APP-*-WSR-*`). Pure `ansible.builtin` — no extra
collections.

## Why "grab and go"

* **Safe by default**: `apply_changes=false` runs in check mode (reports, no
  changes); the hardening drop-in is validated with `apachectl -t` before any
  reload, which only fires on real changes.
* Idempotent template + `replace`/`lineinfile`; per-host JSON findings artifact.

## Quick start

```bash
cd app_web_server/roles/apache_web_server_srg/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE
cat /tmp/apache-srg-artifacts/web01_apache_web_srg.json
```

## Controls implemented

| SRG ID | Control |
|--------|---------|
| SRG-APP-000516-WSR-000174 | Suppress product/version disclosure (`ServerTokens Prod`, `ServerSignature Off`) |
| SRG-APP-000141-WSR-000081 | Disable HTTP TRACE (`TraceEnable Off`) |
| SRG-APP-000001-WSR-000001 | Connection/session limits (Timeout, KeepAlive) |
| SRG-APP-000439-WSR-000156 | TLS protocol + cipher hardening (no SSLv3/TLS1.0/1.1) |
| SRG-APP-000211-WSR-000031 | Directory browsing disabled, autoindex module off |
| SRG-APP-000358-WSR-000063 | Logging level |

## ⚠️ Pre-flight

* Defaults assume **RHEL/EL** paths (`/etc/httpd`). For Debian/Ubuntu set the
  `apache_*` path vars (see `vars.example.yml`).
* The TLS directives apply inside `mod_ssl`; ensure your vhosts reference valid
  certificates. Review the dry-run artifact before enforcing.

## Tags

`--tags apache`, `report`, `stig_cat2`, and per-rule SRG IDs.

# Splunk Enterprise STIG (`splunk_enterprise_stig`)

Hardens and assesses **Splunk Enterprise** to the DISA STIG (`SPLK-CL-*`) by
managing `$SPLUNK_HOME/etc/system/local/*.conf` with
**`community.general.ini_file`**.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` runs `ini_file` in check mode
  (reports the diff, no write, no restart). `apply_changes=true` writes the conf
  files and restarts Splunk (handler).
* Per-host JSON evidence artifact.

## Quick start
```bash
cd splunk/roles/splunk_enterprise_stig/playbooks
ansible-galaxy collection install community.general
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml                       # DRY-RUN (report)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE (+restart)
cat /tmp/splunk-stig-artifacts/splunk-01_splunk_stig.json
```

## Controls
| STIG ID | Control |
|---------|---------|
| SPLK-CL-000070 | Splunk Web TLS (`enableSplunkWebSSL`), session/inactivity timeout, DoD login banner |
| SPLK-CL-000090 | splunkd TLS 1.2 + approved ciphers (`server.conf [sslConfig]`) |
| SPLK-CL-000400 | Password/lockout policy (`server.conf [general]`) |

External authentication (LDAP/SAML), RBAC roles, and remote audit forwarding are
flagged as operator follow-ups in the artifact.

## ⚠️ Pre-flight
* Changes require a **Splunk restart** (handler) — schedule a window.
* TLS for Splunk Web/`splunkd` requires valid certificates configured in
  `web.conf`/`server.conf`.

## Tags
`--tags web`, `ssl`, `policy`, `report`, `stig_cat2`.

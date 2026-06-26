# Apache Tomcat — Application Server SRG (`tomcat_app_server_srg`)

Production-ready Ansible role that hardens **Apache Tomcat** to the DISA
**Application Server SRG (Ver 4, Rel 4)** (`SRG-APP-*-AS-*`). Uses
`community.general.xml` for idempotent `server.xml` / `web.xml` edits.

## Why "grab and go"

* **Safe by default**: `apply_changes=false` runs in check mode and assesses
  default-webapp presence; nothing changes until `-e apply_changes=true`.
* Idempotent XML attribute/text sets; restart handler fires only on change.

## Quick start

```bash
cd app_web_server/roles/tomcat_app_server_srg/playbooks
ansible-galaxy collection install community.general
cp inventory.example inventory && $EDITOR inventory   # set tomcat_home etc.
ansible-playbook -i inventory run.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE
cat /tmp/tomcat-srg-artifacts/app01_tomcat_app_srg.json
```

## Controls implemented

| SRG ID | Control |
|--------|---------|
| SRG-APP-000142-AS-000014 | Disable shutdown port (`Server port="-1"`) |
| SRG-APP-000439-AS-000155 | TLS protocols on SSL connectors |
| SRG-APP-000295-AS-000263 | Default session timeout (15 min) |
| SRG-APP-000211-AS-000146 | Remove default/example webapps (docs, examples, ROOT, host-manager) |
| SRG-APP-000141-AS-000095 | Run as dedicated non-root account (verified) |

## ⚠️ Pre-flight

* Set `tomcat_home`/`tomcat_service_name`/`tomcat_run_user` for your install.
* The TLS connector task only updates connectors already marked
  `SSLEnabled="true"`; create the HTTPS connector first if you don't have one.
* `manager`/`host-manager` are not removed unless you add them to
  `tomcat_remove_default_webapps` — remove if unused.
* Review the dry-run artifact before enforcing; changes trigger a Tomcat restart.

## Tags

`--tags tomcat`, `report`, `stig_cat2`, and per-rule SRG IDs.

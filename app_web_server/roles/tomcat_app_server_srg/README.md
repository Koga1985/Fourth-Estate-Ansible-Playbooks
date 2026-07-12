# Apache Tomcat — Application Server SRG (`tomcat_app_server_srg`)

Production-ready Ansible role that hardens **Apache Tomcat** to the DISA
**Application Server SRG (Ver 4, Rel 4)** (`SRG-APP-*-AS-*`). Uses
`community.general.xml` for idempotent `server.xml` / `web.xml` edits.

## Requirements

- Ansible 2.15+
- Collection: `community.general` (`ansible-galaxy collection install community.general`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | Deployment control |
| `artifacts_dir` | `"/tmp/tomcat-srg-artifacts"` | No | — |
| `tomcat_home` | `/opt/tomcat` | No | Tomcat paths (override per install) |
| `tomcat_conf_dir` | `"{{ tomcat_home }}/conf"` | No | — |
| `tomcat_server_xml` | `"{{ tomcat_conf_dir }}/server.xml"` | No | — |
| `tomcat_web_xml` | `"{{ tomcat_conf_dir }}/web.xml"` | No | — |
| `tomcat_webapps_dir` | `"{{ tomcat_home }}/webapps"` | No | — |
| `tomcat_service_name` | `tomcat` | No | — |
| `tomcat_run_user` | `tomcat` | No | — |
| `stig_tomcat_hardening` | `true` | No | Control toggles |
| `stig_compliance_report` | `true` | No | — |
| `tomcat_disable_shutdown_port` | `true` | No | Application Server SRG settings SRG-APP-000142-AS-000014 - disable the shutdown port (-1) |
| `tomcat_remove_default_webapps` | `(see defaults/main.yml)` | No | SRG-APP-000211-AS-000146 - remove default/example web applications |
| `tomcat_session_timeout` | `15` | No | 'manager' intentionally NOT removed by default - remove if unused: - manager SRG-APP-000295-AS-000263 - session timeout (minutes) |
| `tomcat_ssl_enabled_protocols` | `"TLSv1.2+TLSv1.3"` | No | SRG-APP-000439-AS-000155 - TLS protocols on SSL connectors |
| `tomcat_error_report_show_report` | `"false"` | No | SRG-APP-000266-AS-000168 - suppress error detail / version (ErrorReportValve) |
| `tomcat_error_report_show_server_info` | `"false"` | No | — |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Application Server SRG (Apache Tomcat)"` | No | — |
| `stig_version` | `"V4R4"` | No | — |

## Example Playbook

```yaml
- name: Use tomcat_app_server_srg
  hosts: all
  gather_facts: false
  roles:
    - role: tomcat_app_server_srg
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags tomcat`, `report`, `stig_cat2`, and per-rule SRG IDs.

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

## License

MIT

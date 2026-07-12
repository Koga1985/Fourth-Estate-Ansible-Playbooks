# Apache HTTP Server — Web Server SRG (`apache_web_server_srg`)

Production-ready Ansible role that hardens **Apache HTTP Server** to the DISA
**Web Server SRG** (`SRG-APP-*-WSR-*`). Pure `ansible.builtin` — no extra
collections.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | Deployment control |
| `artifacts_dir` | `"/tmp/apache-srg-artifacts"` | No | — |
| `apache_service_name` | `httpd` | No | Apache paths (RHEL/EL defaults; override for Debian/SUSE) |
| `apache_conf_dir` | `/etc/httpd/conf.d` | No | — |
| `apache_main_conf` | `/etc/httpd/conf/httpd.conf` | No | — |
| `apache_hardening_conf` | `/etc/httpd/conf.d/00-srg-hardening.conf` | No | — |
| `apache_run_user` | `apache` | No | — |
| `apache_run_group` | `apache` | No | — |
| `stig_apache_hardening` | `true` | No | Control toggles |
| `stig_compliance_report` | `true` | No | — |
| `apache_server_tokens` | `"Prod"` | No | Web Server SRG settings SRG-APP-000516-WSR-000174 - hide product/version info |
| `apache_server_signature` | `"Off"` | No | — |
| `apache_trace_enable` | `"Off"` | No | SRG-APP-000141-WSR-000081 - disable HTTP TRACE |
| `apache_timeout` | `10` | No | SRG-APP-000001-WSR-000001 - session/connection limits |
| `apache_keepalive` | `"On"` | No | — |
| `apache_keepalive_timeout` | `5` | No | — |
| `apache_max_keepalive_requests` | `100` | No | — |
| `apache_ssl_protocol` | `"all -SSLv3 -TLSv1 -TLSv1.1"` | No | SRG-APP-000439-WSR-000156 - TLS only, strong protocols/ciphers |
| `apache_ssl_cipher_suite` | `"HIGH:!aNULL:!MD5:!3DES:!RC4"` | No | — |
| `apache_ssl_honor_cipher_order` | `"On"` | No | — |
| `apache_error_log` | `"logs/error_log"` | No | SRG-APP-000266-WSR-000159 - custom error pages (suppress detailed errors) |
| `apache_log_level` | `"warn"` | No | — |
| `apache_custom_log_format` | `'combined'` | No | — |
| `apache_disable_indexes` | `true` | No | SRG-APP-000211-WSR-000031 - directory browsing disabled |
| `apache_disable_modules` | `(see defaults/main.yml)` | No | Modules that must NOT be loaded (information disclosure / unused) |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Web Server SRG (Apache HTTP Server)"` | No | — |
| `stig_version` | `"V3R1"` | No | — |

## Example Playbook

```yaml
- name: Use apache_web_server_srg
  hosts: all
  gather_facts: false
  roles:
    - role: apache_web_server_srg
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags apache`, `report`, `stig_cat2`, and per-rule SRG IDs.

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

## License

MIT

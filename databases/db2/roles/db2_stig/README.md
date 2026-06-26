# IBM DB2 V10.5 STIG (`db2_stig`)

Production-ready Ansible role that assesses and hardens **IBM DB2 V10.5 (LUW)**
to the DISA **IBM DB2 V10.5 STIG (Ver 2, Rel 1)** (`DB2X-00-XXXXXX`). It runs on
the DB2 server, becomes the instance owner, sources `db2profile`, and applies
controls through the DB2 CLP (`dbm cfg`, `db cfg`), `db2audit`, and SQL.

> No certified DB2 Ansible module exists; the supported way to apply these
> controls is the DB2 CLP run as the instance owner, which is exactly what this
> role does. Confirm the benchmark release in `defaults/main.yml`.

## Why "grab and go"

* No extra collections — pure SSH + `become` to the instance owner.
* **Safe by default**: `apply_changes=false` only runs `db2 get dbm/db cfg` and
  `db2audit describe` (read-only) and writes a JSON drift report. Nothing is
  changed until `-e apply_changes=true`.
* Drift-aware: configuration is applied only where the current value differs, so
  reruns are idempotent.

## Quick start

```bash
cd databases/db2/roles/db2_stig/playbooks
cp inventory.example inventory && $EDITOR inventory   # set instance/db + vault creds

# DRY-RUN (assessment) — writes the drift report
ansible-playbook -i inventory run.yml

# ENFORCE
ansible-playbook -i inventory run.yml -e apply_changes=true -e @vars.example.yml

cat /tmp/db2-stig-artifacts/db2-prod-01_db2_stig.json
```

## Controls implemented

| Area | STIG IDs |
|------|----------|
| Instance auth (dbm cfg) | DB2X-00-000700 (AUTHENTICATION SERVER_ENCRYPT), 000800 (TRUST_*), 001100 (CATALOG_NOAUTH), 001700 (DIAGLEVEL) |
| Database (db cfg) | DB2X-00-001300 (archival logging), 001600 (native encryption / data-at-rest) |
| Audit | DB2X-00-0007xx (`db2audit` categories, fail-closed on audit error) |
| Privileges | Revoke BINDADD/CONNECT/CREATETAB/IMPLICIT_SCHEMA/DBADM from PUBLIC |
| Transmission | DB2X-00-0014xx (SSL/TLS — labels, keystore, TLSv1.2, DB2COMM) |

## ⚠️ Pre-flight before enforcing

* Several `dbm cfg` and all SSL changes require a **DB2 instance restart**
  (handled by the `restart db2 instance` handler) — schedule a window.
* `ENCRLIB`/native encryption requires the instance to be licensed and the
  keystore configured; otherwise drop those keys from `db2_db_cfg`.
* SSL requires a populated GSKit keystore at `db2_ssl_svr_keydb` with the
  `db2_ssl_svr_label` certificate — create it before enabling.
* PUBLIC revokes need `db2_connect_password` (vaulted); they are skipped in
  dry-run.
* Always review the dry-run drift report before enforcing on production.

## Tags

`--tags dbm_cfg`, `db_cfg`, `audit`, `privileges`, `ssl`, `report`.

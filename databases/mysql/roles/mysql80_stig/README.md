# MySQL 8.0 STIG (`mysql80_stig`)

Hardens and assesses **Oracle MySQL 8.0** to the DISA STIG via the certified
**`community.mysql`** collection.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` only *reads* current GLOBAL values
  and reports; nothing changes until `-e apply_changes=true`.
* Dynamic GLOBAL variables are set at runtime; static settings are written to a
  `my.cnf` STIG drop-in (flagged as needing a `mysqld` restart).

## Quick start
```bash
cd databases/mysql/roles/mysql80_stig/playbooks
ansible-galaxy collection install community.mysql
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/mysql80-stig-artifacts/mysql-01_mysql80_stig.json
```

## Controls
`require_secure_transport=ON` (force TLS), `local_infile=OFF`, general log off
(use audit plugin), strict `sql_mode`, `caching_sha2_password`, `secure_file_priv`,
`skip_symbolic_links`, error logging. The role flags MySQL Enterprise Audit and
the `validate_password` component (min length 15) as operator follow-ups.

## ⚠️ Pre-flight
* Static settings in the drop-in require a **mysqld restart** — schedule a window.
* `require_secure_transport=ON` forces TLS — ensure clients present certificates.

## Tags
`--tags variables`, `static`, `report`, `stig_cat2`.

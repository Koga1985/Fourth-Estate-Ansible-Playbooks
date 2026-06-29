# PostgreSQL STIG (`postgresql_stig`)

Hardens and assesses **PostgreSQL** (Crunchy Data benchmark) to the DISA STIG
(`PGS9-00-*`) via the certified **`community.postgresql`** collection.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` runs `postgresql_set` in check mode
  (reports drift, changes nothing) and writes a per-host JSON artifact; nothing
  changes until `-e apply_changes=true`.
* Drift- and restart-aware (the artifact lists parameters needing a restart).

## Quick start
```bash
cd databases/postgresql/roles/postgresql_stig/playbooks
ansible-galaxy collection install community.postgresql
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/postgresql-stig-artifacts/pg-01_postgresql_stig.json
```

## Controls
Server parameters (SSL on, `scram-sha-256` password encryption, logging
collector/destination, `log_connections`/`log_disconnections`,
`log_line_prefix`, `log_statement=ddl`), plus a `pg_hba.conf` assessment for
`trust` authentication (PGS9-00-008600). Confirm exact rule IDs against your STIG
release; `pgaudit` and `pg_hba.conf` remediation are operator follow-ups noted in
the artifact.

## ⚠️ Pre-flight
* Some parameters require a **reload or restart** (listed under `restart_required`
  in the artifact) — schedule a window.
* `pg_hba.conf` `trust` rules are reported, not auto-edited — fix them manually.

## Tags
`--tags parameters`, `report`, `stig_cat1`, `stig_cat2`.

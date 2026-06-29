# Microsoft SQL Server STIG (`mssql_stig`)

Hardens and assesses **Microsoft SQL Server** to the DISA **SQL Server 2016
Instance STIG** (`SQL6-D0-*`) — the latest published SQL Server benchmark,
applicable to later versions — via **`community.general.mssql_script`**.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` only reads `sys.configurations`
  (assessment) and writes a per-host JSON artifact; nothing changes until
  `-e apply_changes=true`.

## Quick start
```bash
cd databases/mssql/roles/mssql_stig/playbooks
ansible-galaxy collection install community.general
pip install pymssql
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/mssql-stig-artifacts/mssql-01_mssql_stig.json
```

## Controls
Surface-area `sp_configure` settings disabled per STIG: `clr enabled`,
`xp_cmdshell`, `Ole Automation Procedures`, `remote access`,
`cross db ownership chaining`, `Ad Hoc Distributed Queries`,
`scan for startup procs`, `remote admin connections`. The role flags SQL Server
Audit (login auditing) and Force Encryption / AD authentication as operator
follow-ups.

## ⚠️ Pre-flight
* Requires `pymssql` on the runner and a login with `ALTER SETTINGS` rights.
* Audit configuration and TLS/Force-Encryption are environment-specific and are
  reported as follow-ups rather than auto-applied.

## Tags
`--tags assess`, `configure`, `report`, `stig_cat2`.

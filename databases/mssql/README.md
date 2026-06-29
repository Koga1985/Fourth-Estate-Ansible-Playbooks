# Microsoft SQL Server

Ansible automation for Microsoft SQL Server security compliance.

## Roles

| Role | Purpose |
|------|---------|
| [`mssql_stig`](roles/mssql_stig/) | SQL Server DISA STIG (SQL6-D0-*) hardening + assessment via `community.general.mssql_script`. |

**Safe by default** (assessment) until you pass `-e apply_changes=true`.

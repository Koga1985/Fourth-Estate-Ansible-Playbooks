# IBM DB2

Ansible automation for IBM DB2 (LUW) security compliance.

## Roles

| Role | Purpose |
|------|---------|
| [`db2_stig`](roles/db2_stig/) | IBM DB2 V10.5 DISA STIG (V2R1) hardening + assessment (`DB2X-00-*`). |

See [`roles/db2_stig/README.md`](roles/db2_stig/README.md) for the grab-and-go
quick start. The role is **safe by default** (assessment only) until you pass
`-e apply_changes=true`.

# MongoDB

Ansible automation for MongoDB security compliance.

## Roles

| Role | Purpose |
|------|---------|
| [`mongodb_stig`](roles/mongodb_stig/) | MongoDB Enterprise DISA STIG hardening + assessment (`mongod.conf`). |

**Safe by default** (renders config + shows diff, no write/restart) until you
pass `-e apply_changes=true`.

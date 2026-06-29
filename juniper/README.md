# Juniper

Ansible automation for Juniper Junos security compliance.

## Roles

| Role | Purpose |
|------|---------|
| [`junos_stig`](roles/junos_stig/) | Juniper Junos DISA STIG (NDM `JUNI-ND-*` + Router `JUNI-RT-*`) hardening + assessment. |

**Safe by default**: `apply_changes=false` loads the candidate config and shows
the diff but does not commit. Pass `-e apply_changes=true` to commit.

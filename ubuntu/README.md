# Canonical Ubuntu

Ansible automation for Ubuntu LTS security compliance.

## Roles

| Role | Purpose |
|------|---------|
| [`ubuntu2204_stig`](roles/ubuntu2204_stig/) | Ubuntu 22.04 LTS DISA STIG (`UBTU-22-*`) hardening + assessment. |

See [`roles/ubuntu2204_stig/README.md`](roles/ubuntu2204_stig/README.md) for the
grab-and-go quick start. **Safe by default** (assessment / check mode) until you
pass `-e apply_changes=true`.

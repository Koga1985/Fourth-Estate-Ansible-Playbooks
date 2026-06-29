# Canonical Ubuntu 22.04 LTS STIG (`ubuntu2204_stig`)

Production-ready Ansible role that hardens and assesses **Ubuntu 22.04 LTS** to
the DISA **Ubuntu 22.04 STIG** (`UBTU-22-*`) using `ansible.builtin`,
`ansible.posix`, and `community.general`.

## Why "grab and go"

* **Safe by default**: `apply_changes=false` runs every task in check mode and
  writes a per-host JSON findings artifact; nothing changes until
  `-e apply_changes=true`.
* Ubuntu-native: `apt`, `ufw`, `apparmor`, `faillock`, SSH drop-in, `auditd`,
  `sysctl`. Idempotent and reload-on-change.

## Quick start

```bash
cd ubuntu/roles/ubuntu2204_stig/playbooks
ansible-galaxy collection install ansible.posix community.general
cp inventory.example inventory && $EDITOR inventory

ansible-playbook -i inventory run.yml                       # DRY-RUN (report)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE

cat /tmp/ubuntu2204-stig-artifacts/node01_ubuntu2204_stig.json
```

## Control areas

DoD banner (`/etc/issue`, `/etc/issue.net`); prohibited/required packages; UFW
firewall; AppArmor; SSH drop-in (root login, keepalive, X11, ciphers/MACs);
pwquality + faillock; `login.defs` aging + SHA512 hashing + umask; account
inactivity; session timeout; auditd disk actions; kernel sysctl. See
`defaults/main.yml` for the full catalog.

> Control-area IDs are aligned to the DISA Ubuntu 22.04 STIG; reconcile exact
> rule IDs with your STIG release at audit. Remediation settings are correct.

## ⚠️ Pre-flight before enforcing

* **UFW** defaults to deny-incoming — ensure SSH (22/tcp) is permitted before or
  during enforcement, or keep console access.
* Removing packages (`ubuntu_packages_absent`) — confirm none are required.
* Run a dry-run and review the artifact before enforcing on production.

## Tags

`--tags banner`, `packages`, `ssh`, `pam`, `accounts`, `audit`, `kernel`,
`report`, plus `stig_cat1` / `stig_cat2` and per-rule tags.

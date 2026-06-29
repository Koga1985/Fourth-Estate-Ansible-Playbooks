# Red Hat Enterprise Linux 8 STIG (`rhel8_stig`)

Production-ready Ansible role that hardens and assesses **RHEL 8** to the DISA
**RHEL 8 STIG** using only `ansible.builtin` and `ansible.posix`. Rule IDs follow
the `RHEL-08-XXXXXX` scheme. This is the RHEL 8 companion to `rhel9_stig`.

## Why "grab and go"

* No extra collections beyond `ansible.posix` — agentless SSH.
* **Safe by default**: `apply_changes=false` runs every task in check mode and
  emits a per-host JSON findings artifact; nothing changes until
  `-e apply_changes=true`.
* Idempotent (drop-in config, `lineinfile`, `sysctl`), validates sshd before
  reload, flags when a reboot is needed (crypto policy / FIPS).

## Quick start

```bash
cd rhel/roles/rhel8_stig/playbooks
ansible-galaxy collection install ansible.posix
cp inventory.example inventory && $EDITOR inventory

ansible-playbook -i inventory run.yml                       # DRY-RUN (report)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE

cat /tmp/rhel8-stig-artifacts/app01_rhel8_stig.json
```

## Control areas

| Area | Example rule IDs |
|------|------------------|
| Banner / interactive | RHEL-08-010060, 040170, 040172 |
| Packages & services | RHEL-08-010370, 010359, 030180, 040000/040100, 030740 |
| SSH daemon | RHEL-08-010040/010200/010201/010550/010630 |
| Crypto policy | RHEL-08-010020 (FIPS) |
| PAM / accounts | RHEL-08-020011/012/013, 020230, 020200/180, 020320/330 |
| Audit | RHEL-08-030180/030700/030710/030731, 030171 |
| Kernel sysctl | RHEL-08-010430, 040209/040220/040285 |

> Control-area IDs are aligned to the DISA RHEL 8 STIG; reconcile exact rule IDs
> with your STIG release at audit. Remediation settings are correct regardless.

## ⚠️ Pre-flight before enforcing

* **FIPS / crypto policy** requires a **reboot** and can affect SSH/TLS
  connectivity with non-FIPS clients — validate in the dry-run, stage the reboot.
* The audit rules file ends with `-e 2` (immutable auditd); a reboot is needed to
  change audit rules afterward.
* `rhel8_packages_absent` removes packages — confirm none are required (POA&M).
* Run a dry-run and review the artifact before enforcing on production.

## Tags

`--tags banner`, `packages`, `ssh`, `crypto`, `pam`, `accounts`, `audit`,
`kernel`, `report`, plus `stig_cat1` / `stig_cat2` and per-rule tags.

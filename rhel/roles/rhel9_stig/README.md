# Red Hat Enterprise Linux 9 STIG (`rhel9_stig`)

Production-ready Ansible role that hardens and assesses **RHEL 9** to the DISA
**RHEL 9 STIG (Ver 2, Rel 6)** using only `ansible.builtin` and `ansible.posix`.
Rule IDs follow the modern `RHEL-09-XXXXXX` scheme.

> This is the RHEL 9 companion to the existing `rhel-hardening` role (which
> targets RHEL 8 / V1R14). Confirm the benchmark release in `defaults/main.yml`
> (`stig_version`) against the [DISA STIG library](https://public.cyber.mil/stigs/).

## Why "grab and go"

* No extra collections beyond `ansible.posix` — pure agentless SSH.
* **Safe by default**: `apply_changes=false` runs every task in check mode and
  emits a per-host JSON findings artifact; nothing is changed until
  `-e apply_changes=true`.
* Idempotent (drop-in config files, `lineinfile`, `sysctl`), validates sshd
  syntax before reload, and flags when a reboot is required (crypto policy/FIPS).

## Quick start

```bash
cd rhel/roles/rhel9_stig/playbooks
ansible-galaxy collection install ansible.posix
cp inventory.example inventory && $EDITOR inventory

# DRY-RUN (assessment) — writes the findings artifact, changes nothing
ansible-playbook -i inventory run.yml

# ENFORCE
ansible-playbook -i inventory run.yml -e apply_changes=true

cat /tmp/rhel9-stig-artifacts/web01_rhel9_stig.json
```

## Control areas

| Area | Example rule IDs |
|------|------------------|
| Banner / interactive | RHEL-09-211010, 211045, 211050 |
| Packages & services | RHEL-09-212010, 214xxx, 215xxx, 251010, 252010 |
| SSH daemon | RHEL-09-255030/035/040/045/065/090/100/105/110/120 |
| Crypto policy | RHEL-09-672010 (FIPS) |
| PAM / accounts | RHEL-09-611045/055/080/085/150, 411010/015/035, 412025/035 |
| Audit | RHEL-09-653010/025/080/085, 654010 |
| Kernel sysctl | RHEL-09-213095, 253020/080, 254010/015 |

## ⚠️ Pre-flight before enforcing

* **FIPS / crypto policy** (`rhel9_crypto_policy: FIPS`) requires a **reboot**
  and can affect SSH/TLS connectivity if your clients don't support FIPS
  ciphers — validate in the dry-run first, and stage the reboot.
* The audit rules file ends with `-e 2` (immutable auditd) — a reboot is needed
  to change audit rules afterward. Remove that line if you need runtime edits.
* `rhel9_packages_absent` removes packages — confirm none are required and
  record a POA&M for any you must keep.
* Run a **dry-run** and review the JSON artifact before enforcing on production.

## Tags

`--tags banner`, `packages`, `ssh`, `crypto`, `pam`, `accounts`, `audit`,
`kernel`, `report`, plus `stig_cat1` / `stig_cat2` and per-rule tags
(e.g. `--tags RHEL-09-255040`).

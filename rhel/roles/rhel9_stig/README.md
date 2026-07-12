# Red Hat Enterprise Linux 9 STIG (`rhel9_stig`)

Production-ready Ansible role that hardens and assesses **RHEL 9** to the DISA
**RHEL 9 STIG (Ver 2, Rel 6)** using only `ansible.builtin` and `ansible.posix`.
Rule IDs follow the modern `RHEL-09-XXXXXX` scheme.

> This is the RHEL 9 companion to the existing `rhel-hardening` role (which
> targets RHEL 8 / V1R14). Confirm the benchmark release in `defaults/main.yml`
> (`stig_version`) against the [DISA STIG library](https://public.cyber.mil/stigs/).

## Requirements

- Ansible 2.15+
- Collection: `ansible.posix` (`ansible-galaxy collection install ansible.posix`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | Deployment control |
| `artifacts_dir` | `"/tmp/rhel9-stig-artifacts"` | No | — |
| `stig_banner_login` | `true` | No | Control-area toggles |
| `stig_packages_services` | `true` | No | — |
| `stig_sshd` | `true` | No | — |
| `stig_crypto_policy` | `true` | No | — |
| `stig_accounts_pam` | `true` | No | — |
| `stig_auditd` | `true` | No | — |
| `stig_kernel_sysctl` | `true` | No | — |
| `stig_compliance_report` | `true` | No | — |
| `rhel9_sshd_dropin` | `/etc/ssh/sshd_config.d/00-stig.conf` | No | RHEL-09-255xxx - SSH daemon (written to a STIG drop-in) |
| `rhel9_ssh_permit_root_login` | `"no"` | No | RHEL-09-255035 |
| `rhel9_ssh_client_alive_interval` | `600` | No | RHEL-09-255040 |
| `rhel9_ssh_client_alive_count_max` | `1` | No | RHEL-09-255045 |
| `rhel9_ssh_x11_forwarding` | `"no"` | No | RHEL-09-255065 |
| `rhel9_ssh_permit_empty_passwords` | `"no"` | No | RHEL-09-255090 |
| `rhel9_ssh_print_last_log` | `"yes"` | No | RHEL-09-255100 |
| `rhel9_ssh_ignore_rhosts` | `"yes"` | No | RHEL-09-255105 |
| `rhel9_ssh_gss_api_auth` | `"no"` | No | RHEL-09-255110 |
| `rhel9_ssh_banner` | `/etc/issue` | No | RHEL-09-255030 |
| `rhel9_dod_banner` | `(multi-line text — see defaults/main.yml)` | No | RHEL-09-211xxx - Banner / interactive |
| `rhel9_packages_absent` | `(see defaults/main.yml)` | No | RHEL-09-215xxx - Packages that must NOT be installed |
| `rhel9_packages_present` | `(see defaults/main.yml)` | No | RHEL-09-214xxx - Packages that MUST be installed |
| `rhel9_crypto_policy` | `"FIPS"` | No | RHEL-09-672xxx - System-wide crypto policy FIPS \| DEFAULT:NO-SHA1 \| etc. |
| `rhel9_pwquality` | `(see defaults/main.yml)` | No | RHEL-09-611xxx - PAM password quality / faillock |
| `rhel9_pwhistory_remember` | `5` | No | RHEL-09-611150 |
| `rhel9_faillock` | `(see defaults/main.yml)` | No | — |
| `rhel9_pass_max_days` | `60` | No | RHEL-09-411xxx / 412xxx - login.defs / account policy RHEL-09-411010 |
| `rhel9_pass_min_days` | `1` | No | RHEL-09-411015 |
| `rhel9_pass_warn_age` | `7` | No | — |
| `rhel9_account_inactive_days` | `35` | No | RHEL-09-412025 |
| `rhel9_session_tmout` | `900` | No | RHEL-09-412035 |
| `rhel9_umask` | `"077"` | No | RHEL-09-411035 |
| `rhel9_auditd_space_left_action` | `email` | No | RHEL-09-653xxx - auditd RHEL-09-653080 |
| `rhel9_auditd_disk_full_action` | `halt` | No | RHEL-09-653085 |
| `rhel9_auditd_max_log_file_action` | `syslog` | No | RHEL-09-653025 |
| `rhel9_sysctl` | `(see defaults/main.yml)` | No | RHEL-09-2xxxxx - Kernel sysctl hardening |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Red Hat Enterprise Linux 9 STIG"` | No | — |
| `stig_version` | `"V2R6"` | No | — |

## Example Playbook

```yaml
- name: Use rhel9_stig
  hosts: all
  gather_facts: false
  roles:
    - role: rhel9_stig
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags banner`, `packages`, `ssh`, `crypto`, `pam`, `accounts`, `audit`,
`kernel`, `report`, plus `stig_cat1` / `stig_cat2` and per-rule tags
(e.g. `--tags RHEL-09-255040`).

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

## License

MIT

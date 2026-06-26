# IBM z/OS RACF STIG (`zos_racf_stig`)

Assessment + command-reference **skeleton** for the DISA **IBM z/OS RACF STIG**.

> ⚠️ z/OS ESM hardening cannot be safely applied blind. This role does **not**
> change the system. It (1) always generates a STIG checklist (JSON + Markdown)
> with the exact RACF/TSO verify commands and documented remediation — runs
> anywhere, no mainframe needed; and (2) optionally runs the **read-only**
> verify commands against a real LPAR via `ibm.ibm_zos_core` and captures the
> output as evidence. Remediation is performed by the z/OS systems programmer.

## Quick start

```bash
cd ibm_zos/roles/zos_racf_stig/playbooks

# Checklist only (no mainframe) — produces the command reference + remediation
ansible-playbook -i inventory.example run.yml
cat /tmp/zos-racf-stig-artifacts/zos_racf_stig_checklist.md

# Live read-only assessment against an LPAR
ansible-galaxy collection install -r ../../../requirements.yml
ansible-playbook -i inventory.example run.yml \
  -e zos_live_assessment=true -e zos_target=zos-lpar-01
```

## Control areas

SETROPTS password policy, PROTECTALL/ERASE, RACF audit options (SAUDIT/CMDVIOL/
OPERAUDIT/INITSTATS), APF library protection, SYS1.PARMLIB/PROCLIB protection,
SMF security recording, STARTED class, SPECIAL/OPERATIONS/AUDITOR limits, z/OS
UNIX superuser & BPX.SUPERUSER, default UACC, TAPEVOL/TAPEDSN, and RACLISTed
classes. See `defaults/main.yml` for the full catalog with commands.

## Live mode requirements

`ibm.ibm_zos_core` ≥ 1.10, z/OS Open Enterprise Python, ZOAU, and SSH to USS on
the LPAR with an automation user authorized for the (read-only) commands.

## Tags

`--tags report` (checklist), `--tags live` (read-only assessment).

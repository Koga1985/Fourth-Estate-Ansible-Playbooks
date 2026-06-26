# IBM z/OS TSS (CA Top Secret) STIG (`zos_tss_stig`)

Assessment + command-reference **skeleton** for the DISA **IBM z/OS TSS (CA Top Secret) STIG**.

> ⚠️ z/OS hardening cannot be safely applied blind. This role does **not** change
> the system. It (1) always generates a STIG checklist (JSON + Markdown) with the
> exact read-only verify commands and documented remediation — runs anywhere, no
> mainframe needed; and (2) optionally runs the **read-only** verify commands
> against a real LPAR via `ibm.ibm_zos_core` and captures the output as evidence.
> Remediation is performed by the z/OS systems programmer / ESM administrator.

## Quick start

```bash
cd ibm_zos/roles/zos_tss_stig/playbooks

# Checklist only (no mainframe) — command reference + remediation
ansible-playbook -i inventory.example run.yml
cat /tmp/zos-tss-stig-artifacts/zos_tss_stig_checklist.md

# Live read-only assessment against an LPAR
ansible-galaxy collection install -r ../../../requirements.yml
ansible-playbook -i inventory.example run.yml \
  -e zos_live_assessment=true -e zos_target=zos-lpar-01
```

See `defaults/main.yml` for the full control catalog (IDs, severity, verify
command, remediation). Control-area IDs align to the DISA STIG control set;
reconcile with exact V-/rule-IDs in your STIG release at audit time.

## Live mode requirements

`ibm.ibm_zos_core` ≥ 1.10, z/OS Open Enterprise Python, ZOAU, and SSH to USS on
the LPAR with an automation user authorized for the (read-only) commands.

## Tags

`--tags report` (checklist), `--tags live` (read-only assessment).

# IBM z/OS (Mainframe) STIG Assessment

DISA STIG **assessment skeletons** for the IBM z/OS mainframe ecosystem.

> ⚠️ **Read the model first.** z/OS External Security Manager (RACF / CA Top
> Secret) and product hardening **cannot be applied blind** — a wrong command can
> lock out the system. These roles therefore do **not** enforce. Each role:
>
> 1. **Always** generates a STIG checklist (JSON + Markdown) with the exact
>    READ-ONLY verify commands and the documented remediation. This runs on the
>    control node with **no mainframe required** — the grab-and-go deliverable.
> 2. **Optionally** runs the read-only verify commands against a real LPAR via
>    `ibm.ibm_zos_core` (`zos_operator` / `zos_tso_command`) when
>    `zos_live_assessment=true` and `zos_target=<lpar>`, capturing output as
>    evidence for the ATO package.
>
> Remediation is always performed by the z/OS systems programmer / ESM admin
> after review.

## Roles

| Role | Benchmark |
|------|-----------|
| [`zos_racf_stig`](roles/zos_racf_stig/) | IBM z/OS RACF STIG |
| [`zos_tss_stig`](roles/zos_tss_stig/) | IBM z/OS TSS (CA Top Secret) STIG |
| [`zos_cics_tss_stig`](roles/zos_cics_tss_stig/) | IBM z/OS CICS Transaction Server (TSS) STIG (V7R2) |
| [`zos_netview_tss_stig`](roles/zos_netview_tss_stig/) | IBM z/OS NetView for TSS STIG (V7R2) |
| [`zos_tdmf_tss_stig`](roles/zos_tdmf_tss_stig/) | IBM z/OS TDMF for TSS STIG (V7R2) |
| [`zos_zsecure_stig`](roles/zos_zsecure_stig/) | IBM zSecure Suite STIG (V1R3) |

## Quick start (checklist, no mainframe)

```bash
ansible-playbook ibm_zos/roles/zos_racf_stig/playbooks/run.yml
cat /tmp/zos-racf-stig-artifacts/zos_racf_stig_checklist.md
```

## Live assessment

```bash
ansible-galaxy collection install -r ibm_zos/requirements.yml
ansible-playbook ibm_zos/roles/zos_racf_stig/playbooks/run.yml \
  -i ibm_zos/roles/zos_racf_stig/playbooks/inventory.example \
  -e zos_live_assessment=true -e zos_target=zos-lpar-01
```

Live mode requires `ibm.ibm_zos_core` ≥ 1.10, z/OS Open Enterprise Python, ZOAU,
and SSH to USS on the LPAR with an automation user authorized for the
(read-only) commands.

## Why these are skeletons (and not full enforcement)

Unlike the network/Linux/Windows/container roles in this repo, z/OS controls are
applied through ESM commands whose correct values are highly site-specific and
whose misapplication is high-risk. The honest, safe deliverable is an accurate
**assessment + command reference** an authorized sysprog executes — not blind
automation. The verify commands and remediation in each role's `defaults/main.yml`
are real and audit-ready; reconcile control-area IDs with the exact V-/rule-IDs
in your STIG release.

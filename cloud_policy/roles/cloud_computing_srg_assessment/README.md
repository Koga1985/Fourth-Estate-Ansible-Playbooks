# DoD Cloud Computing SRG + SaaS Assessment (`cloud_computing_srg_assessment`)

Production-ready Ansible role implementing the **DoD Cloud Computing SRG** (CC
SRG) and **SaaS** shared-responsibility assessment as a **control-mapping +
evidence generator**. The CC SRG is a policy SRG built on the FedRAMP+ / NIST
800-53 baselines and DoD Impact Levels (IL2/IL4/IL5/IL6) — it is *verified*, not
*configured*.

This role maps each CC SRG / FedRAMP control family to the AWS / Azure / GCP
provider roles in this repository that implement it, aggregates any per-provider
assessment artifacts present, and emits a consolidated JSON + Markdown evidence
package, plus the DoD-specific (Impact Level, FedRAMP authorization, CAP/CSSP)
and SaaS shared-responsibility checklists. Pure `ansible.builtin` — read-only.

## Why "grab and go"

* Runs out of the box on the control node — no cloud credentials needed for the
  mapping/evidence rollup itself.
* **Read-only** — never changes a cloud resource.
* Scope it to the providers and Impact Level you actually use.

## Quick start

```bash
cd cloud_policy/roles/cloud_computing_srg_assessment/playbooks
ansible-playbook run.yml -e @vars.example.yml
cat /tmp/cloud-srg-artifacts/cloud_computing_srg_assessment.md
```

## What it produces

| Section | Content |
|---------|---------|
| Control families | FedRAMP/NIST 800-53 families (AC, AU, CA, CM, CP, IA, IR, RA, SC, SI, SA) mapped to implementing `aws_*` / `azure_*` / `gcp_*` roles, with coverage/gap status |
| DoD CC SRG-specific | Impact Level determination, FedRAMP/PA authorization, data location, CSSP/CND, CAP/BCAP connectivity, continuous monitoring (procedural) |
| SaaS | Shared-responsibility checklist (FedRAMP authorization, customer-responsibility matrix, SSO+MFA, SIEM export, encryption/key ownership, data location/exit, DLP) |

## How evidence is gathered

The role aggregates per-provider artifacts from `cc_evidence_input_dirs` (the
`/tmp/<provider>-artifacts` directories the AWS/Azure/GCP roles write to). Run
those provider roles first for live per-control evidence; the mapping/coverage
view works regardless.

## Related provider roles

`aws/roles/aws_fedramp_compliance`, `azure/roles/azure_fedramp_compliance`,
`azure/roles/azure_nist_compliance`, `azure/roles/azure_compliance`, and the
broader `aws_*` / `azure_*` / `gcp_*` security roles.

## Tags

`--tags assess`, `report`.

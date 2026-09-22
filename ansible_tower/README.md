# Ansible Automation Platform — controller as code

Five roles that declare an Automation Controller's configuration — access, credentials, content, job templates and workflows — as reviewable code rather than as clicks in a web form.

This is the directory named after the platform most customers actually consume this repository through. Every other directory here automates a *target*; this one automates the thing that runs the automation.

## Why this exists

Without it, every organization hand-builds job templates against these playbooks and wires the variables differently. That puts the most error-prone integration step in the environment with the least visibility. Worse, two safeguards this repository relies on are easy to lose in the translation:

- **The dry-run gate.** Every playbook here defaults to `apply_changes: false`. A job template that neither surveys that variable nor sets it in `extra_vars` silently removes the safeguard, because the operator launching it cannot see or choose it.
- **The pinned project.** A project tracking `main` with *Update Revision on Launch* turns every commit in this repository into an immediate change in your control plane.

Both are enforced here as preflight checks, with a documented waiver for the cases where you mean it.

## Roles

| Role | What it declares |
|------|------------------|
| [`aap_controller_organizations`](roles/aap_controller_organizations/README.md) | Organizations, teams, user accounts, role bindings |
| [`aap_controller_credentials`](roles/aap_controller_credentials/README.md) | Custom credential types for the vendor APIs, and credentials |
| [`aap_controller_projects`](roles/aap_controller_projects/README.md) | Projects (pinned), inventories, execution environments |
| [`aap_controller_job_templates`](roles/aap_controller_job_templates/README.md) | Job templates and surveys |
| [`aap_controller_workflows`](roles/aap_controller_workflows/README.md) | Workflow job templates with approval nodes |

## Quick start

```bash
ansible-galaxy collection install -r ansible_tower/requirements.yml

# 1. Dry run. Writes the plans, changes nothing.
ansible-playbook ansible_tower/site.yml \
  -e @ansible_tower/vars/fourth_estate_controller.example.yml \
  -e @group_vars/all/vault.yml --ask-vault-pass

# 2. Read what it would do.
cat /tmp/aap-artifacts/*.json

# 3. Apply it.
ansible-playbook ansible_tower/site.yml \
  -e @ansible_tower/vars/fourth_estate_controller.example.yml \
  -e @group_vars/all/vault.yml --ask-vault-pass \
  -e apply_changes=true
```

[`vars/fourth_estate_controller.example.yml`](vars/fourth_estate_controller.example.yml) is a worked configuration for this repository: real playbook paths, an assess/apply template pair, credential types for the Cisco ISE and Infoblox APIs, and a workflow with an approval node. Copy it, change the names and hosts, and you have a starting configuration rather than a blank page.

## The control worth having

The reason to drive this repository from AAP rather than a shell is the approval node:

```
  assess  ──►  approve  ──►  apply
 (dry run)   (recorded)    (changes)
```

`apply_changes` is the right control at the command line, but it is a variable — an assertion. An approval node is a pause the controller records, together with the person who approved it, in its own audit log. For a DoD STIG or FedRAMP audience that is evidence.

The assess node publishes its findings as job artifacts under `fe_evidence` (see [`VALIDATION_AND_STATS.md`](https://github.com/Koga1985/Fourth-Estate-Ansible-Playbooks/blob/main/docs/VALIDATION_AND_STATS.md#compliance-evidence-delivery)), so the approver reads the evidence in the same place they approve.

## Dry run by default

Every role here writes a plan on every run — including a dry run — and applies nothing until `apply_changes=true`:

| File | Contents |
|------|----------|
| `aap_access_plan.json` | Organizations, teams, users, role bindings |
| `aap_credential_plan.json` | Credential types in full; each credential's shape only |
| `aap_content_plan.json` | Projects, inventories, execution environments |
| `aap_job_template_plan.json` | Job templates, and which carry a survey |
| `aap_workflow_plan.json` | Workflows, and the identifier of every approval node |

Secrets never reach a plan: user passwords and credential `inputs` are dropped before the file is built, not redacted afterwards, and the credential apply task runs under `no_log`.

Under AAP these files do not outlive the job, so each role also publishes them through `set_stats` under `fe_evidence` — the same mechanism the rest of the repository uses for compliance evidence.

## Requirements

- Ansible 2.15+
- `infra.controller_configuration`, which drives both AAP and AWX
- An execution environment image the controller can pull — build one from [`execution_environment/`](../execution_environment/README.md)
- An account on the controller with permission to manage the objects you declare

`ansible.controller` and `ansible.hub` ship only from Red Hat Automation Hub, not community Galaxy; [`requirements.yml`](requirements.yml) carries the repository's `# automation-hub-only:` marker for them.

## What this does not do

It does not install or upgrade the Automation Platform itself. It configures a controller that already exists. Installation is a Red Hat installer workflow, not something to reimplement here.

It also cannot be tested against a live controller from this repository's CI, which has no controller to talk to. What CI does prove is that a dry run completes, writes every plan, and rejects an unpinned project, an ungated job template and a workflow with no approval node. Validate against your own controller in a non-production organization first.

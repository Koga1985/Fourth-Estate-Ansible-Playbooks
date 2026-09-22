# aap_controller_workflows

Declares an Automation Controller's workflow job templates as code, built around the control this repository most wants from AAP: a dry run, a recorded human approval, then the apply.

## Requirements

- Ansible 2.15+
- Collection: `infra.controller_configuration`
- The job templates the workflow nodes reference must already exist — run `aap_controller_job_templates` first
- Runs on `localhost`; no `become` required

## Role Variables

### Safety

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | When false the role writes its plan and changes nothing. |
| `aap_artifacts_dir` | `"/tmp/aap-artifacts"` | No | Where the plan and evidence are written. |
| `aap_allow_workflow_without_approval` | `false` | No | Waives the preflight below. |

### Controller connection

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `aap_controller_host` | `""` | **Yes** | Controller hostname or URL. |
| `aap_controller_username` | `""` | **Yes** | Account used to apply the configuration. |
| `aap_controller_password` | `""` | **Yes** | Supply from Ansible Vault or the controller's credential store. |
| `aap_controller_validate_certs` | `true` | No | Leave true outside a bootstrap. |

### Desired state

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `aap_workflows` | `[]` | No | Workflow job templates. Shape matches `infra.controller_configuration.workflow_job_templates`. |

## Why the approval node is enforced

This repository's own safeguard is `apply_changes`, a variable. That is the right control at the command line, but AAP offers a stronger one: a workflow can pause at an approval node, and the controller records both the decision and the person who made it in its audit log. For a DoD STIG or FedRAMP audience that is evidence; a survey checkbox is an assertion.

The preflight therefore requires each workflow to carry at least one approval node, unless `aap_allow_workflow_without_approval` is set.

## The shape worth copying

```yaml
aap_workflows:
  - name: "RHEL 9 STIG - assess, approve, apply"
    organization: "Fourth Estate"
    simplified_workflow_nodes:
      - identifier: assess
        unified_job_template: "RHEL 9 STIG - assess"
        extra_data:
          apply_changes: false
        success_nodes: [approve]

      - identifier: approve
        approval_node:
          name: "Approve applying the RHEL 9 STIG baseline"
          description: >-
            The assess job above has run. Review its evidence before approving;
            approving applies the baseline to every host in the chosen limit.
          timeout: 86400
        success_nodes: [apply]

      - identifier: apply
        unified_job_template: "RHEL 9 STIG - apply"
        extra_data:
          apply_changes: true
```

The assess node publishes its findings as job artifacts under `fe_evidence` (see [`VALIDATION_AND_STATS.md`](https://github.com/Koga1985/Fourth-Estate-Ansible-Playbooks/blob/main/docs/VALIDATION_AND_STATS.md#compliance-evidence-delivery)), so the approver has the evidence in front of them rather than having to go and find it.

## Example Playbook

```yaml
- name: Declare controller workflows
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: aap_controller_workflows
      vars:
        apply_changes: false
        aap_controller_host: "controller.example.mil"
        aap_controller_username: "{{ vault_aap_username }}"
        aap_controller_password: "{{ vault_aap_password }}"
        aap_workflows: "{{ fourth_estate_workflows }}"
```

## Tags

| Tag | Description |
|-----|-------------|
| `preflight` | The approval-node check |
| `plan` | Build and write the desired-state plan |
| `workflows` | Apply workflow job templates |
| `evidence` | Publish the plan into the job artifacts |

## What is written

`{{ aap_artifacts_dir }}/aap_workflow_plan.json` — the workflows this run would declare, and the identifier of every approval node in them.

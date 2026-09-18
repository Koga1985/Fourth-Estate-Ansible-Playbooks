# aap_controller_job_templates

Declares an Automation Controller's job templates and surveys as code, and refuses to plan a template that hides this repository's dry-run gate from the operator.

## Requirements

- Ansible 2.15+
- Collection: `infra.controller_configuration`
- The projects, inventories, credentials and execution environments the templates reference must already exist — run `aap_controller_projects` and `aap_controller_credentials` first
- Runs on `localhost`; no `become` required

## Role Variables

### Safety

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | When false the role writes its plan and changes nothing. |
| `aap_artifacts_dir` | `"/tmp/aap-artifacts"` | No | Where the plan and evidence are written. |
| `aap_allow_template_without_apply_gate` | `false` | No | Waives the preflight below. |

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
| `aap_job_templates` | `[]` | No | Job templates. Shape matches `infra.controller_configuration.job_templates`. |

## Why the apply gate is enforced

Every playbook in this repository defaults to `apply_changes: false`, so a run is a dry run until someone says otherwise. A job template that neither surveys `apply_changes` nor sets it in `extra_vars` removes that safeguard: the operator launching it cannot see, or choose, whether the run will change anything.

The preflight therefore requires each template to do one or the other, unless `aap_allow_template_without_apply_gate` is set.

## Writing a survey

The flat, defaulted variables this repository uses map onto survey questions almost one to one. Each role's `defaults/main.yml` documents what it takes; the ones worth surveying are the safety gate, the target scope, and anything with no safe default.

```yaml
survey_enabled: true
survey_spec:
  name: "RHEL 9 STIG"
  description: "Assess or apply the RHEL 9 STIG baseline"
  spec:
    - question_name: "Apply changes? Leave false for a dry run."
      variable: apply_changes
      type: multiplechoice
      choices: ["false", "true"]
      default: "false"
      required: true
```

## Example Playbook

```yaml
- name: Declare controller job templates
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: aap_controller_job_templates
      vars:
        apply_changes: false
        aap_controller_host: "controller.example.mil"
        aap_controller_username: "{{ vault_aap_username }}"
        aap_controller_password: "{{ vault_aap_password }}"
        aap_job_templates:
          - name: "RHEL 9 STIG - assess"
            job_type: run
            organization: "Fourth Estate"
            project: "Fourth Estate Playbooks"
            playbook: "rhel/playbooks/compliance-check.yml"
            inventory: "RHEL Servers"
            execution_environment: "Fourth Estate EE"
            ask_limit_on_launch: true
            extra_vars:
              apply_changes: false
```

## Tags

| Tag | Description |
|-----|-------------|
| `preflight` | The apply-gate check |
| `plan` | Build and write the desired-state plan |
| `job_templates` | Apply job templates |
| `evidence` | Publish the plan into the job artifacts |

## What is written

`{{ aap_artifacts_dir }}/aap_job_template_plan.json` — the templates this run would declare, and which of them carry a survey.

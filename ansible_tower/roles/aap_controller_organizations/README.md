# aap_controller_organizations

Declares an Automation Controller's organizations, teams, user accounts and role bindings as code, so who may launch what is reviewable in git rather than clicked into a web form.

## Requirements

- Ansible 2.15+
- Collection: `infra.controller_configuration` (install via `ansible-galaxy collection install -r ansible_tower/requirements.yml`)
- A reachable Automation Controller (AAP) or AWX, and an account with permission to manage organizations
- Runs on `localhost`; no `become` required

## Role Variables

### Safety

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | When false the role writes its plan and changes nothing. Set true to apply. |
| `aap_artifacts_dir` | `"/tmp/aap-artifacts"` | No | Where the plan and evidence are written. Under AAP this path does not outlive the job, so the evidence is also published through `set_stats`. |

### Controller connection

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `aap_controller_host` | `""` | **Yes** | Controller hostname or URL. |
| `aap_controller_username` | `""` | **Yes** | Account used to apply the configuration. |
| `aap_controller_password` | `""` | **Yes** | Supply from the controller's credential store or Ansible Vault; never commit it. |
| `aap_controller_validate_certs` | `true` | No | Leave true. Set false only against a controller still presenting a self-signed certificate. |

### Desired state

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `aap_organizations` | `[]` | No | Organizations to declare. Shape matches `infra.controller_configuration.organizations`. |
| `aap_teams` | `[]` | No | Teams, each scoped to an organization. |
| `aap_users` | `[]` | No | Local user accounts. A `password` key is dropped before the plan is written. Prefer an external identity provider. |
| `aap_roles` | `[]` | No | Role bindings — who may use which templates, projects and inventories. |

## Example Playbook

```yaml
- name: Declare controller access
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: aap_controller_organizations
      vars:
        apply_changes: false        # plan only; set true to apply
        aap_controller_host: "controller.example.mil"
        aap_controller_username: "{{ vault_aap_username }}"
        aap_controller_password: "{{ vault_aap_password }}"
        aap_organizations:
          - name: "Fourth Estate"
            description: "Newsroom infrastructure automation"
        aap_teams:
          - name: "Network Engineering"
            organization: "Fourth Estate"
        aap_roles:
          - team: "Network Engineering"
            organization: "Fourth Estate"
            role: execute
            job_templates:
              - "Cisco ISE - Policy - assess"
```

## Tags

| Tag | Description |
|-----|-------------|
| `plan` | Build and write the desired-state plan; runs in dry run too |
| `organizations` | Apply organizations |
| `teams` | Apply teams |
| `users` | Apply user accounts |
| `rbac` | Apply role bindings |
| `evidence` | Publish the plan into the job artifacts |

## What is written

`{{ aap_artifacts_dir }}/aap_access_plan.json` — the organizations, teams, users and role bindings this run would declare. User passwords are removed before the file is created, so no secret reaches it. The same content is published through `set_stats` under `fe_evidence`, which is what survives an execution-environment container.

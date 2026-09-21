# aap_controller_projects

Declares an Automation Controller's projects, inventories and execution environments as code, and refuses to plan a project that tracks a branch instead of a release tag.

## Requirements

- Ansible 2.15+
- Collection: `infra.controller_configuration`
- A reachable Automation Controller (AAP) or AWX, and an account with permission to manage projects
- An execution environment image the controller can pull — build one from [`execution_environment/`](../../../execution_environment/README.md)
- Runs on `localhost`; no `become` required

## Role Variables

### Safety

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | When false the role writes its plan and changes nothing. |
| `aap_artifacts_dir` | `"/tmp/aap-artifacts"` | No | Where the plan and evidence are written. |
| `aap_allow_branch_tracking` | `false` | No | Waives the preflight that requires every project to be pinned. See [Why pinning is enforced](#why-pinning-is-enforced). |

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
| `aap_projects` | `[]` | No | Projects. `scm_branch` should be a release tag of this repository. |
| `aap_execution_environments` | `[]` | No | Execution environments to register, by image reference. |
| `aap_inventories` | `[]` | No | Inventories. |
| `aap_inventory_sources` | `[]` | No | Inventory sources attached to those inventories. |

## Why pinning is enforced

A project that tracks `main` with *Update Revision on Launch* enabled turns every commit in the content repository into an immediate change in the control plane. The preflight therefore rejects a project whose `scm_branch` is `main`, `master`, `devel` or `development` unless `aap_allow_branch_tracking` is set, which makes accepting that risk a deliberate, reviewable act rather than a default.

Pin to a tag, and review [`CHANGELOG.md`](https://github.com/Koga1985/Fourth-Estate-Ansible-Playbooks/blob/main/docs/CHANGELOG.md) before moving the pin.

## Example Playbook

```yaml
- name: Declare controller content
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: aap_controller_projects
      vars:
        apply_changes: false
        aap_controller_host: "controller.example.mil"
        aap_controller_username: "{{ vault_aap_username }}"
        aap_controller_password: "{{ vault_aap_password }}"
        aap_execution_environments:
          - name: "Fourth Estate EE"
            image: "registry.example.mil/fourth-estate-ee:1.1.0"
            pull: missing
        aap_projects:
          - name: "Fourth Estate Playbooks"
            organization: "Fourth Estate"
            scm_type: git
            scm_url: "https://github.com/Koga1985/Fourth-Estate-Ansible-Playbooks.git"
            scm_branch: "1.1.0"          # a tag, not a branch
            scm_update_on_launch: false
            default_environment: "Fourth Estate EE"
```

## Tags

| Tag | Description |
|-----|-------------|
| `preflight` | The pinning check |
| `plan` | Build and write the desired-state plan |
| `execution_environments` | Register execution environments |
| `projects` | Apply projects |
| `inventories` | Apply inventories and their sources |
| `evidence` | Publish the plan into the job artifacts |

## What is written

`{{ aap_artifacts_dir }}/aap_content_plan.json` — the projects, inventories, inventory sources and execution environments this run would declare.

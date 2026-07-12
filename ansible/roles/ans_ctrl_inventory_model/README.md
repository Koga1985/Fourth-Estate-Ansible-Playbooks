# ans_ctrl_inventory_model

Build orgs/teams, inventories & sources, credentials, projects, EE registries/images.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | — |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `controller_host` | `"{{ lookup('env', 'CONTROLLER_HOST') \| default('https://controller....` | No | — |
| `controller_oauthtoken` | `"{{ lookup('env', 'CONTROLLER_OAUTH_TOKEN') \| default('') }}"` | No | — |
| `inventory_structure` | `(see defaults/main.yml)` | No | Inventory Model |
| `inventory_sources` | `(see defaults/main.yml)` | No | Inventory Sources |
| `fourth_estate_inventory_encryption` | `true` | No | Fourth Estate |

## Example
```yaml
- hosts: localhost
  roles:
    - role: ans_ctrl_inventory_model
      vars:
        apply_changes: true
        organizations: [{ name: Platform }]
        teams: [{ name: NetOps, organization: Platform }]
        inventories: [{ name: Prod, organization: Platform }]
        projects: [{ name: Playbooks, organization: Platform, scm_url: "https://git/repo.git" }]
        registries: [{ name: Harbor, host: harbor.local, username: robot, password: vault_robot }]
        execution_environments: [{ name: ee-netops, image: harbor.local/ee/netops:latest, registry_credential: Harbor }]
```

## License

MIT

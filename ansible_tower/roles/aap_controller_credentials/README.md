# aap_controller_credentials

Declares an Automation Controller's custom credential types and credentials as code, so an operator can launch a job template against a vendor API without ever handling the secret.

## Requirements

- Ansible 2.15+
- Collection: `infra.controller_configuration`
- A reachable Automation Controller (AAP) or AWX, and an account with permission to manage credentials
- Runs on `localhost`; no `become` required

## Role Variables

### Safety

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | When false the role writes its plan and changes nothing. |
| `aap_artifacts_dir` | `"/tmp/aap-artifacts"` | No | Where the plan and evidence are written. |

### Controller connection

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `aap_controller_host` | `""` | **Yes** | Controller hostname or URL. |
| `aap_controller_username` | `""` | **Yes** | Account used to apply the configuration. |
| `aap_controller_password` | `""` | **Yes** | Supply from Ansible Vault or the controller's own credential store. |
| `aap_controller_validate_certs` | `true` | No | Leave true outside a bootstrap. |

### Desired state

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `aap_credential_types` | `[]` | No | Custom credential types for the vendor APIs this repository drives. The `injectors` section is what hands the secret to the playbook at launch. |
| `aap_credentials` | `[]` | No | Credentials themselves. The `inputs` key holds secret material and is never written to the plan. |

## Example Playbook

```yaml
- name: Declare controller credentials
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: aap_controller_credentials
      vars:
        apply_changes: false
        aap_controller_host: "controller.example.mil"
        aap_controller_username: "{{ vault_aap_username }}"
        aap_controller_password: "{{ vault_aap_password }}"
        aap_credential_types:
          - name: "Cisco ISE API"
            kind: cloud
            inputs:
              fields:
                - id: ise_hostname
                  type: string
                  label: "ISE hostname"
                - id: ise_password
                  type: string
                  label: "ISE password"
                  secret: true
              required: [ise_hostname, ise_password]
            injectors:
              extra_vars:
                ise_hostname: "{% raw %}{{ ise_hostname }}{% endraw %}"
                ise_password: "{% raw %}{{ ise_password }}{% endraw %}"
```

## Tags

| Tag | Description |
|-----|-------------|
| `plan` | Build and write the desired-state plan |
| `credentials` | Apply credential types and credentials |
| `evidence` | Publish the plan into the job artifacts |

## What is written

`{{ aap_artifacts_dir }}/aap_credential_plan.json` — the credential types in full, and each credential's *shape* only. The `inputs` key is dropped before the plan is built, so secret material never reaches an artifact rather than being redacted after the fact.

The apply runs inside a block carrying `no_log: true`. That detail matters: `no_log` on an `include_role` does **not** reach the tasks it includes — verified against ansible-core 2.19, where a task inside an included role still printed its message. Only an enclosing block, or the play, propagates it.

# Pure Storage Ansible Playbooks

This folder contains Ansible playbooks and roles to automate Pure Storage FlashArray and FlashBlade operations: volumes, snapshots, host groups, protection, and exports.

This README is a detailed reference for running and extending playbooks safely.

## Table of contents

- Overview
- Prerequisites
- Inventory & recommended group_vars
- Common variables
- Example playbooks
  - Create a volume
  - Create a snapshot and replicate
- Testing & validation
- Security
- Troubleshooting
- Contributing
- References

## Overview

Automate Pure Storage tasks using REST APIs (FlashArray REST) or the `purestorage` Python SDK. Playbooks in this folder follow an API-first approach and assume a service account with appropriate Pure RBAC.

Supported tasks (examples):

- Create/resize/delete volumes (FlashArray)
- Snapshot and snapshot policies
- Replication (protection/replication links)
- Host registration and host group management
- Export/attach volumes to hosts
- Collect inventory, export metrics and reports

## Prerequisites

- Ansible 2.9+ (2.10+ recommended)
- Python 3.8+ on the control host
- Python packages: `purestorage` SDK (for FlashArray/FlashBlade) and `requests` for direct REST calls

Install via pip:

```bash
python -m pip install --user purestorage requests
```

Or include `purestorage` in your Execution Environment / container image.

## Inventory & recommended group_vars

Example minimal inventory (API-only workflows):

```ini
[localhost]
127.0.0.1 ansible_connection=local
```

Example `group_vars/pure.yml` (vault this file in production):

```yaml
---
pure_array_api: "https://pure-array.example.local"
pure_api_token: "!vault_pure_api_token!"    # or use username/password
pure_username: "ansible_bot"
pure_password: "!vault_hidden!"
pure_verify_certs: false
pure_default_tenant: "default"
```

Notes:

- Prefer the `purestorage` SDK for idempotent modules (e.g., `purefa_volume`, `purefb_*` collections) where available.
- `pure_api_token` is preferred over basic auth where supported.

## Common variables

- `pure_array_api` — FlashArray/FlashBlade management endpoint
- `pure_api_token`, `pure_username`, `pure_password` — credentials (vault or token preferred)
- `pure_verify_certs` — TLS verification (true in prod)
- `pure_volume_name`, `pure_volume_size_gb` — used by volume playbooks
- `pure_snapshot_name`, `pure_snapshot_retention` — snapshots
- `pure_replication_target` — replication target array (for protection)

## Example playbooks

1. Create a volume (FlashArray) using the `purestorage` SDK via an Ansible task

```yaml
- name: Create Pure volume
  hosts: localhost
  gather_facts: false
  vars_files:
    - ../group_vars/pure.yml
  tasks:
    - name: Ensure volume exists
      community.general.purefa_volume:
        array: "{{ pure_array_api }}"
        api_token: "{{ pure_api_token }}"
        name: "{{ pure_volume_name | default('ansible-vol-01') }}"
        size_gb: "{{ pure_volume_size_gb | default(10) }}"
        state: present
      register: vol

    - debug:
        var: vol
```

1. Create a snapshot and replicate (pseudo-example)

```yaml
- name: Snapshot and replicate
  hosts: localhost
  gather_facts: false
  vars_files:
    - ../group_vars/pure.yml
  tasks:
    - name: Create snapshot
      uri:
        url: "{{ pure_array_api }}/api/1.12/volume/{{ pure_volume_name }}/snapshot"
        method: POST
        headers:
          Accept: application/json
          Authorization: "Bearer {{ pure_api_token }}"
        body_format: json
        body:
          name: "{{ pure_snapshot_name }}"
        validate_certs: "{{ pure_verify_certs }}"
      register: snap

    - name: Trigger replication (pseudo)
      debug:
        msg: "Would trigger replication to {{ pure_replication_target }}"
```

Adapt the API paths to your Pure REST API version. Prefer SDK modules where present.

## Testing & validation

- Use `--check` for dry-run where modules support that behavior.
- Validate changes in the Pure Storage GUI or `pure` CLI.
- For replication or destructive tasks, test in a lab and use `serial` and `limit` to limit blast radius.

## Security

- Store `pure_api_token` or credentials in Ansible Vault or use a secrets manager.
- Use TLS verification in production and trust a CA; set `pure_verify_certs: true`.
- Use least-privilege service accounts.

## Troubleshooting

- Authentication failures: verify token/credentials and API version compatibility.
- TLS errors: check `pure_verify_certs` and CA trust chain.
- API differences: Pure API versions sometimes change endpoints—check the vendor docs for your appliance.

## Contributing

- Document variables and expected behavior in each playbook or role README.
- Include sanitized logs (`-vvv`) and Pure OS/array firmware versions when opening issues/PRs.

## References

- Pure Storage REST API and SDK docs: <https://support.purestorage.com/>
- Ansible `uri` module docs: <https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html>

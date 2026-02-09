# ScienceLogic SL1 Ansible Automation

This directory contains **31 Ansible roles** for automating **ScienceLogic SL1** platform monitoring, discovery, device management, governance, and ITSM integration.

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your SL1 platform details

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Configure platform
ansible-playbook -i inventory site.yml --tags config

# Configure discovery
ansible-playbook -i inventory site.yml --tags discovery

# Configure monitoring
ansible-playbook -i inventory site.yml --tags monitoring

# Configure ITSM integration
ansible-playbook -i inventory site.yml --tags itsm

# Configure governance
ansible-playbook -i inventory site.yml --tags governance
```

## Overview

ScienceLogic SL1 exposes REST APIs for inventory, device management, and monitoring configuration. These playbooks use the SL1 API to perform idempotent operations where possible. They run on the Ansible control host and call SL1 endpoints over HTTPS.

This repository assumes an API-first approach (no SSH into SL1 appliances required) and that you have an SL1 user with appropriate API permissions.

## Prerequisites

- Ansible 2.9+ (2.10+ recommended)
- Python 3.8+ on the control node
- Python packages: `requests` (used by many simple REST tasks). Install:

```bash
python -m pip install --user requests
```

- If you prefer an Ansible module or collection for SL1, install it accordingly (this README uses generic REST calls for portability).
- Network connectivity to SL1 API (usually TCP/443) from the control host.

## Inventory & variables

Suggested minimal inventory (API-driven workflows):

```ini
[localhost]
127.0.0.1 ansible_connection=local
```

Recommended `group_vars/sciencelogic.yml` (vault this file in production):

```yaml
---
sl1_api_url: "https://sl1.example.local/api"
sl1_user: "ansible_bot"
sl1_password: "!vault_secret_here!"
sl1_verify_certs: false     # true in production with trusted CA
sl1_timeout: 30
```

Notes:

- Prefer Ansible Vault or a secrets manager for `sl1_password`.
- You can also export `SL1_USER` and `SL1_PASSWORD` environment variables and reference them with the `lookup('env', ...)` function in playbooks.

## Example playbooks

Below are two compact example playbooks: a discovery job trigger and a create-device example using the SL1 REST API. These are minimal examples and should be adapted to your SL1 schema and workflows.

1. Trigger a Discovery (example)

```yaml
- name: Trigger SL1 discovery for an IP range
  hosts: localhost
  gather_facts: no
  vars_files:
    - ../group_vars/sciencelogic.yml
  tasks:
    - name: Build discovery payload
      set_fact:
        payload:
          name: "ansible-discovery-{{ lookup('pipe','date +%Y%m%d%H%M%S') }}"
          type: "ip_range"
          range: "10.0.0.0/24"

    - name: Trigger discovery via SL1 API
      uri:
        url: "{{ sl1_api_url }}/discovery"
        method: POST
        user: "{{ sl1_user }}"
        password: "{{ sl1_password }}"
        force_basic_auth: yes
        status_code: 201,202
        body_format: json
        body: "{{ payload }}"
        validate_certs: "{{ sl1_verify_certs }}"
      register: discovery_resp

    - name: Show discovery response
      debug:
        var: discovery_resp.json
```

1. Create a device in SL1 (example)

```yaml
- name: Create device in SL1
  hosts: localhost
  gather_facts: no
  vars_files:
    - ../group_vars/sciencelogic.yml
  tasks:
    - name: Build device object
      set_fact:
        device_obj:
          hostname: "test-device-01"
          ip: "10.0.10.20"
          class: "Server"

    - name: Create or update device via REST
      uri:
        url: "{{ sl1_api_url }}/devices"
        method: POST
        user: "{{ sl1_user }}"
        password: "{{ sl1_password }}"
        force_basic_auth: yes
        status_code: 200,201
        body_format: json
        body: "{{ device_obj }}"
        validate_certs: "{{ sl1_verify_certs }}"
      register: device_resp

    - name: Display device API result
      debug:
        var: device_resp.json
```

Adapt the body and endpoints to match your SL1 API version and payload schema.

## Testing & validation

- Use `--check --diff` for dry-run where operations are safe — note that most REST-based creation endpoints may not support dry-run.
- After running a task, validate in SL1 UI and check SL1 audit/log entries.
- For playbooks that change many devices, use `serial` and run against a small subset first.

## Security

- Never commit `sl1_password` or plaintext credentials to source control.
- Use Ansible Vault for `group_vars` or use environment-based secrets injected by your CI/CD system.
- Set `sl1_verify_certs: true` in production and use a trusted CA.

## Troubleshooting

- Connection refused or TLS errors: verify network access and `sl1_verify_certs`/CA chain.
- Authentication failures: test credentials in a browser or curl to isolate Ansible issues.
- API schema mismatches: check your SL1 API docs and the returned JSON for keys and structure.

## Contributing & style

- Keep playbooks idempotent when possible.
- Document required variables at the top of each playbook or in a role README.
- Use `-vvv` for detailed Ansible output when reporting issues.

## References

- ScienceLogic API docs: <https://docs.sciencelogic.com/>
- Ansible `uri` module docs: <https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html>

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

# Ansible-Playbooks-2.0

A curated collection of vendor and platform-specific Ansible playbooks, roles, and examples for infrastructure automation. The repository contains per-vendor folders (for example: `palo_alto`, `vmware`, `pure`, `veeam`) plus shared patterns and checkpoints used for Day-0 / Day-1 operations.

This README provides a guide to the repository layout, conventions, prerequisites, example usage, and recommendations for running playbooks safely in production.

## Table of contents

- Repository purpose
- Repository layout
- Conventions and best practices
- Execution environments & dependencies
- Credentials and secrets
- Running playbooks (tips and examples)
- Testing and CI guidance
- Contribution guidelines
- Where to get help

## Repository purpose

This repository is intended to collect reusable Ansible automation for multiple vendors, including (but not limited to):

- Check Point (checkpoint)
- Palo Alto Networks (palo_alto)
- VMware (vmware)
- Pure Storage (pure)
- Veeam (veeam)

Each top-level folder is focused on a vendor or a specific automation domain and contains roles, playbooks, and supporting documentation related to that vendor.

## Repository layout

- `/<vendor>/` — vendor-specific folder containing `roles/`, `playbooks/`, `tasks/`, and a `README.md` with usage notes.
- `/roles/` — shared roles used across playbooks (may be nested under vendor folders)
- `/group_vars/` and `/host_vars/` — recommended locations for environment-specific variables (not committed with secrets)
- `/checkpoint/` — checkpoint and example Day-0 configurations and playbooks
- `/docs/` — (optional) more extensive documentation and design notes

Example:

```text
palo_alto/
  README.md
  roles/
  playbooks/
pure/
  README.md
  roles/
  playbooks/
```

## Conventions and best practices

- Run API-based playbooks from a control host (use `hosts: localhost` and `connection: local`) unless you are running agent-based automation.
- Keep secrets out of the repo. Use Ansible Vault or a secrets manager and reference secrets via `{{ vault_var }}` or lookup plugins.
- Prefer published collections (Ansible Galaxy) and pin collection versions inside Execution Environments or requirements files.
- Write idempotent tasks and prefer collection modules (for example `paloaltonetworks.panos` or `purestorage.flasharray`) over `uri` when possible.
- For any playbook that can make breaking changes (commits, reboots, NAT changes), include a `--check` dry-run guidance and prefer `--limit` for staged rollouts.

## Execution Environments & dependencies

For reproducible runs and CI, build or use an Execution Environment (EE) that includes required collections and Python packages. Maintain a `requirements.yml` or `collections/requirements.yml` for Ansible Galaxy collections and a `requirements.txt` or `pyproject.toml` for Python packages.

Example `collections/requirements.yml`:

```yaml
- name: paloaltonetworks.panos
  version: 2.0.0
- name: purestorage.flasharray
  version: 1.0.0
```

Build/pull this into your EE or run `ansible-galaxy collection install -r collections/requirements.yml` on the control host.

## Credentials and secrets

- Store passwords, API keys, and tokens in Ansible Vault or an external secrets manager.
- Use dedicated automation accounts with least privilege and monitor/rotate credentials regularly.
- Example usage (group_vars):

```yaml
# group_vars/env.yml
ansible_user: automation
ansible_password: "{{ vault_automation_password }}"
api_key: "{{ vault_api_key }}"
```

## Running playbooks (tips and examples)

- Dry-run: `ansible-playbook playbook.yml --check --diff` (note: not all modules support check mode)
- Limit target scope: `ansible-playbook playbook.yml --limit firewall01`
- Use `--tags` and `tags:` on tasks to target small changes during rollouts.

Example (run a vendor playbook from repo root):

```bash
ansible-playbook palo_alto/playbooks/panos_create_object.yml -i inventories/prod.ini --ask-vault-pass
```

## Testing and CI guidance

- Include a minimal test matrix in CI that runs playbooks in `--check` mode against a mocked or lab environment.
- Use linting: `ansible-lint` and `markdownlint` for README/MD files.
- For behavioral tests, use molecule for roles where appropriate and configure drivers (docker, podman, or custom) that match the target environment.

## Contribution guidelines

- Please open PRs against the main branch. Provide a description of the change, affected vendors, and any new dependencies.
- Don't commit plaintext secrets. Use placeholders and document required secret names in `group_vars` or README.

## Where to get help

- For vendor-specific API questions, consult vendor documentation (links in vendor README files).
- If you want me to scaffold sample `group_vars` or create runnable playbooks from the examples in any vendor folder, tell me which folder and whether you prefer API keys or username/password placeholders.

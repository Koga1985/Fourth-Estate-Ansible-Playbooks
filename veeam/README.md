# Veeam Backup & Replication

This directory contains **6 Ansible roles** for automating **Veeam Backup & Replication** lifecycle management including installation, backup job configuration, restore operations, replication, cloud tiering, and automated testing with SureBackup.

## Overview

Comprehensive Veeam automation covering backup server installation, repository management, backup job creation and scheduling, restore operations, replication configuration, cloud archive tier setup, and automated backup testing.

## 📋 Roles

### Installation & Configuration (1 role)
- **veeam_backup_server_install** - Veeam Backup & Replication server installation and initial configuration

### Backup Operations (2 roles)
- **veeam_backup_jobs** - Backup job creation, scheduling, and management
- **veeam_restore_operations** - Automated restore workflows and testing

### Advanced Features (3 roles)
- **veeam_replication** - Replication job configuration for DR
- **veeam_cloud_tier** - Cloud archive tier (AWS, Azure, S3-compatible) setup
- **veeam_surebackup** - Automated backup verification and testing

## Contents

- `roles/` — 6 production-ready roles
- `tasks/` — standalone task files for common operations
- `playbooks/` — example playbooks for common scenarios

## Prerequisites

- Ansible 2.9+ (2.10+ recommended)
- Python packages on the control node where needed (e.g., `requests`)
- Access to the Veeam server(s) and API/CLI credentials

## Quick start

1. Ensure prerequisites are installed.
2. Provide inventory and vaulted variables (see `group_vars` or use environment variables).
3. Run a playbook, for example:

```bash
ansible-playbook -i inventory.ini playbooks/veeam_install.yml
```

## Overview

This folder contains Ansible playbooks and tasks intended to automate common Veeam administration workflows, including:

- Installing or patching Veeam components
- Creating and validating backup repositories
- Creating backup jobs and schedules
- Exporting inventory and reports
- Performing operational tasks (validate backups, trigger restores, manage retention)

Where possible the playbooks use idempotent operations or guard checks; however, some Veeam API calls may be inherently imperative. Review each playbook's README and variable list before running in production.

## Inventory & example group_vars

Minimal inventory for API-driven workflows:

```ini
[localhost]
127.0.0.1 ansible_connection=local
```

Example `group_vars/veeam.yml` (vault this file in production):

```yaml
---
veeam_server: "veeam.example.local"
veeam_user: "ansible_bot"
veeam_password: "!vault_hidden!"
veeam_validate_certs: false
veeam_repository: "MainRepo"
veeam_repo_path: "/backup/repo"
```

## Detailed variables

Describe the commonly used variables and what they control:

- `veeam_server` — FQDN/IP for Veeam Backup & Replication (or REST API gateway)
- `veeam_user` — service account with API/CLI rights
- `veeam_password` — vault this value; prefer not to store plaintext
- `veeam_validate_certs` — set `true` in production when using trusted CA
- `veeam_repository` — repository name or identifier used by repository playbooks
- `veeam_repo_path` — path for file-based repositories (if applicable)
- `veeam_job_name`, `veeam_job_schedule` — used by job creation tasks

## Example playbooks

Below are compact examples that mirror common tasks; adapt paths and variable names to match your repo layout.

1. Install or configure Veeam components (example stub)

```yaml
- name: Install Veeam Backup & Replication (stub)
  hosts: localhost
  gather_facts: no
  vars_files:
    - ../group_vars/veeam.yml
  tasks:
    - name: Ensure Veeam MSI installed (Windows)
      win_package:
        path: "./artifacts/VeeamBackup.msi"
        state: present
      when: ansible_os_family == 'Windows'
```

1. Create/ensure a repository

```yaml
- name: Ensure repository exists
  hosts: localhost
  gather_facts: no
  vars_files:
    - ../group_vars/veeam.yml
  tasks:
    - name: Ensure repository present via Veeam API (pseudo)
      uri:
        url: "https://{{ veeam_server }}/api/repositories"
        method: POST
        user: "{{ veeam_user }}"
        password: "{{ veeam_password }}"
        body_format: json
        body:
          name: "{{ veeam_repository }}"
          path: "{{ veeam_repo_path | default('/backup/repo') }}"
        status_code: 200,201
        validate_certs: "{{ veeam_validate_certs }}"
      register: repo_resp

    - debug:
        var: repo_resp.json
```

1. Create a backup job (example using a role)

```yaml
- name: Create a backup job
  hosts: localhost
  gather_facts: no
  vars_files:
    - ../group_vars/veeam.yml
  tasks:
    - include_role:
        name: veeam_create_job
      vars:
        veeam_job_name: "nightly-vm-backup"
        veeam_vm_list:
          - "vm-01"
          - "vm-02"
```

## Testing & validation

- Use `--check --diff` for dry runs where safe, but note many API endpoints do not fully support dry-run semantics.
- Run playbooks against a lab Veeam environment before production.
- Validate the Veeam UI and job history after changes.

## Security

- Store secrets in Ansible Vault or a secrets manager. Example to run with vault:

```bash
ansible-playbook playbooks/veeam_install.yml -e @group_vars/veeam.yml --ask-vault-pass
```

- Ensure service accounts have only the permissions required for automation.

## Troubleshooting

- TLS/connection errors: confirm `veeam_validate_certs` and network reachability.
- Authentication errors: verify the `veeam_user` has API privileges.
- API schema changes: consult Veeam API docs for your product version.

## Contributing

- Document variables required by each playbook/role in the playbook header or role `README.md`.
- When opening PRs, include sanitized logs (`-vvv`) and environment details (Veeam version, Ansible version, collection versions).

## References

- Veeam REST API / PowerShell SDK docs (vendor docs for your version)
- Ansible `uri` module: <https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html>

## Notes

- This is an overview. See `tasks/` and any role README files for detailed usage and required variables.
- If you want, I can add an example `inventory.ini` and a small test playbook to this folder.

## Maintainers / Contact

- Repository: Koga1985/Ansible-Playbooks-2.0
- Maintainers: see top-level README for contact details

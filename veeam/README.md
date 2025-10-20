
# Veeam Ansible Playbooks

This folder contains Ansible tasks and roles to automate configuration and operational tasks for Veeam Backup & Replication environments.

Contents

- roles/: opinionated roles for common Veeam operations (if present)

- tasks/: standalone playbooks and task files for ad-hoc operations

Quick start

1. Ensure you have Ansible 2.9+ (recommended 2.10+) and the necessary Python dependencies installed on your control host.
2. Copy or adapt `inventory.ini` from the checkpoint examples and set the target hosts.
3. Run a playbook from this folder, for example:

```bash
ansible-playbook -i inventory.ini playbooks/veeam_install.yml
```

Typical variables

Below are commonly used variables. Check individual playbooks or roles for the full set.

- veeam_server: the FQDN or IP of the Veeam server
- veeam_user: administrative user for API/CLI operations
- veeam_password: password for `veeam_user` (use Ansible Vault or external secrets)
- veeam_repository: name or id of the backup repository to use

Example playbook snippet

```yaml
- name: Example — create backup job for VM
  hosts: veeam_servers
  vars:
    veeam_user: "admin@example.local"
    veeam_password: "!vault_encrypted!"
    veeam_repository: "MainRepo"
  tasks:
    - include_role:
        name: veeam_create_job
      vars:
        job_name: "nightly-vm-backup"
        vm_list:
          - "vm-01"
          - "vm-02"
```

Testing and validation

- Dry-run: use `--check --diff` for non-destructive validation where supported.
- Logs: check the Veeam server logs and the Ansible output for task-level details.

Security

- Never store plaintext credentials in this repository. Use Ansible Vault or a secrets manager.

Notes

- This is a lightweight overview. See task files in `tasks/` and role README files for detailed instructions and required variables.
- If you want, I can add an example `inventory.ini` and a small test playbook to this folder.

Maintainers / Contact

- Repository: Koga1985/Ansible-Playbooks-2.0
- Maintainers: see top-level README for contact details


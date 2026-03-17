# claroty_xdome_inventory_scheduler

Installs a shell wrapper script and a cron entry on the Ansible control host (or a designated scheduler node) to run a Claroty xDome delta-sync playbook on a configurable schedule. Credential environment variables are embedded in the wrapper script so that the cron job can run non-interactively.

## Requirements

- Ansible 2.12+
- The target host must have `ansible-playbook` installed at the path specified by `ansible_cmd`
- The delta-sync playbook referenced by `scheduled_playbook` must exist at the configured path
- Write access to `artifacts_dir` on the target host

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `artifacts_dir` | `"/tmp/claroty-artifacts"` | Directory where the wrapper script is installed and where delta-sync logs are written. |
| `cron_schedule` | `"0 * * * *"` | Cron schedule expression in standard five-field format (minute hour day month weekday). Default runs every hour. |
| `scheduled_playbook` | `"/opt/ansible/claroty/claroty_delta_sync.yml"` | Absolute path to the playbook that the cron job will invoke. |
| `ansible_cmd` | `"/usr/bin/ansible-playbook"` | Absolute path to the `ansible-playbook` binary. |
| `cron_env` | `{CLAROTY_TOKEN: "", SNOW_TOKEN: ""}` | Dictionary of environment variable names and values to export in the wrapper script. Used to pass credentials to the scheduled playbook without interactive prompts. **Set via Ansible Vault.** |

## Dependencies

- `claroty_xdome_inventory_export` — The `scheduled_playbook` should include this role for the actual delta-sync work.

## Example Playbook

```yaml
---
- name: Install Claroty xDome delta-sync scheduler
  hosts: scheduler_host
  become: false

  vars:
    artifacts_dir: "/opt/claroty/artifacts"
    cron_schedule: "*/30 * * * *"    # Every 30 minutes
    scheduled_playbook: "/opt/ansible/claroty/claroty_delta_sync.yml"
    ansible_cmd: "/usr/bin/ansible-playbook"
    cron_env:
      CLAROTY_TOKEN: "{{ vault_claroty_token }}"
      SNOW_TOKEN: "{{ vault_snow_token }}"

  roles:
    - role: claroty/roles/claroty_xdome_inventory_scheduler
```

## What Gets Created

- `{{ artifacts_dir }}/claroty_delta_sync.sh` — Shell wrapper script with exported credential environment variables that invokes `ansible-playbook {{ scheduled_playbook }}` and appends output to `{{ artifacts_dir }}/delta_sync.log`.
- A cron entry named `"Claroty xDome delta sync"` for the current user, running the wrapper at the configured schedule.

## Security Considerations

- The wrapper script contains plaintext environment variable values. Ensure `artifacts_dir` is owned by the service account running the cron job with permissions `0755` on the directory and `0755` on the script.
- Prefer using a dedicated least-privilege service account for the scheduler host.
- Rotate `CLAROTY_TOKEN` and `SNOW_TOKEN` regularly and re-run this role to update the wrapper script.

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

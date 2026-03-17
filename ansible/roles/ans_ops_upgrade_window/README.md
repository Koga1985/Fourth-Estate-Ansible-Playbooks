
# ans_ops_upgrade_window

Manages scheduled upgrade windows for Ansible Automation Platform (AAP) Controller and Execution Nodes. Performs preflight version checks, creates recurring maintenance schedules via the Controller API, and emits upgrade window notifications.

## What it does

1. **Preflight version check** — GETs `/api/v2/config/` on the target Controller to retrieve the current platform version before any changes are made.
2. **Creates maintenance schedules** — When `apply_changes: true`, uses the `ansible.controller.schedule` module to create or update recurring schedules for each entry in `maintenance_windows`. Schedules default to monthly recurrence.
3. **Sends upgrade notifications** — When `upgrade_window_enabled: true`, emits a debug notification confirming the scheduled upgrade window and the configured schedule string.
4. **Displays upgrade summary** — Prints the configured `upgrade_schedule` and `fourth_estate_change_control` flag for confirmation before any upgrade actions proceed.

## Variables (see `defaults/main.yml`)

```yaml
apply_changes: false
artifacts_dir: "/tmp/ansible-artifacts"
validate_certs: true

# Upgrade window configuration
upgrade_window_enabled: true
upgrade_schedule: "monthly"
upgrade_notification_days: 14

# Maintenance windows (creates Controller schedules when apply_changes: true)
maintenance_windows:
  - name: "Monthly Patching"
    schedule: "0 2 * * 0"   # 2 AM Sunday
    duration: 4              # hours

# Fourth Estate change control requirements
fourth_estate_change_control: true
fourth_estate_rollback_plan_required: true
```

Required variables (not in defaults):

```yaml
controller_host: "https://controller.example.com"
controller_oauthtoken: "{{ vault_controller_token }}"
```

## Rolling upgrade procedure

Rolling upgrades for Controller and Execution Nodes are performed outside this role using the `ansible.controller` collection or the AAP installer. This role handles the scheduling and notification steps. The recommended sequence is:

1. Run this role with `apply_changes: false` to verify the current version and review the maintenance schedule.
2. Obtain change control approval (`fourth_estate_change_control: true` enforces this gate).
3. Ensure a rollback plan is documented (`fourth_estate_rollback_plan_required: true`).
4. Run this role with `apply_changes: true` to register the maintenance window schedule.
5. Execute the AAP upgrade playbook within the scheduled window, targeting Execution Nodes before the Controller.

## Example play

```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: ans_ops_upgrade_window
      vars:
        controller_host: "https://controller.example.com"
        controller_oauthtoken: "{{ vault_controller_token }}"
        apply_changes: true
        upgrade_schedule: "2026-04-06T02:00:00"
        maintenance_windows:
          - name: "AAP April Patching"
            schedule: "0 2 6 4 *"
            duration: 4
```

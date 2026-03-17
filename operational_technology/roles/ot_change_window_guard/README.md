# ot_change_window_guard

Restricts automation-driven OT changes to approved maintenance windows. The role asserts that the current system time (in the configured timezone) falls within one of the defined `change_windows` windows before allowing downstream tasks to proceed. It also supports a dry-run mode that reports what would happen without taking action, and captures a what-if summary to an artifact file.

## Requirements

- Ansible 2.12+
- The Ansible control host must have an accurate system clock
- `pytz` Python library on the control node if timezone conversion is required

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `artifacts_dir` | `/tmp/ot-artifacts` | Directory for dry-run and what-if output artifacts. Created if it does not exist. |
| `dry_run` | `true` | When `true`, the role reports change window status but does not block execution. Set to `false` to enforce hard blocking outside windows. |
| `change_tz` | `UTC` | Timezone for change window evaluation (IANA timezone string, e.g. `America/New_York`). |
| `change_windows` | `[]` | List of approved change window definitions. Each entry is a dict with `start` and `end` keys in `HH:MM` 24-hour format and an optional `days` key (list of weekday names). An empty list means no windows are defined; behavior depends on `dry_run`. |
| `change_window_override` | `false` | When `true`, bypasses window enforcement regardless of current time. Use only for emergency operations; should be controlled by a separate approval workflow. |
| `what_if_summary` | `""` | Optional human-readable description of the planned changes, written to the what-if artifact file for review. |

## Change Window Definition

```yaml
change_windows:
  - start: "22:00"
    end: "02:00"
    days: ["Saturday", "Sunday"]
  - start: "02:00"
    end: "06:00"
    days: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
```

`end` times earlier than `start` times are treated as spanning midnight.

## Dependencies

None.

## Example Playbook

```yaml
---
- name: OT network configuration with change window enforcement
  hosts: ot_network_devices
  gather_facts: false

  pre_tasks:
    - name: Enforce change window
      ansible.builtin.include_role:
        name: operational_technology/roles/ot_change_window_guard
      vars:
        dry_run: false
        change_tz: "America/Chicago"
        change_windows:
          - start: "23:00"
            end: "03:00"
            days: ["Saturday", "Sunday"]
        what_if_summary: "Apply VLAN changes to OT DMZ switches"

  tasks:
    - name: Apply network configuration
      # ... network tasks here
```

## Output Artifacts

- `{{ artifacts_dir }}/change_window_status.txt` — Records whether the current time is inside or outside the defined windows, the effective timezone, and whether override is active.
- `{{ artifacts_dir }}/what_if.txt` — Contains the `what_if_summary` string for change review documentation.

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

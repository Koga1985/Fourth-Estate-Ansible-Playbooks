# ot_emergency_freeze

Implements an emergency change-freeze toggle for OT automation pipelines. When a freeze is active the role short-circuits execution, preventing any downstream OT configuration changes from proceeding. The freeze state can be set via a playbook variable (`freeze_flag`) or read from a source-of-truth (SoT) flag file on the control host, allowing operations teams to activate a freeze out-of-band without modifying playbook code.

## Requirements

- Ansible 2.12+
- Write access to `artifacts_dir` for status artifact output

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `/tmp/ot-artifacts` | No | Directory for freeze status output artifacts. |
| `freeze_flag` | `false` | No | Direct variable-based freeze toggle. Set to `true` to activate an emergency freeze immediately. This variable can be passed at runtime with `-e freeze_flag=true`. |
| `sot_freeze_file` | `""` | No | Absolute path to a SoT flag file on the control host. When this file exists and contains the string `frozen`, the freeze is activated regardless of `freeze_flag`. Leave empty to disable file-based freeze checking. |

## Freeze Activation Logic

The freeze is considered active when either of the following is true:

1. `freeze_flag` is `true` (variable-based activation), or
2. `sot_freeze_file` is a non-empty string pointing to a file that exists and contains `frozen`.

When a freeze is active, the role fails the play with a clear message explaining the freeze state. Downstream tasks in the same play do not execute.

## Tasks Executed

1. **read_flag** — Reads the `sot_freeze_file` if configured, registering the file content. Skipped if `sot_freeze_file` is empty.
2. **short_circuit** — Evaluates the combined freeze state and fails the play if active, writing a freeze-status artifact to `artifacts_dir`.

## Dependencies

None. Typically used as a `pre_tasks` guard before OT configuration roles.

## Example Playbook

### Variable-based freeze check

```yaml
---
- name: OT configuration pipeline with emergency freeze guard
  hosts: ot_devices
  gather_facts: false

  pre_tasks:
    - name: Check emergency freeze
      ansible.builtin.include_role:
        name: operational_technology/roles/ot_emergency_freeze
      vars:
        freeze_flag: "{{ emergency_freeze | default(false) }}"

  roles:
    - role: operational_technology/roles/ot_change_window_guard
    # ... other OT roles
```

### File-based freeze (SoT controlled)

```yaml
---
- name: OT pipeline with file-based freeze
  hosts: localhost
  gather_facts: false

  pre_tasks:
    - name: Check SoT freeze flag
      ansible.builtin.include_role:
        name: operational_technology/roles/ot_emergency_freeze
      vars:
        sot_freeze_file: "/etc/ot-automation/freeze.flag"
        freeze_flag: false
```

To activate a freeze without running Ansible:
```bash
echo "frozen" > /etc/ot-automation/freeze.flag
```

To deactivate:
```bash
rm /etc/ot-automation/freeze.flag
```

## Output Artifacts

- `{{ artifacts_dir }}/freeze_status.txt` — Records whether a freeze is active, the source of the freeze (variable or file), and a timestamp.

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

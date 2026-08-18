# Preflight / Postflight Validation and Run Statistics

Every task file, role and playbook in this repository is wrapped in a uniform
`block` / `rescue` / `always` validation harness that publishes its outcome
through `ansible.builtin.set_stats`.

The goal is that **"did this run work?" is answerable from structured data**
rather than by scraping console output — from a wrapping playbook, from AWX /
Ansible Automation Platform (which surfaces `set_stats` data on the job), or
from CI.

---

## Table of Contents

- [What was applied where](#what-was-applied-where)
- [The task-file / role shape](#the-task-file--role-shape)
- [The playbook shape](#the-playbook-shape)
- [Handlers](#handlers)
- [Published statistics](#published-statistics)
- [Consuming the statistics](#consuming-the-statistics)
- [The fe_validation callback plugin](#the-fe_validation-callback-plugin)
- [Control variables](#control-variables)
- [Adding component-specific preflight checks](#adding-component-specific-preflight-checks)
- [Tag behaviour](#tag-behaviour)
- [Behaviour changes to be aware of](#behaviour-changes-to-be-aware-of)

---

## What was applied where

| Scope | Files | Shape |
|-------|-------|-------|
| Role task entrypoints (`*/roles/*/tasks/main.yml`) | 572 | task-file wrapper |
| Role sub-task files (`*/roles/*/tasks/*.yml`) | 848 | task-file wrapper |
| Standalone task files (`<platform>/tasks/*.yml`) | 430 | task-file wrapper |
| Playbooks (`site.yml`, `*/playbooks/*.yml`, `*/roles/*/playbooks/run.yml`) | 274 | playbook wrapper |
| **Total** | **2,124** | |

Deliberately **not** wrapped:

- **Handler files** (`*/roles/*/handlers/main.yml`) — see
  [Handlers](#handlers) below. The wrapper cannot be expressed on a handler at
  all; handler failures are covered a different way.
- **`defaults/`, `vars/`, `meta/`** and other non-task YAML — these are data,
  not task lists.

Every component is identified by a repo-relative id such as
`cisco/ise_profiling__probes` or `splunk/site`, which is unique across the
repository. Its facts are namespaced with a matching `fe_<sanitised_id>_`
prefix, so nested execution (a playbook running a role that includes sub-task
files) never collides.

---

## The task-file / role shape

```yaml
- name: "<component> | Initialize validation state"
  ansible.builtin.set_fact: ...          # timestamps, status=running

- name: "<component> | Guarded execution with preflight and postflight validation"
  block:
    # ---- preflight ----
    #   - control node meets the minimum ansible-core version
    #   - every variable named in <prefix>_required_vars is defined
    #   - records preflight_passed=true
    # ---- execute ----
    #   ... the original tasks, untouched ...
    # ---- postflight ----
    #   - asserts preflight passed and no failure was recorded
    #   - records status=succeeded
  rescue:
    #   - captures ansible_failed_task.name and ansible_failed_result.msg
    #   - reports the failure
    #   - re-raises unless fe_validation_continue_on_error is true
  always:
    #   - computes duration
    #   - publishes the record with set_stats
```

`always` runs even when the `rescue` re-raises, so **statistics are published on
both the success and the failure path**.

---

## The playbook shape

Each play gains three sections:

| Section | Contents |
|---------|----------|
| `pre_tasks` | `block`/`rescue`/`always` preflight. On failure it records the reason, publishes the record with `set_stats`, and aborts the play **before any role or task runs**. |
| `tasks` | The original task list, wrapped in `block`/`rescue`/`always`. A failure is captured (which task, which error), published, and re-raised. |
| `post_tasks` | `block`/`rescue`/`always` postflight validation, then the run record is published with `set_stats`. |

Existing `pre_tasks` / `post_tasks` are preserved — the harness is prepended to
`pre_tasks` and appended to `post_tasks`. Playbooks that only have `roles:` get
`pre_tasks` and `post_tasks` added.

The record is published exactly once per play, guarded by a
`<prefix>_stats_published` fact:

- preflight failed → published from the `pre_tasks` rescue,
- `tasks` failed → published from the `tasks` always block,
- otherwise → published from the `post_tasks` always block.

---

## Handlers

Handler files are **not** wrapped, and cannot be. This section records why, and
how handler failures are covered instead.

### Why the wrapper cannot be applied to a handler

A `handlers/main.yml` is not a task list — it is a **registry of individually
addressable units**. `notify: restart splunk` resolves one handler by name and
runs only that handler; the file is never executed as a sequence.

Wrapping the file the way task files are wrapped is therefore **inert**. The
handler name still resolves through the block, but:

- the `always:` section never runs, so `set_stats` never publishes;
- the `rescue:` never engages — a failing handler reports `rescued=0` and the
  error propagates untouched;
- the `Initialize validation state` task becomes a handler nobody notifies, so
  every `fe_*` fact stays undefined.

The obvious alternative — defining each handler *as* a named block with its own
`rescue`/`always` — does not work either:

```
[ERROR]: The requested handler 'restart splunk' was not found in either the
main handlers list nor in the listening handlers list
```

A named block is not registered as a notifiable handler. There is no way to
express preflight/postflight-with-`set_stats` on a handler using
`block`/`rescue`/`always`.

### How handler failures are covered instead

Handlers normally flush **after** the tasks section completes — that is, after
the wrapper's `block`/`rescue`/`always` has already finished. A failing handler
would fail the run (exit 2) but publish **no validation record at all**, because
the wrapper had closed and `post_tasks` are skipped once the host fails.

Every play therefore ends its guarded block with an explicit flush:

```yaml
tasks:
  - name: "<component> | Guarded execution with rescue and always handling"
    block:
      # ... the original tasks ...
      - name: "<component> | Flush notified handlers inside the guarded block"
        ansible.builtin.meta: flush_handlers
    rescue: ...
    always: ...
```

Because the flush happens *inside* the block, a handler failure is captured,
published and re-raised on exactly the same path as an ordinary task failure —
with the handler named in `failed_task`:

```json
{
  "status": "failed",
  "failed_task": "simulated failing handler",
  "error": "handler blew up"
}
```

Roles notify handlers from inside the role, but Ansible flushes them at the end
of the combined roles + tasks section — so this covers role handlers too.
Roles-only plays (no `tasks:` of their own) were given a `tasks:` section whose
guarded block contains just the flush, which is the same point in the play where
their handlers would have flushed anyway.

Applied to all 311 plays across the 274 playbooks: 204 had the flush appended to
an existing guarded block, 107 roles-only plays gained a `tasks:` section.

### Timing note

For a play that already had `tasks:`, handlers now flush at the end of the block
body instead of a few harness tasks later. Handlers already ran between `tasks`
and `post_tasks`, so their position relative to your own tasks is unchanged; the
run duration now includes handler execution time, which is more accurate.

`pre_tasks` are covered too. A play's own `pre_tasks` entries (everything after
the harness's preflight block) are wrapped in the same guarded shape, ending
with their own `meta: flush_handlers`:

```yaml
pre_tasks:
  - name: "<component> | Preflight validation"        # harness
    ...
  - name: "<component> | Guarded pre_tasks with rescue and always handling"
    block:
      # ... the play's own pre_tasks ...
      - name: "<component> | Flush notified handlers inside the guarded block"
        ansible.builtin.meta: flush_handlers
    rescue: ...
    always: ...
```

This closed two gaps at once: a handler notified from `pre_tasks` now fails
inside the wrapper, and a failure in one of the play's own `pre_tasks` is now
captured and published instead of aborting the play silently. Applied to 104
plays covering 173 original `pre_tasks` entries.

---

## Published statistics

All values are published with `aggregate: true` and `per_host: false`, so
counters sum and the results dictionary merges across every role, task file and
play in a run.

| Key | Type | Meaning |
|-----|------|---------|
| `fe_validation_results` | dict | One record per component, keyed by component id |
| `fe_validation_executions` | int | Number of wrapped components that ran |
| `fe_validation_succeeded` | int | How many finished with `status: succeeded` |
| `fe_validation_failed` | int | How many did not |
| `fe_validation_duration_seconds` | int | Summed wall-clock seconds |
| `fe_validation_failed_components` | list | Component ids that failed |

Each entry in `fe_validation_results` looks like:

```json
{
  "component": "cloud_policy/cloud_computing_srg_assessment",
  "type": "role",
  "platform": "cloud_policy",
  "host": "localhost",
  "status": "succeeded",
  "preflight_passed": true,
  "postflight_passed": true,
  "started_at": "2026-08-17T18:20:37Z",
  "ended_at": "2026-08-17T18:20:40Z",
  "duration_seconds": 3,
  "failed_task": "",
  "error": "",
  "check_mode": false
}
```

`type` is one of `role`, `role-tasks`, `tasks` or `playbook`.
`status` is one of `succeeded`, `failed` or `preflight_failed`.

---

## Consuming the statistics

### On the command line

`set_stats` output is hidden by default. Enable it:

```bash
ANSIBLE_SHOW_CUSTOM_STATS=true ansible-playbook -i inventory site.yml
```

or in `ansible.cfg`:

```ini
[defaults]
show_custom_stats = True
```

### In AWX / Ansible Automation Platform

Nothing to configure — `set_stats` data is attached to the job and available to
workflow nodes as `fe_validation_*` variables, so a downstream node can branch
on `fe_validation_failed`.

### From a wrapping playbook

Statistics set by an inner play are available to later plays as ordinary
variables:

```yaml
- name: Gate on the validation results
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Fail if any component failed
      ansible.builtin.fail:
        msg: >-
          {{ fe_validation_failed }} of {{ fe_validation_executions }} components
          failed: {{ fe_validation_failed_components | join(', ') }}
      when: fe_validation_failed | default(0) | int > 0

    - name: Write a machine-readable run report
      ansible.builtin.copy:
        dest: /tmp/fe_validation_report.json
        mode: "0640"
        content: "{{ fe_validation_results | default({}) | to_nice_json }}"
```

---

## The fe_validation callback plugin

`callback_plugins/fe_validation.py` collects the same per-component record with
**no in-play tasks at all**, by watching callback events. Enable it with
environment variables:

```bash
ANSIBLE_CALLBACK_PLUGINS=./callback_plugins \
ANSIBLE_CALLBACKS_ENABLED=fe_validation \
ansible-playbook -i inventory site.yml
```

or copy `ansible.cfg.example` to `ansible.cfg`. It prints a summary and writes
`fe_validation_report.json`:

```
FE VALIDATION ******************************************************************
2 components, 1 succeeded, 1 failed, 2.039s total
  failed       0.00s  cloud_policy/cloud_computing_srg_assessment  (ok=0 changed=0 failed=1 skipped=0)
             failed at 'cloud_computing_srg_assessment : TEMP explode': simulated failure
  succeeded    0.00s  cloud_policy/cloud_computing_srg_assessment/run  (ok=1 changed=0 failed=0 skipped=0)
```

It derives component ids from each task's source file, so they match the
in-play harness exactly. Running both together on the same playbook produces
identical key sets, types, statuses and counters.

### What it does *not* replace

**It cannot feed AWX/AAP.** Only `set_stats` does that: AAP builds job artifacts
and workflow variables from the `set_stats` events in the event stream. A
callback calling `stats.set_custom_stats()` is accepted but never surfaces --
the stdout callback's stats hook has already run by then. This was tested, not
assumed.

So the two are complementary:

| | in-play `set_stats` | `fe_validation` callback |
|---|---|---|
| Feeds AWX/AAP artifacts and workflow vars | yes | **no** |
| Costs tasks in the play | yes | **no** |
| Covers components the harness does not wrap (handlers, external roles) | no | **yes** |
| Per-task ok/changed/failed/skipped counts | no | **yes** |
| Works with no changes to any file | no | **yes** |

### What it does not remove

It does not shrink the in-play harness. The `set_stats` and bookkeeping tasks
are roughly 2 of the ~11 tasks each wrapper adds; the rest is the preflight and
postflight validation itself, which has to run in the play to gate execution.
Use the callback when you want the data without the AAP integration, or
alongside `set_stats` when you want both.

---

## Control variables

| Variable | Default | Effect |
|----------|---------|--------|
| `fe_validation_continue_on_error` | `false` | When `true`, a captured failure is recorded and published but **not** re-raised, so the run continues. Useful for assessment/reporting runs that should survey everything before reporting. |
| `fe_validation_min_ansible_version` | `'2.12'` | Minimum ansible-core version asserted by every preflight. |
| `<prefix>_required_vars` | `[]` | Variables the component's preflight requires to be defined. |

Example:

```bash
# Survey every component, record failures, never abort
ansible-playbook -i inventory site.yml -e fe_validation_continue_on_error=true
```

---

## Adding component-specific preflight checks

The generic preflight is intentionally minimal so it is safe everywhere. To
require component-specific inputs, set the component's `_required_vars` list —
no need to edit the harness. Put it in the role's `defaults/main.yml`, in group
vars, or on the command line:

```yaml
# cisco/roles/ise_profiling__probes/defaults/main.yml
fe_cisco_ise_profiling__probes_required_vars:
  - ise_hostname
  - ise_username
  - ise_password
```

A missing variable then fails in preflight — before any change is attempted —
and the published record names the exact variable.

For richer checks (reachability, credentials, capacity), add tasks to the
`preflight` section of the component's `block`.

---

## Tag behaviour

Existing tags are untouched. The harness's own tasks are tagged
`always` plus `preflight` / `postflight` / `rescue` / `validation`, and the
wrapper block itself carries **no** tags, so tag inheritance cannot widen the
selection of the original tasks.

The practical consequences:

- `--tags <existing_tag>` selects the same original tasks as before, and the
  harness still runs and still publishes statistics.
- `--tags validation` runs the preflight/postflight checks only.
- `--skip-tags always` disables the harness (and anything else the repository
  already tagged `always`).

---

## Behaviour changes to be aware of

1. **Failures are still failures.** The `rescue` re-raises by default, so exit
   codes and `PLAY RECAP` results are unchanged. What is new is the recorded
   `rescued=1` in the recap, and a published record describing the failure.

2. **`any_errors_fatal` aborts slightly later.** A rescued failure is not fatal
   until the `rescue` re-raises, which happens a few harness tasks after the
   original failing task. On a multi-host play, other hosts may progress a
   little further than before the abort takes effect.

3. **Each wrapped component adds ~10 bookkeeping tasks.** They are all
   `set_fact` / `assert` / `debug` / `set_stats` and run on the control node, so
   the cost is small, but task counts in `PLAY RECAP` are higher than before.

4. **A role failure skips that play's `post_tasks`.** Ansible removes the failed
   host, so the play-level record is not published for it — but the failing
   role published its own record, which is where the useful detail lives.

5. **Handlers flush at the end of the guarded block.** See
   [Handlers](#handlers). This is what brings a failing handler under the
   capture/publish path; without it a handler failure fails the run silently as
   far as the statistics are concerned. `pre_tasks` are covered by their own
   guarded block with the same flush.

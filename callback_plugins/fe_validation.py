# -*- coding: utf-8 -*-
"""Fourth Estate validation statistics, collected without any in-play tasks."""

from __future__ import annotations

import json
import os
import time

from ansible.plugins.callback import CallbackBase

DOCUMENTATION = r"""
    name: fe_validation
    type: aggregate
    short_description: Collect per-component run statistics with no task overhead
    version_added: "2.12"
    description:
      - Records status, timing and failure detail for every role, task file and
        playbook a run touches, keyed by the same component ids the in-play
        validation harness uses, and writes them as JSON at the end of the run.
      - Derives everything from callback events, so it costs no tasks and needs
        no changes to any playbook or role.
      - This does B(not) replace C(ansible.builtin.set_stats). Only C(set_stats)
        feeds AWX/AAP job artifacts and workflow variables; a callback cannot.
        The two are complementary - see docs/VALIDATION_AND_STATS.md.
    options:
      output_path:
        description: Where to write the JSON report. Empty disables the file.
        default: fe_validation_report.json
        env:
          - name: FE_VALIDATION_REPORT
        ini:
          - section: callback_fe_validation
            key: output_path
      show_summary:
        description: Print a per-component summary at the end of the run.
        type: bool
        default: true
        env:
          - name: FE_VALIDATION_SUMMARY
        ini:
          - section: callback_fe_validation
            key: show_summary
      include_harness_tasks:
        description:
          - Count the in-play harness's own bookkeeping tasks (Preflight,
            Postflight, Rescue, Always, Initialize, Guarded, Flush) in the
            per-component task totals.
        type: bool
        default: false
        env:
          - name: FE_VALIDATION_INCLUDE_HARNESS
        ini:
          - section: callback_fe_validation
            key: include_harness_tasks
    requirements:
      - enable in configuration
"""

HARNESS_MARKERS = (
    "| Preflight", "| Postflight", "| Rescue", "| Always", "| Initialize",
    "| Guarded", "| Flush notified handlers", "| No tasks are defined",
)


def component_id(path: str, role: str | None, root: str) -> tuple:
    """Map a task's source file to the (component id, type) the harness uses."""
    if not path:
        return (role or "unknown"), "role"
    path = path.split(":", 1)[0]
    try:
        rel = os.path.relpath(path, root)
    except ValueError:
        rel = path
    rel = rel.replace("\\", "/")
    if rel.startswith(".."):
        rel = path.replace("\\", "/").lstrip("/")
    for ext in (".yml", ".yaml"):
        if rel.endswith(ext):
            rel = rel[: -len(ext)]
            break
    parts = [p for p in rel.split("/") if p]
    if "roles" in parts:
        i = parts.index("roles")
        prefix = parts[:i]
        tail = parts[i + 2:]
        in_playbooks = "playbooks" in tail
        rest = [p for p in tail if p not in ("tasks", "playbooks")]
        base = "/".join(prefix + parts[i + 1:i + 2])
        if in_playbooks:
            return (base + "/" + "/".join(rest)) if rest else base, "playbook"
        if rest in ([], ["main"]):
            return base, "role"
        return base + "/" + "/".join(rest), "role-tasks"
    ident = "/".join(p for p in parts if p not in ("tasks", "playbooks"))
    return ident, "playbook"


class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = "aggregate"
    CALLBACK_NAME = "fe_validation"
    CALLBACK_NEEDS_ENABLED = True

    def __init__(self):
        super().__init__()
        self.components = {}
        self.root = os.getcwd()
        self._current = None
        self._current_type = "role"
        self._started_at = time.time()

    # ---- helpers ---------------------------------------------------------
    def _record(self, cid, ctype="role"):
        rec = self.components.get(cid)
        if rec is None:
            rec = {
                "component": cid,
                "type": ctype,
                "platform": cid.split("/")[0],
                "hosts": [],
                "status": "succeeded",
                "started_at": None,
                "ended_at": None,
                "duration_seconds": 0,
                "failed_task": "",
                "error": "",
                "tasks_ok": 0,
                "tasks_changed": 0,
                "tasks_failed": 0,
                "tasks_skipped": 0,
                "tasks_unreachable": 0,
            }
            self.components[cid] = rec
        return rec

    def _touch(self, result, outcome):
        cid = self._current
        if cid is None:
            return
        rec = self._record(cid, self._current_type)
        if rec["_skip"] if "_skip" in rec else False:
            return
        now = time.time()
        if rec["started_at"] is None:
            rec["started_at"] = now
        rec["ended_at"] = now
        host = getattr(result, "_host", None)
        name = host.get_name() if host is not None else None
        if name and name not in rec["hosts"]:
            rec["hosts"].append(name)
        rec[f"tasks_{outcome}"] += 1
        if outcome in ("failed", "unreachable"):
            task = getattr(result, "_task", None)
            rec["status"] = "failed"
            if not rec["failed_task"] and task is not None:
                rec["failed_task"] = task.get_name()
            if not rec["error"]:
                res = getattr(result, "_result", {}) or {}
                rec["error"] = str(res.get("msg", "no error detail reported"))

    # ---- events ----------------------------------------------------------
    def v2_playbook_on_task_start(self, task, is_conditional):
        name = task.get_name() or ""
        if not self.get_option("include_harness_tasks") and \
                any(m in name for m in HARNESS_MARKERS):
            self._current = None
            return
        role = task._role.get_name() if getattr(task, "_role", None) else None
        self._current, self._current_type = component_id(
            task.get_path(), role, self.root)

    v2_playbook_on_handler_task_start = v2_playbook_on_task_start

    def v2_runner_on_ok(self, result):
        changed = (result._result or {}).get("changed", False)
        self._touch(result, "changed" if changed else "ok")

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self._touch(result, "ok" if ignore_errors else "failed")

    def v2_runner_on_skipped(self, result):
        self._touch(result, "skipped")

    def v2_runner_on_unreachable(self, result):
        self._touch(result, "unreachable")

    # ---- output ----------------------------------------------------------
    def v2_playbook_on_stats(self, stats):
        results = {}
        for cid, rec in sorted(self.components.items()):
            rec = dict(rec)
            rec.pop("_skip", None)
            start, end = rec["started_at"], rec["ended_at"]
            rec["duration_seconds"] = round((end - start), 3) if start and end else 0
            for key in ("started_at", "ended_at"):
                if rec[key]:
                    rec[key] = time.strftime(
                        "%Y-%m-%dT%H:%M:%SZ", time.gmtime(rec[key]))
            results[cid] = rec

        failed = sorted(c for c, r in results.items() if r["status"] != "succeeded")
        report = {
            "fe_validation_results": results,
            "fe_validation_executions": len(results),
            "fe_validation_succeeded": len(results) - len(failed),
            "fe_validation_failed": len(failed),
            "fe_validation_failed_components": failed,
            "fe_validation_duration_seconds": round(time.time() - self._started_at, 3),
            "collected_by": "fe_validation callback (no in-play tasks)",
        }

        path = self.get_option("output_path")
        if path:
            try:
                with open(path, "w", encoding="utf-8") as handle:
                    json.dump(report, handle, indent=2, sort_keys=True)
            except OSError as exc:
                self._display.warning(f"fe_validation: could not write {path}: {exc}")

        if self.get_option("show_summary"):
            self._display.banner("FE VALIDATION")
            self._display.display(
                f"{report['fe_validation_executions']} components, "
                f"{report['fe_validation_succeeded']} succeeded, "
                f"{report['fe_validation_failed']} failed, "
                f"{report['fe_validation_duration_seconds']}s total")
            for cid, rec in results.items():
                line = (f"  {rec['status']:<9} {rec['duration_seconds']:>7.2f}s  {cid}"
                        f"  (ok={rec['tasks_ok']} changed={rec['tasks_changed']} "
                        f"failed={rec['tasks_failed']} skipped={rec['tasks_skipped']})")
                self._display.display(line)
                if rec["failed_task"]:
                    self._display.display(
                        f"             failed at {rec['failed_task']!r}: {rec['error']}")
            if path:
                self._display.display(f"  report written to {path}")

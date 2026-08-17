#!/usr/bin/env python3
"""Fail if a playbook/role uses a collection that no requirements.yml declares.

Why this exists
---------------
The enforced `ansible-lint` gate runs with `--offline` and no collections
installed, so its `syntax-check[unknown-module]` findings fire for *every*
non-builtin module and are permanently baselined in `.ansible-lint-ignore`.
That makes the rule useless for catching the failure it is named after: a
module the user cannot actually install.

This check finds that class of bug deterministically and offline. It does not
verify that a module *exists* inside a collection (that needs Galaxy); it
verifies that every collection the repository actually calls is declared
somewhere a user would install from:

  * the repo-root requirements.yml, or
  * the platform's own <platform>/requirements.yml, or
  * any nested requirements.yml under that platform.

Usage:
    python3 scripts/check_collections.py [path ...]   # defaults to repo root
Exit code 0 = every used collection is declared; 1 = at least one gap.
"""
from __future__ import annotations

import glob
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

for _tag in ("!unsafe", "!vault"):
    yaml.SafeLoader.add_constructor(
        _tag, lambda loader, node: loader.construct_scalar(node)
    )

SKIP_DIRS = (".git/", ".github/", ".vscode/", "docs/", "scripts/")

# Keys that appear alongside a module in a task but are not the module itself.
NON_MODULE_KEYS = {
    "name", "when", "tags", "block", "rescue", "always", "loop", "with_items",
    "with_dict", "with_fileglob", "with_nested", "with_subelements", "register",
    "become", "become_user", "become_method", "vars", "notify", "delegate_to",
    "delegate_facts", "ignore_errors", "ignore_unreachable", "changed_when",
    "failed_when", "no_log", "loop_control", "until", "retries", "delay",
    "run_once", "check_mode", "environment", "args", "any_errors_fatal",
    "throttle", "listen", "connection", "remote_user", "diff", "timeout",
    "poll", "async", "collections", "module_defaults", "local_action",
}

PLAY_KEYS = {
    "hosts", "import_playbook", "ansible.builtin.import_playbook", "roles",
    "pre_tasks", "post_tasks", "tasks", "handlers", "vars_files", "serial",
    "strategy", "force_handlers", "max_fail_percentage", "order", "vars_prompt",
    "gather_facts",
}


def iter_yaml(paths):
    for base in paths:
        if os.path.isfile(base):
            yield base
            continue
        for pattern in ("**/*.yml", "**/*.yaml"):
            for f in glob.glob(os.path.join(base, pattern), recursive=True):
                rel = os.path.relpath(f).replace("\\", "/")
                if any(rel.startswith(s) for s in SKIP_DIRS):
                    continue
                yield f


def walk_tasks(tasks):
    for task in tasks or []:
        if not isinstance(task, dict):
            continue
        yield task
        for section in ("block", "rescue", "always"):
            if isinstance(task.get(section), list):
                yield from walk_tasks(task[section])


def task_lists(data):
    """Yield every task list in a playbook or task file."""
    if not isinstance(data, list):
        return
    is_play = any(isinstance(i, dict) and (PLAY_KEYS & set(i)) and "hosts" in i
                  for i in data)
    if is_play:
        for play in data:
            if not isinstance(play, dict):
                continue
            for section in ("pre_tasks", "tasks", "post_tasks", "handlers"):
                if isinstance(play.get(section), list):
                    yield play[section]
    else:
        yield data


def used_collections(paths):
    """{collection: {file, ...}} for every FQCN module actually called."""
    found = {}
    for path in iter_yaml(paths):
        try:
            with open(path, encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
        except (yaml.YAMLError, OSError):
            continue
        for tasks in task_lists(data):
            for task in walk_tasks(tasks):
                if "block" in task:
                    continue
                for key in task:
                    if key in NON_MODULE_KEYS or key.count(".") < 2:
                        continue
                    collection = ".".join(key.split(".")[:2])
                    if collection == "ansible.builtin":
                        continue
                    found.setdefault(collection, set()).add(
                        os.path.relpath(path).replace("\\", "/"))
    return found


def declared_in(req_files):
    names = set()
    for req in req_files:
        try:
            with open(req, encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
        except (yaml.YAMLError, OSError):
            continue
        items = data.get("collections") if isinstance(data, dict) else data
        for item in items or []:
            name = item.get("name") if isinstance(item, dict) else item
            if isinstance(name, str):
                names.add(name)
    return names


def main(argv):
    paths = argv[1:] or ["."]
    used = used_collections(paths)
    root_declared = declared_in(glob.glob("requirements.yml"))

    gaps = []
    for collection, files in sorted(used.items()):
        platforms = sorted({f.split("/")[0] for f in files})
        for platform in platforms:
            local = declared_in(
                glob.glob(f"{platform}/**/requirements.yml", recursive=True))
            if collection in (local | root_declared):
                continue
            example = sorted(f for f in files if f.startswith(platform + "/"))[0]
            gaps.append((platform, collection, example, len(
                [f for f in files if f.startswith(platform + "/")])))

    print(f"Collections used: {len(used)}")
    print(f"Declaration gaps: {len(gaps)}")
    if gaps:
        print("\nEach of these is called by a playbook or role but is not declared in")
        print("that platform's requirements.yml (or the repo-root one), so")
        print("`ansible-galaxy collection install -r requirements.yml` will not")
        print("install it and the run fails with a module-not-found error:\n")
        for platform, collection, example, count in gaps:
            print(f"  {platform}: {collection}")
            print(f"      used in {count} file(s), e.g. {example}")
        return 1
    print("Every collection in use is declared in a requirements.yml.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

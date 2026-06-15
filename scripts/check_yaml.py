#!/usr/bin/env python3
"""Fail if any YAML file in the repository does not parse.

This is the cheapest, most reliable guard against the single biggest class of
"looks ready but won't run" bugs: YAML that aborts `ansible-playbook` before any
task executes. It does NOT require Ansible collections to be installed, so it
works on any runner regardless of Galaxy access.

Usage:
    python3 scripts/check_yaml.py [path ...]   # defaults to repo root
Exit code 0 = all files parse; 1 = one or more parse failures.
"""
from __future__ import annotations

import glob
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

SKIP_DIRS = (".git/", ".github/", ".vscode/")


def iter_yaml(paths):
    for base in paths:
        if os.path.isfile(base):
            yield base
            continue
        for pattern in ("**/*.yml", "**/*.yaml"):
            for f in glob.glob(os.path.join(base, pattern), recursive=True):
                if any(s in f.replace("\\", "/") for s in SKIP_DIRS):
                    continue
                yield f


def main(argv):
    paths = argv[1:] or ["."]
    failures = []
    total = 0
    for f in iter_yaml(paths):
        total += 1
        try:
            with open(f, encoding="utf-8") as fh:
                list(yaml.safe_load_all(fh))
        except yaml.YAMLError as exc:
            mark = getattr(exc, "problem_mark", None)
            where = f":{mark.line + 1}" if mark else ""
            msg = str(exc).splitlines()[0]
            failures.append(f"{f}{where}: {msg}")

    print(f"Checked {total} YAML files.")
    if failures:
        print(f"\n{len(failures)} file(s) failed to parse:\n")
        for line in failures:
            print(f"  - {line}")
        return 1
    print("All YAML files parse successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

#!/usr/bin/env python3
"""Verify that what the documentation claims about this repository is true.

The README says the repository statistics "are verified in CI". They were not:
yamllint and a YAML parse check verify that YAML parses, and say nothing about
role counts, platform counts or compliance coverage. Three consequences had
accumulated by the time this script was written:

  * KNOWN_LIMITATIONS.md understated three platforms (azure 7 where 15 exist).
  * README.md claimed 8 roles each for MySQL and Oracle in one section while
    another section correctly said they had none.
  * COMPLIANCE_MAPPING.md -- the document an agency reads to decide what this
    repository covers -- claimed MySQL STIG V2R2 and Oracle STIG V2R4 coverage,
    naming control IDs, for two platforms that contained no automation at all.

The last one is the reason this runs in CI. A stale role count is untidy; an
unbacked compliance claim is a different kind of problem.

    ./scripts/check_docs_claims.py          # what CI runs
    ./scripts/check_docs_claims.py --stats  # print the real numbers
"""
from __future__ import annotations

import argparse
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def role_dirs() -> list[str]:
    """Every directory that is a role with tasks, repo-relative."""
    out = []
    for dirpath, dirnames, _ in os.walk(REPO_ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        if os.path.basename(dirpath) != "roles":
            continue
        for name in sorted(dirnames):
            role = os.path.join(dirpath, name)
            if os.path.isdir(os.path.join(role, "tasks")):
                out.append(os.path.relpath(role, REPO_ROOT))
    return out


def roles_under(platform: str) -> list[str]:
    prefix = platform.rstrip("/") + os.sep
    return [r for r in role_dirs() if r.startswith(prefix)]


def _platform_dirs() -> list[str]:
    """Platform directories, defined exactly as stamp_platform_versions.py does,
    so the two gates cannot disagree about what a platform is."""
    import importlib.util
    path = os.path.join(REPO_ROOT, "scripts", "stamp_platform_versions.py")
    spec = importlib.util.spec_from_file_location("_stamp", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.platform_dirs()


def real_stats() -> dict:
    yml = sum(1 for dp, _, fn in os.walk(REPO_ROOT)
              if ".git" not in dp.split(os.sep)
              for f in fn if f.endswith((".yml", ".yaml")))
    j2 = sum(1 for dp, _, fn in os.walk(REPO_ROOT)
             if ".git" not in dp.split(os.sep)
             for f in fn if f.endswith(".j2"))
    readmes = sum(1 for dp, _, fn in os.walk(REPO_ROOT)
                  if ".git" not in dp.split(os.sep)
                  for f in fn if f.upper() == "README.MD")
    inventories = sum(1 for dp, _, fn in os.walk(REPO_ROOT)
                      if ".git" not in dp.split(os.sep)
                      for f in fn if f.startswith("inventory") and "example" in f)
    return {"roles": len(role_dirs()), "yaml": yml, "templates": j2,
            "readmes": readmes, "inventories": inventories}


def check_readme_stats(problems: list[str]) -> None:
    """The headline 'Total Roles' must match reality."""
    path = os.path.join(REPO_ROOT, "README.md")
    text = open(path).read()
    stats = real_stats()
    m = re.search(r"\*\*Total Roles:\*\*\s*([\d,]+)", text)
    if not m:
        problems.append("README.md: no '**Total Roles:**' line to check")
    elif int(m.group(1).replace(",", "")) != stats["roles"]:
        problems.append("README.md claims %s roles; %d roles with tasks/ exist"
                        % (m.group(1), stats["roles"]))

    # Only claims about capability are checked. File and README counts drift
    # with every commit that adds a file, so gating them would fail nearly every
    # PR for no benefit; they are marked approximate in the README instead.
    platforms = len(_platform_dirs())
    m = re.search(r"\*\*Technology Platforms:\*\*\s*([\d,]+)", text)
    if not m:
        problems.append("README.md: no '**Technology Platforms:**' line to check")
    elif int(m.group(1).replace(",", "")) != platforms:
        problems.append("README.md claims %s platforms; %d exist"
                        % (m.group(1), platforms))


def check_platform_paths(problems: list[str]) -> None:
    """Every platform path named in a doc table must exist and hold roles.

    This is the check that catches a compliance claim for a platform that was
    deleted, or never had automation in the first place.
    """
    for doc in ("docs/COMPLIANCE_MAPPING.md", "docs/CUSTOMER_QUICK_START.md",
                "docs/STIG_COVERAGE_MATRIX.md"):
        path = os.path.join(REPO_ROOT, doc)
        if not os.path.exists(path):
            continue
        for line in open(path):
            if not line.lstrip().startswith("|"):
                continue
            for claimed in re.findall(r"`([a-z0-9_]+(?:/[a-z0-9_]+)*)/`", line):
                full = os.path.join(REPO_ROOT, claimed)
                if not os.path.isdir(full):
                    problems.append("%s names `%s/`, which does not exist"
                                    % (doc, claimed))
                elif not roles_under(claimed):
                    problems.append(
                        "%s claims coverage for `%s/`, which contains no roles"
                        % (doc, claimed))


def check_named_roles(problems: list[str]) -> None:
    """A `<platform>/roles/<name>` path named in a doc must exist.

    Only full paths are checked. A bare backticked identifier is too ambiguous
    to flag: in this document it can be a role, a variable
    (`fourth_estate_mandatory_mfa`), a platform directory, or a role explicitly
    annotated as not implemented. Checking the unambiguous form catches the
    failure that matters -- a control mapped to something that is not there --
    without inventing findings.
    """
    for doc in ("docs/COMPLIANCE_MAPPING.md", "docs/CUSTOMER_QUICK_START.md",
                "docs/STIG_COVERAGE_MATRIX.md"):
        path = os.path.join(REPO_ROOT, doc)
        if not os.path.exists(path):
            continue
        for line in open(path):
            for named in re.findall(r"`([a-z0-9_]+/roles/[a-z0-9_]+)`", line):
                if not os.path.isdir(os.path.join(REPO_ROOT, named)):
                    problems.append("%s names `%s`, which does not exist"
                                    % (doc, named))
                elif (not os.path.isdir(os.path.join(REPO_ROOT, named, "tasks"))
                      and "not implemented" not in line.lower()):
                    problems.append(
                        "%s cites `%s`, which has no tasks/ -- say so on that "
                        "line, or implement it" % (doc, named))


def check_known_limitations(problems: list[str]) -> None:
    """The 'Roles remaining' column must match the roles that exist."""
    path = os.path.join(REPO_ROOT, "docs/KNOWN_LIMITATIONS.md")
    if not os.path.exists(path):
        return
    label_to_dir = {
        "ansible tower / aap": "ansible_tower", "mysql / mariadb": "databases/mysql",
        "oracle database": "databases/oracle", "windows server": "windows",
        "fortinet fortigate": "fortinet", "microsoft azure": "azure",
        "tenable": "tenable", "hashicorp vault": "hashicorp_vault",
        "f5 big-ip": "f5_bigip", "netapp ontap": "netapp", "veeam": "veeam",
        "elk stack": "elk_stack", "cohesity": "cohesity", "servicenow": "servicenow",
        "prometheus/grafana": "prometheus_grafana",
    }
    for line in open(path):
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|", line)
        if not m:
            continue
        for label in [p.strip().lower() for p in m.group(1).split(",")]:
            platform = label_to_dir.get(label)
            if not platform:
                continue
            if not os.path.isdir(os.path.join(REPO_ROOT, platform)):
                problems.append("KNOWN_LIMITATIONS.md has a row for '%s', but "
                                "%s/ does not exist" % (m.group(1).strip(), platform))
                continue
            actual = len(roles_under(platform))
            if actual != int(m.group(2)):
                problems.append("KNOWN_LIMITATIONS.md says %s has %s role(s); "
                                "%d exist" % (platform, m.group(2), actual))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--stats", action="store_true",
                        help="print the real numbers and exit")
    args = parser.parse_args()

    if args.stats:
        for key, value in real_stats().items():
            print("%-14s %d" % (key, value))
        return 0

    problems: list[str] = []
    check_readme_stats(problems)
    check_platform_paths(problems)
    check_named_roles(problems)
    check_known_limitations(problems)

    if problems:
        print("Documentation claims that are not backed by the repository:\n")
        for p in sorted(set(problems)):
            print("  %s" % p)
        print("\n%d problem(s). Fix the documentation, or the repository, so the"
              " two agree." % len(set(problems)))
        return 1
    print("Every documented platform, role and count matches the repository.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

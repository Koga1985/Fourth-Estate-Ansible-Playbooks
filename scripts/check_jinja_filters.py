#!/usr/bin/env python3
"""Fail if a Jinja expression cannot parse, or uses a filter or test that does not exist.

Why this exists
---------------
A Jinja expression is only parsed when it is actually rendered. A broken one is
valid YAML, passes `yamllint`, passes `ansible-lint` and passes
`ansible-playbook --syntax-check`; it fails at run time, on the customer's
machine.

That is not hypothetical. Five such expressions shipped in this repository:

  * `| splitlines` (4 sites, dragos) -- a Python string method, not a filter, so
    reading the findings CSV always failed and ticket creation could never run.
  * `| enumerate` (2 sites, infoblox) -- a Python builtin, not a filter.
  * `| all` (1 site, policy_as_code) -- no such filter, so the test that was
    meant to verify the policy directories raised a template error instead of
    asserting anything.
  * `| aci_dns_servers` (1 site, cisco) -- an expression that piped into a
    *variable*. The task was `no_log`, so it would have failed with no context.
  * Doubled `{{` / `}}` braces used to keep literal braces in an embedded
    PowerShell block (vmware). Doubling escapes braces in Python's str.format,
    not in Jinja: Jinja reads `{{` as the start of an expression and then chokes
    on the shell syntax inside it. Use `{% raw %} ... {% endraw %}` instead.

None of them were reachable by the molecule gate: they sit behind
`apply_changes`, behind credential preflights, in a role that needs a real
vCenter, or in a test playbook that is not a role. A static check reaches all of
them, because it never has to run the task.

How it works, and why it never executes anything
------------------------------------------------
Each string scalar containing a Jinja block is *parsed* -- never rendered --
with `jinja2.Environment().parse()`. Parsing reports malformed expressions and
yields an AST whose filter and test names are read directly, so no regular
expression has to guess where an expression begins or ends. Each distinct name
is then resolved once against a real `Templar`, using a trivial `{{ 'x' | name }}`
probe.

Rendering the repository's own expressions would be unsafe: they contain
`lookup('pipe', ...)`, `lookup('file', ...)` and `lookup('template', ...)`, and
rendering them would run commands and read files. This gate must never do that,
which is why it parses and probes instead of templating.

What it does and does not prove
-------------------------------
It proves every Jinja expression parses and every filter and test name resolves.
It does not evaluate expressions, so it cannot catch a filter applied to the
wrong operand, nor an operator-precedence error such as `not x | lower` -- which
parses cleanly but is a *constant*, because `lower` returns an always-truthy
string. Those need the expression to actually run: that is the molecule gate's
job, and the two gates are complementary.

Collection-provided names
-------------------------
This check runs offline, like the other enforced gates, so a filter or test that
ships in a collection cannot resolve here and would look like a bug. Those names
are allowlisted below, each tied to the collection that provides it. Adding a
name here asserts it is real and installable -- it is not a way to silence an
inconvenient finding.

Usage:
    python3 scripts/check_jinja_filters.py [path ...]   # defaults to repo root
Exit code 0 = everything parses and resolves; 1 = at least one does not.
"""
from __future__ import annotations

import os
import sys
import warnings

warnings.filterwarnings("ignore")
# Keep the output clean: this is a gate, not a playbook run.
os.environ.setdefault("ANSIBLE_DEPRECATION_WARNINGS", "False")
os.environ.setdefault("ANSIBLE_SYSTEM_WARNINGS", "False")

from pathlib import Path  # noqa: E402

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

try:
    import jinja2
    from jinja2 import nodes
except ImportError:
    sys.exit("Jinja2 is required: pip install jinja2")

try:
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar, trust_as_template
except ImportError:
    sys.exit("ansible-core is required: pip install ansible-core")

SKIP_DIRS = (".git/", ".github/", ".vscode/", "docs/", "scripts/")
SUFFIXES = (".yml", ".yaml", ".j2")
HAS_JINJA = ("{{", "{%")

# Baseline of known-broken expressions, in the same spirit as
# .ansible-lint-ignore: the gate blocks new breakage while these are tracked.
BASELINE_FILE = ".jinja-check-ignore"


def load_baseline(path):
    """Return {relative path: reason} from the baseline file."""
    baseline = {}
    try:
        text = Path(path).read_text()
    except OSError:
        return baseline
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        baseline[parts[0]] = parts[1] if len(parts) > 1 else ""
    return baseline

# Filters and tests provided by a collection, so unresolvable in this offline
# gate. name -> collection that ships it.
COLLECTION_NAMES = {
    "ipaddr": "ansible.utils / ansible.netcommon",
    "ipv4": "ansible.utils / ansible.netcommon",
    "ipv6": "ansible.utils / ansible.netcommon",
    "ipmath": "ansible.utils / ansible.netcommon",
    "ipsubnet": "ansible.utils / ansible.netcommon",
    "json_query": "community.general",
}


class _UnsafeMarker(str):
    """A scalar that carried a !unsafe tag: Ansible never templates it."""


def _scalar_or_empty(loader, node):
    try:
        return loader.construct_scalar(node)
    except Exception:  # noqa: BLE001 - a non-scalar tagged node carries no template
        return ""


class _Loader(yaml.SafeLoader):
    pass


_Loader.add_constructor("!unsafe", lambda ldr, n: _UnsafeMarker(ldr.construct_scalar(n)))
_Loader.add_constructor("!vault", lambda ldr, n: "")
_Loader.add_multi_constructor("!", lambda ldr, suffix, n: _scalar_or_empty(ldr, n))


def iter_scalars(node):
    """Yield every string scalar in a loaded document, skipping !unsafe ones."""
    if isinstance(node, _UnsafeMarker):
        return
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for key, value in node.items():
            yield from iter_scalars(key)
            yield from iter_scalars(value)
    elif isinstance(node, (list, tuple)):
        for value in node:
            yield from iter_scalars(value)


def templates_in(path):
    """Yield every templatable string in a file."""
    try:
        raw = path.read_text(errors="replace")
    except OSError:
        return
    if not any(marker in raw for marker in HAS_JINJA):
        return
    if path.suffix == ".j2":
        yield raw
        return
    try:
        docs = list(yaml.load_all(raw, Loader=_Loader))
    except yaml.YAMLError:
        # check_yaml.py is the gate for unparsable YAML; do not double-report.
        return
    for doc in docs:
        for scalar in iter_scalars(doc):
            if any(marker in scalar for marker in HAS_JINJA):
                yield scalar


class _quiet_stderr:
    """Silence fd 2 for the duration of the block.

    Probing a name renders a trivial template, and some filters make Ansible's
    display emit a warning (tojson returns Markup, for instance). Those
    warnings are about the probe, not about the repository, so they would only
    mislead someone reading this gate's output. Ansible writes them to the real
    file descriptor, so a Python-level redirect is not enough.
    """

    def __enter__(self):
        self._saved = os.dup(2)
        self._devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(self._devnull, 2)
        return self

    def __exit__(self, *exc):
        os.dup2(self._saved, 2)
        os.close(self._devnull)
        os.close(self._saved)
        return False


def line_of(path, snippet):
    """Best-effort line number for a failing template, for a clickable report."""
    stripped = snippet.strip()
    if not stripped:
        return 1
    head = stripped.splitlines()[0][:60]
    try:
        for number, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
            if head and head in line:
                return number
    except OSError:
        pass
    return 1


def main(argv):
    roots = [Path(p) for p in (argv[1:] or ["."])]
    env = jinja2.Environment()
    baseline = load_baseline(BASELINE_FILE)
    baseline_hit = set()

    files = 0
    parsed = 0
    syntax_errors = []
    names = {}  # name -> {"kind": filter|test, "files": set}

    for root in roots:
        candidates = [root] if root.is_file() else sorted(root.rglob("*"))
        for path in candidates:
            rel = str(path).lstrip("./")
            if path.is_dir() or path.suffix not in SUFFIXES:
                continue
            if any(part in rel for part in SKIP_DIRS):
                continue
            files += 1
            for snippet in templates_in(path):
                try:
                    ast = env.parse(snippet)
                except jinja2.TemplateSyntaxError as exc:
                    if rel in baseline:
                        baseline_hit.add(rel)
                        continue
                    syntax_errors.append((rel, line_of(path, snippet), str(exc), snippet))
                    continue
                parsed += 1
                for node in ast.find_all(nodes.Filter):
                    entry = names.setdefault(node.name, {"kind": "filter", "files": set()})
                    entry["files"].add(rel)
                for node in ast.find_all(nodes.Test):
                    entry = names.setdefault(node.name, {"kind": "test", "files": set()})
                    entry["files"].add(rel)

    templar = Templar(loader=DataLoader())
    unresolved = {}
    allowlisted = set()
    for name, entry in sorted(names.items()):
        if name in COLLECTION_NAMES or "." in name:
            allowlisted.add(name)
            continue
        probe = "{{ 'x' | %s }}" % name if entry["kind"] == "filter" else "{{ 'x' is %s }}" % name
        try:
            with _quiet_stderr():
                templar.template(trust_as_template(probe))
        except Exception as exc:  # noqa: BLE001
            text = str(exc)
            if "No filter named" in text or "No test named" in text:
                unresolved[name] = entry

    print(f"Files scanned: {files}")
    print(f"Jinja expressions parsed: {parsed}")
    print(f"Distinct filters and tests: {len(names)}")
    if allowlisted:
        print(f"Allowlisted as collection-provided: {', '.join(sorted(allowlisted))}")
    print(f"Malformed expressions: {len(syntax_errors)}")
    print(f"Unresolvable names: {len(unresolved)}")
    if baseline:
        print(f"Baselined in {BASELINE_FILE}: {len(baseline)} "
              f"({len(baseline_hit)} still failing)")

    # A baselined path that no longer fails means the baseline is stale. Say so
    # rather than letting a fixed entry sit there forever pretending to be a bug.
    stale = sorted(set(baseline) - baseline_hit)
    if stale:
        print(f"\nThese {BASELINE_FILE} entries no longer have findings. Remove them:")
        for rel in stale:
            print(f"  {rel}")

    if not syntax_errors and not unresolved:
        if stale:
            return 1
        print("Every Jinja expression parses, and every filter and test resolves.")
        if baseline_hit:
            print(f"({len(baseline_hit)} known-broken file(s) tracked in {BASELINE_FILE}.)")
        return 0

    if syntax_errors:
        print("\nThese expressions do not parse. Each fails at run time, not at lint time:\n")
        for rel, line, message, snippet in syntax_errors:
            print(f"  {rel}:{line}")
            print(f"      {message}")
            print(f"      in: {' '.join(snippet.split())[:110]}...")
            print()
        print("  To keep literal braces in an embedded script, wrap the block in")
        print("  {% raw %} ... {% endraw %}. Doubling them escapes braces in Python's")
        print("  str.format, not in Jinja.\n")

    if unresolved:
        print("\nThese filters or tests do not exist:\n")
        for name, entry in unresolved.items():
            print(f"  '{name}' ({entry['kind']}) used in:")
            for rel in sorted(entry["files"]):
                print(f"      {rel}")
            print()
        print("  A Python method or builtin is not a Jinja filter: use .method() or")
        print("  the Jinja equivalent. An expression must never pipe into a variable.")
        print("  If it comes from a collection, add it to COLLECTION_NAMES here.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
"""Fail on a Jinja expression that cannot parse, names a filter or test that does
not exist, renders a Python boolean into JSON, or reads an Ansible keyword as a
variable.

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
  * `{{ x | bool }}` in a JSON template (gcp, 5 fields). `bool` renders Python's
    True/False, capitalised, which is not valid JSON.
  * `{{ environment | default('production') }}` (prometheus, 3 roles).
    `environment` is a play/task keyword, always defined, so `default()` never
    fired and the value rendered as []. Every Prometheus deployment labelled its
    metrics environment: '[]'.

None of them were reachable by the molecule gate: they sit behind
`apply_changes`, behind credential preflights, in a role that needs a real
vCenter, or in a test playbook that is not a role. A static check reaches all of
them, because it never has to run the task.

The last two are different in kind from the first four: those expressions parse
and their filters exist, so nothing rejects them -- they simply render the wrong
thing. They are checked here because the mistake is recognisable from the AST
alone, which makes it cheap to enforce rather than remember.

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
It proves every Jinja expression parses, every filter and test name resolves,
no JSON template renders a Python boolean, and no expression reads an Ansible
keyword as a variable.

It does not evaluate expressions, so it cannot catch a filter applied to the
wrong operand, nor an operator-precedence error such as `not x | lower` -- which
parses cleanly but is a *constant*, because `lower` returns an always-truthy
string. Those need the expression to actually run: that is the molecule gate's
job, and the two gates are complementary.

The two rendering checks are deliberately narrow, so that a finding is always a
real defect:

  * `| bool` is flagged only in a .json.j2 file, and only as the OUTERMOST
    filter. `| bool | lower` is the fix, not a finding, and `| bool` in a YAML
    template is fine because YAML accepts True. A template that emits JSON under
    another name is not covered.
  * A keyword is flagged only when read as a bare name that the template does
    not bind itself. `labels.environment` is an attribute of another variable,
    and `{% for environment in ... %}{{ environment }}` is the loop's own
    variable; neither is a finding.

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

# Ansible play/task keywords that are ALWAYS defined, so reading one as if it
# were an ordinary variable silently yields the keyword's value and `default()`
# never fires. `environment` is the one that shipped: it is the play's
# environment, an empty list by default, so
# `{{ environment | default('production') }}` rendered [] -- and every
# Prometheus deployment labelled its metrics environment: '[]'.
#
# Only names that are useless to read are listed. Magic variables that are
# normal to read (hostvars, groups, inventory_hostname, role_name, omit) are
# deliberately absent: reading those is correct Ansible.
RESERVED_READS = {
    "environment": "the play/task environment keyword (always defined, a list)",
}


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


def json_bool_outputs(ast):
    """Yield expressions in a JSON template whose OUTERMOST filter is `bool`.

    `{{ x | bool }}` renders Python's True/False, capitalised, which is not
    valid JSON. `{{ x | bool | lower }}` is correct and must not be flagged, so
    only the outermost filter is examined: once another filter wraps it, the
    output is a string and the capitalisation is gone. The fix is to append
    `| lower` rather than to drop `| bool`, because the coercion still matters
    -- a value of "yes" must render true, and `| lower` alone would emit the
    literal yes and break the document.
    """
    for out in ast.find_all(nodes.Output):
        for child in out.nodes:
            if isinstance(child, nodes.Filter) and child.name == "bool":
                yield child


def locally_bound(ast):
    """Names the template binds itself, via a for target, a set, or a macro arg.

    A read of such a name refers to the local binding, not to Ansible's
    keyword, so it must not be flagged: inside
    `{% for environment in env_list %}{{ environment }}{% endfor %}` the read is
    the loop variable. Jinja marks the loop target as a store but leaves reads
    of it inside the body as loads, so the ctx alone is not enough.
    """
    bound = set()
    for node in ast.find_all(nodes.Name):
        if getattr(node, "ctx", "load") in ("store", "param"):
            bound.add(node.name)
    for node in ast.find_all(nodes.Macro):
        for arg in node.args:
            if isinstance(arg, nodes.Name):
                bound.add(arg.name)
    return bound


def reserved_reads(ast):
    """Yield names read as variables that are really Ansible keywords.

    An attribute access such as `prometheus_external_labels.environment` is a
    Getattr on another name, so a dict key called environment is unaffected.
    """
    bound = locally_bound(ast)
    for node in ast.find_all(nodes.Name):
        if (node.name in RESERVED_READS
                and getattr(node, "ctx", "load") == "load"
                and node.name not in bound):
            yield node


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
    json_bools = []
    reserved = []
    scanned = set()
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
            scanned.add(rel)
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

                if rel in baseline:
                    continue
                # JSON booleans: only meaningful where the output really is JSON.
                if path.name.endswith(".json.j2"):
                    for _ in json_bool_outputs(ast):
                        json_bools.append((rel, line_of(path, snippet), snippet))
                        break
                for node in reserved_reads(ast):
                    reserved.append((rel, line_of(path, snippet), node.name, snippet))
                    break

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
    print(f"`| bool` rendering a JSON boolean: {len(json_bools)}")
    print(f"Reads of an Ansible keyword as a variable: {len(reserved)}")
    if baseline:
        print(f"Baselined in {BASELINE_FILE}: {len(baseline)} "
              f"({len(baseline_hit)} still failing)")

    # A baselined path that no longer fails means the baseline is stale. Say so
    # rather than letting a fixed entry sit there forever pretending to be a bug.
    # Only judge entries this run actually looked at: scanning a subdirectory
    # reaches none of the others, and they are not stale merely for being
    # outside the scan.
    stale = sorted((set(baseline) & scanned) - baseline_hit)
    if stale:
        print(f"\nThese {BASELINE_FILE} entries no longer have findings. Remove them:")
        for rel in stale:
            print(f"  {rel}")

    if not syntax_errors and not unresolved and not json_bools and not reserved:
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

    if json_bools:
        print("\nThese render a Python boolean into a JSON document:\n")
        for rel, line, snippet in json_bools:
            print(f"  {rel}:{line}")
            print(f"      in: {' '.join(snippet.split())[:110]}...")
            print()
        print("  `| bool` renders True/False, capitalised, which is not valid JSON.")
        print("  Append `| lower`, do not drop `| bool`: the coercion still matters, so")
        print("  that a value of \"yes\" renders true where `| lower` alone would emit the")
        print("  literal yes and break the document. (`| bool` is fine in a YAML template:")
        print("  YAML accepts True.)\n")

    if reserved:
        print("\nThese read an Ansible keyword as if it were a variable:\n")
        for rel, line, name, snippet in reserved:
            print(f"  {rel}:{line}  reads '{name}'")
            print(f"      {name} is {RESERVED_READS[name]}")
            print(f"      in: {' '.join(snippet.split())[:110]}...")
            print()
        print("  The keyword is always defined, so `| default(...)` never fires and the")
        print("  expression silently yields the keyword's value. Rename the variable --")
        print("  this repository uses fourth_estate_environment for the environment.")
        print("  Reading a dict key of the same name (labels.environment) is unaffected.\n")

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

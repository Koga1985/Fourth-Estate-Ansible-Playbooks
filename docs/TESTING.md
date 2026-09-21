# Testing

This document describes what is actually tested in this repository, what is
not, and how to add coverage.

---

## Table of Contents

- [The gates](#the-gates)
- [Molecule coverage](#molecule-coverage)
- [Which roles are onboarded, and why only those](#which-roles-are-onboarded-and-why-only-those)
- [Adding a role to the molecule gate](#adding-a-role-to-the-molecule-gate)
- [Promoting the Galaxy-enabled lint gate](#promoting-the-galaxy-enabled-lint-gate)
- [What automated testing does and does not cover](#what-automated-testing-does-and-does-not-cover)

---

## The gates

Every one of these blocks a merge.

| Gate | What it proves | Needs network? |
|------|----------------|----------------|
| `scripts/check_yaml.py` | Every YAML file parses | no |
| `yamllint -c .yamllint` | No duplicate keys, no `yes`/`no` booleans, sequences indented | no |
| `scripts/check_collections.py` | Every collection called is installable from a `requirements.yml` | no |
| `scripts/check_jinja_filters.py` | Every Jinja expression parses, its filters/tests exist, and it renders the value it claims | no |
| `gitleaks` | No credential in the working tree or in any ref's history | yes (downloads the pinned binary) |
| `stamp_platform_versions.py --check` | Every platform directory carries a valid `VERSION.yml`, so a copied directory stays traceable to a release | no |
| `compose-requirements.py` + `ansible-builder create` | Every platform's execution environment composes; the committed union has not drifted | no |
| `ansible-lint --offline` | No new lint violation against the ratcheted baseline | no |
| `ansible-playbook --syntax-check` | The core-only playbooks parse | no |
| `molecule test` | Onboarded roles parse, run, and are idempotent | no |
| `ansible-lint` with collections | Modules resolve in their real collections | yes (blocking once baselined) |

A final job, `ansible-lint with collections`, installs the declared collections
and becomes blocking the moment its baseline is committed — see
[Promoting the Galaxy-enabled lint gate](#promoting-the-galaxy-enabled-lint-gate).

### Why the secret gate needed its own rules

`gitleaks` with default rules finds nothing in this repository, and that is a
correct result — there is no AWS key or GitHub token here. It is also not the
shape a secret would take in an Ansible repository. What would actually get
committed is an ordinary password typed into a `vars` block:

```yaml
ansible_password: Summer2024!
```

No entropy signature, no provider prefix, nothing a default rule looks for.
`.gitleaks.toml` keeps every default rule and adds two of its own: a
credential-shaped key assigned a literal value, and an `ansible-vault` password
file committed by accident.

The rules only work because of what they *don't* fire on. Allowlists cover the
indirection this repository already uses — `{{ vault_x_password }}`, `lookup()`,
`$ANSIBLE_VAULT`, and the `CHANGE_ME` placeholder that all 36
`vault.yml.example` files share — plus values that name something rather than
being it (`password: secret_access_key`, `update_password: on_create`). Getting
that balance right took measurement, not judgement: the first draft produced 152
findings, every one a false positive, and a later draft silently missed any
password containing an `@` because the email allowlist was too loose.

Both scans matter. The working tree is the obvious one; every ref's history is
the one that finds a credential committed in March and deleted in April, which
is still in the objects and still valid. That is why the CI checkout uses
`fetch-depth: 0`.

Findings that already exist are recorded in `.gitleaks-baseline.json`, the same
ratchet as `.ansible-lint-ignore` and `.jinja-check-ignore`: what is there today
does not fail the build, anything new does. The eight baselined entries are
documentation placeholders in `cisco/IMPLEMENTATION_COMPLETE.md` and
`vast/vars/vault.yml.example` as they stood in older commits — the working-tree
copies have since been normalised to `CHANGE_ME`. Regenerate the baseline only
to record a finding you have confirmed is not a secret:

```bash
gitleaks git . --log-opts="--all" --config .gitleaks.toml \
  --report-format json --report-path .gitleaks-baseline.json --exit-code 0
```

A detection gate has a failure mode the others do not: it can go blind and still
pass, quietly, forever. So the job ends by planting a credential of each shape
the custom rules exist for, asserting all five are caught, and deleting them. A
change to `.gitleaks.toml` that silences a rule fails there, with a message
saying so, rather than years later.

### Why the Jinja gate exists separately

A broken Jinja expression is valid YAML. It passes `yamllint`, passes
`ansible-lint`, passes `--syntax-check`, and then fails at run time on the
customer's machine, because a filter name is only resolved when the expression
is actually rendered. Five such expressions shipped before this gate existed:
`| splitlines` and `| enumerate` (Python methods, not filters), `| all` (no such
filter), a pipe into a *variable*, and doubled `{{ }}` braces used to keep
literal braces in an embedded script.

Every one of them sat in a path the molecule gate cannot reach — behind
`apply_changes`, behind a credential preflight, in a role that needs a real
vCenter, or in a playbook that is not a role. That is the division of labour
between the two gates:

- **The Jinja gate** reaches every expression in the repository, because it
  never has to run the task. It parses, and probes each filter and test name
  once. It deliberately does **not** render: the repository's own expressions
  contain `lookup('pipe', ...)` and `lookup('file', ...)`, and a gate must never
  execute those.
- **The molecule gate** actually runs the code, so it catches what parsing
  cannot: a filter applied to the wrong operand, a wrong value, or an
  operator-precedence error such as `not x | lower` — which parses perfectly and
  is a *constant*, because `lower` returns an always-truthy string.

Known-broken expressions are tracked in `.jinja-check-ignore` with the reason
each one needs a human decision rather than a mechanical fix. New breakage fails
the build, and the gate reports a baselined entry that no longer has findings so
a stale entry cannot hide.

#### Two expressions that parse but render the wrong thing

The gate also checks two mistakes that parsing cannot catch, because the
expression is well-formed and its filters exist — it simply produces the wrong
output. Both were found by rendering every template in the repository, and both
are recognisable from the AST, which makes them cheap to enforce rather than
remember.

| Flagged | Why | Fix |
|---------|-----|-----|
| `{{ x \| bool }}` in a `.json.j2` | `bool` renders Python's `True`/`False`, capitalised, which is not valid JSON | `{{ x \| bool \| lower }}` |
| `{{ environment \| ... }}` | `environment` is a play/task keyword, always defined, so `default()` never fires and the value renders as `[]` | use `fourth_estate_environment` |

Both checks are deliberately narrow, so a finding is always a real defect:

- `| bool` is flagged only in a `.json.j2`, and only as the **outermost** filter.
  `| bool | lower` is the fix, not a finding. `| bool` in a YAML template is fine,
  because YAML accepts `True`. Append `| lower` rather than dropping `| bool`:
  the coercion still matters, so a value of `yes` renders `true` where `| lower`
  alone would emit the literal `yes` and break the document.
- A keyword is flagged only when read as a **bare name the template does not bind
  itself**. `prometheus_external_labels.environment` is an attribute of another
  variable, and `{% for environment in ... %}{{ environment }}{% endfor %}` is the
  loop's own variable; neither is a finding.

Only keywords that are useless to read are listed. Magic variables that are
normal to read — `hostvars`, `groups`, `inventory_hostname`, `role_name`, `omit`
— are deliberately absent, because reading those is correct Ansible.

---

## Molecule coverage

Scenarios are **delegated**: the role runs against the control node, with no
container and no VM. That means the gate needs no Docker daemon and runs on any
runner. The sequence is deliberately short, and the last step is the one that
earns its keep:

```yaml
scenario:
  test_sequence:
    - syntax        # the role parses
    - converge      # the role runs, and the validation harness reports success
    - idempotence   # a second run reports no changes
```

`converge.yml` runs the role with `apply_changes: false` and then asserts the
validation harness's own contract:

```yaml
- name: Assert the validation harness reported success
  ansible.builtin.assert:
    that:
      - fe_<component>_preflight_passed | bool
      - fe_<component>_postflight_passed | bool
      - fe_<component>_status == 'succeeded'
```

Run one locally:

```bash
pip install ansible-core==2.19.11 molecule==26.8.0
cd cloud_policy/roles/cloud_computing_srg_assessment
ANSIBLE_ROLES_PATH=$PWD/../ molecule test -s default
```

---

## Which roles are onboarded, and why only those

**49 roles** are in the gate. They were not picked by hand — a role qualifies
only if it passes two filters:

1. **Safe to run on an arbitrary control node.** A delegated scenario executes
   the role *for real* on the machine running CI. A role that installs packages,
   edits `sshd_config` or restarts services would harden or damage the runner.
   So a role qualifies only if every task uses `ansible.builtin`,
   `ansible.posix` or `community.general`, avoids state-changing modules
   (`package`, `service`, `user`, `lineinfile`, `command`, `shell`, …), and
   writes only under its `artifacts_dir` or `/tmp`. 105 of 421 roles pass this.

2. **Actually runs clean with no credentials.** Each of those 105 was executed
   twice and kept only if the first run reported `failed=0` and the second
   reported `changed=0`. 47 qualified. Two more were added later under a
   narrower contract -- see [Fixture-driven scenarios](#fixture-driven-scenarios-for-roles-that-cannot-converge-whole).

The other 58 fail for a legitimate reason: they refuse to start without their
required vault variables, which is their own preflight working as designed.

```
fatal: [localhost]: FAILED! => {"msg": "cisco/cybervision_center_deploy/prerequisites:
  FAILED at 'Verify required vault variables are defined' ..."}
```

That is a passing behaviour, not a bug — but it means those roles cannot be
exercised without a target system, so they are out of scope for this gate.

### Fixture-driven scenarios, for roles that cannot converge whole

Two roles — `dragos_vulnerability_mgmt` and `dragos_jira_integration` — are in
the gate under a narrower contract, and the reason is worth stating because it
generalises.

Neither can be converged whole: `main.yml` begins by calling the Dragos API. But
the part of each that had actually broken needs no API at all. Both parsed their
findings CSV with `| splitlines`, a Python string method rather than a Jinja
filter, so the task raised "No filter named 'splitlines'" every time it ran and
ticket creation could never have worked. Nothing caught it, because no gate ever
rendered that expression.

So each scenario writes a fixture CSV and includes the *specific task file* via
`tasks_from`, choosing conditions that leave the API calls unexecuted:

- `dragos_vulnerability_mgmt` sets `itsm.provider` to a value that is neither
  `servicenow` nor `jira`, so both ticket-creating tasks skip on their existing
  `when`.
- `dragos_jira_integration` has no such gate — its issue loop runs over
  `_lines[1:]` — so the fixture is header-only, which leaves the loop empty. The
  fixture is written as `vuln_findings.csv` rather than `vuln_worklist_high.csv`
  so the `_csv_path` fallback is exercised too.

Two rules make this kind of scenario worth having rather than merely reassuring:

1. **Include the role's real task file, never a copy of the expression.** A test
   that re-implements the expression passes while the role stays broken.
2. **Prove the scenario fails on the bug.** Both were verified by restoring the
   broken expression and confirming the converge fails with the exact template
   error, then restoring the fix. A test that has never failed has not been
   shown to test anything.

### What the gate already caught

Adding idempotence to the sequence immediately found real defects. Three roles
reported `changed` on every run because their evidence artifacts embed a fresh
timestamp:

```
CRITICAL Idempotence test failed because of the following tasks:
*  => cloud_computing_srg_assessment : Write JSON evidence artifact
*  => cloud_computing_srg_assessment : Render Markdown evidence report
```

Those tasks now carry `changed_when: false` — generating an evidence report is
not a managed state change. The repository's own conventions put "Idempotency
First" at the top, and until now nothing checked it.

---

## Adding a role to the molecule gate

1. Confirm the role is safe to run on the control node (filter 1 above). If it
   changes system state, it does **not** belong in a delegated scenario.
2. Copy `molecule/default/` from any onboarded role, e.g.
   `cloud_policy/roles/cloud_computing_srg_assessment/molecule/default/`.
3. In `converge.yml`, set the role name and the `fe_<component>_*` fact prefix
   (the component id is `<platform>/<role>` with non-alphanumerics replaced by
   underscores, prefixed `fe_`).
4. Ensure `meta/main.yml` has a `namespace:` under `galaxy_info:` — molecule
   refuses to run without a galaxy-resolvable role name.
5. Run it. If idempotence fails, fix the role rather than dropping the step.

CI discovers scenarios automatically by looking for `managed: false` in any
`molecule.yml`, so there is no list to update.

---

## Promoting the Galaxy-enabled lint gate

### The problem

The required `ansible-lint` gate runs `--offline` with no collections
installed. In that mode `syntax-check[unknown-module]` fires for **every**
non-builtin module, so ~269 of those findings sit in `.ansible-lint-ignore`
permanently. The rule can never catch what it is named after: a module that
genuinely does not exist, or a typo in an FQCN.

`scripts/check_collections.py` covers half of that offline — every collection
called must be installable from a `requirements.yml`. The other half, "does this
module exist inside that collection", needs the collections actually installed.

### The promotion

The `ansible-lint-online` CI job already installs the collections. It ratchets
against its **own** baseline, `.ansible-lint-ignore-online`, and switches itself
from informational to blocking the moment that file is committed. **No workflow
edit is required.**

On a machine that can reach `galaxy.ansible.com`:

```bash
pip install ansible-core==2.19.11 ansible-lint==26.6.0
./scripts/generate_online_baseline.sh
git add .ansible-lint-ignore-online && git commit -m "Baseline ansible-lint with collections installed"
```

The script refuses to write a baseline if any `requirements.yml` fails to
install, because the result would record missing-collection artifacts instead of
real findings.

### What to expect

The online baseline will be **smaller and more meaningful** than the offline
one. Diff the two: every `syntax-check[unknown-module]` entry that disappears
was an offline artifact, and every one that remains is a module that does not
exist in the installed collection — a real defect worth fixing rather than
baselining.

> This procedure has not been executed. The environment this work was done in
> blocks `galaxy.ansible.com` (403 on CONNECT), so the collections could not be
> installed and the baseline could not be generated. The job's blocking command
> was verified by running the identical `ansible-lint -i <file> <dirs>`
> invocation against a stand-in baseline: it passes when the baseline covers the
> findings and fails when it does not.

---

## What automated testing does and does not cover

Being explicit about this matters more than the coverage number.

### Production use is real validation, of a different kind

Fourth Estate customers run these playbooks against real infrastructure. That is
genuine evidence — real vendor systems, real configurations, at real scale, and
it exercises behaviour no lab reproduces faithfully.

It is not interchangeable with a test gate, because the two answer different
questions:

| | Production use | CI gate |
|---|---|---|
| Validates | the version customers are running | the commit in a pull request |
| Tells you | after deployment | before merge |
| Covers | whichever roles those customers use | exactly the 50 with a scenario |
| A regression appears as | a customer incident | a red check |

So the honest word for the other 373 roles is not *untested* — it is
**unguarded**. A change merged today is not protected by a customer's successful
run last month, and a regression in a role that production depends on reaches a
customer before it reaches anyone here.

### The concrete gaps

- **371 of 421 roles have no automated test.** Most drive a vendor API and
  cannot run in CI without an endpoint and credentials, so nothing catches a
  regression in them before merge.
- **This repository does not record which roles are in production use.** That
  matters more than it sounds: without it there is no way to tell a change to a
  heavily-relied-on role from a change to one nobody runs, and no way to
  prioritise where an integration test would actually pay for itself.
- **Container-driver scenarios.** `kubernetes/roles/k8s-cluster-hardening`
  keeps a Docker-driver scenario for local use. It is not in the gate, because
  it needs a driver plugin and a daemon.
- **A passing molecule run is not a correctness proof.** It proves the role
  parses, completes its no-op path, and is idempotent. It does not prove the
  changes it would make with `apply_changes: true` are right — that is a
  compliance-scan question, not a molecule question.

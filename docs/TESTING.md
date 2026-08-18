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
- [What is still not tested](#what-is-still-not-tested)

---

## The gates

Every one of these blocks a merge.

| Gate | What it proves | Needs network? |
|------|----------------|----------------|
| `scripts/check_yaml.py` | Every YAML file parses | no |
| `yamllint -c .yamllint` | No duplicate keys, no `yes`/`no` booleans, sequences indented | no |
| `scripts/check_collections.py` | Every collection called is installable from a `requirements.yml` | no |
| `ansible-lint --offline` | No new lint violation against the ratcheted baseline | no |
| `ansible-playbook --syntax-check` | The core-only playbooks parse | no |
| `molecule test` | Onboarded roles parse, run, and are idempotent | no |
| `ansible-lint` with collections | Modules resolve in their real collections | yes (blocking once baselined) |

A sixth job, `ansible-lint with collections`, installs the declared collections
and becomes blocking the moment its baseline is committed — see
[Promoting the Galaxy-enabled lint gate](#promoting-the-galaxy-enabled-lint-gate).

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

**47 roles** are in the gate. They were not picked by hand — a role qualifies
only if it passes two filters:

1. **Safe to run on an arbitrary control node.** A delegated scenario executes
   the role *for real* on the machine running CI. A role that installs packages,
   edits `sshd_config` or restarts services would harden or damage the runner.
   So a role qualifies only if every task uses `ansible.builtin`,
   `ansible.posix` or `community.general`, avoids state-changing modules
   (`package`, `service`, `user`, `lineinfile`, `command`, `shell`, …), and
   writes only under its `artifacts_dir` or `/tmp`. 105 of 422 roles pass this.

2. **Actually runs clean with no credentials.** Each of those 105 was executed
   twice and kept only if the first run reported `failed=0` and the second
   reported `changed=0`. 47 qualified.

The other 58 fail for a legitimate reason: they refuse to start without their
required vault variables, which is their own preflight working as designed.

```
fatal: [localhost]: FAILED! => {"msg": "cisco/cybervision_center_deploy/prerequisites:
  FAILED at 'Verify required vault variables are defined' ..."}
```

That is a passing behaviour, not a bug — but it means those roles cannot be
exercised without a target system, so they are out of scope for this gate.

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

## What is still not tested

Being explicit about this matters more than the coverage number.

- **375 of 422 roles have no functional test.** Most drive a vendor API and
  cannot run without a real endpoint and credentials.
- **No role is tested against a real target.** Nothing here proves that
  `cisco.ise` or `azure.azcollection` calls do the right thing on real kit;
  that needs an integration environment this repository does not define.
- **Container-driver scenarios.** `kubernetes/roles/k8s-cluster-hardening`
  keeps a Docker-driver scenario for local use. It is not in the gate, because
  it needs a driver plugin and a daemon.
- **A passing molecule run is not a correctness proof.** It proves the role
  parses, completes its no-op path, and is idempotent. It does not prove the
  changes it would make with `apply_changes: true` are right.

# Production Readiness Assessment

**Date:** 2026-07-02
**Scope:** Entire repository at `main` (ffd9918) — 41 platform directories, 604 roles, 3,684 YAML files
**Question assessed:** Is this repo "grab and go" production ready for customers?

## Verdict

**Not yet grab-and-go. Close, but three blockers and a handful of high-priority gaps stand in the way.**

The foundation is genuinely strong: consistent per-platform scaffolding, safety-first
defaults, a real documentation suite, enforced CI gates, and disciplined secret
handling. But the repo currently fails its **own** definition of production ready —
the required CI gate is red on `main` — and a customer cloning it today hits broken
front-page links and finds no license telling them they may use it at all.

---

## Blockers (must fix before any customer handoff)

### B1. CI is failing on `main`

The `ansible-lint (required, baseline-ratcheted)` job — an **enforced** gate — has
failed on the last three commits to `main` (`73b0e53`, `fce5d88`, `ffd9918`, i.e.
everything since the June 2026 STIG/SRG expansion):

```
Failed: 42 failure(s), 1527 warning(s) in 4038 files processed
 41 syntax-check   profile:min  tags:core,unskippable
  1 command-instead-of-module
  1 jinja
```

Representative failures, all in the newly added STIG roles:

- `*/roles/*/playbooks/vars.example.yml` files are picked up as playbooks and fail
  `syntax-check[specific]` ("A playbook must be a list of plays, got a dict")
  — e.g. `rhel/roles/rhel9_stig/playbooks/vars.example.yml`,
  `windows/roles/win_server2022_stig/playbooks/vars.example.yml`.
- `windows/roles/win_server2022_stig/playbooks/run.yml` references the role by bare
  name, which does not resolve from that directory's `roles_path`.

The new files were never added to the `.ansible-lint-ignore` baseline (the ratchet
worked as designed — it caught them). Fix the findings or triage them into the
baseline; either way `main` must be green before the "verified in CI" claim in the
README is true again. The YAML gates still pass (verified locally at HEAD:
`scripts/check_yaml.py` → 3,683 files OK; `yamllint` → clean).

### B2. The front-page documentation links are all broken

Commit `ffd9918` moved the customer docs into `docs/`, and `fce5d88` deleted
`STIG_COVERAGE_MATRIX.md`, but the root `README.md` was not updated. Every doc link
a customer would click first is dead:

| Referenced from README | Count | Actual state |
|---|---|---|
| `./STIG_COVERAGE_MATRIX.md` | 5 | **Deleted** (no replacement in `docs/`) |
| `./CHANGELOG.md` | 3 | Moved to `docs/CHANGELOG.md` |
| `./CUSTOMER_QUICK_START.md` | 2 | Moved to `docs/` |
| `./KNOWN_LIMITATIONS.md` | 2 | Moved to `docs/` |
| `./TROUBLESHOOTING.md` | 2 | Moved to `docs/` |
| `./COMPLIANCE_MAPPING.md` | 2 | Moved to `docs/` |
| `./PRODUCTION_READINESS_ASSESSMENT.md` | 1 | Removed in `a078d5d`; also referenced by `.github/workflows/ci.yml` and `.ansible-lint` |

The STIG coverage matrix needs to be restored (five references, and it is the
advertised index for the repo's headline feature) or the references removed.

### B3. No LICENSE file

There is no `LICENSE`, no license statement in the README, and no per-directory
license. "Grab and go for customers" is legally impossible without one — customers
have no rights to use, modify, or redistribute the content. Add a license (and a
`SECURITY.md` / support statement while at it).

---

## High priority (needed for a credible customer package)

### H1. No versioning or releases

Zero git tags, zero GitHub releases. `docs/CHANGELOG.md` exists but customers
cannot pin, download, or diff a version. Grab-and-go means a tagged release with
release notes; cut `v1.0.0` once CI is green.

### H2. The June 2026 expansion directories are missing the standard scaffolding

Every established platform directory follows the convention `README.md` +
`requirements.yml` + `inventory.example`. The four newest directories do not:

| Directory | `requirements.yml` | `inventory.example` | Collections actually used |
|---|---|---|---|
| `app_web_server` | missing | missing | `community.general` |
| `databases` | missing | partial (mysql only) | `community.postgresql`, `community.general`, `ansible.posix` |
| `cloud_policy` | missing | missing | builtin only |
| `network_policy` | missing | missing | builtin only |
| `ibm_zos` | present | missing | `ibm.ibm_zos_core` |

`databases` is the sharpest edge: it uses three external collections with nothing
declaring them.

### H3. README statistics and claims have drifted

- README says **577 roles**; the tree contains **604** role directories.
- "Repository statistics are verified in CI" — CI is currently failing (B1).
- The stats block is hand-maintained; either generate it in CI or drop the counts.

### H4. Known lint debt is large and includes potential runtime bugs

The `.ansible-lint-ignore` baseline is 1,064 entries. The ratchet strategy is sound
(new violations fail CI), but note what is being carried:

- **100 × `parser-error` + 97 × `schema[tasks]`** — playbooks stored under `tasks/`
  directories (e.g. `ansible/tasks/*.yml` are full plays with `hosts:`). They run
  fine with `ansible-playbook`, but the layout contradicts Ansible conventions and
  confuses every tool that walks the tree. A one-time move to `playbooks/` clears
  ~200 baseline entries.
- **33 × `jinja[invalid]`** — these can be real runtime template errors, not style.
  Worth a targeted triage pass; a broken Jinja expression fails at execution time,
  at the customer's site.
- 306 × `jinja[spacing]`, 119 × `name[missing]`, etc. — cosmetic, fine to carry.

### H5. Effectively no automated functional testing

One Molecule scenario exists (`kubernetes/roles/k8s-cluster-hardening`) across 604
roles. The `ansible-playbook --syntax-check` CI job is informational-only
(`continue-on-error: true`). `docs/KNOWN_LIMITATIONS.md` is honest about this
(several roles "not yet validated against live hosts"), and full functional testing
of 41 vendor platforms is unrealistic — but a customer-facing package should at
minimum promote the syntax-check job to a required gate for the directories whose
collections install cleanly, and add Molecule/container coverage for the handful of
roles that can run against localhost (rhel, databases, elk_stack, kubernetes).

---

## Medium priority

- **M1. Root-level meta files:** no `CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`,
  or issue/PR templates. The README has a "Contribution Guidelines" section, which
  helps, but the standard files are what customers and scanners look for.
- **M2. CI runtime:** the full `ansible-lint --offline` run exceeds 10 minutes.
  Sharding by directory (matrix job) would keep the required gate fast and make
  failures attributable to a platform.
- **M3. Actions deprecation warnings:** `actions/checkout@v4` / `setup-python@v5`
  emit Node 20 deprecation warnings; bump before GitHub enforces removal.
- **M4. Placeholder features:** several advanced workflows are fail-fast
  placeholders (OT firmware ops, Illumio PCE clustering, SL1 HA — see
  `docs/KNOWN_LIMITATIONS.md` §13–14). This is handled *well* (documented,
  fail-fast, safe defaults) — just ensure the sales/handoff message matches, since
  "grab and go" overstates these areas.

---

## What is already in good shape

Credit where due — these are above the bar for repos of this size:

- **Safety defaults.** `apply_changes: false` dry-run convention everywhere;
  destructive operations double-gated (`prune.dry_run` + `prune.allow_delete`);
  OT-specific safeguards documented.
- **Secret hygiene.** No hardcoded credentials found. Flagged candidates were all
  false positives (FortiOS `enable`/`disable` enums, example-playbook placeholder
  values like `feedpass` under `feeds.example.com`, and Tower credential-type field
  mappings). ~450 files use `no_log`; Vault-based patterns referenced throughout.
- **Scaffolding consistency.** 36 of 41 platform directories carry the full
  README + `requirements.yml` + `inventory.example` set; 651 README files total.
- **Customer documentation.** `docs/CUSTOMER_QUICK_START.md`,
  `KNOWN_LIMITATIONS.md` (unusually honest and specific), `TROUBLESHOOTING.md`,
  `COMPLIANCE_MAPPING.md`, `CHANGELOG.md`.
- **CI design.** Two enforced deterministic gates (YAML parse, offline
  ansible-lint with a ratcheting baseline) plus an informational
  collections-installed lint/syntax job. The design is right; it just needs to be
  green again (B1) and the informational job promoted over time (H5).

---

## Scorecard

| Area | Grade | Notes |
|---|---|---|
| Code hygiene / lint | C+ | Gates well designed but red on `main`; 1,064-entry baseline; ~200 entries are a fixable layout issue |
| Documentation | B− | Excellent content, but every front-page link is broken and the coverage matrix is deleted |
| Security / secrets | A− | No real secrets, `no_log` discipline, Vault patterns, safety gating |
| Packaging / distribution | D | No license, no tags, no releases, stats drift |
| Testing | D+ | Parse/lint only; 1 Molecule scenario in 604 roles; syntax-check non-blocking |
| Dependency declaration | B | 36/41 dirs complete; 4 new dirs missing `requirements.yml`/inventory |
| Operational safety | A− | Dry-run defaults, destructive-op gating, honest limitations doc |

## Recommended order of work

1. Fix or baseline the 42 lint failures → green `main` (hours).
2. Fix README links; restore or replace `STIG_COVERAGE_MATRIX.md` (≤1 hour).
3. Add `LICENSE` (+ `SECURITY.md`, `CONTRIBUTING.md`) (≤1 hour, pending license choice).
4. Add `requirements.yml` + `inventory.example` to the 5 new directories (hours).
5. Tag `v1.0.0`, publish a release referencing the changelog (minutes, after 1–4).
6. Triage the 33 `jinja[invalid]` baseline entries (day).
7. Relocate playbooks out of `tasks/` dirs; shrink baseline by ~200 (day, mechanical).
8. Promote syntax-check to required for clean directories; seed Molecule for localhost-testable roles (ongoing).

Items 1–5 are the customer-facing minimum: with those done, "grab and go" becomes a
defensible claim, with `docs/KNOWN_LIMITATIONS.md` defining the supported envelope.

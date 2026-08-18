# Production Readiness Assessment

**Date:** 2026-08-18 (re-assessment; supersedes the 2026-07-02 version — see git history)
**Scope:** Entire repository at `main` (`6eb954f0`) — 41 platform directories, 421 roles, 3,345 YAML files
**Question assessed:** Is this repo "grab and go" production ready for customers?
**Method:** Every statistic and CI claim below was independently re-verified
against the tree and the actual CI run on `6eb954f0` — not carried forward
from the previous assessment.

## Verdict

**Yes — grab-and-go remains a defensible claim within the documented envelope,
and the repository is in its best-verified state to date.** All five CI gates
are green on the current head, the published statistics match the tree
exactly, the empty-role class is fully eliminated, and the lint baseline has
shrunk since July. The supported envelope — validated automation versus
documented procedure or fail-fast placeholder — is still defined by
`docs/KNOWN_LIMITATIONS.md`, and customer handoff should always pair a release
with that document.

Two risks lead the list now:

1. **Release drift.** The only published release (`Prod1`, 2026-07-02) is 26
   commits and ~3,500 changed files behind `main` — customers pinned to it are
   missing the empty-role purge, the validation framework, and the Molecule
   coverage. Cutting `v1.1.0` from the current green head is the single
   highest-value action available.
2. **Functional coverage of the API-driven roles** (unchanged): ~374 of the
   421 roles drive vendor APIs and need a real target system to exercise.
   CI proves everything parses, lints, and (where core-only) syntax-checks;
   customer production runs are real validation, but they happen post-merge
   and their coverage is not recorded, so a regression can reach a customer
   before it reaches CI (see `docs/TESTING.md`).

---

## Verified state of the repository (2026-08-18)

| Claim | Verified value | Method |
|---|---|---|
| Roles | **421**, all with non-empty `tasks/main.yml` | recounted from tree |
| YAML files | **3,345** | recounted from tree |
| Jinja2 templates | **291** | recounted from tree |
| Platform directories | 41, each with `README.md` + `requirements.yml` + `inventory.example` | tree |
| Collections in use | 34, declaration gaps: **0** | `scripts/check_collections.py` run locally |
| Branches | `main` only; no open PRs or issues | remote refs + GitHub API |
| License / release | MIT `LICENSE`; one release, tag `Prod1` at `f762a82` | tree + GitHub API |
| Lint baseline | ~1,109 entries (down from 1,228 in July — the ratchet works) | `.ansible-lint-ignore` |

The README statistics block matches the tree exactly — a first across these
assessments.

## Current CI posture (verified per-job on the run for `6eb954f0`)

| Gate | Status | Enforced |
|------|--------|----------|
| YAML parse (`scripts/check_yaml.py`, all files) | ✅ green (also re-run locally) | required |
| yamllint (syntax, duplicate keys, truthy, indentation) | ✅ green (also re-run locally) | required |
| Collection declarations (`scripts/check_collections.py`) | ✅ green (also re-run locally) | required |
| ansible-lint `--offline`, pinned toolchain, ratcheting baseline | ✅ green (~29 min) | required |
| syntax-check, 11 core-only playbooks, pinned ansible-core | ✅ green | required |
| Molecule (`syntax` + `converge` + `idempotence`), 47 delegated scenarios | ✅ green (~8 min) | required |
| ansible-lint with Galaxy collections | ✅ green (informational path) | **not yet blocking** — see below |

Determinism note: the lint gates pin `ansible-core==2.19.11` /
`ansible-lint==26.6.0`. Bumping the pins requires regenerating
`.ansible-lint-ignore` in the same PR, as documented in `.ansible-lint` and
the workflow.

**Galaxy-enabled gate is armed but not promoted:** the job is designed to
become blocking the moment `.ansible-lint-ignore-online` is committed, and
that file does not exist yet — on the verified run its blocking step was
skipped and only the informational lint ran. Running
`./scripts/generate_online_baseline.sh` on a Galaxy-reachable machine and
committing the result promotes it with no workflow edit. Until then, the
`syntax-check[unknown-module]` class (a module that genuinely doesn't exist)
has no blocking check.

## Changes since the 2026-07-02 assessment

- **Validation framework:** every customer-facing playbook now carries
  preflight/postflight validation (including `pre_tasks` and handler
  failures) plus the `fe_validation` callback plugin and per-run statistics
  (`docs/VALIDATION_AND_STATS.md`).
- **Molecule gate added:** 47 control-node-runnable roles run
  `syntax` + `converge` + `idempotence` as a required gate.
- **155 empty roles removed**, with the 120 playbook invocations that called
  them — each such invocation had silently performed no changes. This closes
  an integrity gap the July assessment did not detect.
- **Collection-declaration gate added**; yamllint tightened (truthy,
  indentation).
- **Layout settled** after the Aug 18 restructure: standalone plays under
  `playbooks/`, task files under `tasks/`.
- **Stability note:** `main` went red three times during the Aug 17–18 churn,
  each fixed within hours. Customers should track tagged releases, not
  `main` — one more reason to cut the next release.

## Scorecard (July → now)

| Area | Was | Now | Notes |
|---|-----|-----|-------|
| Code hygiene / lint | A− | **A−** | Baseline shrunk ~10%; empty-role class eliminated; stats verified accurate |
| Documentation | A− | **A−** | Suite current; changelog release-name mismatch fixed in this pass |
| Security / secrets | A− | **A−** | No hardcoded secrets; `no_log` discipline; Vault patterns; `SECURITY.md` added |
| Packaging / distribution | B+ | **C+** | Downgraded on release drift: the only tag is 26 commits behind `main` |
| Testing | B− | **B** | Molecule idempotence gate live for 47 roles; ~374 API-driven roles still need an integration environment |
| Dependency declaration | A− | **A** | Declaration now CI-enforced, 0 gaps |
| Operational safety | A− | **A** | Validation wrapper + run statistics on every playbook, on top of dry-run defaults and double-gated destructive ops |

## Open items

**Now (blocking the "grab and go" story, not the code)**
- **R1 — Cut a release.** Tag `v1.1.0` (adopting semver) from the current
  green head and paste the `[Unreleased]` section of `docs/CHANGELOG.md` into
  the release body. Everything since `Prod1` is otherwise invisible to
  customers.

**Quick wins — closed in this pass**
- ~~M1 — Root meta files~~: `CONTRIBUTING.md`, `SECURITY.md`,
  `.github/CODEOWNERS`, issue + PR templates added.
- ~~M3 — Actions deprecations~~: bumped to `actions/checkout@v5` /
  `actions/setup-python@v6`.
- ~~Changelog naming~~: first-release entry now matches the actual `Prod1`
  tag.

**Medium priority**
- **M2 — CI runtime:** the offline lint gate runs ~29 minutes as one job;
  shard by platform directory (matrix) to speed feedback and localize
  failures.
- **M5 — Promote the Galaxy lint gate:** generate and commit
  `.ansible-lint-ignore-online` (see above).
- **M4 — Placeholder features:** OT firmware ops, Illumio PCE clustering, SL1
  HA remain fail-fast placeholders (documented in `KNOWN_LIMITATIONS.md`
  §13–14). Keep the sales/handoff message aligned.

**Larger investments**
- **Functional testing (the real gap):** an integration environment (live or
  mocked vendor targets) for the API-driven roles; grow the Molecule set and
  the required syntax-check list as more playbooks become collection-free at
  parse time.
- **Release cadence:** semver tags plus a changelog-driven release body as a
  repeatable process, so drift like the current one doesn't recur.

---

## Customer handoff checklist

What a customer gets today:

- ✅ MIT-licensed snapshot with green, deterministic, six-gate CI on `main`
- ✅ Per-platform `README.md` + `requirements.yml` + `inventory.example` (41/41)
- ✅ Quick start, troubleshooting, compliance mapping, STIG coverage matrix,
  changelog, contribution and security policy — all links verified
- ✅ Safety defaults: `apply_changes: false` everywhere, double-gated
  destructive operations, OT-specific safeguards, run validation + statistics
- ⚠️ **Pin to a tagged release, not `main`** — and note the current tag
  (`Prod1`) predates the validation framework and empty-role purge; a fresh
  release is the open action R1
- ⚠️ Read `docs/KNOWN_LIMITATIONS.md` first — it defines the supported
  envelope, the not-yet-validated areas, and the fail-fast placeholders
- ⚠️ Functional validation in a lab remains the customer's first step for any
  role they intend to run against production (run everything twice in
  non-prod, per the limitations doc)

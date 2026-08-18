# Contributing

Thanks for contributing. This repository automates working customer
environments, so the bar is: **every change must keep CI green and must not
weaken the safety defaults.**

## Workflow

1. Branch from `main`, make your change, and open a pull request.
2. All required CI gates must pass (they run on every push and PR):
   - **YAML parse** — `python3 scripts/check_yaml.py .`
   - **yamllint** — `yamllint -c .yamllint .` (syntax, duplicate keys,
     `true`/`false` truthy spellings, consistent indentation)
   - **Collection declarations** — `python3 scripts/check_collections.py .`
     (every collection used must appear in a `requirements.yml`)
   - **ansible-lint (offline, baseline-ratcheted)** — pinned toolchain, see
     below
   - **syntax-check** of the core-only playbooks
   - **Molecule** (`syntax` + `converge` + `idempotence`) for the delegated
     control-node scenarios
3. Update documentation in the same PR: the platform `README.md` for role
   changes, `docs/CHANGELOG.md` (under `[Unreleased]`) for anything
   customer-visible.

Run the fast checks locally before pushing:

```bash
pip install yamllint pyyaml ansible-core==2.19.11 ansible-lint==26.6.0
python3 scripts/check_yaml.py .
yamllint -c .yamllint .
python3 scripts/check_collections.py .
```

## The pinned lint toolchain and its baseline

CI pins `ansible-core==2.19.11` / `ansible-lint==26.6.0` and ratchets against
`.ansible-lint-ignore`. Rules:

- **New violations fail the build.** Fix them; do not add baseline entries for
  new code.
- **Never hand-edit the baseline to silence a finding.** The baseline may only
  shrink, except when bumping the pinned tool versions — then regenerate it in
  the same PR (`ansible-lint --offline --generate-ignore <dirs>`), as
  documented in `.ansible-lint` and the workflow.
- The Galaxy-enabled lint job becomes blocking automatically once
  `.ansible-lint-ignore-online` is committed — generate it with
  `./scripts/generate_online_baseline.sh` on a machine that can reach
  galaxy.ansible.com.

## Conventions (non-negotiable)

- **Safe by default:** roles that change systems default to
  `apply_changes: false` (assessment/check mode). Enforcement requires the
  operator to opt in (`-e apply_changes=true`). Destructive operations are
  double-gated.
- **No secrets in the repo.** Credentials come from Ansible Vault, environment
  variables, or an external secrets manager. Credential-handling tasks carry
  `no_log: true`.
- **Layout:** roles live under `<platform>/roles/<role>/`; standalone plays
  live under `playbooks/` directories; task files (no `hosts:`) live under
  `tasks/`.
- **Idempotence:** query/report tasks set `changed_when`; roles onboarded to
  Molecule must pass the idempotence step.
- **No empty roles.** A role must do something; scaffolding-only roles were
  removed once and stay removed.
- Every platform directory carries a `README.md`, `requirements.yml`, and
  `inventory.example` — keep all three current.

## Adding test coverage

New roles that can execute on the control node without changing it should ship
a delegated Molecule scenario (`managed: false`) — the CI gate discovers and
runs these automatically. Playbooks that parse with ansible-core alone can be
added to the syntax-check list in `.github/workflows/ci.yml`. See
`docs/TESTING.md` for details.

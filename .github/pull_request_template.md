## What does this PR change?

<!-- One or two sentences: what changed and why. -->

## Type of change

- [ ] New role / playbook
- [ ] Fix to existing automation
- [ ] Documentation
- [ ] CI / tooling
- [ ] Other (describe above)

## Checklist

- [ ] All required CI gates pass (YAML parse, yamllint, collection
      declarations, ansible-lint, syntax-check, Molecule)
- [ ] No new `.ansible-lint-ignore` baseline entries (baseline only shrinks,
      unless this PR bumps the pinned toolchain and regenerates it)
- [ ] Safety defaults preserved (`apply_changes: false`, double-gated
      destructive operations, `no_log` on credential-handling tasks)
- [ ] No secrets, credentials, or customer-identifying data in the diff
- [ ] Docs updated in this PR (platform `README.md`,
      `docs/CHANGELOG.md` under `[Unreleased]`, and `docs/` pages as needed)
- [ ] New control-node-runnable roles ship a delegated Molecule scenario

## How was this validated?

<!-- Lab run, molecule output, check-mode run against a test target, etc.
     For API-driven roles, name the target system/version if you ran one. -->

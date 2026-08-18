# Security Policy

This repository's automation runs against production customer environments,
including regulated (DoD STIG / NIST / FedRAMP) and operational-technology
networks. Security reports are taken seriously.

## Reporting a vulnerability

**Please do not open a public issue for security problems.**

Report privately via GitHub's private vulnerability reporting:
**Security → Report a vulnerability** on this repository
([direct link](https://github.com/Koga1985/Fourth-Estate-Ansible-Playbooks/security/advisories/new)).

Include what you can: the affected role/playbook path, the class of issue, and
reproduction steps or a proof of concept. You can expect an acknowledgement
within a few business days.

## What counts as a vulnerability here

- Hardcoded or leaked credentials, tokens, or keys anywhere in the tree
- Tasks that expose secrets (missing `no_log` on credential-handling tasks,
  secrets written to logs, evidence artifacts, or `set_stats` output)
- Safety-gate bypasses: a role that changes systems despite
  `apply_changes: false`, or a destructive operation reachable without its
  double gate
- Injection risks in templates or shell/command tasks fed by inventory or
  API-sourced data
- Hardening roles that claim to enforce a control but demonstrably do not
  (a compliance gap presented as compliance)

## Scope notes

- Vulnerabilities in the third-party Ansible collections this repo declares in
  its `requirements.yml` files should be reported upstream to the collection
  maintainers; report them here only if this repo's usage makes them worse.
- The supported envelope — what is validated automation versus documented
  procedure or fail-fast placeholder — is defined in
  [docs/KNOWN_LIMITATIONS.md](./docs/KNOWN_LIMITATIONS.md).

## Supported versions

Security fixes land on `main` and are included in the next tagged release.
Pin production use to tagged releases and review
[docs/CHANGELOG.md](./docs/CHANGELOG.md) when upgrading.

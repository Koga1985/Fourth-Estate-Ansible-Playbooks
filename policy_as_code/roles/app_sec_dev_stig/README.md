# Application Security & Development STIG (`app_sec_dev_stig`)

Production-ready Ansible role implementing the DISA **Application Security and
Development STIG (Ver 6, Rel 4)** (`APSC-DV-*`) as a **CI/CD policy gate**. The
ASD STIG governs the software development lifecycle, not host configuration, so
this role runs on your build runner against an application source tree, executes
the security scanners that are present, maps results to APSC-DV control
families, writes a compliance-evidence package, and (optionally) **fails the
build** when policy thresholds are exceeded.

Pure `ansible.builtin` — the scanners are external tools detected on `PATH`.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ansible_connection` | `local` | No | Run context (CI runner / control node) |
| `app_src_dir` | `"{{ playbook_dir }}"` | No | Application source tree to assess (the repo/workspace root). |
| `app_name` | `"{{ app_src_dir \| basename }}"` | No | — |
| `artifacts_dir` | `"/tmp/appsec-stig-artifacts"` | No | — |
| `enforce_gate` | `false` | No | Gate control true = fail the build when thresholds exceeded |
| `gate_max_critical` | `0` | No | Per-severity ceilings for the gate (only used when enforce_gate=true) |
| `gate_max_high` | `0` | No | — |
| `gate_fail_on_secrets` | `true` | No | — |
| `scan_secrets` | `true` | No | Scanner selection - each runs only if its binary is on PATH. Override the command if you wrap them differently. |
| `scan_sast` | `true` | No | — |
| `scan_dependencies` | `true` | No | — |
| `scan_iac` | `true` | No | — |
| `appsec_tools` | `(see defaults/main.yml)` | No | — |
| `app_sec_dev_catalog` | `(see defaults/main.yml)` | No | APSC-DV control catalog - auto controls are evidenced by a scanner; manual controls require documented procedural verification. |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Application Security and Development STIG"` | No | — |
| `stig_version` | `"V6R4"` | No | — |

## Example Playbook

```yaml
- name: Use app_sec_dev_stig
  hosts: all
  gather_facts: false
  roles:
    - role: app_sec_dev_stig
```

## Tags

`--tags scan` (all scanners), `secrets`, `sast`, `sca`, `iac`, `report`, `gate`.

## Why "grab and go"

* **Report-only by default** (`enforce_gate=false`) — produces JSON + Markdown
  evidence and never breaks a build until you opt in.
* **Degrades gracefully** — each scanner runs only if installed; missing tools
  are reported as `tool-not-available` (attach manual evidence) rather than
  failing.
* Drop straight into a pipeline stage and set `enforce_gate=true`.

## Quick start

```bash
cd policy_as_code/roles/app_sec_dev_stig/playbooks

# Report-only evidence run
ansible-playbook run.yml -e app_src_dir=/path/to/app/repo
cat /tmp/appsec-stig-artifacts/<app>_app_sec_dev_stig.md

# CI gate (fails the build on critical/high/secrets)
ansible-playbook run.yml -e app_src_dir=$CI_PROJECT_DIR -e enforce_gate=true
```

## Scanners and control mapping

| Evidence | Default tool | APSC-DV controls |
|----------|--------------|------------------|
| Secret detection | `gitleaks` | APSC-DV-001740 |
| SAST | `semgrep` | APSC-DV-002400, 002560, 003215, 001995, 003285 |
| Dependency / SCA + SBOM | `grype` | APSC-DV-003235, 002950 |
| IaC | `checkov` | APSC-DV-003180 |
| Manual review | — | APSC-DV-000160, 003170, 003200 |

Any tool is overridable via `appsec_tools` (e.g. swap `grype` for `trivy`,
`semgrep` for another SAST engine) — see `vars.example.yml`.

## Gate thresholds

| Variable | Default | Meaning |
|----------|---------|---------|
| `enforce_gate` | `false` | `true` fails the build on violation |
| `gate_max_critical` | `0` | Max allowed critical findings |
| `gate_max_high` | `0` | Max allowed high findings |
| `gate_fail_on_secrets` | `true` | Any detected secret fails the gate |

## Output

* `<app>_app_sec_dev_stig.json` — machine-readable evidence (scanner findings +
  per-control evaluation).
* `<app>_app_sec_dev_stig.md` — human-readable evidence report for the ATO package.

## License

MIT

# Changelog

All notable changes to the Fourth Estate Ansible Playbooks are documented here.
The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

Everything below has landed on `main` since the `Prod1` release and is not yet
in any tagged release. Recommended next release: `v1.1.0` (adopting semver
going forward), with this section pasted into the release body.

### Added
- **Preflight/postflight validation on every customer-facing playbook**: a
  shared validation wrapper (covering `pre_tasks` and handler failures) plus
  the `fe_validation` callback plugin, emitting per-run statistics via
  `set_stats`. See [VALIDATION_AND_STATS.md](./VALIDATION_AND_STATS.md).
- **Molecule coverage for the 47 roles that can run on the control node**
  (delegated driver; `syntax` + `converge` + `idempotence`), enforced as a
  required CI gate. See [TESTING.md](./TESTING.md).
- **CI gate: collections in use must be declared in a `requirements.yml`**
  (`scripts/check_collections.py`; 34 collections, 0 gaps).
- Root meta files: `CONTRIBUTING.md`, `SECURITY.md`, `.github/CODEOWNERS`,
  issue and pull request templates.
- **Galaxy-enabled ansible-lint gate promoted to blocking**:
  `.ansible-lint-ignore-online` (952 entries) generated and committed, so
  the "ansible-lint with collections" CI job now ratchets and blocks —
  `syntax-check[unknown-module]` is finally meaningful. Added the
  dispatchable `generate-online-baseline` workflow that regenerates the
  baseline on a Galaxy-reachable runner (re-run it whenever the pinned
  toolchain changes).
- `# automation-hub-only:` marker for requirements files whose collections
  have no stable community-Galaxy release (currently
  `ansible/requirements.yml` / `ansible.controller`): the baseline script
  and the online lint job treat their install failure as expected instead
  of aborting, while unmarked failures still abort.

### Changed
- **Removed 155 roles with empty `tasks/main.yml`** and the 120 playbook
  invocations that called them — each such invocation silently performed no
  changes. Repository statistics corrected accordingly (now 421 roles /
  3,345 YAML files / 61 inventory examples).
- Repository layout: standalone plays live under `playbooks/` directories;
  task files remain under `tasks/`.
- yamllint now also enforces `truthy` (true/false spellings) and consistent
  indentation; collection declaration gaps closed.
- CI workflow actions bumped (`actions/checkout@v5`, `actions/setup-python@v6`)
  to clear Node deprecation warnings.

### Fixed
- **Three `requirements.yml` declarations that were never installable from
  community Galaxy** (flushed out by the first baseline-generation run —
  the CI collection-install step had been silently failing on them):
  `openshift/` declared the Automation-Hub-only `redhat.openshift >=2.3.0`
  without using it (removed; `community.okd` stays); `servicenow/` pinned
  the deprecated `servicenow.servicenow` at `>=2.0.0`, a version line that
  never existed (relaxed to `>=1.0.0`, where its `snow_record` modules
  live); `ansible/` pins `ansible.controller >=4.5.0`, which is correct
  for Automation Hub customers and now carries the `automation-hub-only`
  marker instead of a broken community install expectation.
- Molecule CI job derived role paths with the wrong number of `dirname` calls.
- Removed an orphaned duplicate role; corrected repository statistics.
- Testing docs no longer claim API-driven roles are unvalidated — customer
  production use is real (post-merge) validation; the docs now describe that
  gap accurately.

## [Prod1] — 2026-07-02 — First tagged release

First tagged, customer-consumable release — GitHub tag **`Prod1`**
("Production Ready Release", commit `f762a82`). This entry was originally
titled "v1.0.0"; the actual published tag is `Prod1`, and semver tags are
adopted from the next release onward. See
[PRODUCTION_READINESS_ASSESSMENT.md](./PRODUCTION_READINESS_ASSESSMENT.md) for
the audit this release closes out.

### Added
- **MIT `LICENSE`** — the repository is now legally redistributable.
- `docs/PRODUCTION_READINESS_ASSESSMENT.md` — full production-readiness audit.
- `requirements.yml` + `inventory.example` scaffolding for the newest platform
  directories (`app_web_server`, `cloud_policy`, `network_policy`,
  `databases/db2`, `ibm_zos`).
- **CI gate 3**: required `ansible-playbook --syntax-check` for the 11
  grab-and-go playbooks that parse with ansible-core alone (cloud_policy,
  network_policy, db2, app_sec_dev_stig, apache SRG, and the six `ibm_zos`
  checklist generators).

### Fixed
- **CI determinism**: the required ansible-lint gate now pins
  `ansible-core==2.19.11` / `ansible-lint==26.6.0`; the baseline was
  regenerated against those exact versions. (An unpinned toolchain let a new
  ansible-lint release silently invalidate the baseline and turn `main` red.)
- **All 30 `jinja[invalid]` findings triaged — every one was a real runtime
  bug** and all are fixed: Python list comprehensions and nested `{{ }}` in
  Dragos drift/allowlist/topology tasks; `{% if %}`/`{% else %}` split across
  separate `msg` list items in the Illumio OT ACL playbooks (crashed on every
  run); `{% do %}` tags (extension not enabled) in the OT inventory tasks;
  malformed division-guard ternaries in the Infoblox capacity reports;
  Jinja-precedence bugs (`x | length > 0 | ternary(...)`) in Cohesity restore
  and Panorama commit; `#` comments inside Jinja expressions (Infoblox RPZ,
  vSphere permissions export, VM encryption); a stray `.` before pipes in the
  Dragos sensor report; `{{ sl1. }}` dangling attribute in ScienceLogic system
  settings; doubled PowerShell braces + `\$`/`\"` mis-escapes in the vSphere
  host-profile and PowerCLI report tasks; block tags inside `{{ }}` in vSphere
  RBAC delta computation; a templated `vars:` mapping in the Illumio guard;
  Prometheus/Velero alert annotations (`{{ $labels.* }}`) now marked `!unsafe`
  so the Ansible templar never renders them.
- PowerShell `#` line comments inside folded (`>-`) script blocks converted to
  `<# … #>` block comments — YAML folding was silently commenting out the rest
  of the folded line, swallowing statements.
- Root README links updated for the `docs/` move; `STIG_COVERAGE_MATRIX.md`
  restored to `docs/`; README statistics corrected (604 roles, 3,688 YAML
  files, 63 inventory examples).
- `scripts/check_yaml.py` now accepts the Ansible-specific `!unsafe` / `!vault`
  YAML tags.

## [2026-06-26] — DoD STIG / SRG expansion

Added **21 dedicated DoD STIG / SRG roles** across **5 new platform areas**. Every
runnable role is **safe by default** (`apply_changes=false` / assessment mode runs
in check mode and writes a per-host JSON evidence artifact; pass
`-e apply_changes=true` to enforce). See
[STIG_COVERAGE_MATRIX.md](./STIG_COVERAGE_MATRIX.md) for the full mapping of every
requested benchmark to its role/status.

### Added — Cisco network device STIGs (`cisco/roles/`)
- `cisco_ios_xe_l2_stig` — IOS XE Catalyst as a Layer-2 device (L2S `CISC-L2-*` + NDM `CISC-ND-*`), `cisco.ios`.
- `cisco_nxos_stig` — Nexus NX-OS Switch STIG (NDM + L2), `cisco.nxos`.
- `cisco_asa_stig` — ASA NDM (`CASA-ND-*`) + Firewall (`CASA-FW-*`), `cisco.asa`.
- `cisco_ftd_stig` — Firepower Threat Defense via the FMC REST API (assess + data-driven enforce).
- `cisco_aci_router_stig` — ACI L3Out routing-plane STIG (`CISC-RT-*`) via `cisco.aci`.
- `cisco_ise_stig` — ISE NDM (`CISC-ND-*`) assess + OpenAPI enforce via `uri`.

### Added — Operating systems & containers
- `rhel/roles/rhel9_stig` — RHEL 9 STIG (`RHEL-09-*`, V2R6), `ansible.builtin`/`ansible.posix`.
- `windows/roles/win_server2022_stig` — Windows Server 2022 STIG (`WN22-*`, V2R6) with optional Active Directory Domain (`AD.*`) and Windows DNS (`WDNS-*`) controls.
- `openshift/roles/ocp_stig_profile` — OpenShift Container Platform 4.x STIG (`CNTR-OS-*`, V2R4) via `kubernetes.core`.

### Added — Database
- `databases/db2/roles/db2_stig` — IBM DB2 V10.5 STIG (`DB2X-00-*`, V2R1) via the DB2 CLP, `db2audit`, and SQL (drift-aware).

### Added — Application / Web (`app_web_server/`)
- `tomcat_app_server_srg` — Application Server SRG V4R4 (`SRG-APP-*-AS-*`) via idempotent XML edits.
- `apache_web_server_srg` — Web Server SRG (`SRG-APP-*-WSR-*`), `apachectl`-validated drop-in.

### Added — Policy / SRG assessments
- `policy_as_code/roles/app_sec_dev_stig` — Application Security & Development STIG V6R4 (`APSC-DV-*`) CI/CD gate (gitleaks/semgrep/grype/checkov → evidence; optional build-fail).
- `network_policy/roles/ndm_srg_assessment` — Network Device Management SRG (V5R3) + Network Infrastructure Policy STIG (V10R7) evidence rollup.
- `cloud_policy/roles/cloud_computing_srg_assessment` — DoD Cloud Computing SRG (IL2–IL6) + SaaS shared-responsibility mapping onto the AWS/Azure/GCP roles.

### Added — IBM z/OS family (`ibm_zos/`, read-only assessment skeletons)
- `zos_racf_stig`, `zos_tss_stig`, `zos_cics_tss_stig`, `zos_netview_tss_stig`,
  `zos_tdmf_tss_stig`, `zos_zsecure_stig`. Each generates a STIG checklist +
  command reference (runs anywhere) and can run read-only verify commands against
  a live LPAR via `ibm.ibm_zos_core` (`zos_live_assessment=true`). **No blind
  enforcement** — remediation is documented for the z/OS systems programmer.

### Added — Documentation
- `STIG_COVERAGE_MATRIX.md` — full request-to-role traceability matrix.
- Per-platform and per-role READMEs for all new areas; `CHANGELOG.md` (this file).

### Notes
- Repository totals at this expansion: **41 platforms**. (The role/YAML counts
  originally published in this entry were later found inaccurate and corrected
  to **604 roles** / **3,688 YAML files** in the `Prod1` entry above.)
- All new YAML passes the CI gate (`scripts/check_yaml.py` + `yamllint`). The
  localhost-executable assessment roles (`ndm_srg_assessment`,
  `cloud_computing_srg_assessment`, `app_sec_dev_stig`, the six `ibm_zos/*`
  checklist generators) were additionally run end-to-end during development.

## [2026-03-16] — Production readiness / security hardening
- Added `no_log: true` to credential-handling tasks, `changed_when` correctness
  to query tasks, `any_errors_fatal: true` to plays, and the customer docs
  (CUSTOMER_QUICK_START, KNOWN_LIMITATIONS, TROUBLESHOOTING).

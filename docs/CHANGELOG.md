# Changelog

All notable changes to the Fourth Estate Ansible Playbooks are documented here.
The format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Security
- **Elasticsearch superuser passwords no longer leak.**
  `elasticsearch_security` ran `elasticsearch-setup-passwords auto` with
  `no_log: false`, so every generated superuser password reached stdout — and
  under Automation Platform, the controller database, the job-history UI, and
  any forwarded log aggregation. It also redirected the same passwords to
  `/tmp/elasticsearch_passwords.txt`, which persisted at default permissions.
  That redirect additionally left `stdout` empty, so the follow-on "Save
  generated passwords" task wrote an empty file. Passwords are now captured in
  memory under `no_log: true`, the `/tmp` copy is gone, and the completion
  marker is written only after a successful run so a failure is retried rather
  than skipped forever.
- **Pure Storage API tokens no longer leak.**
  `pure_flasharray_config` looped a `debug` task over `api_tokens.results` with
  `no_log: false` and no loop label, printing each created API client's token
  in the task output. The loop now labels on the client name only.
- **Vendor API credentials no longer reach verbose output (550 tasks, 311 files).**
  Roles under `operational_technology/`, `claroty/`, `dragos/`, `pure_storage/`,
  `cohesity/`, `cisco/`, `sciencelogic/`, `tenable/`, `ansible/`, `veeam/`,
  `hashicorp_vault/`, `illumio/`, `crowdstrike/`, `infoblox/`, `azure/` and
  `sentinelone/` passed session cookies, CSRF tokens, API keys and bearer
  tokens in `ansible.builtin.uri` and `get_url` headers, bodies and URLs
  without `no_log`. Ansible prints a module's invocation arguments at `-vvv`, so
  raising verbosity to debug an API call published the credential with it — and
  under Automation Platform that output is the controller's job record, which
  outlives the run and is readable by anyone with access to the job. Each of
  those tasks now sets `no_log: true`.

  Measured on one task before and after the change, with a canary token and a
  live endpoint: the token appears in the result's
  `invocation.module_args.headers` at `-vvv`, and at no lower verbosity. So the
  exposure was real but bounded — it needed someone to raise verbosity, which is
  exactly what an operator does when an API call misbehaves.

  Two SD-WAN tasks in `sdwan_security_hardening` explicitly set `no_log: false`
  while sending a vManage session cookie; neither was overriding an enclosing
  block, so the setting bought nothing and cost the cookie. Both are now `true`.

  This changes only what is displayed. `no_log` does not affect execution, and
  registered results still carry their full data for later tasks to read.
- **Credentials on a command line no longer reach job output (16 tasks).**
  Sixteen `command` and `shell` tasks interpolated a credential
  into the command they ran: the ScienceLogic installers' `--db-root-password`
  and `--admin-password`, `falconctl --provisioning-token`, and
  `Connect-VIServer -Password` in thirteen vmware PowerCLI tasks. All now carry
  `no_log: true`.

  This class is more severe than the `uri` header class above, and in a way that
  is easy to get backwards. Measured on the CrowdStrike task before and after:

  | verbosity | before | after |
  |-----------|--------|-------|
  | default   | 1      | 0     |
  | `-vvv`    | 2      | 0     |

  A failing `command` puts the whole command string in its `cmd` field, and that
  field is part of the failure message printed at **default** verbosity. No `-vvv`
  required. Under Automation Platform, every failed run of those tasks wrote the
  credential into the controller's job record.

  What `no_log` does **not** cover is now documented in
  [`KNOWN_LIMITATIONS.md` section 16](KNOWN_LIMITATIONS.md#16-credentials-on-a-command-line),
  together with the measurements behind it: a command line stays readable through
  `ps` while the command runs; Ansible's `environment:` keyword is *worse* than a
  command line rather than better, putting the secret on two command lines and in
  three process environments; and `no_log` does not suppress an `environment:`
  secret at all, because the connection plugin prints its `EXEC` line before the
  module runs. Two tasks that pass a secret that way — `PGPASSWORD` for
  `pg_basebackup` and `ILLUMIO_PCE_ADMIN_PASSWORD` for the PCE installer — are
  recorded there rather than given a `no_log` that would not protect them.

- **Vault unseal keys and the root token no longer land in plaintext on the Vault node.**
  `vault_cluster` initialised a cluster and wrote the unseal (or recovery)
  shares and the initial root token to one file on the Vault server, mitigated
  by a `debug` task telling the operator to remove it by hand. Splitting a key
  into shares only protects anything if the shares end up in different hands;
  one file on the cluster gives that up, and `mode: 0600` does not help against
  a backup, a snapshot, or root on that host.

  The role now refuses to initialise unless Vault will PGP-encrypt every share
  and the root token to their holders — `vault_init_recovery_pgp_keys` under an
  auto-unseal seal, `vault_init_pgp_keys` under Shamir, plus
  `vault_init_root_token_pgp_key`. The refusal is a preflight, deliberately:
  failing after initialisation would leave a live Vault whose only copy of the
  shares sat in a `no_log` register nobody can read. Set
  `vault_allow_plaintext_key_material: true` to accept plaintext on a cluster
  you are willing to lose.

  Two bugs surfaced while fixing it, both worse than the exposure:

  - **The keys were never written at all.** The save was guarded by
    `when: vault_init_result is changed`, and `ansible.builtin.uri` reports
    `changed: false` for a successful POST — measured, not assumed. So the
    shares and root token were returned, held in a `no_log` register, and
    discarded when the play ended, leaving a cluster that could never be
    unsealed — while the next task printed "Unseal keys and root token saved to:
    /etc/vault.d/vault-init-keys.json", naming a file it had just skipped
    creating. Confirmed by running the previous version against a stub Vault:
    the initialize call goes out, no file appears, the message claims otherwise.
    The guard now tests the response for key material, and a response carrying
    none fails loudly.
  - **PGP was never actually requested.** `pgp_keys: "{{ vault_init_pgp_keys |
    default(omit) }}"` with a default of `[]` sends `pgp_keys: []`, because
    `default(omit)` only fires when a variable is *undefined*, not when it is
    empty. An operator who set nothing got plaintext; the `omit` was decorative.

- **The same `is changed` guard is fixed in two other roles.** A scan for the
  pattern found `elasticsearch_security` never writing down the API keys it had
  just created in Elasticsearch, and `vast_config` never waiting for an Active
  Directory join to finish before configuring SMB against it.

- **Two `no_log: true` keys that never did anything are gone.**
  One sat in `policy_as_code/inventory/example.yml`, where `no_log` is not an
  inventory keyword; the other was an element of a `specs` list item in a vmware
  playbook, which is data passed to a role, not a key on a task. Both read as
  protection that was not there. The vmware one is replaced by a real `no_log`
  on the task that actually runs the credential.
- **TLS certificate validation defaults to on (141 sites, 100 files).**
  Every hardcoded `validate_certs: false` became either a documented variable
  with a secure default (`"{{ <role>_validate_certs | default(true) }}"`) or a
  `true` default in `defaults/main.yml`. Bootstrap against self-signed
  endpoints is still supported — it is now an explicit, per-run opt-out rather
  than the shipped default. The worst cases were the HashiCorp Vault
  initialization call (which returns the root token and unseal keys) and the
  Illumio PCE verification tasks (which send the admin password with
  `force_basic_auth`).

### Added
- **Automation Platform controller as code (`ansible_tower/`, 5 roles)**: the
  directory named after the platform most customers consume this repository
  through had no working automation at all -- its README advertised 8 roles that
  the empty-role purge had removed, and `site.yml` said so and did nothing.
  It now declares a controller's organizations, teams and role bindings;
  credential types and credentials; projects, inventories and execution
  environments; job templates and surveys; and workflow job templates.

  Three preflight checks encode the safeguards that were easiest to lose in
  translation from the command line to a controller, each with a documented
  waiver:
  - a project must be pinned to a tag, not tracking a branch, because a project
    tracking `main` with *Update Revision on Launch* turns every commit here
    into an immediate change in that control plane
    (`aap_allow_branch_tracking`);
  - a job template must expose `apply_changes` on its survey or in its extra
    vars, since every playbook here defaults to a dry run and a template that
    hides the gate removes the safeguard from the operator
    (`aap_allow_template_without_apply_gate`);
  - a workflow must carry an approval node, which is the control AAP offers that
    the command line cannot: the pause and the person who approved it are
    recorded in the controller's own audit log, where `apply_changes` is only an
    assertion (`aap_allow_workflow_without_approval`).

  Every role is dry run by default and writes its plan on every run, including a
  dry run. Secrets never reach a plan: user passwords and credential `inputs`
  are dropped before the file is built rather than redacted afterwards, and the
  credential apply task runs under `no_log`. The plans are published through
  `set_stats` under `fe_evidence`, so they survive an execution-environment
  container like the rest of the repository's compliance evidence.

  `vars/fourth_estate_controller.example.yml` is a worked configuration against
  real playbook paths in this repository: an assess/apply template pair,
  credential types for the Cisco ISE and Infoblox APIs, and an
  assess/approve/apply workflow.

- **Execution Environment (`execution_environment/`)**: an ansible-builder v3
  definition that builds one image capable of running any playbook in this
  repository. `requirements.yml` there is the union of all 79 platform
  requirements files (58 collections) merged to the highest declared version
  floor; `generate-lock.sh` resolves those floors into exact pins
  (`requirements-lock.yml`) so every environment builds an identical
  collection set, and `build.sh` prefers the lock when present. Includes
  `requirements.txt` (WinRM/Kerberos/network transports), `bindep.txt`, and a
  README covering base-image choice, the two Automation-Hub-only collections,
  and registering the image in Automation Controller.
- README guidance to pin AAP *projects* to a release tag rather than `main`.

## [1.1.0] — 2026-08-19

Everything that landed on `main` since the `Prod1` release. Published as
[GitHub release `1.1.0`](https://github.com/Koga1985/Fourth-Estate-Ansible-Playbooks/releases/tag/1.1.0)
— the first semver-tagged release.

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

# Production Readiness Assessment

**Repository:** Fourth-Estate-Ansible-Playbooks
**Assessment date:** 2026-06-15
**Scope:** All Ansible content (playbooks, roles, tasks) and documentation
**Method:** Static analysis with `yamllint`, Python YAML parser, and structural/semantic
grep audits. `ansible-core 2.19` and `ansible-lint` were installed locally; full
`--syntax-check` against vendor collections was **not** possible because Ansible Galaxy
is unreachable from the build environment (HTTP 403), so collection-resolved checks are
out of scope for this pass.

---

> **UPDATE 2026-06-15 — P0 remediation applied.** All hard blockers identified in this
> report have been fixed and verified (0 YAML parse failures, 0 duplicate keys, 0
> references to non-existent modules across all 3,474 YAML files). See
> **"Remediation applied"** below for details and the small set of follow-ups that need
> owner sign-off. The original findings are preserved below for the record.

## Verdict: NOT production ready (looks ready, does not yet run)

The repository is **broad, well-organized, and structurally professional** — 43 vendor
areas, ~556 roles, customer scaffolding (`inventory.example`, `vault.yml.example`) present
in **every** vendor directory, `requirements.yml` widely declared, real modules (not debug
stubs) doing real work, and dry-run defaults in places. The "grab it, change variables,
run it" intent is clearly designed in.

**However, a customer cannot grab many of these and run them today.** Automated parsing
found **86 files with hard YAML syntax errors** that abort `ansible-playbook` before any
task executes, plus **~50 runtime-fatal references to non-existent modules** and **~50
duplicate-key bugs** that silently do the wrong thing. Several documents assert
"PRODUCTION READY ✅", "ALL TESTS PASSED", and "YAML SYNTAX VALIDATION ✅ PASS" — claims
the code contradicts. This is the gap between *looks* production ready and *is* production
ready.

| Category | Result |
|---|---|
| Files that fail to parse (hard blocker) | **86** |
| Non-existent / wrong-namespace module references (runtime fatal) | **~50 files** |
| Duplicate-key bugs (silent wrong behavior) | **~50 occurrences** |
| Customer scaffolding (inventory/vault examples) | ✅ Present in all 43 areas |
| `requirements.yml` collection declarations | ✅ Broad coverage |
| Hardcoded production secrets | ✅ None found (examples/placeholders only) |
| Documentation accuracy | ⚠️ Overclaims testing; minor count drift |

---

## P0 — Hard blockers (playbook aborts before running)

### 1. 86 files do not parse as valid YAML

These were confirmed with the standard Python YAML parser (not just linter strictness).
None are false positives from Ansible custom tags (`!vault`/`!unsafe`). They fall into a
small number of **systematic, auto-generated patterns** — strong evidence the affected
files were never executed:

| # | Pattern | Files | Root cause | Fix |
|---|---|---|---|---|
| A | Unquoted colon in string | 24 | `description: Bootstrap Grid: create members…` — the second `:` ends the mapping | Quote the value |
| B | Invalid `**_creds` dict-unpack | 18 (all Infoblox) | `**_creds` Python-style spread is not YAML; the auth block never loads | Replace with a real var merge / explicit keys |
| C | Play body indentation break | 28 (all `ansible/tasks/ans_*`) | `tasks:` is dedented to column 0, outside the play mapping | Re-indent `tasks:`/`pre_tasks:` consistently |
| D | Bad backslash escape in `"…"` | 4 | `'no \1'`, `\s`, `\W` regex backrefs inside double quotes | Single-quote the Jinja or escape `\\` |
| F | Broken inline `[ ]` sequence | 3 | malformed flow sequence | Fix bracket/element syntax |
| G | Indentation / block structure | 6 | mis-nested mappings | Re-indent |
| H | Other structural | 3 | misc | Case-by-case |

**Example B — `infoblox/tasks/infoblox_rpz_policies.yml` (every Infoblox role is affected):**
```yaml
    params:
      _return_as_object: 1
      "_return_fields+": "fqdn,name,comment"
    **_creds          # <-- not valid YAML; file never loads
```

**Example C — `ansible/tasks/ans_ctrl__credentials.yml` (all 28 AAP controller tasks):**
```yaml
- name: ans_ctrl__credentials.yml
  hosts: localhost
  vars: ...
  pre_tasks: ...
tasks:                # <-- dedented to col 0, outside the play -> parse error
  - name: Plan credentials
```

Full file list is in **Appendix A**.

### 2. References to modules that do not exist (runtime fatal)

These parse fine but fail the moment the task runs:

- **`ansible.builtin.syslog`** — no such module exists. **29 files** (mostly `cisco/roles/ise_*`
  and `illumio/roles/illumio_ot_acl_deployment` handlers). Use `community.general.syslogger`
  or `ansible.builtin.command: logger …`.
- **`ansible.builtin.mail`** — `mail` lives in **`community.general.mail`**, not builtin.
  **32 files** (notification handlers across `cisco/roles/ise_*`, `ansible/roles/*`). Change
  the FQCN and add `community.general` to the relevant `requirements.yml`.

Because these sit in **handlers** ("notify on change"), they only fire on a successful
change — so they would pass a smoke test and then fail the first real run in production.

### 3. Duplicate keys — parse silently, behave wrong (~50 occurrences)

PyYAML keeps the **last** duplicate key and discards the first with no error, so these
"work" while doing the wrong thing — the most dangerous class for production:

- `vars:` declared twice (most `arista/tasks/*`, `cisco/tasks/ise_*`, `veeam`, `cohesity`)
  — the first `vars:` block (often the real defaults) is dropped.
- `when:` declared twice (`ansible/roles/ans_access_sso_directory`, several `arista` roles,
  `palo_alto`, `illumio`) — one condition is silently ignored, so tasks run when they
  shouldn't (or vice-versa).
- `password:` twice (`cisco/.../ucs_security_hardening`, `aci_network_config/bgp_peers`),
  `loop:` twice, duplicate default vars (`postgresql_config/defaults`,
  `pure_flasharray_performance/defaults`).

Full list in **Appendix B**.

---

## P1 — Should fix before customer hand-off

- **Documentation overclaims testing.** `cisco/playbooks/PLAYBOOK_TEST_RESULTS.txt` states
  "TEST STATUS: ✅ ALL TESTS PASSED" and "YAML SYNTAX VALIDATION ✅ PASS"; `IMPLEMENTATION_COMPLETE.md`
  and multiple READMEs say "PRODUCTION READY" / "battle-tested". With 86 parse failures
  present, these are not defensible and erode customer trust. Either make them true (CI gate,
  below) or soften the language to reflect actual validation status.
- **Secret hygiene gap.** ~788 files pass `password`/`secret`/`token` to a module; only ~431
  use `no_log`. Tasks handling secrets should set `no_log: true` to avoid leaking into job
  output/logs.
- **No CI gate.** There is no `.github/workflows`, `.ansible-lint`, or `.yamllint` config in
  the repo. Every issue above is mechanically detectable; the reason they shipped is that
  nothing runs `yamllint` / `ansible-playbook --syntax-check` on push. This is the single
  highest-leverage fix — it prevents regression of all P0 items.

## P2 — Polish

- **Count drift in `README.md`.** Header says "550 roles / 3,395 YAML files / 37 platforms",
  body says "39+ technologies"; actual counts are ~556 role `main.yml`, 3,474 `.yml`, 43
  vendor directories. Per-vendor numbers also drift (e.g. VMware "32 roles" vs 25 found).
  Generate these from the tree rather than hand-maintaining.
- **Idempotency is reasonable** (~314 files use `command`/`shell`, ~315 use `changed_when`),
  but worth a spot-audit to confirm raw commands pair with `changed_when`/`creates`.

---

## What is genuinely good (keep)

- Consistent role layout (`tasks/handlers/defaults/meta/templates/README`) across 556 roles.
- **Customer-onboarding scaffolding in every vendor area** — `inventory.example` and
  `vault.yml.example` present everywhere; many roles ship `playbooks/vars.example.yml`.
- `requirements.yml` declared broadly (collections are at least documented).
- Real automation, not placeholders — heavy use of `uri`, vendor REST/config modules
  (`cisco.aci.aci_rest`, `arista.eos.eos_config`, `paloaltonetworks.panos.*`,
  `amazon.aws.*`, `azure.azcollection.*`).
- No hardcoded production secrets detected.
- Dry-run defaults (`apply_changes: false`) in the Cisco content — a good safety pattern to
  propagate everywhere.
- Strong supporting docs: `COMPLIANCE_MAPPING.md`, `TROUBLESHOOTING.md`,
  `KNOWN_LIMITATIONS.md`, `CUSTOMER_QUICK_START.md`.

---

## Recommended remediation path

1. **Add a CI gate first** (`.yamllint`, `.ansible-lint`, and a GitHub Action running
   `yamllint .` + `ansible-playbook --syntax-check`). This makes "production ready" a
   verifiable state instead of a claim, and stops regressions.
2. **Fix the 86 parse failures** (Appendix A) — largely mechanical, pattern-by-pattern.
3. **Fix the ~50 fake-module references** — rename `ansible.builtin.mail` →
   `community.general.mail`, replace `ansible.builtin.syslog`, update `requirements.yml`.
4. **Fix the ~50 duplicate-key bugs** (Appendix B) — verify which value was intended.
5. **Reconcile documentation** with reality (testing claims + counts).
6. **Sweep `no_log`** onto secret-handling tasks.

Once 1–4 are done and `yamllint .` is clean, the repository moves from *looks ready* to
*demonstrably parseable and runnable*, and the customer "change variables and run" promise
holds.

---

## Remediation applied (2026-06-15)

All P0 blockers were fixed across **180 files**. Verification: `python3 -c "yaml.safe_load_all"`
over all 3,474 YAML files and `yamllint` key-duplicate scan both come back clean.

| Fix | Count | What was done |
|---|---|---|
| YAML parse failures | 86 → 0 | Quoted colon-bearing `name:`/`description:` values; replaced invalid `**_creds` spread with explicit `url_username`/`url_password`/`force_basic_auth`/`validate_certs`; re-indented dedented `tasks:`/`handlers:` blocks back under their play; merged dedented duplicate `vars:` blocks; fixed `\1`/`\s`/`\W` escapes and nested quotes; converted broken inline `that: [ … ]` to block lists; quoted bare `{{ }}` scalars |
| Non-existent module refs | 61 → 0 | `ansible.builtin.mail` → `community.general.mail` (32); `ansible.builtin.syslog` → `community.general.syslogger` (29). `community.general` already declared in the affected `requirements.yml` files |
| Duplicate keys | ~50 → 0 | Merged duplicate `vars:` blocks (both keys preserved); merged duplicate `when:` into a single `(a) and (b)` (preserves the `apply_changes` safety gate); deduped identical defaults; `vmware_host_dns` second `hostname:` → correct `host_name:` param |
| Single-brace Jinja `"{ x }"` | 66 → 1 | Converted to `"{{ x }}"` (these were rendering literally). The 1 remaining is a legitimate AWS CloudWatch metric-filter pattern, intentionally left as-is |

### Follow-ups needing owner sign-off (functional, not parse-level)

These were made **runnable** but reflect deeper design choices the module owner should confirm:

1. **`cisco/roles/ucs_security_hardening/tasks/access_control.yml`** and
   **`cisco/roles/aci_network_config/tasks/bgp_peers.yml`** — a resource-level `password`
   (UCS local-user password / BGP MD5 key) collided with the module's **connection**
   `password`. The connection credential was kept (required to authenticate); the
   resource-level password line was removed. To actually provision those secrets, use the
   module-appropriate parameter rather than the shared `password` key, and verify against
   the collection docs.
2. **`splunk/roles/splunk_indexer_cluster/tasks/main.yml`** — a task had two `loop:` keys
   with contradictory logic (one silently won). Rewrote it to a `product()` loop that
   creates all four sub-directories per index. Confirm the resulting paths match your
   Splunk layout.
3. **`dragos/roles/dragos_mssp_orchestrator/tasks/include_action.yml`** — removed an invalid
   YAML merge key (`<<: "{{ action_vars }}"`) that never parsed. Caller-provided vars still
   propagate via normal scoping; if you need explicit per-action var injection, pass them
   through `include_tasks … vars:` or `combine()`.

### Still open (P1/P2 — not addressed in this pass)

- Documentation testing claims (`PLAYBOOK_TEST_RESULTS.txt`, "PRODUCTION READY",
  "battle-tested") should be reconciled with reality or backed by a CI gate.
- No CI gate yet — add `.yamllint`, `.ansible-lint`, and a GitHub Action running
  `yamllint .` + `ansible-playbook --syntax-check` so these issues cannot regress. This
  remains the single highest-leverage improvement.
- `no_log` coverage on secret-handling tasks (~45% gap).
- README count drift.

> Note on scope: Ansible Galaxy is unreachable from the build environment, so vendor
> collections could not be installed and full `ansible-playbook --syntax-check` /
> `ansible-lint` (which resolve FQCN modules against installed collections) could not be
> run. Verification here is YAML-parse + structural. Running the CI gate above in an
> environment with Galaxy access is recommended to catch any collection-level issues.

---

## Appendix A — 86 files that fail to parse

### A. Unquoted colon in string value (24)
arista/tasks/arista_cvp__inventory_model.yml · dragos/roles/dragos_governance_pack/meta/main.yml ·
dragos/roles/dragos_sensor_ops/meta/main.yml · dragos/tasks/dragos_cases__status_sync.yml ·
google_cloud_platform/roles/gcp_assured_workloads_operations/meta/main.yml ·
google_cloud_platform/roles/gcp_cloudrun_locked_down/meta/main.yml ·
google_cloud_platform/roles/gcp_landing_zone_dod/meta/main.yml ·
google_cloud_platform/roles/gcp_scc_response_playbooks/meta/main.yml ·
google_cloud_platform/tasks/gcp_bq__datasets_policies.yml ·
infoblox/roles/infoblox_capacity_reports/meta/main.yml · infoblox/roles/infoblox_dhcp_failover/meta/main.yml ·
infoblox/roles/infoblox_grid_bootstrap/meta/main.yml · infoblox/roles/infoblox_inventory_model/meta/main.yml ·
infoblox/roles/infoblox_rpz_policies/meta/main.yml · openshift/roles/ocp_cost_management/meta/main.yml ·
openshift/tasks/ocp_olm__subscriptions_lifecycle.yml ·
operational_technology/roles/ot_change_window_guard/tasks/includes/window_assert.yml ·
operational_technology/roles/ot_metrics_reporting/meta/main.yml ·
operational_technology/roles/ot_network_backup/tasks/includes/restore_dryrun.yml ·
palo_alto/roles/pa_vpn_ipsec/tasks/main.yml · palo_alto/roles/panorama_fleet_package/tasks/main.yml ·
vmware/roles/cluster_baseline/meta/main.yml · vmware/roles/guest_customization_specs/meta/main.yml ·
vmware/roles/vm_placement_policies/meta/main.yml

### B. Invalid `**_creds` dict-unpack — all Infoblox (18)
infoblox/day0_deploy_config/roles/infoblox_audit_compliance/tasks/main.yml ·
infoblox/day0_deploy_config/roles/infoblox_extattrs_enforce/tasks/main.yml ·
infoblox/day0_deploy_config/roles/infoblox_grid_bootstrap/tasks/main.yml ·
infoblox/day0_deploy_config/roles/infoblox_rpz_policies/tasks/main.yml ·
infoblox/day0_deploy_config/roles/infoblox_tsig_acls/tasks/main.yml ·
infoblox/roles/infoblox_capacity_reports/tasks/main.yml · infoblox/roles/infoblox_dhcp_failover/tasks/main.yml ·
infoblox/roles/infoblox_dnssec/tasks/main.yml · infoblox/roles/infoblox_grid_bootstrap/tasks/main.yml ·
infoblox/roles/infoblox_grid_upgrade/tasks/main.yml · infoblox/roles/infoblox_rpz_policies/tasks/main.yml ·
infoblox/tasks/infoblox_audit_compliance.yml · infoblox/tasks/infoblox_capacity_reports.yml ·
infoblox/tasks/infoblox_dhcp_failover.yml · infoblox/tasks/infoblox_extattrs_enforce.yml ·
infoblox/tasks/infoblox_rpz_policies.yml · infoblox/tasks/infoblox_subnet_lifecycle.yml ·
infoblox/tasks/infoblox_tsig_acls.yml

### C. Play body indentation break — all `ansible/tasks/ans_*` + policy_as_code (28)
ansible/tasks/ans_core__fact_caching.yml · ans_ctrl__api_health · ans_ctrl__approvals ·
ans_ctrl__audit_export · ans_ctrl__backups_export · ans_ctrl__content_signed_only · ans_ctrl__credentials ·
ans_ctrl__ee_images_map · ans_ctrl__ee_registries · ans_ctrl__instance_groups · ans_ctrl__inventories_sources ·
ans_ctrl__job_cleaner · ans_ctrl__notifications · ans_ctrl__org_settings · ans_ctrl__orgs_teams ·
ans_ctrl__projects_git · ans_ctrl__restore_sandbox · ans_ctrl__schedules · ans_ctrl__survey_policies ·
ans_ctrl__upgrade_window · ans_ctrl__wf_pipelines · ans_perf__forks_strategy ·
ans_perf__instance_group_placement · ans_perf__ssh_controlpersist · ans_secrets__env_to_vault ·
ans_secrets__vault_rotate · ans_sso__ldap_saml · policy_as_code/site.yml

### D. Bad backslash escape in double-quoted string (4)
arista/tasks/arista_stig__hardening.yml · illumio/tasks/illumio_ven__install_windows.yml ·
vmware/roles/guest_customization_specs/playbooks/vmware.guest-customization-specs.ensure.yml ·
vmware/roles/linux_virtual_machine_provsion/tasks/main.yml

### F. Broken inline flow sequence (3)
illumio/roles/illumio_policy_lifecycle/tasks/includes/illumio_policy__promote.yml ·
illumio/tasks/illumio_policy__promote.yml · sciencelogic/tasks/sl1_admin__orgs_and_users.yml

### G. Indentation / block structure (6)
checkpoint/cp_day0_deploy_configure/roles/cp_identity_awareness/tasks/cp_ia__ad_connectors.yml ·
checkpoint/roles/cp_identity_awareness/tasks/cp_ia__ad_connectors.yml ·
checkpoint/tasks/cp_ia__ad_connectors.yml ·
illumio/roles/illumio_reporting_pack/tasks/includes/illumio_report__daily_digest.yml ·
illumio/tasks/illumio_report__daily_digest.yml ·
infoblox/roles/infoblox_rpz_policies/playbooks/infoblox.rpz-policies.apply.yml

### H. Other structural (3)
dragos/roles/dragos_mssp_orchestrator/tasks/include_action.yml ·
kubernetes/roles/k8s-rbac-management/tasks/service-accounts.yml ·
veeam/roles/veeam_backup_server_config/tasks/main.yml

---

## Appendix B — Duplicate-key occurrences (parse OK, silent override)

`cisco/tasks/ise_*` (17 files, duplicate `vars:`) · cisco/roles/ucs_security_hardening/tasks/access_control.yml
(`password`) · cisco/roles/aci_network_config/tasks/external_epgs.yml (`loop`) ·
cisco/roles/aci_network_config/tasks/bgp_peers.yml (`password`) · veeam/tasks/veeam_job_run_now.yml (`vars`) ·
cohesity/tasks/cohesity_job_run_now.yml (`vars`) · palo_alto/roles/pa_logging_telemetry/tasks/bind_to_rules.yml
(`when`) · ansible/roles/ans_access_sso_directory/tasks/main.yml (`when` ×2) ·
arista/tasks/* (13 files, `vars`) · arista/roles/arista_backup_restore/tasks/main.yml (`when`) ·
arista/roles/arista_interfaces_fabric/tasks/main.yml (`when` ×2) ·
arista/roles/arista_cvp_inventory_model/tasks/main.yml (`when`) ·
vmware/roles/vsphere_esxi_config/tasks/main.yml (`hostname`) ·
checkpoint/roles/cp_access_policy/tasks/cp_policy__hitcount_report.yml (`mode`) ·
databases/postgresql/roles/postgresql_config/defaults/main.yml (`postgresql_log_directory`,
`postgresql_effective_cache_size`) · pure_storage/roles/pure_flasharray_performance/defaults/main.yml
(`flasharray_nvme_queue_depth`) · illumio/tasks/illumio_labels__golden_enforce.yml (`when`) ·
splunk/roles/splunk_indexer_cluster/tasks/main.yml (`loop`)

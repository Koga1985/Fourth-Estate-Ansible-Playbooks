# Dynatrace log monitoring (`dynatrace_log_monitoring`)

Assesses and (optionally) enforces **Dynatrace log monitoring** via the Dynatrace Settings 2.0 API.
Maps to **NIST 800-53 AU-9 / SC-28 (log masking, storage)**.

## Why "grab and go"
* Read-only **assessment** of the relevant Settings 2.0 objects
  (`builtin:logmonitoring.sensitive-data-masking-settings`) runs out of the box; `apply_changes=false` performs zero writes;
  token `no_log`.
* Enforcement is a **data-driven** list (`dt_log_operations`) of Settings 2.0 calls,
  gated behind `apply_changes=true` and validated against your tenant schema.

## Quick start
```bash
cd dynatrace/roles/dynatrace_log_monitoring/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/dynatrace-artifacts/dynatrace_log_monitoring.json
```

> Inspect the exact schema/fields with `GET /api/v2/settings/schemas/builtin:logmonitoring.sensitive-data-masking-settings`
> before populating `dt_log_operations`. Token scopes: `settings.read settings.write`.

## Tags
`--tags assess` (read-only), `apply`, `report`.

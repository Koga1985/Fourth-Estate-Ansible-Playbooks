# Dynatrace data privacy / masking (`dynatrace_data_privacy`)

Assesses and (optionally) enforces **Dynatrace data privacy / masking** via the Dynatrace Settings 2.0 API.
Maps to **NIST 800-53 SC-28 / SI-12 (PII masking, data privacy)**.

## Why "grab and go"
* Read-only **assessment** of the relevant Settings 2.0 objects
  (`builtin:preferences.privacy`) runs out of the box; `apply_changes=false` performs zero writes;
  token `no_log`.
* Enforcement is a **data-driven** list (`dt_privacy_operations`) of Settings 2.0 calls,
  gated behind `apply_changes=true` and validated against your tenant schema.

## Quick start
```bash
cd dynatrace/roles/dynatrace_data_privacy/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/dynatrace-artifacts/dynatrace_data_privacy.json
```

> Inspect the exact schema/fields with `GET /api/v2/settings/schemas/builtin:preferences.privacy`
> before populating `dt_privacy_operations`. Token scopes: `settings.read settings.write`.

## Tags
`--tags assess` (read-only), `apply`, `report`.

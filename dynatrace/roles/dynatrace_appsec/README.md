# Dynatrace Application Security (`dynatrace_appsec`)

Assesses and (optionally) enforces **Dynatrace Application Security** via the Dynatrace Settings 2.0 API.
Maps to **NIST 800-53 SA-11 / RA-5 (runtime vulnerability + attack protection)**.

## Why "grab and go"
* Read-only **assessment** of the relevant Settings 2.0 objects
  (`builtin:appsec.attack-protection-advanced-config`) runs out of the box; `apply_changes=false` performs zero writes;
  token `no_log`.
* Enforcement is a **data-driven** list (`dt_appsec_operations`) of Settings 2.0 calls,
  gated behind `apply_changes=true` and validated against your tenant schema.

## Quick start
```bash
cd dynatrace/roles/dynatrace_appsec/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/dynatrace-artifacts/dynatrace_appsec.json
```

> Inspect the exact schema/fields with `GET /api/v2/settings/schemas/builtin:appsec.attack-protection-advanced-config`
> before populating `dt_appsec_operations`. Token scopes: `settings.read settings.write`.

## Tags
`--tags assess` (read-only), `apply`, `report`.

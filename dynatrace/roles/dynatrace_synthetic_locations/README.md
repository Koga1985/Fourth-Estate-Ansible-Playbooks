# Dynatrace private synthetic locations (`dynatrace_synthetic_locations`)

Manages **private synthetic locations (run on ActiveGates with the synthetic capability)** via the Dynatrace REST APIs.

## Why "grab and go"
* Read-only **assessment** (`GET /api/v2/synthetic/locations`) runs out of the box;
  `apply_changes=false` performs zero writes; token `no_log`.
* Enforcement is a **data-driven** list (`dt_synthetic_location_operations`) gated behind
  `apply_changes=true` and validated against your tenant's API docs.

## Quick start
```bash
cd dynatrace/roles/dynatrace_synthetic_locations/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/dynatrace-artifacts/dynatrace_synthetic_locations.json
```

Token scopes: `ExternalSyntheticIntegration`.

## Tags
`--tags assess` (read-only), `apply`, `report`.

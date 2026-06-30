# Dynatrace Extensions (Framework 2.0) (`dynatrace_extensions`)

Manages **Extension Framework 2.0 install/activate** via the Dynatrace REST APIs.

## Why "grab and go"
* Read-only **assessment** (`GET /api/v2/extensions`) runs out of the box;
  `apply_changes=false` performs zero writes; token `no_log`.
* Enforcement is a **data-driven** list (`dt_extension_operations`) gated behind
  `apply_changes=true` and validated against your tenant's API docs.

## Quick start
```bash
cd dynatrace/roles/dynatrace_extensions/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/dynatrace-artifacts/dynatrace_extensions.json
```

Token scopes: `extensions.read extensions.write`.

## Tags
`--tags assess` (read-only), `apply`, `report`.

# Dynatrace cloud integrations (`dynatrace_cloud_integrations`)

Manages **AWS/Azure/GCP monitoring connectors** via the Dynatrace REST APIs.

## Why "grab and go"
* Read-only **assessment** (`GET /api/config/v1/aws/credentials`) runs out of the box;
  `apply_changes=false` performs zero writes; token `no_log`.
* Enforcement is a **data-driven** list (`dt_cloud_operations`) gated behind
  `apply_changes=true` and validated against your tenant's API docs.

## Quick start
```bash
cd dynatrace/roles/dynatrace_cloud_integrations/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/dynatrace-artifacts/dynatrace_cloud_integrations.json
```

Token scopes: `ReadConfig WriteConfig`.

## Tags
`--tags assess` (read-only), `apply`, `report`.

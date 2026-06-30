# Dynatrace Tenant Config (`dynatrace_tenant_config`)

Configures a **Dynatrace tenant** via the Configuration / Settings 2.0 REST APIs
(management zones, alerting profiles, auto-tags, problem notifications,
maintenance windows). Uses `ansible.builtin.uri` only.

## Why "grab and go"
* Assessment runs out of the box against any tenant and reports counts of
  management zones / alerting profiles / auto-tags — no write risk.
* `apply_changes=false` (default) performs **zero** writes.
* Enforcement is a **data-driven** operations list (`dt_config_operations`) so it
  stays correct across API versions — validate each call against your tenant's
  API docs before enabling.

## Quick start
```bash
cd dynatrace/roles/dynatrace_tenant_config/playbooks
cp inventory.example inventory && $EDITOR inventory      # env URL + vaulted API token
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
cat /tmp/dynatrace-artifacts/dynatrace_tenant_config.json
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
```

## Token scopes
`ReadConfig`, `WriteConfig`, `settings.read`, `settings.write` (least privilege).

## Tags
`--tags assess` (read-only), `apply`, `report`.

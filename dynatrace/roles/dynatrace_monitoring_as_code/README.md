# Dynatrace Monitoring-as-Code (`dynatrace_monitoring_as_code`)

Provisions **SLOs, synthetic monitors and dashboards** from version-controlled
definitions via the Dynatrace REST APIs.

## Why "grab and go"
* Read-only **assessment** (counts of SLOs / synthetic monitors / dashboards)
  runs out of the box; `apply_changes=false` performs zero writes; token `no_log`.
* Enforcement is a **data-driven** operations list (`dt_mac_operations`) — define
  your SLOs/monitors/dashboards as data and apply with `apply_changes=true`.

## Quick start
```bash
cd dynatrace/roles/dynatrace_monitoring_as_code/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/dynatrace-artifacts/dynatrace_monitoring_as_code.json
```

## Token scopes
`slo.write`, `ExternalSyntheticIntegration`, `WriteConfig` (dashboards).

## Tags
`--tags assess` (read-only), `apply`, `report`.

# Dynatrace Notifications (`dynatrace_notifications`)

Manages **Dynatrace problem-notification integrations** — ServiceNow, Slack,
email, PagerDuty, Jira, webhooks — via the Configuration API, tied to alerting
profiles.

## Why "grab and go"
* Read-only **assessment** of existing notifications runs out of the box;
  `apply_changes=false` performs zero writes; token + secrets `no_log`.
* Enforcement is a **data-driven** list (`dt_notifications`) — define each
  integration as data and apply with `apply_changes=true`.

## Quick start
```bash
cd dynatrace/roles/dynatrace_notifications/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/dynatrace-artifacts/dynatrace_notifications.json
```

Integrations bind to an **alerting profile** (create one with
`dynatrace_tenant_config`). Token scope: `WriteConfig`.

## Tags
`--tags assess` (read-only), `apply`, `report`.

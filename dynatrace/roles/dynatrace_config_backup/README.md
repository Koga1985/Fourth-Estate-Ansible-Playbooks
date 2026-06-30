# Dynatrace Config Backup (`dynatrace_config_backup`)

Exports **Dynatrace tenant configuration** to timestamped JSON files for
disaster recovery and change-audit (config-as-code-style backup). **Read-only**
against Dynatrace.

## Why "grab and go"
* Pure read (`GET`) — no tenant changes; token `no_log`.
* Writes one JSON file per object type (management zones, alerting profiles,
  auto-tags, notifications, dashboards, maintenance windows, request attributes,
  SLOs, synthetic monitors, API-token inventory) plus selected Settings 2.0
  schemas, under a timestamped backup directory. Designed to run on a **schedule**.

## Quick start
```bash
cd dynatrace/roles/dynatrace_config_backup/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml
cat /tmp/dynatrace-artifacts/dynatrace_config_backup.json   # manifest
ls -R /var/backups/dynatrace/                               # the backup set
```

## Customize
Edit `dt_backup_endpoints` and `dt_backup_settings_schemas` to add/remove object
types. Token scopes: `ReadConfig`, `settings.read`.

## Tags
`--tags backup`, `report`.

# Dynatrace OneAgent Lifecycle (`dynatrace_oneagent_lifecycle`)

Manages the lifecycle of an **already-installed OneAgent** across a fleet:
version assessment, host-group / network-zone / monitoring-mode changes, service
restart, and a **guarded decommission/uninstall**.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` only reports the current version and
  what *would* change — no reconfigure, restart, or uninstall.
* **Decommission is double-gated**: requires both `apply_changes=true` **and**
  `oneagent_decommission=true`.
* Per-host JSON lifecycle artifact.

## Quick start
```bash
cd dynatrace/roles/dynatrace_oneagent_lifecycle/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml                                   # ASSESS (versions)
ansible-playbook -i inventory run.yml -e apply_changes=true \
  -e oneagent_set_host_group=PROD                                       # RECONFIGURE
ansible-playbook -i inventory run.yml -e apply_changes=true \
  -e oneagent_decommission=true --limit retired-host                    # DECOMMISSION
cat /tmp/dynatrace-artifacts/app-linux-01_oneagent_lifecycle.json
```

> OneAgent self-updates from the cluster (auto-update); to pin/upgrade versions,
> manage the auto-update policy centrally or re-run `dynatrace_oneagent`.

## Tags
`--tags assess`, `reconfigure`, `decommission`, `report`.

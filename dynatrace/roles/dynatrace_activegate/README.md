# Dynatrace ActiveGate (`dynatrace_activegate`)

Deploys a **Dynatrace ActiveGate** on Linux and sets its collector group /
network zone.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` only reports whether ActiveGate is
  installed and what would change — no download, install, or restart.
  `apply_changes=true` installs (fresh) or updates `custom.properties` and
  manages the service; a per-host state artifact is written.

## Quick start
```bash
cd dynatrace/roles/dynatrace_activegate/playbooks
ansible-galaxy collection install community.general
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e apply_changes=true # INSTALL/CONFIGURE
```

## Key variables
| Variable | Purpose |
|----------|---------|
| `dt_environment_url` / `dt_paas_token` | tenant URL + PaaS token (`InstallerDownload`) — vault it |
| `activegate_group` | collector group (`custom.properties [collector] group`) |
| `activegate_network_zone` | network zone for OneAgent affinity |

## ⚠️ Notes
* Network zone is set via the installer on fresh installs and via
  `custom.properties` on existing ones; both trigger an ActiveGate restart.

## Tags
`--tags activegate`, `report`.

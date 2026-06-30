# Dynatrace OneAgent (`dynatrace_oneagent`)

Deploys and configures the **Dynatrace OneAgent** on Linux and Windows hosts.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` only checks whether OneAgent is
  installed and reports what it *would* do — no download, install, or restart.
  `apply_changes=true` installs (fresh) or reconfigures via `oneagentctl`
  (idempotent), and writes a per-host state artifact.
* Cross-platform (Linux installer `.sh` / Windows `.exe`), `no_log` on tokens.

## Quick start
```bash
cd dynatrace/roles/dynatrace_oneagent/playbooks
ansible-galaxy collection install ansible.windows
cp inventory.example inventory && $EDITOR inventory      # tenant URL + vaulted PaaS token
ansible-playbook -i inventory run.yml                       # DRY-RUN (assessment)
ansible-playbook -i inventory run.yml -e apply_changes=true # INSTALL/CONFIGURE
```

## Key variables
| Variable | Purpose |
|----------|---------|
| `dt_environment_url` | SaaS `https://<env-id>.live.dynatrace.com` or Managed `.../e/<env-id>` |
| `dt_paas_token` | PaaS token (scope `InstallerDownload`) — **vault it** |
| `oneagent_host_group` / `oneagent_network_zone` | logical grouping / ActiveGate affinity |
| `oneagent_monitoring_mode` | `fullstack` \| `infra-only` \| `discovery` |
| `oneagent_app_log_content_access` | **security**: keep `false` unless required |

## ⚠️ Notes
* The PaaS token only needs `InstallerDownload`; rotate it per policy.
* Existing agents are reconfigured with `oneagentctl` rather than reinstalled.

## Tags
`--tags linux`, `windows`, `report`.

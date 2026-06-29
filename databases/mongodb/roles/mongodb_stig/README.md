# MongoDB Enterprise STIG (`mongodb_stig`)

Hardens and assesses **MongoDB Enterprise** to the DISA STIG by managing the
security-relevant settings of `mongod.conf`.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` renders the managed `mongod.conf`
  and shows the **diff in check mode without writing or restarting**.
  `apply_changes=true` writes it (timestamped backup kept) and restarts mongod.
* Per-host JSON evidence artifact (with an assessment of the current file).

## Quick start
```bash
cd databases/mongodb/roles/mongodb_stig/playbooks
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml --diff                  # DRY-RUN (config diff)
ansible-playbook -i inventory run.yml -e apply_changes=true   # ENFORCE (+restart)
cat /tmp/mongodb-stig-artifacts/mongo-01_mongodb_stig.json
```

## Controls
RBAC enabled (`security.authorization`), server-side JavaScript disabled, TLS
required (`net.tls.mode=requireTLS` + disabled legacy protocols), audit logging
(`auditLog`), `bindIp` not `0.0.0.0`, and `SCRAM-SHA-256` authentication.

## ⚠️ Pre-flight
* The role manages the **whole** `mongod.conf` from variables — merge your
  site-specific tuning into `defaults`/vars and **review the `--diff`** first.
* `requireTLS` needs valid certificate/CA files in place before enforcing.
* After enabling `authorization`, create admin + least-privilege users (mongosh).
* Changes trigger a **mongod restart** — schedule a window.

## Tags
`--tags assess`, `config`, `report`, `stig_cat2`.

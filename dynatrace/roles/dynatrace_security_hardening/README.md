# Dynatrace Security Hardening (`dynatrace_security_hardening`)

Assesses and hardens a **Dynatrace tenant's security posture** against
**NIST 800-53 Rev 5** (AC/AU/IA/SC) via the Dynatrace REST APIs. (There is no
DISA STIG for Dynatrace; this applies vendor + NIST best practices.)

## Why "grab and go"
* Assessment runs out of the box and writes a **NIST-mapped evidence artifact** —
  no write risk. `apply_changes=false` (default) performs zero writes.
* Enforcement is a **data-driven** operations list (`dt_security_operations`)
  gated behind `apply_changes=true`.

## Quick start
```bash
cd dynatrace/roles/dynatrace_security_hardening/playbooks
cp inventory.example inventory && $EDITOR inventory      # env URL + vaulted API token
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
cat /tmp/dynatrace-artifacts/dynatrace_security_hardening.json
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
```

## Controls assessed (NIST 800-53)
| Control | Check |
|---------|-------|
| AU-2 / AU-12 | Audit log accessible (`/api/v2/auditlogs`) |
| IA-5 | Every API token has an expiration date |
| AC-6 | API tokens avoid broad/admin scopes (least privilege) |
| AC-3 | IP address restrictions configured |
| AC-2 | SSO/IdP federation + RBAC (manual-review pointer) |
| SC-8 | TLS in transit (SaaS default) |

## Token scopes
`auditLogs.read`, `apiTokens.read`, `settings.read` (+ `settings.write` to enforce).

## Tags
`--tags assess` (read-only), `apply`, `report`.

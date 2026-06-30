# Dynatrace IAM (`dynatrace_iam`)

Manages **Dynatrace Account Management (IAM)** — groups, users, policies, and
group→policy bindings — via the Account Management API with OAuth2 client
credentials. Maps to **NIST 800-53 AC-2 / AC-6** (account management, least
privilege).

## Why "grab and go"
* Retrieves an OAuth token and runs read-only **assessment** (group/user counts)
  out of the box. `apply_changes=false` (default) performs zero writes; OAuth
  secret + bearer token are `no_log`.
* Enforcement is a **data-driven** operations list (`dt_iam_operations`) gated
  behind `apply_changes=true`.

## Quick start
```bash
cd dynatrace/roles/dynatrace_iam/playbooks
cp inventory.example inventory && $EDITOR inventory      # account UUID + vaulted OAuth client
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # ASSESS
cat /tmp/dynatrace-artifacts/dynatrace_iam.json
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
```

## OAuth client
Create under **Account Management ▸ Identity & access management ▸ OAuth clients**
with scopes `account-idm-read account-idm-write`. Store the secret in Vault.

## Tags
`--tags assess` (read-only), `apply`, `report`.

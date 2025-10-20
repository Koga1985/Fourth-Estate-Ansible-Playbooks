
# Role: dragos_mssp_orchestrator

**Purpose**: multi-tenant loops to run any `dragos_*` task with per-tenant creds.

## Includes
- `dragos_int__mssp_multi_tenant.yml` (inlined as role task logic)

## Variables
- `tenants`: list of `{ name, base_url, token }`
- `action_task`: path to the task file to include
- `action_vars`: dict of extra vars passed into the included task

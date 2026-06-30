# Dynatrace

Ansible automation for the **Dynatrace** observability platform — agent/gateway
deployment, tenant configuration, and NIST 800-53 security hardening.

## Roles

| Role | Purpose |
|------|---------|
| [`dynatrace_oneagent`](roles/dynatrace_oneagent/) | Deploy/configure the OneAgent on Linux/Windows hosts. |
| [`dynatrace_activegate`](roles/dynatrace_activegate/) | Deploy an ActiveGate (group / network zone). |
| [`dynatrace_tenant_config`](roles/dynatrace_tenant_config/) | Configure the tenant via the Config / Settings 2.0 APIs (management zones, alerting profiles, auto-tags). |
| [`dynatrace_security_hardening`](roles/dynatrace_security_hardening/) | Assess + harden tenant security against NIST 800-53 (AC/AU/IA/SC). |

All roles are **safe by default** (`apply_changes=false` assesses / reports;
nothing is installed or changed until `-e apply_changes=true`). Tokens are
handled with `no_log`. See each role's README for the grab-and-go quick start.

## Tokens
* **PaaS token** (`InstallerDownload`) — OneAgent / ActiveGate installers.
* **API token** (`ReadConfig`/`WriteConfig`, `settings.*`, `auditLogs.read`,
  `apiTokens.read`) — tenant config + security roles. Store all tokens in Vault.

```bash
ansible-galaxy collection install -r dynatrace/requirements.yml
```

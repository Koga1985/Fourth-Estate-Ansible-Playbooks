# illumio_policy_lifecycle

Manages the end-to-end security policy lifecycle in Illumio PCE: applies rule sets and policy exceptions to the draft policy, performs a traffic-simulation brownout check to gate the promotion on an acceptable deny-flow count, then promotes the policy from Draft to Staged and (when not in dry-run mode) from Staged to Active. A rollback include task is also provided for reverting to a previous policy version.

## Requirements

- Ansible 2.12 or later
- Network connectivity from the Ansible controller to the Illumio PCE API (`pce_url`)
- The following variables must be supplied at runtime (not stored in defaults):
  - `pce_url` — base URL of the PCE (e.g. `https://pce.example.mil:8443`)
  - `org_id` — PCE organization ID (integer)
  - `api_user` — PCE API username
  - `api_key` — PCE API key (store in Ansible Vault)
- `simulate_query` must be defined when `brownout_enabled` is `true` (it is the JSON body for the PCE traffic-flow query)

## Role Variables

All variables are defined in `defaults/main.yml`.

| Variable | Default | Description |
|---|---|---|
| `verify_ssl` | `true` | Verify TLS certificates when calling the PCE API. Set to `false` only in lab environments. |
| `artifacts_dir` | `/tmp/illumio-artifacts` | Directory on the Ansible controller where intermediate artifacts are written. |
| `promote_comment` | `"Change via Ansible"` | Change description recorded in the PCE when the policy is promoted. |
| `deny_threshold` | `0` | Maximum number of blocked flows allowed during the impact simulation before the brownout gate fails the play. |
| `dry_run` | `true` | When `true`, the role promotes Draft to Staged but does **not** promote Staged to Active. Set to `false` to complete a full promotion to Active. |
| `brownout_enabled` | `true` | When `true`, runs the traffic-simulation brownout check before promoting. Set to `false` to skip the gate. |

### Runtime-only variables (no defaults)

| Variable | Description |
|---|---|
| `pce_url` | Base URL of the PCE (e.g. `https://pce.example.mil:8443`). |
| `org_id` | PCE organization ID integer. |
| `api_user` | PCE API authentication username. |
| `api_key` | PCE API key. Store in Ansible Vault. |
| `rule_set` | List of rule objects to apply to the draft policy. When defined, the `illumio_rules__apply` include runs. |
| `exceptions` | List of exception objects to apply to the draft policy. When defined and non-empty, the `illumio_rules__exceptions` include runs. |
| `simulate_query` | JSON body for the PCE traffic-flow simulation query. Required when `brownout_enabled: true`. |
| `target_version` | Optional PCE policy version href to roll back to. When omitted, the rollback include uses the most recent previous version. |

## Example Playbook

```yaml
- name: Promote Illumio security policy
  hosts: localhost
  gather_facts: false
  roles:
    - role: illumio_policy_lifecycle
      vars:
        pce_url: "https://pce.dc1.example.mil:8443"
        org_id: 1
        api_user: "{{ vault_illumio_api_user }}"
        api_key: "{{ vault_illumio_api_key }}"
        dry_run: false
        promote_comment: "Deploy Q2 segmentation rules via Ansible"
        deny_threshold: 5
        simulate_query:
          start_date: "2026-03-01T00:00:00Z"
          end_date: "2026-03-17T00:00:00Z"
          sources:
            include: [[]]
          destinations:
            include: [[]]
          services:
            include: []
        rule_set:
          - name: "DATACENTER_SEGMENTATION"
            enabled: true
            rules: []
```

## Notes and Dependencies

- All PCE API calls use `no_log: true` to prevent credentials and policy payloads from appearing in Ansible output or logs.
- The brownout check (`illumio_policy__brownout_check.yml`) queries the PCE traffic-flow API and fails the play with an `assert` if the number of blocked flows exceeds `deny_threshold`. This prevents a policy promotion from causing unexpected connectivity disruptions.
- With `dry_run: true` (the default), the policy is promoted from Draft to Staged but the Staged-to-Active step is skipped. Review the staged policy in the PCE UI before setting `dry_run: false`.
- The rollback task file (`illumio_policy__rollback.yml`) is not invoked automatically by `tasks/main.yml`. Include it explicitly in a separate play when a rollback is required.
- `artifacts_dir` is created on the Ansible controller before each include task runs. Artifacts are primarily used for inter-task state; no report files are written by this role.
- The role makes direct HTTPS calls to the PCE API using `ansible.builtin.uri`. No Illumio Ansible collection is required.

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

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `verify_ssl` | `true` | No | — |
| `artifacts_dir` | `/tmp/illumio-artifacts` | No | — |
| `promote_comment` | `"Change via Ansible"` | No | — |
| `deny_threshold` | `0` | No | — |
| `dry_run` | `true` | No | — |
| `brownout_enabled` | `true` | No | — |

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

## License

MIT

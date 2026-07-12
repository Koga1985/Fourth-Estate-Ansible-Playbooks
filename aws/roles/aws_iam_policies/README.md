# aws_iam_policies

Aws Iam Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `iam_policy_state` | `"present"` | No | IAM Policy Configuration |
| `iam_policy_tags` | `(see defaults/main.yml)` | No | Default tags for all IAM policies |
| `iam_create_fedramp_policies` | `true` | No | FedRAMP compliance policies |
| `iam_enforce_encryption` | `true` | No | — |
| `iam_restrict_regions` | `true` | No | — |
| `iam_allowed_regions` | `(see defaults/main.yml)` | No | Allowed GovCloud regions |
| `iam_policies` | `[]` | No | Example policy list (override in inventory/playbook) |
| `iam_boundary_policies` | `[]` | No | — |
| `iam_service_policies` | `[]` | No | — |
| `iam_fedramp_policies` | `(see defaults/main.yml)` | No | FedRAMP required policies |
| `iam_policy_attachments` | `[]` | No | — |

## Example Playbook

```yaml
---
- name: Aws Iam Policies
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_iam_policies
```

## License

MIT

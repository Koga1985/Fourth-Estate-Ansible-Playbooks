# aws_ec2_key_pairs

Aws Ec2 Key Pairs role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `key_pair_state` | `"present"` | No | Key Pair Configuration |
| `key_pair_save_private_keys` | `true` | No | — |
| `key_pair_output_dir` | `"/tmp/ec2_keys"` | No | — |
| `key_pair_enable_rotation_tracking` | `true` | No | — |
| `key_pair_rotation_days` | `90` | No | — |
| `key_pair_tags` | `(see defaults/main.yml)` | No | Default tags |
| `ec2_key_pairs` | `[]` | No | Key pairs to create (override in inventory/playbook) |

## Example Playbook

```yaml
---
- name: Aws Ec2 Key Pairs
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_ec2_key_pairs
```

## License

MIT

# aws_ec2_key_pairs

Aws Ec2 Key Pairs role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `key_pair_state` | `"present"` |  |
| `key_pair_save_private_keys` | `true` |  |
| `key_pair_output_dir` | `"/tmp/ec2_keys"` |  |
| `key_pair_enable_rotation_tracking` | `true` |  |
| `key_pair_rotation_days` | `90` |  |
| `ec2_key_pairs` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

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

# aws_eks_node_groups

Aws Eks Node Groups role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `node_group_state` | `"present"` |  |
| `node_group_enforce_imdsv2` | `true` |  |
| `node_group_enable_autoscaling` | `true` |  |
| `eks_node_groups` | `[]` |  |
| `kms_key_id` | `""` |  |
| `eks_cluster_name` | `""` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Aws Eks Node Groups
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_eks_node_groups
```

## License

MIT

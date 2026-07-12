# aws_eks_node_groups

Aws Eks Node Groups role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `node_group_state` | `"present"` | No | Node Group Configuration |
| `node_group_enforce_imdsv2` | `true` | No | — |
| `node_group_enable_autoscaling` | `true` | No | — |
| `node_group_tags` | `(see defaults/main.yml)` | No | Default tags |
| `eks_node_groups` | `[]` | No | Node groups to create (override in inventory/playbook) |
| `kms_key_id` | `""` | No | KMS key for EBS encryption |
| `eks_cluster_name` | `""` | No | EKS cluster name (if not specified per node group) |

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

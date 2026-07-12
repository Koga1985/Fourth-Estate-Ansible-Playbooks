# aws_eks_clusters

Aws Eks Clusters role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `eks_cluster_name` | `"ansible-managed-eks"` | No | defaults file for aws_eks_clusters |
| `eks_region` | `"{{ aws_region \| default('us-east-1') }}"` | No | — |
| `eks_version` | `"1.28"` | No | — |
| `eks_role_arn` | `""` | No | — |
| `eks_subnet_ids` | `[]` | No | — |
| `eks_security_group_ids` | `[]` | No | — |
| `eks_endpoint_private_access` | `true` | No | — |
| `eks_endpoint_public_access` | `false` | No | — |
| `eks_encryption_enabled` | `true` | No | — |
| `eks_kms_key_arn` | `""` | No | — |
| `eks_state` | `"present"` | No | — |
| `eks_tags` | `(see defaults/main.yml)` | No | — |

## Example Playbook

```yaml
---
- name: Aws Eks Clusters
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_eks_clusters
```

## License

MIT

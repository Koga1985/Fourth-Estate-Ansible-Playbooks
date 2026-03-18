# aws_eks_clusters

Aws Eks Clusters role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `eks_cluster_name` | `"ansible-managed-eks"` |  |
| `eks_region` | `"{{ aws_region | No | default('us-east-1') }}"` |
| `eks_version` | `"1.28"` |  |
| `eks_role_arn` | `""` |  |
| `eks_subnet_ids` | `[]` |  |
| `eks_security_group_ids` | `[]` |  |
| `eks_endpoint_private_access` | `true` |  |
| `eks_endpoint_public_access` | `false` |  |
| `eks_encryption_enabled` | `true` |  |
| `eks_kms_key_arn` | `""` |  |
| `eks_state` | `"present"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

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

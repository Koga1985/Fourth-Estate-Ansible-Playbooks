# k8s_backup_velero

K8S Backup Velero role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `kubernetes/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `velero_version` | `"v1.12.3"` |  |
| `velero_namespace` | `"velero"` |  |
| `velero_install_method` | `"helm"` | Options: helm, cli |
| `velero_cli_version` | `"1.12.3"` |  |
| `velero_provider` | `"aws"` | Options: aws, azure, gcp, minio, restic |
| `velero_use_restic` | `true` |  |
| `velero_use_volume_snapshots` | `true` |  |
| `velero_aws_region` | `"us-gov-west-1"` |  |
| `velero_aws_bucket` | `"fourth-estate-k8s-backups"` |  |
| `velero_aws_backup_location` | `"default"` |  |
| `velero_aws_credentials_secret` | `"cloud-credentials"` |  |
| `velero_aws_kms_key_id` | `""` |  |
| `velero_aws_s3_url` | `""` | Custom S3 endpoint (for S3-compatible storage) |
| `velero_aws_s3_force_path_style` | `false` |  |
| `velero_azure_storage_account` | `""` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: K8S Backup Velero
  hosts: localhost
  gather_facts: false
  roles:
    - role: kubernetes/roles/k8s_backup_velero
```

## License

MIT

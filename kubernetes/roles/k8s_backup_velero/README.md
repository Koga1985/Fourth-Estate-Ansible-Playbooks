# k8s_backup_velero

K8S Backup Velero role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `kubernetes/README.md`

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `velero_version` | `"v1.12.3"` | No | Velero Installation |
| `velero_namespace` | `"velero"` | No | — |
| `velero_install_method` | `"helm"` | No | Options: helm, cli |
| `velero_cli_version` | `"1.12.3"` | No | — |
| `velero_provider` | `"aws"` | No | Backup Provider Configuration Options: aws, azure, gcp, minio, restic |
| `velero_use_restic` | `true` | No | — |
| `velero_use_volume_snapshots` | `true` | No | — |
| `velero_aws_region` | `"us-gov-west-1"` | No | AWS S3 Configuration |
| `velero_aws_bucket` | `"fourth-estate-k8s-backups"` | No | — |
| `velero_aws_backup_location` | `"default"` | No | — |
| `velero_aws_credentials_secret` | `"cloud-credentials"` | No | — |
| `velero_aws_kms_key_id` | `""` | No | — |
| `velero_aws_s3_url` | `""` | No | Custom S3 endpoint (for S3-compatible storage) |
| `velero_aws_s3_force_path_style` | `false` | No | — |
| `velero_azure_storage_account` | `""` | No | Azure Configuration |
| `velero_azure_storage_key` | `""` | No | — |
| `velero_azure_resource_group` | `""` | No | — |
| `velero_azure_subscription_id` | `""` | No | — |
| `velero_azure_container` | `"velero"` | No | — |
| `velero_gcp_project` | `""` | No | GCP Configuration |
| `velero_gcp_bucket` | `""` | No | — |
| `velero_gcp_service_account_key` | `""` | No | — |
| `velero_minio_enabled` | `false` | No | MinIO Configuration (Air-gapped/On-prem) |
| `velero_minio_endpoint` | `"minio.{{ velero_namespace }}.svc:9000"` | No | — |
| `velero_minio_access_key` | `""` | No | — |
| `velero_minio_secret_key` | `""` | No | — |
| `velero_minio_bucket` | `"velero"` | No | — |
| `velero_minio_use_ssl` | `true` | No | — |
| `velero_default_backup_ttl` | `"720h"` | No | Backup Configuration 30 days |
| `velero_backup_schedule_enabled` | `true` | No | — |
| `velero_backup_schedules` | `(see defaults/main.yml)` | No | — |
| `velero_snapshot_location_name` | `"default"` | No | Snapshot Configuration |
| `velero_volume_snapshot_locations` | `[]` | No | — |
| `velero_restic_prune_interval` | `"168h"` | No | Restic Configuration 7 days |
| `velero_restic_timeout` | `"4h"` | No | — |
| `velero_restic_resource_requests` | `(see defaults/main.yml)` | No | — |
| `velero_restic_resource_limits` | `(see defaults/main.yml)` | No | — |
| `velero_server_resource_requests` | `(see defaults/main.yml)` | No | Velero Server Configuration |
| `velero_server_resource_limits` | `(see defaults/main.yml)` | No | — |
| `velero_plugins` | `(see defaults/main.yml)` | No | Plugin Configuration |
| `velero_enable_prometheus_metrics` | `true` | No | Monitoring and Alerting |
| `velero_metrics_port` | `8085` | No | — |
| `velero_enable_backup_alerts` | `true` | No | — |
| `velero_alert_on_failure` | `true` | No | — |
| `velero_service_account` | `"velero"` | No | Security Configuration |
| `velero_enable_pod_security_policy` | `true` | No | — |
| `velero_pod_security_standard` | `"restricted"` | No | — |
| `velero_enable_network_policy` | `true` | No | — |
| `velero_default_restore_priority` | `(see defaults/main.yml)` | No | Restore Configuration |
| `velero_fourth_estate_enabled` | `true` | No | Fourth Estate Specific |
| `velero_source_protection_backup` | `true` | No | — |
| `velero_journalist_data_backup` | `true` | No | — |
| `velero_publication_backup` | `true` | No | — |
| `velero_air_gapped_mode` | `false` | No | — |
| `velero_encryption_enabled` | `true` | No | — |
| `velero_encryption_key_rotation` | `true` | No | — |
| `velero_helm_repo` | `"https://vmware-tanzu.github.io/helm-charts"` | No | Helm Chart Configuration |
| `velero_helm_chart` | `"velero"` | No | — |
| `velero_helm_values_file` | `"velero-values.yml"` | No | — |
| `velero_enable_backup_verification` | `true` | No | Backup Verification |
| `velero_verification_schedule` | `"0 4 * * 0"` | No | Weekly on Sunday at 4 AM |
| `velero_dr_enabled` | `true` | No | Disaster Recovery |
| `velero_dr_test_schedule` | `"0 3 1 * *"` | No | Monthly on 1st at 3 AM |
| `velero_dr_restore_namespace_suffix` | `"-dr-test"` | No | — |

## Example Playbook

```yaml
---
- name: K8S Backup Velero
  hosts: localhost
  gather_facts: false
  roles:
    - role: kubernetes/roles/k8s_backup_velero
```

## Tags

| Tag | Description |
|-----|-------------|
| `backup` | Tasks tagged `backup` |
| `compliance` | Tasks tagged `compliance` |
| `credentials` | Tasks tagged `credentials` |
| `fourth-estate` | Tasks tagged `fourth-estate` |
| `hardening` | Tasks tagged `hardening` |
| `install` | Tasks tagged `install` |
| `metrics` | Tasks tagged `metrics` |
| `minio` | Tasks tagged `minio` |
| `monitoring` | Tasks tagged `monitoring` |
| `preflight` | Tasks tagged `preflight` |
| `schedules` | Tasks tagged `schedules` |
| `secrets` | Tasks tagged `secrets` |
| `security` | Tasks tagged `security` |
| `storage` | Tasks tagged `storage` |
| `validation` | Tasks tagged `validation` |
| `velero` | Tasks tagged `velero` |
| `verification` | Tasks tagged `verification` |

## License

MIT

# gcp_cmek_everywhere

CMEK rollout & enforcement; SA-only KMS grants; drift validators for BQ/GCS.

## Variables
```yaml
---
artifacts_dir: "/tmp/gcp-artifacts"
apply_changes: false
gcloud_bin: "gcloud"
cmek: []
kms_bindings: []
cmek_enforce: {}

```
## Included tasks
- gcp_kms__cmek_standards.yml
- gcp_kms__grant_bindings.yml
- gcp_storage__cmek_enforce.yml
- gcp_bq__cmek_validator.yml
- gcp_gcs__cmek_validator.yml

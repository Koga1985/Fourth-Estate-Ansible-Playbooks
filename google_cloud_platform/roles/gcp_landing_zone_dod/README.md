# gcp_landing_zone_dod

DoD-aligned landing zone: org policies, approved locations, project factory, API allowlist, aggregated logging.

## Variables
```yaml
---
artifacts_dir: "/tmp/gcp-artifacts"
apply_changes: false
gcloud_bin: "gcloud"
org_id: ""
folder_id: ""
billing_account: ""
labels_common: {}
api_projects: []
api_allowlist: []

```
## Included tasks
- gcp_org_policies__enforce_dod.yml
- gcp_locations__restrict_regions.yml
- gcp_projects__create_and_label.yml
- gcp_apis__allowlist_enable.yml
- gcp_logging__sinks_and_retention.yml

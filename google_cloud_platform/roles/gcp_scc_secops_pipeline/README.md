# gcp_scc_secops_pipeline

Enable SCC Premium, configure findings routing, monitoring baselines, and export audit evidence.

## Variables
```yaml
---
artifacts_dir: "/tmp/gcp-artifacts"
apply_changes: false
gcloud_bin: "gcloud"
enable_premium: true
scc_policies: {}
monitoring: {}
audit: {}

```
## Included tasks
- gcp_scc__enable_sources.yml
- gcp_scc__findings_policies.yml
- gcp_monitoring__baseline.yml
- gcp_audit__export_bundle.yml

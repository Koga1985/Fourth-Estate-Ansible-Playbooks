# gcp_gke_secure_supplychain

Hardened GKE and secure SDLC (Binary AuthZ, Artifact policy, Cloud Build/Deploy gates).

## Variables
```yaml
---
artifacts_dir: "/tmp/gcp-artifacts"
apply_changes: false
gcloud_bin: "gcloud"
gke_baseline: {}
binauthz: {}
artifact_policies: {}
cloudbuild: {}
clouddeploy: {}

```
## Included tasks
- gcp_gke__cluster_baseline.yml
- gcp_gke__binary_authz.yml
- gcp_artifact__policies.yml
- gcp_cloudbuild__policy.yml
- gcp_clouddeploy__gates.yml

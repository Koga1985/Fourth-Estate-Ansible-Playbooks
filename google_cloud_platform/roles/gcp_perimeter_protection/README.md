# gcp_perimeter_protection

Hub/spoke networking, hierarchical firewall policies, VPC-SC perimeters, and Private Google Access.

## Variables
```yaml
---
artifacts_dir: "/tmp/gcp-artifacts"
apply_changes: false
gcloud_bin: "gcloud"
vpc_plan: {}
firewall_policies: []
vpcsc: []
private_access: {}

```
## Included tasks
- gcp_network__vpc_baseline.yml
- gcp_network__firewall_policies.yml
- gcp_vpcsc__perimeters.yml
- gcp_network__private_access.yml

# Cloud Policy & SRG Assessment

Roles for the cloud policy/architecture benchmarks that are *verified* rather
than *configured*.

## Roles

| Role | Benchmark |
|------|-----------|
| [`cloud_computing_srg_assessment`](roles/cloud_computing_srg_assessment/) | DoD Cloud Computing SRG (IL2–IL6) + SaaS shared-responsibility |

`cloud_computing_srg_assessment` maps the CC SRG / FedRAMP / NIST 800-53 control
families to the provider roles under `aws/`, `azure/`, and
`google_cloud_platform/`, aggregates their assessment artifacts, and produces a
consolidated JSON + Markdown evidence package with the DoD-specific and SaaS
shared-responsibility checklists. **Read-only.**

```bash
ansible-playbook cloud_policy/roles/cloud_computing_srg_assessment/playbooks/run.yml
cat /tmp/cloud-srg-artifacts/cloud_computing_srg_assessment.md
```

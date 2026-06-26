# Network Policy & SRG Assessment

Roles for the policy/architecture network benchmarks that are *verified* rather
than *configured*.

## Roles

| Role | Benchmark |
|------|-----------|
| [`ndm_srg_assessment`](roles/ndm_srg_assessment/) | Network Device Management SRG (V5R3) + Network Infrastructure Policy STIG (V10R7) |

`ndm_srg_assessment` aggregates the per-device JSON artifacts produced by the
device STIG roles (`cisco_ios_xe_l2_stig`, `cisco_nxos_stig`, `cisco_asa_stig`,
`cisco_ftd_stig`, `cisco_ise_stig`, `cisco_aci_router_stig`) and rolls them up to
the parent NDM SRG control families, then emits a consolidated JSON + Markdown
compliance-evidence package. It is **read-only** — it never touches a device.

```bash
# Run device roles first (dry-run produces artifacts), then:
ansible-playbook network_policy/roles/ndm_srg_assessment/playbooks/run.yml
cat /tmp/ndm-srg-artifacts/ndm_srg_assessment.md
```

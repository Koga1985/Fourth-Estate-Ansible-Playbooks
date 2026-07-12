# ndm_srg_assessment

Network Device Management SRG (V5R3) and Network Infrastructure Policy STIG (V10R7) assessment and consolidated compliance-evidence generator.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ansible_connection` | `local` | No | — |
| `artifacts_dir` | `"/tmp/ndm-srg-artifacts"` | No | — |
| `ndm_evidence_input_dirs` | `(see defaults/main.yml)` | No | Directories to scan for per-device STIG artifacts (glob of *.json). |
| `ndm_srg_catalog` | `(see defaults/main.yml)` | No | NDM SRG control families (SRG-APP-*-NDM-*) mapped to the device rule IDs implemented by the device roles. status: auto = evidence collected from device artifacts; manual = requires documented procedural verification. |
| `network_infra_policy_catalog` | `(see defaults/main.yml)` | No | Network Infrastructure Policy STIG (NET-*) - architectural controls. These are procedural/architecture verifications (manual evidence). |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | — |
| `stig_benchmark` | `"Network Device Management SRG + Network Infrastructure Policy STIG"` | No | — |
| `stig_version` | `"NDM SRG V5R3 / NET Policy V10R7"` | No | — |

## Example Playbook

```yaml
- name: Use ndm_srg_assessment
  hosts: all
  gather_facts: false
  roles:
    - role: ndm_srg_assessment
```

## Tags

| Tag | Description |
|-----|-------------|
| `assess` | Tasks tagged `assess` |
| `report` | Tasks tagged `report` |

## License

MIT

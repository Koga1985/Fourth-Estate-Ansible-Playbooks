# cybervision_asset_management

Ansible role for Cisco Cyber Vision OT asset discovery configuration, asset group and tag organization, vulnerability tracking, and network baseline management.

## Requirements

- Ansible 2.15+
- Collection: `community.general` (`ansible-galaxy collection install community.general`)
- Collection: `ansible.utils` (`ansible-galaxy collection install ansible.utils`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cv_center_host` | `"{{ vault_cv_center_hostname }}"` | No | Cyber Vision Center API Connection |
| `cv_api_url` | `"https://{{ cv_center_host }}/api/3.0"` | No | — |
| `cv_api_token` | `"{{ vault_cv_api_token }}"` | No | — |
| `cv_validate_certs` | `true` | No | — |
| `cv_use_proxy` | `false` | No | — |
| `cv_timeout` | `60` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `artifacts_dir` | `"/tmp/cv-artifacts"` | No | — |
| `enable_asset_discovery` | `true` | No | Feature Toggles |
| `enable_asset_tagging` | `true` | No | — |
| `enable_vulnerability_tracking` | `true` | No | — |
| `enable_baseline_config` | `true` | No | — |
| `cv_discovery_passive` | `true` | No | Asset Discovery Configuration Always enabled — passive traffic analysis |
| `cv_discovery_active` | `true` | No | Active probing (ARP/ICMP) — confirm with OT team |
| `cv_active_discovery_rate` | `"low"` | No | Options: low, medium, high — use low in OT |
| `cv_discovery_protocols` | `# Protocols to actively probe (if active enabled)` | No | — |
| `cv_criticality_levels` | `(see defaults/main.yml)` | No | Asset Tagging / Classification Criticality levels — assign to assets based on OT risk |
| `cv_asset_groups` | `(see defaults/main.yml)` | No | Pre-defined asset groups for Fourth Estate OT environment |
| `cv_vuln_enabled` | `true` | No | Vulnerability Tracking |
| `cv_vuln_cvss_threshold` | `7.0` | No | Alert on CVSSv3 >= 7.0 (High and Critical) |
| `cv_vuln_auto_acknowledge_low` | `false` | No | Do not auto-acknowledge — require analyst review |
| `cv_vuln_report_format` | `"json"` | No | Options: json, csv |
| `cv_vuln_report_schedule` | `"weekly"` | No | How often to export vulnerability reports |
| `cv_vuln_priority_categories` | `(see defaults/main.yml)` | No | CVE categories to prioritize for OT/ICS environments |
| `cv_baseline_enabled` | `true` | No | Baseline Configuration A baseline captures the current "known good" state of the network. Deviations (new assets, new flows) trigger alerts. |
| `cv_baseline_name` | `"FourthEstate-Baseline"` | No | — |
| `cv_baseline_description` | `"Fourth Estate OT network known-good baseline"` | No | — |
| `cv_baseline_auto_update` | `false` | No | Require manual approval for baseline updates |
| `cv_new_asset_alert` | `true` | No | Alert on any previously unseen device |
| `cv_new_flow_alert` | `false` | No | Too noisy in most OT environments; enable selectively |

## Example Playbook

```yaml
- name: Use cybervision_asset_management
  hosts: all
  gather_facts: false
  roles:
    - role: cybervision_asset_management
      vars:
        apply_changes: false   # set true to apply
```

## Tags

```bash
--tags assets          # All asset management tasks
--tags discovery       # Discovery config and inventory export
--tags tagging         # Asset groups and criticality labels
--tags vulnerabilities # Vulnerability tracking and report
--tags baseline        # Network baseline configuration
```

## Quick Start

```bash
# Dry-run (exports current asset inventory — safe)
ansible-playbook -i inventory site.yml --tags assets --ask-vault-pass

# Apply group/tag configuration
ansible-playbook -i inventory site.yml --tags assets -e "apply_changes=true" --ask-vault-pass

# Export vulnerability report only
ansible-playbook -i inventory site.yml --tags vulnerabilities --ask-vault-pass
```

## Features

| Module | Task File | Description |
|--------|-----------|-------------|
| Asset Discovery | `asset_discovery.yml` | Passive/active discovery settings; exports inventory |
| Asset Tagging | `asset_tagging.yml` | Criticality levels and OT device group creation |
| Vulnerability Tracking | `vulnerability_tracking.yml` | CVE thresholds and vulnerability report export |
| Baseline Config | `baseline_config.yml` | Known-good network baseline; deviation alerts |
| Validation | `validation.yml` | Group count and vulnerability summary |

## Pre-Defined Asset Groups

| Group | Criticality | Tags |
|-------|------------|------|
| Safety-Systems | critical | sis, safety |
| SCADA-Controllers | critical | plc, rtu, scada |
| HMI-Systems | high | hmi, workstation |
| Engineering-Workstations | high | ew, programming |
| Historians | medium | historian, dmz |
| Network-Infrastructure | high | network, infrastructure |

## Important: Active Discovery in OT Environments

Active discovery sends ARP/ICMP probes and **must be coordinated with OT engineers** before enabling. Many OT devices (PLCs, RTUs) can malfunction under unexpected network probes. The default rate is `low` to minimize risk.

```yaml
cv_discovery_active: true            # Confirm with OT team first
cv_active_discovery_rate: "low"      # Always use low in production OT
```

## Key Variables

```yaml
cv_vuln_cvss_threshold: 7.0          # Alert on CVSSv3 >= 7.0
cv_baseline_enabled: true
cv_baseline_auto_update: false       # Require manual approval
cv_new_asset_alert: true             # Alert on any new/unknown device
```

## Required Vault Variables

```yaml
vault_cv_center_hostname: "cybervision.example.com"
vault_cv_api_token: "your-api-bearer-token"
```

## Generated Artifacts

| Artifact | Description |
|----------|-------------|
| `cv_asset_inventory.json` | Full OT device inventory (up to 1000 assets) |
| `cv_asset_tagging.json` | Criticality levels and group names |
| `cv_vulnerability_report.json` | CVE findings by asset |
| `cv_baseline_config.json` | Baseline settings |
| `cv_asset_management_validation.json` | Group count and vuln summary |

## License

MIT

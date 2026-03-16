# cybervision_asset_management

Ansible role for Cisco Cyber Vision OT asset discovery configuration, asset group and tag organization, vulnerability tracking, and network baseline management.

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

## Tags

```bash
--tags assets          # All asset management tasks
--tags discovery       # Discovery config and inventory export
--tags tagging         # Asset groups and criticality labels
--tags vulnerabilities # Vulnerability tracking and report
--tags baseline        # Network baseline configuration
```

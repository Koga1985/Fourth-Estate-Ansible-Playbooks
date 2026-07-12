# Role: dragos_inventory_model

Authoritative asset inventory pipelines (full/delta), tagging, CMDB sync, coverage.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `dragos_base_url` | `"https://tenant.dragos.com"` | No | Dragos Platform Connection |
| `dragos_token` | `"{{ lookup('env','DRAGOS_TOKEN') }}"` | No | — |
| `dragos_verify_ssl` | `true` | No | — |
| `page_size` | `500` | No | — |
| `artifacts_dir` | `"/tmp/dragos-artifacts"` | No | — |
| `dry_run` | `true` | No | — |
| `asset_operation` | `"all"` | No | Asset Operation Mode Options: discover, classify, enrich, zones, criticality, relationships, communications, protocols, all |
| `trigger_discovery_scan` | `false` | No | Asset Discovery |
| `discovery_scan_type` | `"comprehensive"` | No | Options: quick, standard, comprehensive |
| `discovery_network_ranges` | `[]` | No | — |
| `include_passive_discovery` | `true` | No | — |
| `include_active_discovery` | `false` | No | — |
| `deep_asset_inspection` | `true` | No | — |
| `wait_for_discovery` | `true` | No | — |
| `discovery_max_retries` | `120` | No | — |
| `discovery_check_interval` | `30` | No | — |
| `custom_classifications` | `[]` | No | Asset Classification |
| `default_custom_attributes` | `{}` | No | Asset Enrichment |
| `add_business_context` | `true` | No | — |
| `add_compliance_tags` | `true` | No | — |
| `add_lifecycle_info` | `true` | No | — |
| `network_zones` | `(see defaults/main.yml)` | No | Network Zones |
| `apply_zone_policies` | `false` | No | — |
| `zone_assignment_rules` | `(see defaults/main.yml)` | No | — |
| `purdue_level_mapping` | `(see defaults/main.yml)` | No | — |
| `zone_policies` | `{}` | No | — |
| `enable_enhanced_monitoring` | `true` | No | Asset Criticality |
| `relationship_timerange` | `"7d"` | No | Asset Relationships |
| `min_communication_count` | `10` | No | — |
| `communication_timerange` | `"7d"` | No | Asset Communications |
| `protocol_timerange` | `"7d"` | No | Protocol Detection |
| `tags_desired` | `[]` | No | Asset Tagging |
| `cmdb` | `{}` | No | CMDB Integration Example: { url: "https://cmdb.example.com", token: "...", sync_enabled: true } |
| `delta_since_iso` | `""` | No | Delta Export ISO 8601 timestamp |
| `notification_webhook_url` | `""` | No | Notifications |

## Example Playbook

```yaml
- name: Use dragos_inventory_model
  hosts: all
  gather_facts: false
  roles:
    - role: dragos_inventory_model
```

## Tags

| Tag | Description |
|-----|-------------|
| `classification` | Tasks tagged `classification` |
| `cmdb` | Tasks tagged `cmdb` |
| `communications` | Tasks tagged `communications` |
| `criticality` | Tasks tagged `criticality` |
| `delta` | Tasks tagged `delta` |
| `discovery` | Tasks tagged `discovery` |
| `enrichment` | Tasks tagged `enrichment` |
| `export` | Tasks tagged `export` |
| `protocols` | Tasks tagged `protocols` |
| `relationships` | Tasks tagged `relationships` |
| `report` | Tasks tagged `report` |
| `tagging` | Tasks tagged `tagging` |
| `zones` | Tasks tagged `zones` |

## License

MIT

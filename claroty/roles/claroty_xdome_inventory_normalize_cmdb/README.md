# claroty_xdome_inventory_normalize_cmdb

Reads a Claroty xDome asset export (produced by `claroty_xdome_inventory_export`), normalizes site names, assigns zone classifications and criticality ratings using configurable rules, writes a normalized CSV, and optionally tags assets back in xDome or pushes records to a ServiceNow CMDB table.

## Requirements

- Ansible 2.12+
- A JSON asset export produced by `claroty_xdome_inventory_export` must exist at `{{ artifacts_dir }}/{{ source_json }}`
- For CMDB push: ServiceNow instance with CMDB table write access
- For xDome tagging: network access to the Claroty xDome API and a valid bearer token

## Role Variables

### Source File

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/claroty-artifacts"` | No | Directory containing the source JSON file and where normalized output is written. |
| `source_json` | `"xdome_assets.json"` | No | Filename of the JSON asset export to normalize. |

### Normalization Rules

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `normalize.site_map` | `{}` | No | Dictionary mapping raw xDome site names to normalized names (e.g., `{"Plant A - OT": "plant-a"}`). |
| `normalize.zone_rules` | `[]` | No | List of zone assignment rules. Each rule has a `match` object (with `site` and `type` keys) and a `set` object (with a `zone` key). |
| `normalize.criticality.default` | `"medium"` | No | Default criticality assigned when no asset type match is found. |
| `normalize.criticality.by_type` | `{PLC: high, HMI: high, Switch: medium, Printer: low}` | No | Per-device-type criticality overrides. |

### Optional: Tag Back in xDome

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `tag_in_xdome` | `false` | No | When `true`, patches each normalized asset in xDome with `zone` and `criticality` tags and the normalized site name. |
| `claroty.base_url` | — | No | Required when `tag_in_xdome: true`. xDome API base URL. |
| `claroty.token` | — | No | Required when `tag_in_xdome: true`. xDome bearer token. |
| `claroty.verify_ssl` | `true` | No | Whether to verify xDome TLS certificate. |

### Optional: ServiceNow CMDB Push

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cmdb_push` | `true` | No | Enable pushing normalized assets to the CMDB. |
| `cmdb_system` | `"servicenow"` | No | CMDB target system. Currently supports `servicenow`. |
| `servicenow.instance` | `"yourinstance.service-now.com"` | No | ServiceNow instance hostname. |
| `servicenow.token` | `""` | No | ServiceNow bearer token. Falls back to `SNOW_TOKEN` environment variable. |
| `servicenow.table` | `"cmdb_ci_computer"` | No | ServiceNow CMDB table to write to. |
| `servicenow.verify_ssl` | `true` | No | Whether to verify the ServiceNow TLS certificate. |
| `sn_payload_map` | See defaults | No | Dictionary mapping ServiceNow field names to xDome asset field names for the CMDB payload. |

### Default `sn_payload_map`

```yaml
sn_payload_map:
  name: "name"
  ip_address: "ip"
  mac_address: "mac"
  manufacturer: "vendor"
  model_number: "model"
  serial_number: "serial"
  short_description: "summary"
```

Custom Claroty fields (`u_claroty_id`, `u_claroty_zone`, `u_claroty_criticality`) are added automatically.

## Dependencies

- `claroty_xdome_inventory_export` (or any task that produces the source JSON file at `{{ artifacts_dir }}/{{ source_json }}`)

## Example Playbook

```yaml
---
- name: Normalize Claroty inventory and sync to ServiceNow CMDB
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    artifacts_dir: "/opt/claroty/artifacts"
    normalize:
      site_map:
        "Plant A - Production": "plant-a-prod"
        "Data Center 1": "dc1"
      zone_rules:
        - match: { site: "plant-a-prod", type: "PLC" }
          set: { zone: "purdue-l2" }
        - match: { site: "plant-a-prod", type: "HMI" }
          set: { zone: "purdue-l3" }
      criticality:
        default: "medium"
        by_type:
          PLC: "high"
          HMI: "high"
          RTU: "high"
          Switch: "medium"
          Workstation: "medium"
          Printer: "low"
    tag_in_xdome: false
    cmdb_push: true
    servicenow:
      instance: "myorg.service-now.com"
      token: "{{ vault_snow_token }}"
      table: "cmdb_ci_ot_device"
      verify_ssl: true

  roles:
    - role: claroty/roles/claroty_xdome_inventory_normalize_cmdb
```

## Output Artifacts

- `{{ artifacts_dir }}/xdome_assets_normalized.csv` — Normalized asset data with columns: `id`, `name`, `site`, `site_norm`, `zone`, `criticality`, `type`, `ip`, `mac`, `vendor`, `model`, `firmware`, `risk`.

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

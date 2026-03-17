# claroty_xdome_inventory_export

Exports Claroty xDome assets using a paginated API with optional delta filtering. Produces JSON and/or CSV output files in a local artifacts directory and updates a `last_run` marker file to enable automatic incremental (delta) exports on subsequent runs.

## Requirements

- Ansible 2.12+
- Network access to the Claroty xDome API (HTTPS)
- A valid xDome bearer token

## Role Variables

### Connection (required)

| Variable | Description |
|----------|-------------|
| `claroty.base_url` | Base URL of the Claroty xDome instance (e.g. `https://xdome.example.com`). |
| `claroty.token` | Bearer token for xDome API authentication. Store in Ansible Vault. |
| `claroty.verify_ssl` | Whether to verify the xDome TLS certificate. Default: `true`. |

### Export Options

| Variable | Default | Description |
|----------|---------|-------------|
| `inventory_format` | `"json"` | Output format: `json`, `csv`, or `both`. |
| `include_fields` | `[]` | List of asset fields to include in CSV output. When empty, a default set of fields is used (`id`, `name`, `site`, `type`, `ip`, `mac`, `vendor`, `model`, `firmware`, `riskScore`). |
| `page_size` | `500` | Number of assets to request per API page. |
| `max_pages` | `1000` | Maximum number of pages to fetch. Acts as a safety ceiling. |
| `delta_since` | `null` | Controls delta export behavior: `null` performs a full export; an ISO 8601 string filters by update timestamp; `"auto"` reads the `last_run` marker file and uses it automatically. |
| `request_timeout` | `60` | HTTP request timeout in seconds. |
| `extra_headers` | `{}` | Additional HTTP headers to include in API requests. |

### Output Files

| Variable | Default | Description |
|----------|---------|-------------|
| `artifacts_dir` | `"/tmp/claroty-artifacts"` | Directory where output files are written. Created if it does not exist. |
| `json_filename` | `"xdome_assets.json"` | Filename for JSON output. |
| `csv_filename` | `"xdome_assets.csv"` | Filename for CSV output. |
| `marker_filename` | `"last_run.txt"` | Filename for the last-run UTC timestamp marker used by `delta_since: auto`. |

## Dependencies

None.

## Example Playbook

### Full Export (JSON + CSV)

```yaml
---
- name: Export full Claroty xDome asset inventory
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    claroty:
      base_url: "https://xdome.example.com"
      token: "{{ vault_claroty_token }}"
      verify_ssl: true
    inventory_format: both
    artifacts_dir: "/opt/claroty/artifacts"

  roles:
    - role: claroty/roles/claroty_xdome_inventory_export
```

### Automatic Delta Export

```yaml
---
- name: Claroty xDome delta sync
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    claroty:
      base_url: "https://xdome.example.com"
      token: "{{ vault_claroty_token }}"
      verify_ssl: true
    inventory_format: json
    delta_since: auto
    artifacts_dir: "/opt/claroty/artifacts"

  roles:
    - role: claroty/roles/claroty_xdome_inventory_export
```

## Output Artifacts

- `{{ artifacts_dir }}/{{ json_filename }}` — Asset data as a JSON array (when `inventory_format` is `json` or `both`).
- `{{ artifacts_dir }}/{{ csv_filename }}` — Asset data as a CSV file (when `inventory_format` is `csv` or `both`).
- `{{ artifacts_dir }}/{{ marker_filename }}` — UTC ISO 8601 timestamp of the last successful run, used by the `auto` delta mode.

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

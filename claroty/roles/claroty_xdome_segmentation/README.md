# claroty_xdome_segmentation

Queries the Claroty xDome communications API and generates network segmentation artifacts from observed OT/IT traffic flows.

## What it does

1. **Fetches communication flows** — POSTs to `/v1/communications/search` with a configurable time window and result limit; returns observed source/destination zone pairs, tags, IPs, applications, and services.
2. **Writes a flows CSV** — Saves raw flow data to `artifacts_dir/xdome_flows.csv` with columns: `from_zone`, `to_zone`, `src_tag`, `dst_tag`, `app`, `service`, `src_ip`, `dst_ip`, `remark`.
3. **Generates an allowlist rule set** — Derives deduplicated zone-to-zone allowlist rules from observed communications.
4. **Exports an NGFW policy template** — When `export_ngfw: true`, writes a YAML policy template (`ngfw_template_filename`) formatted for Palo Alto Networks (`panos`) with `allow` rules for each observed flow pattern.
5. **Produces a drift report** — When `deployed_policy_file` is provided, slurps the existing deployed policy and writes a drift summary CSV (`drift_report_filename`) comparing the number of generated rules against the deployed policy. To enable a full line-by-line diff, supply an NGFW export parser that converts your firewall's rule export into the same zone/tag/application/service schema as the generated rules.

## Variables (see `defaults/main.yml`)

```yaml
artifacts_dir: "/tmp/claroty-artifacts"

# Communications query filter
flow_filter:
  timeframe: "7d"
  limit: 5000

# NGFW export options
export_ngfw: true
ngfw_target: "panos"
ngfw_template_filename: "allowlist_template.yml"

# Drift report (set to an existing deployed policy file path to enable)
deployed_policy_file: null
drift_report_filename: "allowlist_drift.csv"
```

Required variable (not in defaults):

```yaml
claroty:
  base_url: "https://xdome.example.com"
  token: "{{ vault_claroty_token }}"
  verify_ssl: true
```

## Example play

```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: claroty_xdome_segmentation
      vars:
        claroty:
          base_url: "https://xdome.example.com"
          token: "{{ vault_claroty_token }}"
        flow_filter:
          timeframe: "30d"
          limit: 10000
        export_ngfw: true
        deployed_policy_file: "/path/to/deployed_policy.yml"
```

## Outputs

| File | Description |
|------|-------------|
| `artifacts_dir/xdome_flows.csv` | Raw observed communication flows |
| `artifacts_dir/allowlist_template.yml` | NGFW-ready allowlist rules (when `export_ngfw: true`) |
| `artifacts_dir/allowlist_drift.csv` | Drift summary comparing generated vs. deployed rules (when `deployed_policy_file` is set) |

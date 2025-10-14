# Role: cp_inventory_prune

Safe, gated cleanup of Check Point objects that are no longer present in your source-of-truth (SoT). Produces CSV previews and requires explicit opt-in for destructive actions.

## Requirements
- Connection: `httpapi` to the Management Server
- Collection: `check_point.mgmt`

## Defaults & Guardrails
```yaml
cp_allow_delete: false
dry_run: true
publish_changes: false
artifacts_dir: "/tmp/checkpoint-artifacts"
protected_names: ["Any","Internet","External","LocalNetwork"]

cp_hosts: []
cp_networks: []
cp_address_ranges: []
cp_groups: []
cp_services_tcp: []
cp_services_udp: []
```

## What it does
1. Reads current objects (hosts, networks, ranges, groups, TCP/UDP services).
2. Computes stale items = (current − desired − protected).
3. Writes CSV previews into `artifacts_dir`.
4. Stops if `dry_run: true` (default).
5. When `dry_run: false` **and** `cp_allow_delete: true`, deletes stale items and (optionally) publishes.

## Usage
```yaml
- hosts: checkpoint_mgmt
  gather_facts: false
  roles:
    - role: cp_inventory_prune
      vars:
        artifacts_dir: "/var/tmp/checkpoint-artifacts"
        cp_hosts: "{{ lookup('file', 'vars/hosts.yml') | from_yaml }}"
        cp_networks: "{{ lookup('file', 'vars/networks.yml') | from_yaml }}"
        cp_groups: "{{ lookup('file', 'vars/groups.yml') | from_yaml }}"
        # Gate destructive step:
        dry_run: false
        cp_allow_delete: true
        publish_changes: true
```
## Tags
- `inventory`, `prune`, `cleanup`, `report`

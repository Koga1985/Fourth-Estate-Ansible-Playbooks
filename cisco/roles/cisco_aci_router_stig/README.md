# Cisco ACI Router STIG (`cisco_aci_router_stig`)

Production-ready Ansible role that hardens the **routing plane of a Cisco ACI
fabric** (L3Out BGP/OSPF peerings) to the DISA **Cisco Router STIG**
(`CISC-RT-XXXXXX`) via the APIC REST API using the certified **`cisco.aci`**
collection.

ACI routes through L3Outs rather than a router CLI, so the router-STIG controls
are applied as APIC managed objects (`bgpPeerP`, `ospfIfP`, `l3extOut`). This
role complements `cisco_aci_*` (fabric/tenant/NDM) hardening with the
routing-protocol security controls.

## Requirements

- Ansible 2.15+
- Collection: `cisco.aci` (`ansible-galaxy collection install cisco.aci`)
- Collection: `ansible.utils` (`ansible-galaxy collection install ansible.utils`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `aci_host` | `"{{ vault_aci_apic_hostname }}"` | No | APIC connection (reuse vault keys from aci_security_hardening) |
| `aci_username` | `"{{ vault_aci_apic_username }}"` | No | — |
| `aci_password` | `"{{ vault_aci_apic_password }}"` | No | — |
| `aci_verify_ssl` | `true` | No | — |
| `aci_use_proxy` | `false` | No | — |
| `apply_changes` | `false` | No | Deployment control |
| `artifacts_dir` | `"/tmp/aci-router-stig-artifacts"` | No | — |
| `stig_bgp_security` | `true` | No | Control-area toggles |
| `stig_ospf_security` | `true` | No | — |
| `stig_route_control` | `true` | No | — |
| `stig_compliance_report` | `true` | No | — |
| `aci_bgp_peers` | `[]` | No | CISC-RT-000010 / CISC-RT-000490 - BGP neighbor authentication + GTSM (TTL) Provide the exact APIC DN of each BGP peer connectivity profile (bgpPeerP). Find them with: GET /api/class/bgpPeerP.json |
| `aci_ospf_auth_interfaces` | `[]` | No | CISC-RT-000020 - OSPF interface authentication Provide the DN of each OSPF interface profile (ospfIfP). Find them with: GET /api/class/ospfIfP.json |
| `aci_l3outs_enforce_route_control` | `[]` | No | CISC-RT-000520 - Inbound/outbound route filtering (default-deny intent) Each L3Out should enforce explicit import/export route control. Provide the L3Out DNs to flag/enforce the 'import-security' (enforced RT control) flag. |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Cisco Router STIG applied to ACI L3Out (CISC-RT)"` | No | — |
| `stig_version` | `"V3R2"` | No | — |

## Example Playbook

```yaml
- name: Use cisco_aci_router_stig
  hosts: all
  gather_facts: false
  roles:
    - role: cisco_aci_router_stig
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags bgp`, `ospf`, `route_control`, `report`, plus `stig_cat2` and per-rule
tags (e.g. `--tags CISC-RT-000010`).

## Why "grab and go"

* Certified `cisco.aci` over the APIC REST API.
* **Safe by default**: `apply_changes=false` issues **GET only** and reports;
  `apply_changes=true` issues POST to remediate. `no_log` on all keys.
* Data-driven by DN — you supply the exact peer/interface/L3Out DNs so the role
  is correct for your fabric topology.

## Quick start

```bash
cd cisco/roles/cisco_aci_router_stig/playbooks
ansible-galaxy collection install cisco.aci ansible.utils
cp inventory.example inventory && $EDITOR inventory   # APIC + vault creds

# Discover DNs, then populate vars.example.yml:
#   curl -k https://<apic>/api/class/bgpPeerP.json

ansible-playbook -i inventory run.yml -e @vars.example.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
```

## Controls implemented

| STIG ID | Control | APIC object |
|---------|---------|-------------|
| CISC-RT-000010 | BGP neighbor MD5 authentication | `bgpPeerP.password` |
| CISC-RT-000490 | BGP GTSM / TTL security | `bgpPeerP.ttl` |
| CISC-RT-000020 | OSPF interface authentication | `ospfIfP.authKey/authType` |
| CISC-RT-000520 | Inbound/outbound route filtering | `l3extOut.enforceRtctrl=import,export` |

## ⚠️ Pre-flight before enforcing

* Discover and verify the exact DNs (`bgpPeerP`, `ospfIfP`, `l3extOut`) — the
  vars are placeholders.
* `enforceRtctrl=import,export` makes the L3Out **default-deny** for route
  import/export; ensure your route-control profiles already permit the required
  prefixes or you will drop routes.
* Run the dry-run and review the JSON artifact first.

## License

MIT

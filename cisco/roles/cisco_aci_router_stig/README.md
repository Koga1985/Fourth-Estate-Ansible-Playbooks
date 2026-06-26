# Cisco ACI Router STIG (`cisco_aci_router_stig`)

Production-ready Ansible role that hardens the **routing plane of a Cisco ACI
fabric** (L3Out BGP/OSPF peerings) to the DISA **Cisco Router STIG**
(`CISC-RT-XXXXXX`) via the APIC REST API using the certified **`cisco.aci`**
collection.

ACI routes through L3Outs rather than a router CLI, so the router-STIG controls
are applied as APIC managed objects (`bgpPeerP`, `ospfIfP`, `l3extOut`). This
role complements `cisco_aci_*` (fabric/tenant/NDM) hardening with the
routing-protocol security controls.

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

## Tags

`--tags bgp`, `ospf`, `route_control`, `report`, plus `stig_cat2` and per-rule
tags (e.g. `--tags CISC-RT-000010`).

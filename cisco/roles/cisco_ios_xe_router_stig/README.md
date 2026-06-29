# Cisco IOS XE Router STIG (`cisco_ios_xe_router_stig`)

Hardens a **Cisco IOS XE router** to the DISA **Cisco IOS XE Router STIG**
(`CISC-RT-*`) via the certified **`cisco.ios`** collection. Complements
`cisco_ios_xe_l2_stig` (the Layer-2 switch role) with the routing/control plane.

## Why "grab and go"
* Certified `cisco.ios` over `network_cli`.
* **Safe by default**: `apply_changes=false` runs in check mode (reports the
  diff, no write). `apply_changes=true` enforces and saves startup-config.

## Quick start
```bash
cd cisco/roles/cisco_ios_xe_router_stig/playbooks
ansible-galaxy collection install cisco.ios ansible.netcommon ansible.utils
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml -e @vars.example.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e @vars.example.yml -e apply_changes=true # ENFORCE
cat /tmp/cisco-ios-xe-router-artifacts/rtr-01_ios_xe_router_stig.json
```

## Controls
| STIG ID | Control |
|---------|---------|
| CISC-RT-000130 | Insecure global IP services disabled (source-route, pad, bootp, gratuitous-arp) |
| CISC-RT-000150 | Control Plane Policing (CoPP) service-policy applied |
| CISC-RT-000160 | Interface proxy-arp / redirects / directed-broadcast / unreachables off |
| CISC-RT-000390 | uRPF on internal interfaces |
| CISC-RT-000010 / 000235 / 000490 | BGP neighbor authentication, max-prefix, GTSM/TTL |
| CISC-RT-000020 | OSPF interface MD5 authentication |

## ⚠️ Pre-flight
* Define a CoPP `policy-map`/`class-map` before setting `rtr_copp_policy_name`.
* uRPF and interface filtering can drop asymmetric traffic — validate the
  dry-run diff first.
* Manage routers in tandem with the NDM controls in `cisco_ios_xe_l2_stig`.

## Tags
`--tags control_plane`, `interfaces`, `routing`, `report`, plus `stig_cat2` and
per-rule tags.

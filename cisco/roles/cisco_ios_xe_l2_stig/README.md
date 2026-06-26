# Cisco IOS XE Catalyst — Layer-2 Device STIG (`cisco_ios_xe_l2_stig`)

Production-ready Ansible role that hardens a **Cisco Catalyst / IOS XE switch
operated as a Layer-2 device** to DISA STIG. It implements the
**Cisco IOS XE Switch L2S STIG** (`CISC-L2-XXXXXX`) plus the management-plane
subset of the **Cisco IOS XE Switch NDM STIG** (`CISC-ND-XXXXXX`) that every
managed switch also requires.

> Benchmark target: `Cisco IOS XE Switch L2S STIG` + `NDM STIG`. Confirm the
> exact release in `defaults/main.yml` (`stig_version`) against the
> [DISA STIG library](https://public.cyber.mil/stigs/) for your environment.

## Why "grab and go"

* Uses the **certified `cisco.ios` collection** over `network_cli` — no custom
  modules, no SDK to install beyond the collection.
* **Safe by default.** `apply_changes=false` runs every task in check mode, so
  the first run is a non-destructive findings report. Nothing is written until
  you pass `-e apply_changes=true`.
* Idempotent (`ios_config`), `no_log` on every secret, per-host JSON artifact,
  and a `write memory` handler that only fires on real changes.

## Quick start

```bash
cd cisco/roles/cisco_ios_xe_l2_stig/playbooks

# 1. Install the collection
ansible-galaxy collection install cisco.ios ansible.netcommon ansible.utils

# 2. Set up inventory + credentials (use Ansible Vault)
cp inventory.example inventory
$EDITOR inventory

# 3. DRY-RUN — report findings, change nothing
ansible-playbook -i inventory run.yml

# 4. ENFORCE — apply hardening and save startup-config
ansible-playbook -i inventory run.yml -e apply_changes=true

# 5. Review the per-host compliance artifact
cat /tmp/cisco-ios-xe-l2-artifacts/access-switch-01_ios_xe_l2_stig.json
```

## Controls implemented

| Area | STIG IDs |
|------|----------|
| Spanning-tree integrity | CISC-L2-000010 (Root Guard), 000020 (BPDU Guard), 000030 (Loop Guard), 000220 (Rapid-PVST), 000230 (UDLD) |
| Data-plane integrity | CISC-L2-000050 (DHCP Snooping), 000060 (IP Source Guard), 000070 (Dynamic ARP Inspection) |
| VLAN / trunk hardening | CISC-L2-000090 (DTP off), 000110 (static trunks), 000120 (unused ports parked), 000130 (default VLAN off host ports), 000140 (prune), 000160 (native VLAN ≠ default), 000170 (no host ports on native) |
| Port / storm control | CISC-L2-000020 (port-security), 000080 (storm-control) |
| Management plane (NDM) | CISC-ND-000010, 000090/000100, 000150/000160, 000160 (AAA), 000280, 000470/000490, 001000/001210, 001310, 001440 |

## ⚠️ Pre-flight before enforcing

Layer-2 changes can isolate a switch. Before `apply_changes=true`:

1. **Edit the topology variables** (`l2_user_vlans`, `l2_*_interfaces`,
   `l2_native_vlan`, `l2_management_vlan`) to match the real switch — the
   defaults are placeholders.
2. Keep **out-of-band/console access** during the change window.
3. Confirm your **management VLAN** is not in `l2_unused_interfaces` and that
   the uplink is listed in `l2_dhcp_trusted_interfaces` (otherwise DHCP
   snooping/DAI will drop control traffic).
4. Run the **dry-run first** and review the JSON artifact.

## Key variables

See [`defaults/main.yml`](defaults/main.yml). Most-edited:

| Variable | Default | Purpose |
|----------|---------|---------|
| `apply_changes` | `false` | `true` enforces; `false` is dry-run |
| `l2_user_vlans` | `[10,20,30]` | VLANs that get DHCP snooping / DAI / IPSG |
| `l2_native_vlan` | `999` | Native VLAN for trunks (must not be 1) |
| `l2_unused_vlan` | `998` | Parking VLAN for disabled ports |
| `l2_management_vlan` | `99` | Dedicated management VLAN (must not be 1) |
| `l2_port_security_max_mac` | `2` | Max MACs per access port |
| `ndm_tacacs_servers` | placeholder | AAA / TACACS+ servers |

## Tags

`--tags l2` (all Layer-2), `--tags spanning_tree`, `dhcp_arp`, `vlan`,
`port_security`, `ndm`, `report`, plus per-severity `stig_cat2` / `stig_cat3`
and per-rule tags (e.g. `--tags CISC-L2-000050`).

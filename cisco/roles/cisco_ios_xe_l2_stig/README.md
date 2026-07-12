# Cisco IOS XE Catalyst — Layer-2 Device STIG (`cisco_ios_xe_l2_stig`)

Production-ready Ansible role that hardens a **Cisco Catalyst / IOS XE switch
operated as a Layer-2 device** to DISA STIG. It implements the
**Cisco IOS XE Switch L2S STIG** (`CISC-L2-XXXXXX`) plus the management-plane
subset of the **Cisco IOS XE Switch NDM STIG** (`CISC-ND-XXXXXX`) that every
managed switch also requires.

> Benchmark target: `Cisco IOS XE Switch L2S STIG` + `NDM STIG`. Confirm the
> exact release in `defaults/main.yml` (`stig_version`) against the
> [DISA STIG library](https://public.cyber.mil/stigs/) for your environment.

## Requirements

- Ansible 2.15+
- Collection: `cisco.ios` (`ansible-galaxy collection install cisco.ios`)
- Collection: `ansible.netcommon` (`ansible-galaxy collection install ansible.netcommon`)
- Collection: `ansible.utils` (`ansible-galaxy collection install ansible.utils`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ansible_network_os` | `cisco.ios.ios` | No | Connection (network_cli via cisco.ios) Set these in inventory/group_vars; values shown reference Ansible Vault. |
| `ansible_connection` | `ansible.netcommon.network_cli` | No | — |
| `apply_changes` | `false` | No | Deployment control false = dry-run (check mode), true = enforce |
| `save_config_when_changed` | `true` | No | run `write memory` on change (handler) |
| `artifacts_dir` | `"/tmp/cisco-ios-xe-l2-artifacts"` | No | — |
| `stig_l2_spanning_tree` | `true` | No | STIG control toggles - disable any block that does not apply |
| `stig_l2_dhcp_arp` | `true` | No | — |
| `stig_l2_vlan_hardening` | `true` | No | — |
| `stig_l2_port_security` | `true` | No | — |
| `stig_ndm_management` | `true` | No | — |
| `stig_compliance_report` | `true` | No | — |
| `l2_user_vlans` | `[10, 20, 30]` | No | Layer-2 topology data (customer-provided) VLANs that carry user/host traffic - DHCP snooping, DAI and IP Source Guard are applied to these. Do NOT include the management VLAN here. |
| `l2_access_interfaces` | `(see defaults/main.yml)` | No | Access (host-facing/edge) interfaces - PortFast + BPDU Guard + port security. |
| `l2_trunk_interfaces` | `(see defaults/main.yml)` | No | Trunk (uplink) interfaces - static trunk, DTP off, native VLAN moved. |
| `l2_dhcp_trusted_interfaces` | `(see defaults/main.yml)` | No | Interfaces that face DHCP servers / are upstream - trusted for DHCP snooping. |
| `l2_unused_interfaces` | `(see defaults/main.yml)` | No | Currently unused/disabled interfaces - shut and parked in the unused VLAN. |
| `l2_native_vlan` | `999` | No | CISC-L2-000160/000170 - Native/unused/management VLAN IDs Must NOT be VLAN 1 (the default VLAN). native VLAN for trunks (not VLAN1, no host ports) |
| `l2_unused_vlan` | `998` | No | parking VLAN for disabled ports (no SVI, shut) |
| `l2_management_vlan` | `99` | No | dedicated OOB/management VLAN (not VLAN1) |
| `l2_storm_control_broadcast_level` | `"5.00"` | No | CISC-L2-000080 - Storm control thresholds (percent of bandwidth) |
| `l2_storm_control_multicast_level` | `"5.00"` | No | — |
| `l2_port_security_max_mac` | `2` | No | CISC-L2-000020 - Port security (max MACs on access ports) |
| `l2_port_security_violation` | `restrict` | No | restrict \| shutdown \| protect |
| `ndm_aaa_new_model` | `true` | No | NDM management-plane subset CISC-ND-000010/000160 - AAA / authentication source |
| `ndm_tacacs_servers` | `(see defaults/main.yml)` | No | — |
| `ndm_local_fallback_user` | `"{{ vault_ios_local_user \| default('breakglass') }}"` | No | — |
| `ndm_exec_timeout_minutes` | `10` | No | CISC-ND-000280/000570 - Idle timeout (seconds) and session limits |
| `ndm_vty_access_class` | `"MGMT-ACL"` | No | — |
| `ndm_management_subnets` | `(see defaults/main.yml)` | No | — |
| `ndm_ssh_version` | `2` | No | CISC-ND-001000/001210 - SSH hardening |
| `ndm_ssh_timeout_seconds` | `60` | No | — |
| `ndm_ssh_auth_retries` | `2` | No | — |
| `ndm_disable_telnet` | `true` | No | — |
| `ndm_logging_hosts` | `(see defaults/main.yml)` | No | CISC-ND-000090/000100/000110 - Logging |
| `ndm_logging_buffer_size` | `1000000` | No | — |
| `ndm_logging_trap_level` | `informational` | No | — |
| `ndm_ntp_authenticate` | `true` | No | CISC-ND-000470/000490 - NTP (authenticated) |
| `ndm_ntp_key_id` | `1` | No | — |
| `ndm_ntp_key` | `"{{ vault_ios_ntp_key \| default('CHANGE_ME') }}"` | **Yes** | — |
| `ndm_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `ndm_snmp_v3_group` | `STIG-RO` | No | CISC-ND-000150/000160 - SNMP (v3 only) |
| `ndm_snmp_v3_user` | `"{{ vault_ios_snmp_user \| default('snmpv3mon') }}"` | No | — |
| `ndm_snmp_v3_auth` | `"{{ vault_ios_snmp_auth \| default('CHANGE_ME_AUTH') }}"` | **Yes** | — |
| `ndm_snmp_v3_priv` | `"{{ vault_ios_snmp_priv \| default('CHANGE_ME_PRIV') }}"` | **Yes** | — |
| `ndm_login_banner` | `(multi-line text — see defaults/main.yml)` | No | CISC-ND-000010 (AC-8) - DoD login banner |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance frameworks (reporting metadata) |
| `stig_benchmark` | `"Cisco IOS XE Switch L2S/NDM STIG"` | No | — |
| `stig_version` | `"V3R1"` | No | — |

## Example Playbook

```yaml
- name: Use cisco_ios_xe_l2_stig
  hosts: all
  gather_facts: false
  roles:
    - role: cisco_ios_xe_l2_stig
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags l2` (all Layer-2), `--tags spanning_tree`, `dhcp_arp`, `vlan`,
`port_security`, `ndm`, `report`, plus per-severity `stig_cat2` / `stig_cat3`
and per-rule tags (e.g. `--tags CISC-L2-000050`).

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

## License

MIT

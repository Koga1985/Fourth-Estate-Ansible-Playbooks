# Cisco NX-OS Switch STIG (`cisco_nxos_stig`)

Production-ready Ansible role that hardens a **Cisco Nexus (NX-OS) switch** to
the DISA **Cisco NX-OS Switch STIG**. It covers the management-plane (NDM,
`CISC-ND-XXXXXX`) and Layer-2 (`CISC-L2-XXXXXX`) control families using the
certified **`cisco.nxos`** collection over `network_cli`.

> Confirm the benchmark release in `defaults/main.yml` (`stig_version`) against
> the [DISA STIG library](https://public.cyber.mil/stigs/).

## Requirements

- Ansible 2.15+
- Collection: `cisco.nxos` (`ansible-galaxy collection install cisco.nxos`)
- Collection: `ansible.netcommon` (`ansible-galaxy collection install ansible.netcommon`)
- Collection: `ansible.utils` (`ansible-galaxy collection install ansible.utils`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ansible_network_os` | `cisco.nxos.nxos` | No | Connection (network_cli via cisco.nxos) |
| `ansible_connection` | `ansible.netcommon.network_cli` | No | — |
| `apply_changes` | `false` | No | Deployment control |
| `save_config_when_changed` | `true` | No | — |
| `artifacts_dir` | `"/tmp/cisco-nxos-artifacts"` | No | — |
| `stig_ndm_features` | `true` | No | Control toggles |
| `stig_ndm_aaa` | `true` | No | — |
| `stig_ndm_logging_ntp` | `true` | No | — |
| `stig_ndm_snmp` | `true` | No | — |
| `stig_l2_hardening` | `true` | No | — |
| `stig_compliance_report` | `true` | No | — |
| `nxos_disable_telnet` | `true` | No | CISC-ND-001310/001440 - Feature hygiene (disable insecure, enable required) |
| `nxos_enable_ssh` | `true` | No | — |
| `nxos_enable_scp` | `true` | No | — |
| `nxos_tacacs_servers` | `(see defaults/main.yml)` | No | CISC-ND-000160/000140 - AAA / TACACS+ |
| `nxos_tacacs_group` | `STIG-TACACS` | No | — |
| `nxos_local_fallback_user` | `"{{ vault_nxos_local_user \| default('breakglass') }}"` | No | — |
| `nxos_exec_timeout_minutes` | `10` | No | CISC-ND-000280 - Idle timeout (minutes) for VTY/console |
| `nxos_mgmt_acl_name` | `MGMT-IN` | No | CISC-ND-000490 - Management ACL |
| `nxos_management_subnets` | `(see defaults/main.yml)` | No | — |
| `nxos_ssh_key_type` | `rsa` | No | CISC-ND-001000/001210 - SSH key strength |
| `nxos_ssh_key_size` | `2048` | No | — |
| `nxos_logging_servers` | `(see defaults/main.yml)` | No | CISC-ND-000090/000100/000110 - Logging |
| `nxos_logging_level_console` | `2` | No | — |
| `nxos_ntp_authenticate` | `true` | No | CISC-ND-000470/000490 - NTP (authenticated) |
| `nxos_ntp_key_id` | `1` | No | — |
| `nxos_ntp_key` | `"{{ vault_nxos_ntp_key \| default('CHANGE_ME') }}"` | **Yes** | — |
| `nxos_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `nxos_snmp_v3_user` | `"{{ vault_nxos_snmp_user \| default('snmpv3mon') }}"` | No | CISC-ND-000150/000160 - SNMPv3 only |
| `nxos_snmp_v3_auth` | `"{{ vault_nxos_snmp_auth \| default('CHANGE_ME_AUTH') }}"` | **Yes** | — |
| `nxos_snmp_v3_priv` | `"{{ vault_nxos_snmp_priv \| default('CHANGE_ME_PRIV') }}"` | **Yes** | — |
| `nxos_snmp_v3_role` | `network-operator` | No | — |
| `nxos_snmp_remove_communities` | `(see defaults/main.yml)` | No | — |
| `nxos_login_banner` | `(multi-line text — see defaults/main.yml)` | No | CISC-ND-000010 (AC-8) - DoD banner |
| `nxos_user_vlans` | `[10, 20, 30]` | No | CISC-L2-XXXXXX - Layer-2 hardening |
| `nxos_native_vlan` | `999` | No | — |
| `nxos_enable_dhcp_snooping` | `true` | No | — |
| `nxos_enable_arp_inspection` | `true` | No | — |
| `nxos_enable_bpduguard_default` | `true` | No | — |
| `nxos_enable_loopguard_default` | `true` | No | — |
| `nxos_copp_profile` | `strict` | No | CISC-ND-001220 - Control Plane Policing strict \| moderate \| lenient \| dense |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Cisco NX-OS Switch STIG"` | No | — |
| `stig_version` | `"V3R2"` | No | — |

## Example Playbook

```yaml
- name: Use cisco_nxos_stig
  hosts: all
  gather_facts: false
  roles:
    - role: cisco_nxos_stig
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags ndm`, `aaa`, `features`, `logging`, `ntp`, `snmp`, `l2`, `report`, plus
`stig_cat2` / `stig_cat3` and per-rule tags (e.g. `--tags CISC-ND-000470`).

## Why "grab and go"

* Certified `cisco.nxos` modules — no SDK beyond the collection.
* **Safe by default**: `apply_changes=false` runs in check mode and emits a
  per-host JSON findings report; nothing is written until `-e apply_changes=true`.
* Idempotent, `no_log` on secrets, `copy run start` handler on change only.

## Quick start

```bash
cd cisco/roles/cisco_nxos_stig/playbooks
ansible-galaxy collection install cisco.nxos ansible.netcommon ansible.utils
cp inventory.example inventory && $EDITOR inventory

# DRY-RUN (report only)
ansible-playbook -i inventory run.yml
# ENFORCE
ansible-playbook -i inventory run.yml -e apply_changes=true

cat /tmp/cisco-nxos-artifacts/nexus-01_nxos_stig.json
```

## Controls implemented

| Area | STIG IDs |
|------|----------|
| Feature hygiene | CISC-ND-001000 (SSH/SCP), 001310 (Telnet off), 001440 (unused services) |
| AAA / access | CISC-ND-000160 (TACACS+), 000280 (idle timeout), 000380 (password strength), 000490 (mgmt ACL), 000550 (accounting) |
| Banner | CISC-ND-000010 |
| Logging / time | CISC-ND-000090/000100/000110 (syslog), 000470 (authenticated NTP) |
| SNMP | CISC-ND-000150/000160 (SNMPv3 only, communities removed) |
| SSH | CISC-ND-001000/001210 (key strength) |
| Control plane | CISC-ND-001220 (CoPP) |
| Layer-2 | CISC-L2-000020 (BPDU Guard), 000030 (Loop Guard), 000050 (DHCP snooping), 000070 (DAI) |

## ⚠️ Pre-flight before enforcing

* Confirm `nxos_user_vlans`, `nxos_management_subnets`, and TACACS keys match
  your environment — defaults are placeholders.
* Keep console/out-of-band access during the window; `feature` and ACL changes
  affect the control plane.
* `feature dhcp` is required for DHCP snooping/DAI and is enabled by the role.

## License

MIT

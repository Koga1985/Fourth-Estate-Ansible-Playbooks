# Cisco ASA STIG (`cisco_asa_stig`)

Production-ready Ansible role that hardens a **Cisco ASA** appliance to the DISA
**Cisco ASA NDM STIG** (`CASA-ND-XXXXXX`) and **Cisco ASA Firewall STIG**
(`CASA-FW-XXXXXX`) using the certified **`cisco.asa`** collection over
`network_cli`.

> Confirm the benchmark release in `defaults/main.yml` (`stig_version`) against
> the [DISA STIG library](https://public.cyber.mil/stigs/). The ASA VPN STIG
> (`CASA-VN-*`) is environment-specific and is intentionally left to a separate
> per-tunnel configuration role.

## Requirements

- Ansible 2.15+
- Collection: `cisco.asa` (`ansible-galaxy collection install cisco.asa`)
- Collection: `ansible.netcommon` (`ansible-galaxy collection install ansible.netcommon`)
- Collection: `ansible.utils` (`ansible-galaxy collection install ansible.utils`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ansible_network_os` | `cisco.asa.asa` | No | Connection (network_cli via cisco.asa) |
| `ansible_connection` | `ansible.netcommon.network_cli` | No | — |
| `apply_changes` | `false` | No | Deployment control |
| `save_config_when_changed` | `true` | No | — |
| `artifacts_dir` | `"/tmp/cisco-asa-artifacts"` | No | — |
| `stig_ndm_auth` | `true` | No | Control toggles |
| `stig_ndm_mgmt_access` | `true` | No | — |
| `stig_ndm_logging_ntp` | `true` | No | — |
| `stig_ndm_snmp` | `true` | No | — |
| `stig_fw_policy` | `true` | No | — |
| `stig_compliance_report` | `true` | No | — |
| `asa_mgmt_interface` | `management` | No | Management interface (ASA SSH/logging/SNMP bind) |
| `asa_aaa_server_group` | `STIG-TACACS` | No | CASA-ND-000190 - AAA / TACACS+ |
| `asa_aaa_protocol` | `tacacs+` | No | — |
| `asa_tacacs_servers` | `(see defaults/main.yml)` | No | — |
| `asa_local_fallback_user` | `"{{ vault_asa_local_user \| default('breakglass') }}"` | No | — |
| `asa_console_timeout_minutes` | `10` | No | CASA-ND-000160 - Idle timeout (minutes) and session limits |
| `asa_ssh_timeout_minutes` | `10` | No | — |
| `asa_max_concurrent_mgmt_sessions` | `2` | No | — |
| `asa_ssh_version` | `2` | No | CASA-ND-001130/001150 - SSH hardening / management ACL |
| `asa_ssh_key_modulus` | `2048` | No | — |
| `asa_ssh_kex_group` | `dh-group14-sha256` | No | — |
| `asa_management_subnets` | `(see defaults/main.yml)` | No | — |
| `asa_password_min_length` | `15` | No | CASA-ND-001440 - Password policy |
| `asa_password_lifetime_days` | `60` | No | — |
| `asa_password_min_changes` | `4` | No | — |
| `asa_logging_hosts` | `(see defaults/main.yml)` | No | CASA-ND-000610/000620 - Logging |
| `asa_logging_trap_level` | `informational` | No | — |
| `asa_logging_buffer_level` | `informational` | No | — |
| `asa_logging_buffer_size` | `1048576` | No | — |
| `asa_ntp_authenticate` | `true` | No | CASA-ND-001200 - NTP (authenticated) |
| `asa_ntp_key_id` | `1` | No | — |
| `asa_ntp_key` | `"{{ vault_asa_ntp_key \| default('CHANGE_ME') }}"` | **Yes** | — |
| `asa_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `asa_snmp_v3_group` | `STIG-RO` | No | CASA-ND-001210 - SNMPv3 only |
| `asa_snmp_v3_user` | `"{{ vault_asa_snmp_user \| default('snmpv3mon') }}"` | No | — |
| `asa_snmp_v3_auth` | `"{{ vault_asa_snmp_auth \| default('CHANGE_ME_AUTH') }}"` | **Yes** | — |
| `asa_snmp_v3_priv` | `"{{ vault_asa_snmp_priv \| default('CHANGE_ME_PRIV') }}"` | **Yes** | — |
| `asa_snmp_host` | `"{{ vault_asa_snmp_host \| default('10.0.0.20') }}"` | No | — |
| `asa_snmp_remove_communities` | `(see defaults/main.yml)` | No | — |
| `asa_enable_threat_detection` | `true` | No | CASA-FW-XXXXXX - Firewall policy |
| `asa_enable_acl_logging` | `true` | No | — |
| `asa_logged_acls` | `[]` | No | Explicit deny-any-any with logging appended to user ACLs (named below). |
| `asa_login_banner_lines` | `(see defaults/main.yml)` | No | CASA-ND-000100 (AC-8) - DoD banner (list of lines) |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Cisco ASA NDM + Firewall STIG"` | No | — |
| `stig_version` | `"V2R1"` | No | — |

## Example Playbook

```yaml
- name: Use cisco_asa_stig
  hosts: all
  gather_facts: false
  roles:
    - role: cisco_asa_stig
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags ndm`, `auth`, `ssh`, `logging`, `ntp`, `snmp`, `firewall`, `report`,
plus `stig_cat2` / `stig_cat3` and per-rule tags (e.g. `--tags CASA-ND-001210`).

## Why "grab and go"

* Certified `cisco.asa` modules over SSH — no SDK to install.
* **Safe by default**: `apply_changes=false` runs in check mode and emits a
  per-host JSON findings report. Nothing is written until `-e apply_changes=true`.
* Idempotent, `no_log` on secrets, `write memory` handler on change only.

## Quick start

```bash
cd cisco/roles/cisco_asa_stig/playbooks
ansible-galaxy collection install cisco.asa ansible.netcommon ansible.utils
cp inventory.example inventory && $EDITOR inventory

ansible-playbook -i inventory run.yml                       # DRY-RUN
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE

cat /tmp/cisco-asa-artifacts/asa-01_asa_stig.json
```

## Controls implemented

| Area | STIG IDs |
|------|----------|
| AAA / fallback | CASA-ND-000190, 000550 |
| Banner | CASA-ND-000100 |
| Password policy | CASA-ND-001440 |
| Idle timeout / sessions | CASA-ND-000160, 000140 |
| SSH / keys | CASA-ND-001130, 001150 |
| Management ACL | CASA-ND-001550 |
| HTTP server | CASA-ND-001310 |
| Logging | CASA-ND-000610, 000620 |
| NTP | CASA-ND-001200 |
| SNMPv3 only | CASA-ND-001210 |
| Firewall | CASA-FW-000010 (threat detection), 000070 (ACL deny logging) |

## ⚠️ Pre-flight before enforcing

* `crypto key generate rsa` regenerates the SSH host key — existing SSH sessions
  must re-trust the host. Only runs when `apply_changes=true`.
* `no http server enable` disables ASDM/HTTP. Re-enable on a restricted
  interface if you manage via ASDM.
* The `asa_logged_acls` deny-any-any is **appended**; confirm those ACLs already
  contain the required permits before enforcing so you don't black-hole traffic.
* Keep console access during the change window.

## License

MIT

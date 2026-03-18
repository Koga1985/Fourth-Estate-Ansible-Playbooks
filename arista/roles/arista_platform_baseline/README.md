# arista_platform_baseline

Applies a DISA STIG-compliant system baseline to Arista EOS devices. The role configures hostname, domain name, management VRF and interface, login/MOTD banners, NTP, DNS, syslog, SNMP (v2c and v3), TACACS+, RADIUS, AAA authentication/authorization/accounting, local users, SSH hardening, eAPI (HTTPS only), session timeouts, logging, password policy, control-plane policing, and disables insecure services (Telnet, HTTP, finger, bootp). Every task is annotated with its corresponding DISA STIG control identifier.

## Requirements

- Ansible 2.12 or later
- `arista.eos` collection (`ansible-galaxy collection install arista.eos`)
- Network connectivity to Arista EOS devices
- EOS user with `network-admin` privilege (the role modifies global system configuration)
- `ansible_network_os: eos` and `ansible_connection: network_cli` (or `httpapi`) set for target hosts

## Role Variables

All variables are nested under the `arista_baseline` dictionary in `defaults/main.yml`. Override individual keys at the `group_vars` or `host_vars` level.

| Variable | Default | Required | Description |
|---|---|---|
| `arista_apply_changes` | `false` | No | Safety gate. Set to `true` to push configuration; otherwise only a plan artifact is written. |
| `arista_artifacts_dir` | `/tmp/arista-artifacts` | No | Directory on the Ansible controller for plan and running-config artifacts. |
| `arista_baseline.hostname` | `{{ inventory_hostname }}` | No | Device hostname. |
| `arista_baseline.domain_name` | `{{ arista_domain_name \| default('mil') }}` | IP domain name. |
| `arista_baseline.mgmt_vrf.name` | `MGMT` | No | Name of the dedicated management VRF. |
| `arista_baseline.mgmt_interface.name` | `Management1` | No | Management interface to configure. |
| `arista_baseline.mgmt_interface.ipv4_address` | `{{ ansible_host }}/24` | No | IPv4 address assigned to the management interface. |
| `arista_baseline.banners.login` | DoD UNCLASSIFIED//FOUO warning | No | Login banner text (STIG V-220520). |
| `arista_baseline.banners.motd` | Warning banner | No | Message-of-the-day banner text (STIG V-220521). |
| `arista_baseline.ntp_servers` | `10.0.0.10` (prefer), `10.0.0.11` | No | List of NTP server entries with VRF and optional `prefer` flag (STIG V-220522). Override with `arista_ntp_server_1` / `arista_ntp_server_2`. |
| `arista_baseline.ntp_auth_enabled` | `true` | No | Enables NTP authentication. |
| `arista_baseline.dns_servers` | `10.0.0.20`, `10.0.0.21` | No | DNS name-server addresses (STIG V-220523). Override with `arista_dns_server_1` / `arista_dns_server_2`. |
| `arista_baseline.syslog_servers` | `10.0.0.30:6514/tcp`, `10.0.0.31:6514/tcp` | No | Syslog destinations (STIG V-220524/V-220525). Override with `arista_syslog_server_1` / `arista_syslog_server_2`. |
| `arista_baseline.snmp_communities` | `public` (ro), `private` (rw) | No | SNMPv2c community strings with ACL bindings (STIG V-220526). Use Vault for these values. |
| `arista_baseline.snmpv3_users` | `snmpv3admin` (sha512/aes256) | No | SNMPv3 user definitions (STIG V-220529). Use Vault for auth/priv passwords. |
| `arista_baseline.tacacs_servers` | `10.0.0.40`, `10.0.0.41` | No | TACACS+ server list with encrypted keys (STIG V-220530/V-220531). Override with `arista_tacacs_server_1/2` and `arista_tacacs_key`. |
| `arista_baseline.radius_servers` | `10.0.0.50`, `10.0.0.51` | No | RADIUS server list (STIG V-220532/V-220533). Override with `arista_radius_server_1/2` and `arista_radius_key`. |
| `arista_baseline.aaa.auth_method` | `tacacs+` | No | Primary AAA authentication/authorization method (STIG V-220534). |
| `arista_baseline.local_users` | `admin` (priv 15), `netops` (network-operator) | No | Local fallback user accounts (STIG V-220535). Passwords via `arista_admin_password` / `arista_netops_password`. |
| `arista_baseline.ssh_timeout` | `60` | No | SSH idle timeout in seconds (STIG V-220538). |
| `arista_baseline.ssh_retries` | `3` | No | Maximum SSH authentication retries. |
| `arista_baseline.eapi.enabled` | `true` | No | Enables eAPI over HTTPS only (STIG V-220539). |
| `arista_baseline.exec_timeout` | `10` | No | VTY session idle timeout in minutes (STIG V-220540). |
| `arista_baseline.logging_buffer_size` | `32768` | No | Logging buffer size in bytes (STIG V-220541). |
| `arista_baseline.logging_level` | `informational` | No | Minimum logging severity (STIG V-220542). |
| `arista_baseline.password_min_length` | `15` | No | Minimum password length (STIG V-220543). |
| `arista_baseline.password_encryption` | `sha512` | No | Password hashing algorithm. |
| `arista_baseline.control_plane_acl` | `CONTROL_PLANE_ACL` | No | ACL name applied to the control-plane for CoPP (STIG V-220545). |
| `arista_baseline.timezone` | `UTC` | No | Device clock timezone (STIG V-220546). |

## Example Playbook

```yaml
- name: Apply STIG-compliant platform baseline
  hosts: arista_switches
  gather_facts: false
  roles:
    - role: arista_platform_baseline
      vars:
        arista_apply_changes: true
        arista_domain_name: "dc1.example.mil"
        arista_mgmt_gateway: "10.10.10.1"
        arista_ntp_server_1: "10.10.0.10"
        arista_ntp_server_2: "10.10.0.11"
        arista_dns_server_1: "10.10.0.20"
        arista_syslog_server_1: "10.10.0.30"
        arista_tacacs_server_1: "10.10.0.40"
        arista_tacacs_key: "{{ vault_tacacs_key }}"
        arista_admin_password: "{{ vault_admin_password }}"
```

## Notes and Dependencies

- `arista_apply_changes` defaults to `false`. A JSON baseline plan (`<hostname>_baseline_plan.json`) is always written to `arista_artifacts_dir`. The running configuration is captured to `<hostname>_running_config.txt` when changes are applied.
- All STIG control identifiers referenced in this role are for Arista EOS (V-220518 through V-220546). Consult your agency's STIG viewer to confirm applicability and CAT levels.
- Sensitive values (SNMP community strings, TACACS+/RADIUS keys, SNMPv3 passwords, user passwords) are handled with `no_log: true` in all relevant tasks. Store them in Ansible Vault.
- The `arista_baseline.ntp_auth_keys` list defaults to a placeholder key (`CHANGEME`). Replace with a real key via `arista_ntp_key` or directly in Vault.
- The handler `save eos configuration` is notified by all configuration tasks and writes the running configuration to startup at play completion.
- This role applies system-level settings only. ACL/QoS hardening is handled by `arista_acl_qos_security`; routing is handled by `arista_routing_baseline`; fabric/VXLAN is handled by `arista_interfaces_fabric`.

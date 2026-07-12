# arista_platform_baseline

Applies a DISA STIG-compliant system baseline to Arista EOS devices. The role configures hostname, domain name, management VRF and interface, login/MOTD banners, NTP, DNS, syslog, SNMP (v2c and v3), TACACS+, RADIUS, AAA authentication/authorization/accounting, local users, SSH hardening, eAPI (HTTPS only), session timeouts, logging, password policy, control-plane policing, and disables insecure services (Telnet, HTTP, finger, bootp). Every task is annotated with its corresponding DISA STIG control identifier.

## Requirements

- Ansible 2.12 or later
- `arista.eos` collection (`ansible-galaxy collection install arista.eos`)
- Network connectivity to Arista EOS devices
- EOS user with `network-admin` privilege (the role modifies global system configuration)
- `ansible_network_os: eos` and `ansible_connection: network_cli` (or `httpapi`) set for target hosts

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `arista_apply_changes` | `false` | No | Control whether changes are applied or just planned |
| `arista_artifacts_dir` | `"/tmp/arista-artifacts"` | No | Artifacts directory for storing configuration plans and backups |
| `arista_baseline` | `(see defaults/main.yml)` | No | Baseline configuration structure |
| `arista_security` | `(see defaults/main.yml)` | No | Additional security settings |
| `arista_qos` | `(see defaults/main.yml)` | No | Quality of Service |
| `arista_storm_control` | `(see defaults/main.yml)` | No | Storm control |

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

## License

MIT

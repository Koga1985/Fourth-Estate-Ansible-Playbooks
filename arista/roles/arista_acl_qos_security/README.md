# arista_acl_qos_security

Configures IPv4 ACLs, Quality of Service (QoS) class and policy maps, and a full suite of layer-2 security controls on Arista EOS devices. The role is built to satisfy DISA STIG requirements and covers DHCP snooping, Dynamic ARP Inspection, 802.1X port authentication, IP source guard, port security, storm control, BPDU/root guard, and unused-port hardening.

## Requirements

- Ansible 2.12 or later
- `arista.eos` collection (`ansible-galaxy collection install arista.eos`)
- Network connectivity to Arista EOS devices
- EOS user with `network-admin` privilege or equivalent
- `ansible_network_os: eos` and `ansible_connection: network_cli` (or `httpapi`) set for target hosts

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `arista_apply_changes` | `false` | No | — |
| `arista_artifacts_dir` | `"/tmp/arista-artifacts"` | No | — |
| `ipv4_acls` | `(see defaults/main.yml)` | No | IPv4 ACLs |
| `acl_interfaces` | `(see defaults/main.yml)` | No | ACL to interface mappings |
| `qos_class_maps` | `(see defaults/main.yml)` | No | QoS Class Maps |
| `qos_policy_maps` | `(see defaults/main.yml)` | No | QoS Policy Maps |
| `qos_interfaces` | `[]` | No | QoS interface applications |
| `storm_control_interfaces` | `[]` | No | Storm Control |
| `port_security_interfaces` | `[]` | No | Port Security |
| `dhcp_snooping` | `(see defaults/main.yml)` | No | DHCP Snooping |
| `arp_inspection` | `(see defaults/main.yml)` | No | Dynamic ARP Inspection |
| `ip_source_guard_interfaces` | `[]` | No | IP Source Guard |
| `dot1x_config` | `(see defaults/main.yml)` | No | 802.1X Configuration |
| `dot1x_interfaces` | `[]` | No | — |
| `static_mac_addresses` | `[]` | No | Static MAC Addresses |
| `unused_ports` | `[]` | No | Unused Ports (DISA STIG Requirement) |
| `blackhole_vlan` | `999` | No | — |
| `bpdu_guard_interfaces` | `[]` | No | BPDU Guard Interfaces (Edge Ports) |
| `root_guard_interfaces` | `[]` | No | Root Guard Interfaces (Uplinks) |
| `rate_limiting` | `(see defaults/main.yml)` | No | Rate Limiting |
| `security_config` | `(see defaults/main.yml)` | No | Security configuration composite |

## Example Playbook

```yaml
- name: Apply ACL, QoS, and security hardening
  hosts: arista_switches
  gather_facts: false
  roles:
    - role: arista_acl_qos_security
      vars:
        arista_apply_changes: true
        unused_ports:
          - "Ethernet5"
          - "Ethernet6"
        bpdu_guard_interfaces:
          - "Ethernet1"
          - "Ethernet2"
        dhcp_snooping:
          enabled: true
          vlans: [10, 20, 30]
          trusted_interfaces:
            - "Ethernet49"
            - "Ethernet50"
        arp_inspection:
          enabled: true
          vlans: [10, 20, 30]
          trusted_interfaces:
            - "Ethernet49"
            - "Ethernet50"
```

## Notes and Dependencies

- `arista_apply_changes` defaults to `false`. No configuration is pushed unless this is explicitly set to `true`, making dry-run the safe default.
- A JSON plan artifact (`<hostname>_security_plan.json`) is always written to `arista_artifacts_dir` regardless of `arista_apply_changes`. A post-run state capture (`<hostname>_security_state.json`) is written only when changes are applied.
- The handler `save eos configuration` is notified by every configuration task. It writes the running configuration to startup after all tasks in the play complete.
- DISA STIG controls addressed include unused-port shutdown, storm control, BPDU guard, and control-plane rate limiting.
- Sensitive variables (community strings, keys) should be stored in Ansible Vault.

## License

MIT

# arista_acl_qos_security

Configures IPv4 ACLs, Quality of Service (QoS) class and policy maps, and a full suite of layer-2 security controls on Arista EOS devices. The role is built to satisfy DISA STIG requirements and covers DHCP snooping, Dynamic ARP Inspection, 802.1X port authentication, IP source guard, port security, storm control, BPDU/root guard, and unused-port hardening.

## Requirements

- Ansible 2.12 or later
- `arista.eos` collection (`ansible-galaxy collection install arista.eos`)
- Network connectivity to Arista EOS devices
- EOS user with `network-admin` privilege or equivalent
- `ansible_network_os: eos` and `ansible_connection: network_cli` (or `httpapi`) set for target hosts

## Role Variables

All variables are defined in `defaults/main.yml`. The most commonly overridden variables are listed below.

| Variable | Default | Required | Description |
|---|---|---|
| `arista_apply_changes` | `false` | No | Safety gate. Set to `true` to push configuration; otherwise the role only writes a plan artifact. |
| `arista_artifacts_dir` | `/tmp/arista-artifacts` | No | Directory on the Ansible controller where plan and state JSON files are written. |
| `ipv4_acls` | See defaults | No | List of IPv4 ACL definitions in `arista.eos.eos_acls` format. Includes a default `MGMT_ACCESS` ACL permitting SSH/HTTPS from `10.0.0.0/8` and denying all else. |
| `acl_interfaces` | `[Management1/ipv4/MGMT_ACCESS/in]` | No | List of interface-to-ACL bindings (`name`, `afi`, `acl`, `direction`). |
| `qos_class_maps` | VOICE, VIDEO, CRITICAL_DATA | No | List of QoS class-map definitions with DSCP/CoS match criteria. |
| `qos_policy_maps` | `QOS_POLICY` | No | List of QoS policy-map definitions referencing the class maps above. |
| `qos_interfaces` | `[]` | No | Interfaces to which QoS service-policies are applied (`name`, `direction`, `policy`). |
| `storm_control_interfaces` | `[]` | No | Interfaces requiring storm control with per-level thresholds (default 10%). |
| `port_security_interfaces` | `[]` | No | Interfaces with port security; supports `max_addresses`, `violation_mode`, and `sticky`. |
| `dhcp_snooping` | `enabled: false` | No | Enables DHCP snooping and lists trusted interfaces and VLANs. |
| `arp_inspection` | `enabled: false` | No | Enables Dynamic ARP Inspection and lists trusted interfaces and VLANs. |
| `ip_source_guard_interfaces` | `[]` | No | Interfaces on which `ip verify source` is enforced. |
| `dot1x_config` | `enabled: false` | No | Enables 802.1X system-auth-control and sets the RADIUS server group. |
| `dot1x_interfaces` | `[]` | No | Per-interface 802.1X settings (`pae`, `port_control`, `reauth_period`). |
| `static_mac_addresses` | `[]` | No | Static MAC entries (`mac`, `vlan`, `interface`). |
| `unused_ports` | `[]` | No | Ports to shut down and move to `blackhole_vlan` (STIG requirement). |
| `blackhole_vlan` | `999` | No | VLAN used to isolate unused ports. |
| `bpdu_guard_interfaces` | `[]` | No | Edge ports on which PortFast + BPDU Guard are enabled. |
| `root_guard_interfaces` | `[]` | No | Uplink ports on which spanning-tree Root Guard is enabled. |
| `rate_limiting` | `enabled: true, acl: RATE_LIMIT_ACL` | No | Applies a control-plane ACL for rate limiting. |

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

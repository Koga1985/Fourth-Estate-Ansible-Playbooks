# ise_profiling__policies

Creates and manages custom Cisco ISE endpoint profiling policies. Profiling policies define the rules ISE uses to classify endpoints by type (workstation, IP phone, printer, IoT device, etc.) based on collected probe data. This role manages custom profiling policy definitions that extend or override ISE's built-in profiles, enabling organization-specific device classification.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE with Profiling licensed and enabled
- ISE admin credentials with ERS API access
- Ansible Vault for credential management

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ise_hostname` | `"{{ vault_ise_hostname }}"` | No | ISE Connection Parameters |
| `ise_username` | `"{{ vault_ise_username }}"` | No | — |
| `ise_password` | `"{{ vault_ise_password }}"` | No | — |
| `ise_verify_ssl` | `true` | No | — |
| `ise_use_proxy` | `false` | No | — |
| `ise_debug` | `false` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `ise_artifacts_dir` | `"/tmp/ise-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Configuration |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `ise_profiling__policies_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_profiling__policies_log_level` | `"INFO"` | No | Logging |
| `ise_profiling__policies_log_to_syslog` | `true` | No | — |
| `ise_profiling__policies_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_profiling__policies_notify_on_completion` | `false` | No | Notification Settings |
| `ise_profiling__policies_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_profiling__policies_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Configure ISE custom profiling policies
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    profiling_policies:
      - name: "Acme-IP-Camera"
        description: "Acme Corp IP camera identification"
        rules:
          - name: "Acme-Camera-DHCP"
            condition:
              attributeName: "DHCP_class-identifier"
              operator: "CONTAINS"
              value: "AcmeCamera"
            certaintyFactor: 20
          - name: "Acme-Camera-OUI"
            condition:
              attributeName: "EndpointMACAddressVendor"
              operator: "EQUALS"
              value: "Acme Systems"
            certaintyFactor: 30
      - name: "Acme-Industrial-Controller"
        description: "Acme Corp industrial OT controller"
        rules:
          - name: "Acme-OT-OUI"
            condition:
              attributeName: "EndpointMACAddressVendor"
              operator: "EQUALS"
              value: "Acme Industrial"
            certaintyFactor: 50
  roles:
    - role: cisco/roles/ise_profiling__policies
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `profiling` | All profiling configuration tasks |
| `policies` | Profiling policy creation tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- Custom policies supplement but do not replace ISE's built-in Cisco-provided profiles.
- Certainty factors accumulate per endpoint; the policy with the highest total certainty factor wins.
- All credentials must be stored in Ansible Vault.

## License

MIT

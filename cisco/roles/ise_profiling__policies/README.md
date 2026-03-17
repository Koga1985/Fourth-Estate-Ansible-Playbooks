# ise_profiling__policies

Creates and manages custom Cisco ISE endpoint profiling policies. Profiling policies define the rules ISE uses to classify endpoints by type (workstation, IP phone, printer, IoT device, etc.) based on collected probe data. This role manages custom profiling policy definitions that extend or override ISE's built-in profiles, enabling organization-specific device classification.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE with Profiling licensed and enabled
- ISE admin credentials with ERS API access
- Ansible Vault for credential management

## Role Variables

### ISE Connection

| Variable | Default | Description |
|---|---|---|
| `ise_hostname` | `{{ vault_ise_hostname }}` | ISE primary PAN hostname or IP |
| `ise_username` | `{{ vault_ise_username }}` | ISE admin username |
| `ise_password` | `{{ vault_ise_password }}` | ISE admin password (vault-protected) |
| `ise_verify_ssl` | `true` | Validate ISE TLS certificate |
| `ise_use_proxy` | `false` | Route ISE API calls through a proxy |
| `ise_debug` | `false` | Enable verbose debug logging |

### Deployment Control

| Variable | Default | Description |
|---|---|---|
| `apply_changes` | `false` | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | Local directory for generated reports |

### Profiling Policies

| Variable | Default | Description |
|---|---|---|
| `profiling_policies` | (required) | List of custom profiling policy definitions. Each entry has: `name` (required), `rules` (list of profiling rule conditions and certainty factors), and optional `description` |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_profiling__policies_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_profiling__policies_log_level` | `INFO` | Log verbosity level |
| `ise_profiling__policies_log_to_syslog` | `true` | Forward events to syslog |
| `ise_profiling__policies_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_profiling__policies_notify_on_completion` | `false` | Send email on completion |
| `ise_profiling__policies_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_profiling__policies_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

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

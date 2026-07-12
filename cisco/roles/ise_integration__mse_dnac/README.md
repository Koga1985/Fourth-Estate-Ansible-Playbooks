# ise_integration__mse_dnac

Integrates Cisco ISE with Cisco DNA Center (DNAC) and Mobility Services Engine (MSE) via pxGrid and REST APIs. This role enables ISE to share session and context information with DNA Center for SD-Access policy enforcement and with MSE for location-aware access control. Both integrations are independently toggleable and default to plan mode.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access and pxGrid enabled
- DNA Center API access (when `dnac_integration_enabled: true`)
- MSE API access (when `mse_integration_enabled: true`)
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
| `pxgrid_auto_approval` | `false` | No | pxGrid Settings |
| `dnac_integration_enabled` | `false` | No | DNA Center Integration |
| `dnac_hostname` | `""` | No | — |
| `dnac_auth_token` | `"{{ vault_dnac_auth_token \| default('') }}"` | No | — |
| `dnac_ise_shared_secret` | `"{{ vault_dnac_ise_shared_secret \| default('') }}"` | No | — |
| `mse_integration_enabled` | `false` | No | MSE Integration |
| `mse_hostname` | `""` | No | — |
| `mse_username` | `"{{ vault_mse_username \| default('') }}"` | No | — |
| `mse_password` | `"{{ vault_mse_password \| default('') }}"` | No | — |
| `mse_verify_ssl` | `true` | No | — |
| `mse_ise_shared_secret` | `"{{ vault_mse_ise_shared_secret \| default('') }}"` | No | — |
| `ise_integration__mse_dnac_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_integration__mse_dnac_log_level` | `"INFO"` | No | Logging |
| `ise_integration__mse_dnac_log_to_syslog` | `true` | No | — |
| `ise_integration__mse_dnac_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_integration__mse_dnac_notify_on_completion` | `false` | No | Notification Settings |
| `ise_integration__mse_dnac_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_integration__mse_dnac_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Integrate ISE with DNA Center and MSE
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    pxgrid_auto_approval: false
    dnac_integration_enabled: true
    dnac_hostname: "dnac.example.com"
    dnac_auth_token: "{{ vault_dnac_token }}"
    dnac_ise_shared_secret: "{{ vault_dnac_ise_secret }}"
    mse_integration_enabled: false
  roles:
    - role: cisco/roles/ise_integration__mse_dnac
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `pxgrid` | pxGrid enablement tasks |
| `integration` | All integration tasks |
| `dnac` | DNA Center integration tasks |
| `mse` | MSE integration tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- DNA Center and MSE integrations are independently controlled via their respective `_enabled` flags.
- All secrets (shared secrets, API tokens, passwords) must be stored in Ansible Vault.

## License

MIT

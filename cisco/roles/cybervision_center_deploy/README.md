# cybervision_center_deploy

Ansible role for initial Cisco Cyber Vision Center deployment and base configuration. Configures system settings, network parameters, license activation, and local admin accounts via the Cyber Vision REST API.

## Requirements

- Cyber Vision Center reachable on port 443 from Ansible controller
- Admin credentials stored in Ansible Vault
- Python `requests` library: `pip install requests`

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cv_center_host` | `"{{ vault_cv_center_hostname }}"` | No | Cyber Vision Center API Connection |
| `cv_api_url` | `"https://{{ cv_center_host }}/api/3.0"` | No | — |
| `cv_api_token` | `"{{ vault_cv_api_token }}"` | No | Bearer token (preferred) |
| `cv_username` | `"{{ vault_cv_admin_username }}"` | No | Used for initial setup only |
| `cv_password` | `"{{ vault_cv_admin_password }}"` | No | — |
| `cv_validate_certs` | `true` | No | — |
| `cv_use_proxy` | `false` | No | — |
| `cv_timeout` | `60` | No | — |
| `cv_port` | `443` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `artifacts_dir` | `"/tmp/cv-artifacts"` | No | — |
| `cv_org_name` | `"FourthEstate"` | No | Fourth Estate Organization |
| `cv_org_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `cv_environment` | `"production"` | No | — |
| `cv_region` | `"primary"` | No | — |
| `enable_initial_setup` | `true` | No | Feature Toggles |
| `enable_network_config` | `true` | No | — |
| `enable_license_activation` | `true` | No | — |
| `enable_user_management` | `true` | No | — |
| `cv_center_name` | `"FourthEstate-CyberVision"` | No | Initial System Setup |
| `cv_center_description` | `"Fourth Estate OT Security Visibility Platform"` | No | — |
| `cv_center_timezone` | `"America/New_York"` | No | — |
| `cv_center_language` | `"en"` | No | — |
| `cv_management_ip` | `"{{ vault_cv_center_management_ip }}"` | No | Network Configuration |
| `cv_management_netmask` | `"{{ vault_cv_center_management_netmask }}"` | No | — |
| `cv_management_gateway` | `"{{ vault_cv_center_management_gateway }}"` | No | — |
| `cv_dns_servers` | `(see defaults/main.yml)` | No | — |
| `cv_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `cv_domain_name` | `"fourthestate.local"` | No | — |
| `cv_license_key` | `"{{ vault_cv_license_key }}"` | No | License Configuration |
| `cv_license_type` | `"advantage"` | No | Options: essentials, advantage, premier |
| `cv_local_users` | `(see defaults/main.yml)` | No | Local User Management (Initial admin and break-glass accounts — operational users via LDAP) |
| `cv_cert_type` | `"self_signed"` | No | HTTPS Certificate Configuration Options: self_signed, uploaded, lets_encrypt |
| `cv_cert_key_size` | `4096` | No | — |
| `cv_cert_validity_days` | `365` | No | — |
| `cv_cert_organization` | `"Fourth Estate"` | No | — |
| `cv_cert_common_name` | `"{{ cv_center_host }}"` | No | — |
| `cv_cert_content` | `"{{ vault_cv_tls_cert \| default('') }}"` | No | Certificate upload (if cv_cert_type = uploaded) |
| `cv_cert_key_content` | `"{{ vault_cv_tls_key \| default('') }}"` | No | — |
| `cv_cert_ca_content` | `"{{ vault_cv_tls_ca \| default('') }}"` | No | — |

## Example Playbook

```yaml
- name: Use cybervision_center_deploy
  hosts: all
  gather_facts: false
  roles:
    - role: cybervision_center_deploy
      vars:
        apply_changes: false   # set true to apply
```

## Tags

```bash
--tags center         # All center deployment tasks
--tags setup          # Initial system setup only
--tags license        # License activation only
--tags users          # User management only
```

## Quick Start

```bash
# Dry-run (no changes)
ansible-playbook -i inventory site.yml --tags center --ask-vault-pass

# Apply
ansible-playbook -i inventory site.yml --tags center -e "apply_changes=true" --ask-vault-pass
```

## Features

| Module | Task File | Description |
|--------|-----------|-------------|
| Initial Setup | `initial_setup.yml` | Center name, timezone, language |
| Network Config | `network_config.yml` | DNS and NTP servers |
| License Activation | `license_activation.yml` | Apply Cyber Vision license key |
| User Management | `user_management.yml` | Local admin and break-glass accounts |
| Validation | `validation.yml` | Post-deployment API health check |

## Key Variables

```yaml
cv_center_host: "{{ vault_cv_center_hostname }}"    # Center FQDN or IP
cv_api_url: "https://{{ cv_center_host }}/api/3.0"  # API base URL
cv_api_token: "{{ vault_cv_api_token }}"            # Bearer token (preferred)
apply_changes: false                                 # false = dry-run

cv_center_name: "FourthEstate-CyberVision"
cv_center_timezone: "America/New_York"
cv_license_type: "advantage"
```

## Required Vault Variables

```yaml
vault_cv_center_hostname: "cybervision.example.com"
vault_cv_api_token: "your-api-bearer-token"         # Preferred
vault_cv_admin_username: "admin"                    # Used only for initial token auth
vault_cv_admin_password: "your-admin-password"
vault_cv_admin_email: "admin@example.com"
vault_cv_breakglass_email: "security@example.com"
vault_cv_breakglass_password: "break-glass-password"
vault_cv_license_key: "XXXX-XXXX-XXXX-XXXX"
vault_cv_center_management_ip: "192.168.10.10"
vault_cv_center_management_netmask: "255.255.255.0"
vault_cv_center_management_gateway: "192.168.10.1"
vault_dns_server_primary: "8.8.8.8"
vault_dns_server_secondary: "8.8.4.4"
vault_fourth_estate_contact: "it@fourthestate.gov"
```

## Generated Artifacts

| Artifact | Description |
|----------|-------------|
| `cv_initial_setup.json` | Center name, timezone, language |
| `cv_network_config.json` | DNS and NTP configuration |
| `cv_license.json` | License type and activation status |
| `cv_user_management.json` | Local user list |
| `cv_center_validation.json` | Post-deployment API check results |

## License

MIT

# cybervision_center_deploy

Ansible role for initial Cisco Cyber Vision Center deployment and base configuration. Configures system settings, network parameters, license activation, and local admin accounts via the Cyber Vision REST API.

## Quick Start

```bash
# Dry-run (no changes)
ansible-playbook -i inventory site.yml --tags center --ask-vault-pass

# Apply
ansible-playbook -i inventory site.yml --tags center -e "apply_changes=true" --ask-vault-pass
```

## Requirements

- Cyber Vision Center reachable on port 443 from Ansible controller
- Admin credentials stored in Ansible Vault
- Python `requests` library: `pip install requests`

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

## Tags

```bash
--tags center         # All center deployment tasks
--tags setup          # Initial system setup only
--tags license        # License activation only
--tags users          # User management only
```

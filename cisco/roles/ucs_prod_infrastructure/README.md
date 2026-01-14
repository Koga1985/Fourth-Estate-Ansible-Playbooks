# ucs_prod_infrastructure

Cisco UCS Production Infrastructure deployment role for Fourth Estate organizations.

## Description

This role automates the deployment of Cisco UCS infrastructure for production environments with a focus on Fourth Estate (free press and media) organizations. It includes comprehensive configuration management for:

- UCS Manager initial setup
- Organization hierarchy
- Service profile templates
- Network and storage connectivity
- Server pools and policies
- High availability configuration
- DoD STIG and NIST 800-53 compliance

## Requirements

- Ansible >= 2.9
- Cisco UCS Python SDK (`pip install ucsmsdk`)
- Cisco UCS Ansible collection (`ansible-galaxy collection install cisco.ucs`)
- Access to UCS Manager with administrative credentials
- Network connectivity to UCS Manager

## Role Variables

### Connection Variables (Required)
- `ucs_hostname`: UCS Manager IP or hostname
- `ucs_username`: UCS Manager username
- `ucs_password`: UCS Manager password

### Fourth Estate Configuration
- `fourth_estate_org_name`: Organization name (default: "FourthEstate")
- `fourth_estate_description`: Organization description
- `fourth_estate_contact`: Technical contact
- `fourth_estate_email`: Contact email
- `fourth_estate_sub_orgs`: List of sub-organizations

### Deployment Control
- `apply_changes`: Set to `true` to apply changes (default: `false` for dry-run)
- `ucs_artifacts_dir`: Directory for deployment artifacts

### Feature Toggles
- `ucs_enable_ucsm_config`: Enable UCS Manager initial configuration
- `ucs_enable_org_setup`: Enable organization setup
- `ucs_enable_service_profiles`: Enable service profile configuration
- `ucs_enable_vnic_vhba`: Enable network/storage templates
- `ucs_enable_san`: Enable SAN connectivity
- `ucs_enable_ha`: Enable high availability features

See `defaults/main.yml` for complete variable documentation.

## Dependencies

None

## Example Playbook

```yaml
---
- name: Deploy UCS Infrastructure for Fourth Estate
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    ucs_hostname: "ucs-manager.example.com"
    fourth_estate_org_name: "NewsOrg"

  roles:
    - role: ucs_prod_infrastructure
```

## Usage

### Dry Run (Validation Only)
```bash
ansible-playbook playbooks/deploy_ucs.yml
```

### Apply Changes
```bash
ansible-playbook playbooks/deploy_ucs.yml -e "apply_changes=true"
```

### Specific Tags
```bash
ansible-playbook playbooks/deploy_ucs.yml --tags "organizations,service_profiles"
```

## Security Considerations

- Store sensitive credentials in Ansible Vault
- Enable `ucs_validate_certs: true` for production
- Review all configurations before setting `apply_changes: true`
- Follow DoD STIG guidelines for UCS hardening
- Implement NIST 800-53 controls as required

## Compliance

This role supports the following compliance frameworks:
- DoD STIG for Cisco UCS
- NIST 800-53 (Moderate and High)
- NIST 800-171
- FISMA requirements

## License

MIT

## Author Information

Created for Fourth Estate production deployments.

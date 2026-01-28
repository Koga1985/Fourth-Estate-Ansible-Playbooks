# Palo Alto Ansible Playbooks

This folder contains Ansible roles and playbooks to automate configuration and operational tasks for Palo Alto Networks firewalls and Panorama.

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your firewall/Panorama details

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Deploy platform baseline only
ansible-playbook -i inventory site.yml --tags baseline

# Deploy security policies
ansible-playbook -i inventory site.yml --tags security

# Configure SSL decryption
ansible-playbook -i inventory site.yml --tags ssl

# Configure VPN
ansible-playbook -i inventory site.yml --tags vpn
```

## Prerequisites

- Ansible 2.9+ (2.10+ recommended)
- The `paloaltonetworks.panos` collection
- Network connectivity to target firewalls/Panorama and appropriate API credentials

## Contents

- `roles/` — any role-level automation maintained here
- `tasks/` — ad-hoc playbooks and task files

## Example — push a configuration change

```yaml
- name: Push address-object to PAN-OS

  hosts: palo
  collections:
    - paloaltonetworks.panos
  vars:
    pano_host: "panorama.example.local"
    pano_user: "admin"
    pano_password: "!vault_encrypted!"
  tasks:
    - name: Create address object
      panos_object:
        provider:
          ip_address: "{{ pano_host }}"
          username: "{{ pano_user }}"
          password: "{{ pano_password }}"
        state: present
        type: address
        name: "web-servers"
        value: "10.0.10.0/24"
```

## Common variables

- `pano_host` / `firewall_host`: address of Panorama or firewall
- `pano_user` / `firewall_user`: API username
- `pano_password` / `firewall_password`: API password (use Ansible Vault)
- `device_group`: Panorama device-group to target (if using Panorama)

## Testing and validation

- Use `--check --diff` to perform dry-runs where modules support it.
- Review firewall/Panorama config and commit history after changes.

## Security

- Do not store plaintext credentials in the repo. Use Ansible Vault or a secrets manager.

## Notes

- Check the task/role README files for per-playbook variables and examples.
- If you'd like, I can add a small sample playbook and an `inventory.ini` for this folder.

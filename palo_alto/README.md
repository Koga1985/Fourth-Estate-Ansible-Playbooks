# Palo Alto Networks Ansible Automation

This directory contains **10 Ansible roles** for automating **Palo Alto Networks** PAN-OS firewalls and Panorama management, including security policies, VPN configuration, QoS, and compliance hardening.

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

## 📋 Roles

### Platform Configuration (3 roles)
- **panos_baseline_config** - System settings, DNS, NTP, management profile
- **panos_network_config** - Zones, interfaces, virtual routers, static routes
- **panos_ha_config** - Active/passive and active/active high availability

### Security (3 roles)
- **panos_security_policies** - Security rules, address/service objects, groups
- **panos_nat_policies** - Source and destination NAT rules
- **panos_ssl_decryption** - SSL decryption profiles and policies

### Connectivity (2 roles)
- **panos_ipsec_vpn** - Site-to-site and GlobalProtect VPN configuration
- **panos_qos** - QoS profiles and traffic shaping policies

### Operations (2 roles)
- **panos_panorama_management** - Panorama device groups, templates, and log forwarding
- **panos_backup_operations** - Configuration backups and commit scheduling

## Prerequisites

- Ansible 2.12+ (2.14+ recommended)
- The `paloaltonetworks.panos` collection
- Python packages: `pan-python`, `pandevice`
- Network connectivity to target firewalls/Panorama and appropriate API credentials

## ⚙️ Configuration

```yaml
# group_vars/paloalto.yml
pano_host: "panorama.example.com"
pano_user: "svc_ansible"
pano_password: "{{ vault_pano_password }}"
device_group: "Fourth-Estate-Firewalls"
```

### Common Variables

| Variable | Description |
|----------|-------------|
| `pano_host` / `firewall_host` | Address of Panorama or firewall |
| `pano_user` / `firewall_user` | API username |
| `pano_password` / `firewall_password` | API password (use Ansible Vault) |
| `device_group` | Panorama device-group to target |

## 📖 Usage Example

```yaml
- name: Push address-object to PAN-OS
  hosts: localhost
  connection: local
  collections:
    - paloaltonetworks.panos
  vars_files:
    - group_vars/paloalto.yml
  tasks:
    - name: Create address object
      paloaltonetworks.panos.panos_address_object:
        provider:
          ip_address: "{{ pano_host }}"
          username: "{{ pano_user }}"
          password: "{{ pano_password }}"
        state: present
        name: "web-servers"
        value: "10.0.10.0/24"
```

## 🛡️ Security & Compliance

- All roles support DoD STIG and NIST 800-53 security baselines
- Firewall rules follow a deny-all default policy
- Audit logging enabled for all configuration changes
- TLS 1.2+ enforced for management connections

## 🔧 Troubleshooting

- **Connection failures**: Verify network access and API credentials
- **Commit errors**: Check configuration validation in Panorama/firewall UI
- **Module compatibility**: Ensure `paloaltonetworks.panos` version matches PAN-OS version
- Use `--check --diff` to perform dry-runs where modules support it

## 📚 References

- [PAN-OS Ansible Collection](https://galaxy.ansible.com/paloaltonetworks/panos)
- [PAN-OS Administrator's Guide](https://docs.paloaltonetworks.com/)
- [DoD STIG for Palo Alto](https://public.cyber.mil/stigs/)

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

# Fortinet FortiGate Automation

This directory contains **12 Ansible roles** for automating **Fortinet FortiGate** next-generation firewall configuration including system setup, network interfaces, firewall policies, VPN, routing, HA, and security profiles.

## 📋 Roles

### System & Network (2 roles)
- **fortigate_system_config** - System-level configuration (hostname, NTP, DNS, admin settings)
- **fortigate_interfaces** - Network interface configuration (physical, VLANs, loopbacks)

### Policy & Objects (4 roles)

### Security Profiles (1 role)

### VPN (2 roles)

### Infrastructure (3 roles)

## 🚀 Quick Start

```bash
# Configure firewall policy
ansible-playbook playbooks/fortigate_policy.yml \
  -e "policy_name=Allow-Web-Traffic" \
  -e "src_zone=internal" \
  -e "dst_zone=external"

# Configure IPsec VPN
ansible-playbook playbooks/fortigate_ipsec_vpn.yml \
  -e "tunnel_name=site-to-site" \
  -e "remote_gateway=203.0.113.1"
```

## ⚙️ Configuration

```yaml
# FortiGate connection
fortigate_host: "{{ vault_fortigate_host }}"
fortigate_token: "{{ vault_fortigate_token }}"
fortigate_vdom: "root"

# Firewall policy
fortigate_policy:
  name: "Allow-HTTPS"
  srcintf: "port1"
  dstintf: "port2"
  action: "accept"
  service: ["HTTPS"]

# VPN configuration
fortigate_vpn_psk: "{{ vault_vpn_psk }}"
fortigate_vpn_encryption: "aes256"
fortigate_vpn_authentication: "sha256"
```

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

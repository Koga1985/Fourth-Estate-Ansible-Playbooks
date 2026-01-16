# Fortinet FortiGate Automation

This directory contains **12 Ansible roles** for automating **Fortinet FortiGate** next-generation firewall configuration including policies, VPN, routing, HA, security profiles, and logging.

## 📋 Roles

### Basic Configuration (3 roles)
- **fortigate_system_config** - System-level configuration
- **fortigate_interfaces** - Interface configuration
- **fortigate_zones** - Security zone management

### Firewall & Security (4 roles)
- **fortigate_addresses** - Address object management
- **fortigate_firewall_policy** - Firewall policy rules
- **fortigate_nat** - NAT and VIP configuration
- **fortigate_security_profiles** - IPS, AV, Web Filter profiles

### VPN Configuration (2 roles)
- **fortigate_vpn_ipsec** - IPsec VPN tunnels
- **fortigate_ssl_vpn** - SSL VPN configuration

### Advanced Features (3 roles)
- **fortigate_routing** - Static and dynamic routing
- **fortigate_ha** - High availability configuration
- **fortigate_logging** - Logging and SIEM integration

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

**Maintained By:** Fourth Estate Infrastructure Team

# Fortinet FortiGate Automation

This directory contains **12 Ansible roles** for automating **Fortinet FortiGate** next-generation firewall configuration including system setup, network interfaces, firewall policies, VPN, routing, HA, and security profiles.

## 📋 Roles

### System & Network (2 roles)
- **fortigate_system_config** - System-level configuration (hostname, NTP, DNS, admin settings)
- **fortigate_interfaces** - Network interface configuration (physical, VLANs, loopbacks)

### Policy & Objects (4 roles)
- **fortigate_zones** - Security zone definition and management
- **fortigate_addresses** - Address object and group management
- **fortigate_firewall_policy** - Firewall policy rule creation and ordering
- **fortigate_nat** - NAT (source NAT, destination NAT, VIP) configuration

### Security Profiles (1 role)
- **fortigate_security_profiles** - AV, IPS, web filter, application control profiles

### VPN (2 roles)
- **fortigate_vpn_ipsec** - IPsec VPN tunnel configuration
- **fortigate_ssl_vpn** - SSL VPN portal and user access

### Infrastructure (3 roles)
- **fortigate_routing** - Static and dynamic routing (BGP, OSPF)
- **fortigate_ha** - High availability (active-passive, active-active) clustering
- **fortigate_logging** - Syslog, FortiAnalyzer, and local logging configuration

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

# F5 BIG-IP Load Balancer

This directory contains **12 Ansible roles** for automating **F5 BIG-IP** load balancer configuration including system management, virtual servers, pools, SSL certificates, iRules, Application Security Manager (ASM/WAF), and high availability.

## 📋 Roles

### System & Network (2 roles)
- **f5_bigip_system** - System configuration (NTP, DNS, licensing)
- **f5_bigip_network** - Network interfaces, VLANs, and self-IPs

### SSL & Certificates (1 role)
- **f5_bigip_ssl** - SSL certificate and key management

### Load Balancing Core (4 roles)
- **f5_bigip_node** - Node (server) management
- **f5_bigip_pool** - Server pool configuration
- **f5_bigip_monitor** - Health monitor configuration
- **f5_bigip_virtual_server** - Virtual server (VIP) management

### Advanced Features (3 roles)
- **f5_bigip_profiles** - Profile management (HTTP, TCP, client SSL)
- **f5_bigip_irules** - iRules for traffic manipulation
- **f5_bigip_persistence** - Session persistence configuration

### High Availability & Security (2 roles)
- **f5_bigip_ha** - High availability (active/standby, active/active)
- **f5_bigip_asm** - Application Security Manager (WAF)

## 🚀 Quick Start

```bash
# Configure basic load balancer
ansible-playbook playbooks/f5_basic_lb.yml \
  -e "f5_host=bigip.example.com" \
  -e "f5_user=admin" \
  -e "f5_password=secret"

# Deploy virtual server with pool
ansible-playbook playbooks/f5_virtual_server.yml \
  -e "vip_name=web-vip" \
  -e "vip_address=10.1.10.100" \
  -e "vip_port=443"
```

## ⚙️ Configuration

### Connection Variables

```yaml
# F5 BIG-IP connection
f5_host: "bigip.example.com"
f5_user: "admin"
f5_password: "{{ vault_f5_password }}"
f5_validate_certs: true
f5_partition: "Common"
```

### Virtual Server Configuration

```yaml
# Virtual server (VIP)
virtual_servers:
  - name: "web-vip"
    destination: "10.1.10.100"
    port: 443
    pool: "web-pool"
    profiles:
      - "http"
      - "clientssl"
    irules:
      - "redirect-to-https"
    persistence: "cookie"

  - name: "api-vip"
    destination: "10.1.10.101"
    port: 8443
    pool: "api-pool"
    snat: "automap"
```

### Pool & Node Configuration

```yaml
# Server pools
pools:
  - name: "web-pool"
    lb_method: "least-connections-member"
    monitor: "https"
    members:
      - host: "10.1.20.10"
        port: 443
      - host: "10.1.20.11"
        port: 443
      - host: "10.1.20.12"
        port: 443

# Nodes (servers)
nodes:
  - name: "web01"
    address: "10.1.20.10"
    monitor: "icmp"
  - name: "web02"
    address: "10.1.20.11"
    monitor: "icmp"
```

### Health Monitor Configuration

```yaml
# Health monitors
monitors:
  - name: "https-monitor"
    type: "https"
    interval: 5
    timeout: 16
    send_string: "GET /health HTTP/1.1\\r\\nHost: example.com\\r\\n\\r\\n"
    receive_string: "200 OK"

  - name: "tcp-monitor"
    type: "tcp"
    interval: 5
    timeout: 16
```

### SSL Certificate Management

```yaml
# SSL certificates
ssl_certificates:
  - name: "example-cert"
    cert_content: "{{ lookup('file', 'certs/example.crt') }}"
    key_content: "{{ lookup('file', 'certs/example.key') }}"
    partition: "Common"

# Client SSL profiles
client_ssl_profiles:
  - name: "example-clientssl"
    cert: "example-cert"
    key: "example-cert"
    chain: "ca-bundle"
    ciphers: "DEFAULT:!SSLv3:!TLSv1"
```

### iRules Configuration

```yaml
# iRules for traffic manipulation
irules:
  - name: "redirect-to-https"
    content: |
      when HTTP_REQUEST {
        if { [HTTP::uri] starts_with "/admin" } {
          HTTP::redirect "https://[HTTP::host][HTTP::uri]"
        }
      }

  - name: "x-forwarded-for"
    content: |
      when HTTP_REQUEST {
        HTTP::header insert X-Forwarded-For [IP::client_addr]
      }
```

### High Availability Configuration

```yaml
# Device group (HA)
device_group:
  name: "bigip-ha-group"
  type: "sync-failover"
  members:
    - "bigip01.example.com"
    - "bigip02.example.com"
  auto_sync: true
  full_sync: false

# Traffic group
traffic_group:
  name: "traffic-group-1"
  ha_order:
    - "bigip01.example.com"
    - "bigip02.example.com"
```

### ASM/WAF Configuration

```yaml
# ASM policies (Web Application Firewall)
asm_policies:
  - name: "web-waf-policy"
    template: "Rapid Deployment Policy"
    enforcement_mode: "blocking"
    learning_mode: true

  - name: "api-waf-policy"
    template: "API Security"
    enforcement_mode: "transparent"
```

## 📖 Common Use Cases

### Use Case 1: Deploy Basic Load Balancer

```yaml
---
# playbooks/f5_basic_lb.yml
- name: Configure F5 BIG-IP Load Balancer
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: f5_bigip_node
      vars:
        nodes:
          - name: "web01"
            address: "10.1.20.10"
          - name: "web02"
            address: "10.1.20.11"

    - role: f5_bigip_monitor
      vars:
        monitors:
          - name: "https-check"
            type: "https"
            send: "GET /health HTTP/1.1\\r\\nHost: example.com\\r\\n\\r\\n"
            receive: "200 OK"

    - role: f5_bigip_pool
      vars:
        pools:
          - name: "web-pool"
            members:
              - host: "10.1.20.10"
                port: 443
              - host: "10.1.20.11"
                port: 443

    - role: f5_bigip_virtual_server
      vars:
        virtual_servers:
          - name: "web-vip"
            destination: "10.1.10.100"
            port: 443
            pool: "web-pool"
```

### Use Case 2: SSL Offloading

```bash
ansible-playbook playbooks/f5_ssl_offload.yml \
  -e "vip_name=secure-web" \
  -e "cert_file=certs/example.crt" \
  -e "key_file=certs/example.key"
```

### Use Case 3: Deploy WAF Protection

```bash
ansible-playbook playbooks/f5_waf_deploy.yml \
  -e "policy_name=web-waf" \
  -e "enforcement_mode=blocking" \
  -e "virtual_server=web-vip"
```

### Use Case 4: Configure High Availability

```bash
ansible-playbook playbooks/f5_ha_setup.yml \
  -e "device_group=bigip-cluster" \
  -e "primary_device=bigip01.example.com" \
  -e "secondary_device=bigip02.example.com"
```

## 🛡️ Security Best Practices

1. **Use HTTPS** - Always use TLS 1.2+ for management
2. **Strong Ciphers** - Configure secure cipher suites
3. **Client Certificate Authentication** - For administrative access
4. **RBAC** - Use partition-based access control
5. **Enable ASM/WAF** - Protect web applications from attacks
6. **Regular Updates** - Keep F5 software up to date
7. **Secure iRules** - Review iRules for security vulnerabilities
8. **Audit Logging** - Enable comprehensive audit logs
9. **Connection Limits** - Set rate limiting and connection limits
10. **Monitor Security Events** - Integrate with SIEM (Splunk, ELK)

## 🔧 Troubleshooting

### Issue: Unable to Connect to F5 BIG-IP

**Symptoms:** Connection timeout or authentication failure

**Resolution:**
```bash
# Test connectivity
curl -k https://bigip.example.com/mgmt/tm/sys/version

# Verify credentials
ansible localhost -m bigip_device_info \
  -a "provider={server: bigip.example.com, user: admin, password: secret}"
```

### Issue: Virtual Server Not Passing Traffic

**Symptoms:** Virtual server shows down or connections fail

**Resolution:**
```bash
# Check pool member status
tmsh show ltm pool web-pool members

# Check virtual server status
tmsh show ltm virtual web-vip

# Verify monitor status
tmsh show ltm monitor https
```

### Issue: High Availability Sync Failing

**Symptoms:** Configuration not syncing between devices

**Resolution:**
```bash
# Force config sync
tmsh run cm config-sync to-group bigip-ha-group

# Check sync status
tmsh show cm sync-status

# Verify network connectivity
tmsh show net interface
```

## 📚 Additional Resources

- [F5 BIG-IP Documentation](https://techdocs.f5.com/)
- [Ansible F5 Collection](https://galaxy.ansible.com/f5networks/f5_modules)
- [F5 iRules Wiki](https://devcentral.f5.com/s/wiki/iRules.Wiki.ashx)
- [F5 Best Practices](https://techdocs.f5.com/en-us/bigip-14-1-0/big-ip-deployment-guide.html)
- [ASM/WAF Configuration Guide](https://techdocs.f5.com/en-us/bigip-14-1-0/big-ip-asm-implementations.html)

## 🤝 Contributing

When contributing to F5 automation:
- Test in lab environment before production
- Follow F5 naming conventions
- Document iRules thoroughly
- Include rollback procedures
- Test high availability failover
- Verify health monitors work correctly

---

**Last Updated:** 2026-01-16
**Maintained By:** Fourth Estate Infrastructure Team
**F5 Versions Supported:** BIG-IP v13.x, v14.x, v15.x, v16.x

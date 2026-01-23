# vcenter_install

Deploy vCenter Server Appliance (VCSA) using the CLI installer with production-ready configuration for Fourth Estate agencies.

## Description

This role automates the deployment of VMware vCenter Server Appliance (VCSA) on an ESXi host using the VCSA CLI installer. It supports both embedded and external PSC deployments, customizable sizing, and Fourth Estate-specific security requirements including DISA STIG compliance.

## Requirements

- VMware vCenter Server Appliance ISO (7.0 U3+ or 8.0+)
- ESXi 7.0+ host for deployment
- Ansible 2.15+
- Python 3.8+
- Collections:
  - community.vmware >= 3.0.0

## Role Variables

### Required Variables

```yaml
vcenter_hostname: "vcsa.example.mil"
vcenter_ip_address: "192.168.1.10"
vcenter_sso_password: "SecurePassword123!"
vcenter_root_password: "RootPassword123!"
esxi_deployment_host: "esxi01.example.mil"
esxi_deployment_username: "root"
esxi_deployment_password: "EsxiPassword123!"
```

### Deployment Configuration

```yaml
# VCSA sizing
vcenter_deployment_size: "small"  # tiny|small|medium|large|xlarge
vcenter_storage_size: "default"   # default|large|xlarge

# Network configuration
vcenter_network_mode: "static"    # static|dhcp
vcenter_gateway: "192.168.1.1"
vcenter_subnet_mask: "255.255.255.0"
vcenter_dns_servers:
  - "192.168.1.53"
  - "192.168.1.54"

# NTP configuration
vcenter_ntp_servers:
  - "time.nist.gov"
```

### Fourth Estate Configuration

```yaml
fourth_estate:
  enhanced_security: true
  syslog_enabled: true
  syslog_server: "syslog.example.mil"
  isolated_network_enabled: true
  journalist_network: "Journalist_Network"
```

## Dependencies

None

## Example Playbook

```yaml
---
- name: Deploy vCenter Server Appliance
  hosts: localhost
  gather_facts: false
  vars:
    vcenter_hostname: "vcsa.example.mil"
    vcenter_ip_address: "10.10.10.10"
    vcenter_sso_password: "{{ vault_vcenter_sso_password }}"
    vcenter_root_password: "{{ vault_vcenter_root_password }}"
    esxi_deployment_host: "esxi01.example.mil"
    esxi_deployment_username: "root"
    esxi_deployment_password: "{{ vault_esxi_password }}"
    esxi_deployment_datastore: "datastore1"
    vcenter_deployment_size: "medium"

  roles:
    - vcenter_install
```

## VCSA Sizing Guide

| Size | vCPU | RAM | Max Hosts | Max VMs | Use Case |
|------|------|-----|-----------|---------|----------|
| tiny | 2 | 12GB | 10 | 100 | Lab/PoC |
| small | 4 | 19GB | 100 | 1,000 | Small production |
| medium | 8 | 28GB | 400 | 4,000 | Medium production |
| large | 16 | 37GB | 1,000 | 10,000 | Large production |
| xlarge | 24 | 56GB | 2,000 | 35,000 | Enterprise |

## Fourth Estate Features

- **Enhanced Security**: Disabled CEIP, SSH access restricted
- **Audit Logging**: Syslog forwarding to centralized server
- **Network Isolation**: Support for isolated journalist networks
- **Compliance**: DISA STIG baseline configuration
- **Evidence Preservation**: Dedicated storage for forensic VMs

## Security Considerations

- Store all passwords in Ansible Vault
- Use strong passwords meeting DoD complexity requirements
- Disable SSH access after initial configuration
- Configure certificate-based authentication
- Enable audit logging to remote syslog server
- Implement network segmentation for different security zones

## License

MIT

## Author Information

Fourth Estate Infrastructure Automation Team

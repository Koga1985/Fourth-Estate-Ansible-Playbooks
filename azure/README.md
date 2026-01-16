# Microsoft Azure

This directory contains **30+ Ansible roles** for managing **Microsoft Azure** infrastructure with emphasis on security, compliance (FedRAMP, NIST 800-53), Azure Government Cloud, and Fourth Estate requirements.

## Overview

Comprehensive Azure automation covering Azure AD/Entra ID, Virtual Networks, Virtual Machines, AKS (Kubernetes), Storage Accounts, SQL Database, Azure Functions, Key Vault, Security Center, Sentinel, and compliance automation.

## 📋 Role Categories

### Identity & Access Management (6 roles)
- **azure_ad** - Azure Active Directory (Entra ID) management
- **azure_rbac** - Role-Based Access Control
- **azure_managed_identity** - Managed identities for Azure resources
- **azure_conditional_access** - Conditional access policies
- **azure_privileged_identity** - PIM (Privileged Identity Management)
- **azure_service_principals** - Service principal automation

### Networking (6 roles)
- **azure_vnet** - Virtual Network creation and management
- **azure_subnets** - Subnet configuration
- **azure_nsg** - Network Security Groups
- **azure_application_gateway** - Application Gateway and WAF
- **azure_vpn_gateway** - VPN Gateway configuration
- **azure_firewall** - Azure Firewall deployment

### Compute (5 roles)
- **azure_vm** - Virtual Machine lifecycle
- **azure_vmss** - Virtual Machine Scale Sets
- **azure_availability_sets** - Availability Set management
- **azure_disk** - Managed Disk operations
- **azure_image** - Custom image management

### Container & Kubernetes (4 roles)
- **azure_aks** - Azure Kubernetes Service
- **azure_acr** - Azure Container Registry
- **azure_aci** - Azure Container Instances
- **azure_service_fabric** - Service Fabric clusters

### Storage (4 roles)
- **azure_storage_account** - Storage Account management
- **azure_blob_storage** - Blob storage and lifecycle
- **azure_file_share** - Azure Files (SMB/NFS)
- **azure_disk_storage** - Premium/Ultra disk storage

### Databases (4 roles)
- **azure_sql_database** - Azure SQL Database
- **azure_cosmos_db** - Cosmos DB management
- **azure_postgresql** - Azure Database for PostgreSQL
- **azure_mysql** - Azure Database for MySQL

### Serverless & Integration (3 roles)
- **azure_functions** - Azure Functions deployment
- **azure_logic_apps** - Logic Apps automation
- **azure_event_grid** - Event Grid configuration

### Security & Compliance (6 roles)
- **azure_key_vault** - Key Vault secrets and keys
- **azure_security_center** - Security Center configuration
- **azure_sentinel** - Azure Sentinel SIEM
- **azure_policy** - Azure Policy enforcement
- **azure_defender** - Microsoft Defender for Cloud
- **azure_compliance** - FedRAMP/NIST compliance

### Monitoring & Management (4 roles)
- **azure_monitor** - Azure Monitor configuration
- **azure_log_analytics** - Log Analytics workspace
- **azure_application_insights** - Application monitoring
- **azure_automation** - Azure Automation accounts

### Azure Government & Compliance (3 roles)
- **azure_gov_cloud** - Azure Government Cloud configuration
- **azure_fedramp_compliance** - FedRAMP baseline controls
- **azure_nist_compliance** - NIST 800-53 implementation

## 🚀 Quick Start

### Prerequisites

- Ansible 2.12.0+
- `azure.azcollection` collection (version 1.14.0+)
- Azure CLI installed and configured
- Python azure-* libraries

### Installation

```bash
# Install Azure collection
ansible-galaxy collection install azure.azcollection

# Install Python Azure SDK
pip install ansible[azure]
# Or individual packages
pip install azure-mgmt-compute azure-mgmt-network azure-mgmt-storage \
    azure-mgmt-resource azure-identity azure-mgmt-keyvault
```

### Azure Authentication

**Option 1: Service Principal (Recommended)**
```bash
export AZURE_SUBSCRIPTION_ID="<subscription-id>"
export AZURE_CLIENT_ID="<client-id>"
export AZURE_SECRET="<client-secret>"
export AZURE_TENANT="<tenant-id>"
```

**Option 2: Ansible Vault**
```yaml
# group_vars/azure.yml
azure_subscription_id: "{{ vault_azure_subscription_id }}"
azure_client_id: "{{ vault_azure_client_id }}"
azure_secret: "{{ vault_azure_secret }}"
azure_tenant: "{{ vault_azure_tenant }}"
```

**Option 3: Azure CLI (Development)**
```bash
az login
az account set --subscription "<subscription-id>"
```

### Basic Configuration

```yaml
# group_vars/azure.yml
azure_region: "eastus"
azure_resource_group: "fourth-estate-prod"
azure_environment: "production"

# Tagging strategy
azure_tags:
  Environment: "{{ azure_environment }}"
  ManagedBy: "Ansible"
  Owner: "Fourth Estate Infrastructure"
  CostCenter: "Engineering"
  Compliance: "FedRAMP-Moderate"
```

## 📖 Common Use Cases

### Use Case 1: Deploy Secure Azure VNet

```yaml
---
# playbooks/azure_vnet_setup.yml
- name: Deploy Azure Virtual Network
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: azure_vnet
      vars:
        vnet_name: "fourth-estate-vnet"
        vnet_address_prefix: "10.0.0.0/16"
        location: "eastus"

    - role: azure_subnets
      vars:
        subnets:
          - name: "web-subnet"
            address_prefix: "10.0.1.0/24"
          - name: "app-subnet"
            address_prefix: "10.0.2.0/24"
          - name: "data-subnet"
            address_prefix: "10.0.3.0/24"

    - role: azure_nsg
      vars:
        nsg_name: "fourth-estate-nsg"
```

### Use Case 2: Deploy AKS Cluster with Security

```bash
ansible-playbook playbooks/azure_aks_cluster.yml \
  -e "cluster_name=fourth-estate-aks" \
  -e "kubernetes_version=1.28" \
  -e "enable_azure_policy=true" \
  -e "enable_defender=true"
```

### Use Case 3: Configure Azure Key Vault

```bash
ansible-playbook playbooks/azure_key_vault.yml \
  -e "vault_name=fourth-estate-kv" \
  -e "enable_rbac=true" \
  -e "enable_purge_protection=true"
```

### Use Case 4: Deploy Azure SQL Database

```bash
ansible-playbook playbooks/azure_sql_database.yml \
  -e "server_name=fourth-estate-sql" \
  -e "database_name=production" \
  -e "sku=P2" \
  -e "enable_tde=true"
```

## ⚙️ Configuration Variables

### Global Azure Configuration

```yaml
# Azure subscription and authentication
azure_subscription_id: "{{ vault_azure_subscription_id }}"
azure_client_id: "{{ vault_azure_client_id }}"
azure_secret: "{{ vault_azure_secret }}"
azure_tenant: "{{ vault_azure_tenant }}"

# Resource location
azure_region: "eastus"  # or eastus2, westus, etc.
azure_resource_group: "fourth-estate-rg"

# Common tags
azure_common_tags:
  Environment: "production"
  ManagedBy: "Ansible"
  Project: "Fourth Estate"
  Compliance: "FedRAMP-Moderate"
```

### Virtual Network Configuration

```yaml
vnet_name: "fourth-estate-vnet"
vnet_address_prefix: "10.0.0.0/16"
vnet_location: "{{ azure_region }}"

# Subnets
vnet_subnets:
  - name: "GatewaySubnet"
    address_prefix: "10.0.0.0/27"
  - name: "AzureFirewallSubnet"
    address_prefix: "10.0.0.32/26"
  - name: "web-tier"
    address_prefix: "10.0.1.0/24"
  - name: "app-tier"
    address_prefix: "10.0.2.0/24"
  - name: "data-tier"
    address_prefix: "10.0.3.0/24"

# DNS servers
vnet_dns_servers:
  - "10.0.0.4"
  - "10.0.0.5"
```

### AKS Configuration

```yaml
aks_cluster_name: "fourth-estate-aks"
aks_kubernetes_version: "1.28"
aks_dns_prefix: "fourth-estate"

# Node pool configuration
aks_node_pools:
  - name: "system"
    vm_size: "Standard_D4s_v3"
    node_count: 3
    mode: "System"
    os_disk_size_gb: 128

  - name: "user"
    vm_size: "Standard_D8s_v3"
    node_count: 3
    mode: "User"
    enable_auto_scaling: true
    min_count: 2
    max_count: 10

# Network configuration
aks_network_plugin: "azure"  # or kubenet
aks_network_policy: "azure"
aks_service_cidr: "172.16.0.0/16"
aks_dns_service_ip: "172.16.0.10"

# Security
aks_enable_rbac: true
aks_enable_azure_policy: true
aks_enable_defender: true
aks_enable_private_cluster: true
```

### Azure SQL Database

```yaml
sql_server_name: "fourth-estate-sql"
sql_admin_username: "sqladmin"
sql_admin_password: "{{ vault_sql_admin_password }}"

# Database configuration
sql_databases:
  - name: "production"
    edition: "Premium"
    service_objective: "P2"
    max_size_gb: 250

# Security
sql_enable_tde: true
sql_enable_auditing: true
sql_audit_storage_account: "fourthestateaudit"

# Firewall rules
sql_firewall_rules:
  - name: "AllowAzureServices"
    start_ip: "0.0.0.0"
    end_ip: "0.0.0.0"
```

## 🛡️ Security & Compliance

### FedRAMP Compliance

Azure roles implement FedRAMP Moderate baseline controls:

| Control Family | Controls | Implementation |
|----------------|----------|----------------|
| **AC** - Access Control | AC-2, AC-3, AC-6 | Azure AD, RBAC, PIM |
| **AU** - Audit & Accountability | AU-2, AU-3, AU-9 | Azure Monitor, Log Analytics |
| **CM** - Configuration Management | CM-2, CM-6, CM-7 | Azure Policy, Blueprints |
| **IA** - Identification & Authentication | IA-2, IA-5, IA-8 | Azure AD, MFA, Conditional Access |
| **SC** - System & Communications | SC-7, SC-8, SC-13 | NSG, Key Vault, TLS |

### NIST 800-53 Rev 5

- **Encryption at Rest** - Azure Storage Service Encryption, SQL TDE
- **Encryption in Transit** - TLS 1.2+ for all communications
- **Network Segmentation** - VNet, Subnets, NSG, Azure Firewall
- **Audit Logging** - Azure Monitor, Log Analytics, Sentinel
- **Identity Management** - Azure AD with MFA and Conditional Access
- **Threat Detection** - Microsoft Defender for Cloud, Sentinel

### Azure Government Cloud

Special configuration for Azure Government regions:

```yaml
# Government cloud settings
azure_cloud_environment: "AzureUSGovernment"
azure_region: "usgovvirginia"  # or usgovtexas, usgovarizona
azure_compliance_framework: "FedRAMP-High"

# Government-specific endpoints
azure_authority_host: "https://login.microsoftonline.us"
azure_resource_manager_endpoint: "https://management.usgovcloudapi.net/"
```

### Security Best Practices

1. **Enable Azure AD MFA** - Require MFA for all users
2. **Use Managed Identities** - Avoid storing credentials
3. **Enable Just-In-Time Access** - PIM for privileged roles
4. **Network Segmentation** - Use NSGs and Azure Firewall
5. **Enable Microsoft Defender** - For all resource types
6. **Use Azure Policy** - Enforce compliance controls
7. **Enable Azure Sentinel** - SIEM for threat detection
8. **Encrypt Everything** - Keys, secrets, storage, databases
9. **Enable Diagnostic Logs** - Send to Log Analytics
10. **Regular Security Reviews** - Azure Security Center recommendations

## 🔧 Troubleshooting

### Issue: Azure Authentication Failed

**Symptoms:** "Azure credentials not found" or "Authentication failed"

**Resolution:**
```bash
# Verify Azure CLI login
az account show

# Test service principal
az login --service-principal \
  -u $AZURE_CLIENT_ID \
  -p $AZURE_SECRET \
  --tenant $AZURE_TENANT

# Verify with Ansible
ansible localhost -m azure.azcollection.azure_rm_resourcegroup_info \
  -a "name=test-rg"
```

### Issue: Resource Already Exists

**Symptoms:** "Conflict - resource already exists"

**Resolution:**
```bash
# Check existing resources
az resource list --resource-group <rg-name> --output table

# Use ansible idempotency - roles handle existing resources
ansible-playbook playbook.yml  # Safe to re-run
```

### Issue: AKS Cluster Creation Fails

**Symptoms:** AKS deployment stuck or failed

**Resolution:**
```bash
# Check AKS deployment status
az aks show -g <rg-name> -n <cluster-name> --query "provisioningState"

# Review activity log
az monitor activity-log list --resource-group <rg-name> \
  --query "[?contains(operationName.value, 'Microsoft.ContainerService')]"

# Check service principal permissions
az role assignment list --assignee $AZURE_CLIENT_ID
```

## 📚 Additional Resources

- [Azure Documentation](https://docs.microsoft.com/en-us/azure/)
- [Azure Well-Architected Framework](https://docs.microsoft.com/en-us/azure/architecture/framework/)
- [FedRAMP on Azure](https://docs.microsoft.com/en-us/azure/compliance/offerings/offering-fedramp)
- [Azure Government Documentation](https://docs.microsoft.com/en-us/azure/azure-government/)
- [Azure Security Best Practices](https://docs.microsoft.com/en-us/azure/security/fundamentals/best-practices-and-patterns)
- [Ansible Azure Collection](https://docs.ansible.com/ansible/latest/collections/azure/azcollection/)

## 🤝 Contributing

When contributing to Azure automation:
- Test in non-production subscription first
- Follow Azure naming conventions
- Include cost estimates for resources
- Document required Azure permissions
- Include rollback procedures
- Tag all resources appropriately
- Test with both Azure Commercial and Government Cloud

---

**Last Updated:** 2026-01-15
**Maintained By:** Fourth Estate Infrastructure Team
**Azure Clouds Supported:** Commercial + Government (usgovvirginia, usgovtexas, usgovarizona)

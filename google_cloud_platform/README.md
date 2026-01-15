# Google Cloud Platform (GCP)

This directory contains **28 Ansible roles** for managing **Google Cloud Platform** infrastructure with emphasis on security, compliance (FedRAMP, NIST 800-53), and Fourth Estate requirements.

## Overview

Comprehensive GCP automation covering IAM, networking, compute, storage, Kubernetes (GKE), security, compliance, and cost optimization.

## 📋 Role Categories

### Identity & Access Management (6 roles)
- **gcp_iam_organization** - Organization-level IAM policies
- **gcp_iam_projects** - Project IAM management
- **gcp_iam_service_accounts** - Service account lifecycle
- **gcp_iam_workload_identity** - GKE workload identity binding
- **gcp_iam_custom_roles** - Custom role definitions
- **gcp_iam_audit** - IAM audit logging

### Networking (5 roles)
- **gcp_vpc_networks** - VPC network management
- **gcp_vpc_subnets** - Subnet configuration
- **gcp_vpc_firewall** - Firewall rule automation
- **gcp_cloud_nat** - Cloud NAT configuration
- **gcp_cloud_vpn** - VPN tunnel management

### Compute & GKE (6 roles)
- **gcp_gke_clusters** - GKE cluster deployment
- **gcp_gke_security** - GKE security hardening
- **gcp_gke_autopilot** - GKE Autopilot clusters
- **gcp_compute_instances** - VM instance management
- **gcp_instance_groups** - Managed instance groups
- **gcp_gce_images** - Custom image management

### Security & Compliance (6 roles)
- **gcp_security_command_center** - SCC configuration
- **gcp_org_policy** - Organization policy constraints
- **gcp_secret_manager** - Secret management
- **gcp_kms_encryption** - Cloud KMS key management
- **gcp_fedramp_compliance** - FedRAMP baseline controls
- **gcp_nist_compliance** - NIST 800-53 implementation

### Cost & Governance (5 roles)
- **gcp_cost_management** - Cost metrics and budgets
- **gcp_billing_alerts** - Budget alert configuration
- **gcp_resource_quotas** - Quota management
- **gcp_labels_governance** - Resource labeling standards
- **gcp_finops_reporting** - FinOps dashboards

## 🚀 Quick Start

### Prerequisites

- Ansible 2.12.0+
- `google.cloud` collection (version 1.0.0+)
- GCP service account with appropriate permissions
- `gcloud` CLI tool installed

### Installation

```bash
# Install required collections
ansible-galaxy collection install google.cloud

# Install Python dependencies
pip install google-auth google-auth-httplib2 google-api-python-client
```

### Basic Configuration

```yaml
# group_vars/gcp.yml
gcp_project: "fourth-estate-prod"
gcp_auth_kind: "serviceaccount"
gcp_service_account_file: "{{ vault_gcp_sa_file }}"
gcp_region: "us-east1"
gcp_zone: "us-east1-b"
```

## 📖 Common Use Cases

### Deploy Secure GKE Cluster

```bash
ansible-playbook playbooks/gcp_gke_secure_cluster.yml \
  -i inventory/gcp.yml \
  -e "cluster_name=prod-gke-01" \
  -e "enable_private_nodes=true" \
  -e "enable_workload_identity=true"
```

### Apply FedRAMP Controls

```bash
ansible-playbook playbooks/gcp_fedramp_compliance.yml \
  -i inventory/gcp.yml \
  -e "fedramp_level=moderate"
```

### Configure Organization Policies

```bash
ansible-playbook roles/gcp_org_policy/playbook.yml \
  -i inventory/gcp.yml \
  -e "enforce_uniform_bucket_access=true"
```

## 🛡️ Security & Compliance

### FedRAMP Moderate Controls
- **AC-2** - Account Management
- **AC-3** - Access Enforcement
- **AU-2** - Audit Events
- **IA-2** - Identification and Authentication
- **SC-7** - Boundary Protection
- **SC-13** - Cryptographic Protection

### NIST 800-53 Implementation
- VPC Service Controls
- Organization Policy constraints
- Cloud KMS encryption
- Audit logging to Cloud Logging
- Security Command Center monitoring

## 📚 Additional Resources

- [GCP Documentation](https://cloud.google.com/docs)
- [GCP Security Best Practices](https://cloud.google.com/security/best-practices)
- [FedRAMP on GCP](https://cloud.google.com/security/compliance/fedramp)

---

**Last Updated:** 2026-01-15
**Maintained By:** Fourth Estate Infrastructure Team

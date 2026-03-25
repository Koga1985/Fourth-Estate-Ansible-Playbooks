# Google Cloud Platform (GCP)

This directory contains **30 Ansible roles** for managing **Google Cloud Platform** infrastructure with emphasis on security, compliance (FedRAMP, NIST 800-53), and Fourth Estate requirements.

## Overview

Comprehensive GCP automation covering IAM, networking, compute, storage, Kubernetes (GKE), security, compliance, and cost optimization.

## 📋 Role Categories

### Landing Zone & Foundation (2 roles)
- **gcp_landing_zone_dod** - DoD-compliant landing zone setup
- **gcp_assured_workloads_operations** - Assured Workloads configuration for regulated workloads

### Identity & Access Management (4 roles)
- **gcp_iam** - Core IAM policies and bindings
- **gcp_iam_foundations** - IAM foundation controls and constraints
- **gcp_service_accounts_broker** - Service account lifecycle management
- **gcp_sso_directory_sync** - SSO and directory synchronization

### Networking (5 roles)
- **gcp_inventory_baseline** - Network inventory and topology baseline
- **gcp_private_service_connect_fabric** - Private Service Connect configuration
- **gcp_dns_enterprise** - Enterprise DNS configuration
- **gcp_ingress_egress_controls** - Ingress/egress firewall controls
- **gcp_perimeter_protection** - VPC Service Controls perimeter

### Security (4 roles)
- **gcp_cmek_everywhere** - Customer-managed encryption keys (CMEK)
- **gcp_scc_secops_pipeline** - Security Command Center SecOps pipeline
- **gcp_scc_response_playbooks** - SCC automated response playbooks
- **gcp_supply_chain_attestations** - Software supply chain attestations

### GKE (3 roles)
- **gcp_gke_workload_identity_rollout** - GKE workload identity rollout
- **gcp_gke_runtime_policy** - GKE runtime security policy
- **gcp_gke_secure_supplychain** - GKE secure software supply chain

### Logging & Monitoring (3 roles)
- **gcp_logging_routing_tiers** - Log routing and tiered retention
- **gcp_monitoring_sre_baseline** - SRE monitoring baseline
- **gcp_audit_governance_pack** - Audit logging governance pack

### Data Services (4 roles)
- **gcp_storage_governance** - Cloud Storage governance and policies
- **gcp_bigquery_governance** - BigQuery dataset governance
- **gcp_sql_baseline** - Cloud SQL security baseline
- **gcp_pubsub_guardrails** - Pub/Sub guardrails

### Serverless (1 role)
- **gcp_cloudrun_locked_down** - Cloud Run locked-down deployment

### Compliance (2 roles)
- **gcp_nist80053_controls_map** - NIST 800-53 control mappings
- **gcp_quota_safeguards** - Quota safeguards and enforcement

### FinOps & Project (2 roles)
- **gcp_finops_budgets** - FinOps budget alerts and controls
- **gcp_project_management** - Project lifecycle management

## 🚀 Quick Start

### Prerequisites

- Ansible 2.12.0+
- `google.cloud` collection (version 1.2.0+)
- GCP service account with appropriate permissions
- `gcloud` CLI tool installed

### Installation

```bash
# Install required collections
ansible-galaxy collection install -r requirements.yml

# Install Python dependencies
pip install google-auth google-api-python-client google-cloud-storage
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

### Deploy GKE with Secure Supply Chain

```bash
ansible-playbook -i inventory site.yml --tags gke
```

### Apply NIST 800-53 Controls

```bash
ansible-playbook -i inventory site.yml --tags compliance,nist
```

### Configure Landing Zone

```bash
ansible-playbook -i inventory site.yml --tags landing_zone
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

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

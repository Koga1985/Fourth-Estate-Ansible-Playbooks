# Google Cloud Platform (GCP) - Basic

This directory contains **2 Ansible roles** for basic **Google Cloud Platform** automation including project management and IAM configuration.

> **Note:** For comprehensive GCP automation with 28+ roles including landing zones, GKE, security, and compliance, see the `google_cloud_platform/` directory.

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your GCP project details

# 3. Deploy
ansible-playbook -i inventory site.yml
```

### Deployment Options

```bash
# Configure project management
ansible-playbook -i inventory site.yml --tags project

# Configure IAM
ansible-playbook -i inventory site.yml --tags iam
```

## 📋 Roles

- **gcp_project_management** - Project creation and configuration
- **gcp_iam** - IAM roles and service accounts

## ⚙️ Configuration

```yaml
# group_vars/gcp.yml
gcp_project: "fourth-estate-prod"
gcp_region: "us-central1"
gcp_credentials_file: "{{ vault_gcp_credentials_file }}"
```

## Prerequisites

- Ansible 2.12.0+
- `google.cloud` collection
- GCP service account with appropriate permissions
- `google-auth` Python library

---

**Maintained By:** Fourth Estate Infrastructure Team

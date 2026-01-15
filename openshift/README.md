# Red Hat OpenShift Container Platform

This directory contains **45 Ansible roles** for comprehensive **Red Hat OpenShift Container Platform (OCP)** lifecycle management, including cluster deployment, operator management, security hardening, GitOps integration, and NIST 800-53/DoD STIG compliance.

## Overview

The OpenShift automation covers the complete platform lifecycle from initial deployment through day-2 operations, monitoring, compliance, and cost management for **Fourth Estate** organizations.

## 📋 Role Categories

### Cluster Management (12 roles)
- **ocp_cluster_install** - Initial cluster deployment
- **ocp_cluster_upgrade** - Cluster version management
- **ocp_cluster_scaling** - Node scaling and machine sets
- **ocp_cluster_config** - Cluster-wide configuration
- **ocp_node_management** - Node lifecycle and maintenance
- **ocp_etcd_backup** - etcd backup and recovery
- **ocp_certificate_management** - Certificate lifecycle
- **ocp_ingress_config** - Ingress controller configuration
- **ocp_storage_config** - Storage class and PV management
- **ocp_network_policies** - Network segmentation
- **ocp_cluster_monitoring** - Prometheus/Grafana setup
- **ocp_cluster_logging** - EFK/Loki stack configuration

### Security & Compliance (10 roles)
- **ocp_stig_hardening** - DoD STIG compliance automation
- **ocp_nist_compliance** - NIST 800-53 control implementation
- **ocp_rbac_management** - Role-based access control
- **ocp_security_contexts** - Pod security contexts
- **ocp_pod_security_admission** - PSA policy enforcement
- **ocp_oauth_config** - Authentication providers (LDAP, OIDC)
- **ocp_service_accounts** - Service account management
- **ocp_secrets_management** - Secret encryption and rotation
- **ocp_image_scanning** - Container image vulnerability scanning
- **ocp_audit_logging** - Comprehensive audit logging

### Operators & Applications (8 roles)
- **ocp_olm_management** - Operator Lifecycle Manager
- **ocp_operator_install** - Operator deployment automation
- **ocp_catalogsource_config** - Custom catalog sources
- **ocp_subscription_management** - Operator subscriptions
- **ocp_application_deployment** - Application lifecycle
- **ocp_helm_integration** - Helm chart deployment
- **ocp_argocd_gitops** - GitOps with ArgoCD
- **ocp_tekton_pipelines** - CI/CD with Tekton

### Monitoring & Observability (5 roles)
- **ocp_prometheus_config** - Prometheus configuration
- **ocp_grafana_dashboards** - Custom Grafana dashboards
- **ocp_alertmanager_config** - Alert routing and notification
- **ocp_servicemonitor_config** - Application monitoring
- **ocp_distributed_tracing** - Jaeger tracing setup

### Multi-Cluster & DR (5 roles)
- **ocp_multicluster_hub** - Red Hat Advanced Cluster Management
- **ocp_gitops_federation** - Multi-cluster GitOps
- **ocp_disaster_recovery** - Backup and recovery procedures
- **ocp_cluster_federation** - Cluster federation setup
- **ocp_migration_toolkit** - Application migration

### Cost & Resource Management (5 roles)
- **ocp_cost_management** - Cost metrics and reporting
- **ocp_resource_quotas** - Namespace resource limits
- **ocp_limit_ranges** - Container resource constraints
- **ocp_chargeback** - Resource usage tracking
- **ocp_capacity_planning** - Cluster capacity analysis

## 🚀 Quick Start

### Prerequisites

- Ansible 2.12.0 or higher
- `kubernetes.core` collection (version 2.3.0+)
- `redhat.openshift` collection (version 2.2.0+)
- Valid OpenShift cluster or installation environment
- `oc` CLI tool installed
- Kubeconfig with cluster-admin privileges

### Installation

```bash
# Install required collections
ansible-galaxy collection install kubernetes.core
ansible-galaxy collection install redhat.openshift

# Verify collections
ansible-galaxy collection list | grep -E 'kubernetes|openshift'
```

### Basic Configuration

1. **Configure Cluster Connection:**

```yaml
# group_vars/openshift.yml
ocp_cluster_url: "https://api.ocp.example.com:6443"
ocp_username: "{{ vault_ocp_username }}"
ocp_password: "{{ vault_ocp_password }}"
ocp_validate_certs: true

# Or use kubeconfig
ocp_kubeconfig: "~/.kube/config"
ocp_context: "default/api-ocp-example-com:6443/admin"
```

2. **Deploy Cluster Monitoring:**

```bash
# Set up monitoring stack
ansible-playbook playbooks/ocp_cluster_monitoring.yml \
  -i inventory/openshift.yml \
  --ask-vault-pass
```

3. **Apply STIG Hardening:**

```bash
# Apply DoD STIG controls
ansible-playbook playbooks/ocp_stig_hardening.yml \
  -i inventory/openshift.yml \
  -e "apply_changes=true"
```

## 📁 Directory Structure

```text
openshift/
├── README.md                           # This file
├── roles/                              # OpenShift roles (45 total)
│   ├── ocp_cluster_install/
│   ├── ocp_cluster_upgrade/
│   ├── ocp_cluster_scaling/
│   ├── ocp_stig_hardening/
│   ├── ocp_nist_compliance/
│   ├── ocp_rbac_management/
│   ├── ocp_oauth_config/
│   ├── ocp_olm_management/
│   ├── ocp_operator_install/
│   ├── ocp_argocd_gitops/
│   ├── ocp_tekton_pipelines/
│   ├── ocp_prometheus_config/
│   ├── ocp_cost_management/
│   └── [32 more roles...]
└── tasks/                              # Standalone task files
    ├── ocp_olm__subscriptions_lifecycle.yml
    └── [other tasks...]
```

## 🔑 Key Features

### STIG Compliance (DoD Requirements)
- **STIGv1R1** implementation for OpenShift 4.x
- Automated finding remediation
- Compliance artifact generation
- Category I/II/III control mapping

### NIST 800-53 Rev 5 Controls
- **AC Family** - Access control policies
- **AU Family** - Audit logging and monitoring
- **IA Family** - Authentication and authorization
- **SC Family** - Encryption and communications protection
- **CM Family** - Configuration management

### GitOps Integration
- **ArgoCD** - Declarative continuous delivery
- **Tekton** - Cloud-native CI/CD pipelines
- **OpenShift GitOps Operator** - Red Hat supported GitOps
- **Multi-cluster deployment** - Hub and spoke architecture

### Multi-Tenancy
- **Namespace isolation** - Strong tenant separation
- **Resource quotas** - Fair resource allocation
- **Network policies** - Microsegmentation
- **RBAC** - Fine-grained access control

### Enterprise Monitoring
- **Prometheus** - Metrics collection
- **Grafana** - Visualization dashboards
- **Alertmanager** - Alert routing and notification
- **EFK/Loki** - Centralized logging

## 📖 Common Use Cases

### Use Case 1: Deploy Production Cluster with STIG Hardening

```yaml
---
# playbook_production_cluster.yml
- name: Deploy Production OpenShift Cluster
  hosts: localhost
  connection: local

  tasks:
    - name: Install OpenShift cluster
      include_role:
        name: ocp_cluster_install
      vars:
        ocp_version: "4.14"
        ocp_install_type: "ipi"  # or upi

    - name: Apply STIG hardening
      include_role:
        name: ocp_stig_hardening
      vars:
        stig_profile: "high"

    - name: Configure monitoring
      include_role:
        name: ocp_cluster_monitoring

    - name: Set up GitOps
      include_role:
        name: ocp_argocd_gitops
```

### Use Case 2: Configure OAuth with LDAP

```bash
# Configure LDAP authentication
ansible-playbook playbooks/ocp_oauth_config.yml \
  -i inventory/openshift.yml \
  -e "oauth_provider=ldap" \
  -e "ldap_url=ldaps://ldap.example.com" \
  --ask-vault-pass
```

### Use Case 3: Deploy Operator via OLM

```bash
# Install cert-manager operator
ansible-playbook playbooks/ocp_operator_install.yml \
  -i inventory/openshift.yml \
  -e "operator_name=cert-manager" \
  -e "operator_channel=stable"
```

### Use Case 4: Multi-Cluster GitOps Setup

```bash
# Configure Red Hat Advanced Cluster Management
ansible-playbook playbooks/ocp_multicluster_hub.yml \
  -i inventory/openshift.yml

# Deploy applications to multiple clusters
ansible-playbook playbooks/ocp_gitops_federation.yml \
  -i inventory/openshift.yml \
  -e "target_clusters=prod-east,prod-west"
```

## ⚙️ Configuration Variables

### Cluster Configuration

```yaml
# Cluster details
ocp_cluster_name: "prod-ocp"
ocp_base_domain: "example.com"
ocp_cluster_url: "https://api.prod-ocp.example.com:6443"

# Authentication
ocp_kubeconfig: "{{ ansible_env.HOME }}/.kube/config"
ocp_context: "default/api-prod-ocp:6443/kube:admin"

# Or use credentials
ocp_username: "{{ vault_ocp_admin }}"
ocp_password: "{{ vault_ocp_password }}"
ocp_validate_certs: true
```

### STIG Hardening

```yaml
# STIG configuration
ocp_stig_profile: "high"  # low, moderate, high
ocp_stig_cat1_enabled: true
ocp_stig_cat2_enabled: true
ocp_stig_cat3_enabled: false
ocp_stig_exceptions: []  # List of STIG IDs to skip
```

### RBAC Configuration

```yaml
ocp_rbac_users:
  - username: "john.doe"
    groups:
      - "cluster-admins"
      - "monitoring-viewers"

ocp_rbac_groups:
  - name: "fourth-estate-devs"
    cluster_roles:
      - "edit"
    namespaces:
      - "development"
      - "staging"
```

### Monitoring Configuration

```yaml
# Prometheus retention
ocp_prometheus_retention: "7d"
ocp_prometheus_storage_size: "100Gi"

# Alertmanager
ocp_alertmanager_config:
  receivers:
    - name: "fourth-estate-ops"
      email_configs:
        - to: "ops@example.com"
      pagerduty_configs:
        - service_key: "{{ vault_pagerduty_key }}"
```

## 🛡️ Security & Compliance

### DoD STIG Findings Coverage

| Category | Total Findings | Automated | Manual | Not Applicable |
|----------|----------------|-----------|---------|----------------|
| **Cat I (High)** | 15 | 12 | 3 | 0 |
| **Cat II (Medium)** | 45 | 38 | 5 | 2 |
| **Cat III (Low)** | 18 | 15 | 2 | 1 |
| **Total** | 78 | 65 | 10 | 3 |

### NIST 800-53 Control Families

- **AC-2** - Account Management (automated)
- **AC-3** - Access Enforcement (automated)
- **AC-6** - Least Privilege (automated)
- **AU-2** - Audit Events (automated)
- **AU-9** - Protection of Audit Information (automated)
- **IA-2** - Identification and Authentication (automated)
- **IA-5** - Authenticator Management (automated)
- **SC-7** - Boundary Protection (automated)
- **SC-8** - Transmission Confidentiality (automated)
- **SC-13** - Cryptographic Protection (automated)

### Compliance Verification

```bash
# Generate STIG compliance report
ansible-playbook playbooks/ocp_stig_hardening.yml \
  -i inventory/openshift.yml \
  --tags verify_only \
  -e "report_format=html"

# Verify NIST controls
ansible-playbook playbooks/ocp_nist_compliance.yml \
  -i inventory/openshift.yml \
  --tags nist_verify
```

## 🔧 Troubleshooting

### Issue: Cluster Upgrade Stuck

**Symptoms:** Cluster upgrade not progressing

**Resolution:**
```bash
# Check cluster operators
oc get clusteroperators

# Check for degraded operators
oc get co | grep -v "True.*False.*False"

# Review operator logs
oc logs -n openshift-cluster-version deployment/cluster-version-operator
```

### Issue: Pod Security Admission Violations

**Symptoms:** Pods failing to start with PSA errors

**Resolution:**
```bash
# Check PSA violations
oc get events -n <namespace> | grep -i "violation"

# Adjust namespace PSA labels
oc label namespace <namespace> \
  pod-security.kubernetes.io/enforce=baseline \
  pod-security.kubernetes.io/audit=restricted \
  pod-security.kubernetes.io/warn=restricted
```

### Issue: GitOps Sync Failures

**Symptoms:** ArgoCD applications out of sync

**Resolution:**
```bash
# Check ArgoCD application status
oc get applications -n openshift-gitops

# Force sync
oc patch application <app-name> -n openshift-gitops \
  --type merge -p '{"operation":{"initiatedBy":{"username":"admin"},"sync":{"syncStrategy":{"hook":{}}}}}'
```

## 📚 Additional Resources

- [OpenShift Documentation](https://docs.openshift.com/)
- [OpenShift STIG Guide](https://www.stigviewer.com/stig/red_hat_openshift_container_platform_4/)
- [Red Hat Advanced Cluster Management](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/)
- [OpenShift GitOps](https://docs.openshift.com/container-platform/latest/cicd/gitops/understanding-openshift-gitops.html)
- [Tekton Pipelines](https://tekton.dev/docs/)

## 🤝 Contributing

When contributing to OpenShift automation:
- Test against OpenShift 4.12+ (supported versions)
- Follow Kubernetes/OpenShift naming conventions
- Include RBAC requirements in role documentation
- Test with both cluster-admin and limited privileges
- Document compliance control mappings (STIG/NIST)
- Include rollback procedures for breaking changes

---

**Last Updated:** 2026-01-15
**Maintained By:** Fourth Estate Infrastructure Team
**OpenShift Versions Supported:** 4.12, 4.13, 4.14, 4.15

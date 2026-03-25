# Red Hat OpenShift Container Platform

This directory contains **45 Ansible roles** for comprehensive **Red Hat OpenShift Container Platform (OCP)** lifecycle management, including cluster deployment, operator management, security hardening, GitOps integration, and NIST 800-53/DoD STIG compliance.

## Overview

The OpenShift automation covers the complete platform lifecycle from initial deployment through day-2 operations, monitoring, compliance, and cost management for **Fourth Estate** organizations.

## 📋 Role Categories

### Cluster Lifecycle (6 roles)
- **ocp_upgrade_channel** - Cluster upgrade channel management
- **ocp_machine_configs** - MachineConfig and node configuration
- **ocp_node_tuning** - Node tuning and performance
- **ocp_autoscaling** - Cluster autoscaling configuration
- **ocp_hpa_vpa_autoscaling** - HPA/VPA workload autoscaling
- **ocp_maintenance_windows** - Maintenance window management

### Security & Identity (9 roles)
- **ocp_rbac_baseline** - RBAC baseline configuration
- **ocp_group_sync** - LDAP group synchronization
- **ocp_sso_tuning** - SSO and authentication tuning
- **ocp_psa_enforce** - Pod Security Admission enforcement
- **ocp_scc_legacy_mgmt** - Legacy SecurityContextConstraints management
- **ocp_secrets_management** - Secret encryption and rotation
- **ocp_gatekeeper_policies** - OPA/Gatekeeper policy enforcement
- **ocp_cert_manager_operator** - Certificate Manager operator
- **ocp_icsp_mirroring** - Image Content Source Policy and mirroring

### Registry & Images (3 roles)
- **ocp_internal_registry** - Internal container registry management
- **ocp_quay_external_registry** - Quay external registry integration
- **ocp_image_signing_policy** - Image signing and verification policy

### Networking (5 roles)
- **ocp_network_policies_baseline** - Network policy baseline
- **ocp_routes_tls_policy** - Route TLS policy enforcement
- **ocp_proxy_trust_bundle** - Proxy configuration and trust bundle
- **ocp_service_mesh** - Service mesh (OpenShift Service Mesh)
- **ocp_multicluster_services** - Multi-cluster service federation

### Storage (4 roles)
- **ocp_storage_classes** - Storage class management
- **ocp_csi_operators** - CSI driver operator management
- **ocp_odf_baseline** - OpenShift Data Foundation baseline
- **ocp_snapshot_policies** - Volume snapshot policies

### Observability (4 roles)
- **ocp_monitoring_user_workloads** - User workload monitoring
- **ocp_log_forwarding** - Log forwarding configuration
- **ocp_events_exporter** - Kubernetes events exporter
- **ocp_audit_config** - API audit logging configuration

### GitOps & CI/CD (3 roles)
- **ocp_argocd_gitops** - GitOps with ArgoCD/OpenShift GitOps
- **ocp_pipelines_tekton** - CI/CD with Tekton Pipelines
- **ocp_build_configs** - BuildConfig management

### Multi-Cluster (ACM) (3 roles)
- **ocp_acm_hub** - ACM hub cluster setup
- **ocp_acm_cluster_sets** - ACM cluster sets management
- **ocp_acm_governance** - ACM governance policies

### Resource & Namespace Management (4 roles)
- **ocp_namespace_blueprints** - Namespace blueprint templates
- **ocp_resource_quotas_limits** - Resource quotas and limit ranges
- **ocp_project_request_template** - Project request template
- **ocp_labels_annotations** - Labels and annotations standards

### Operations & Compliance (4 roles)
- **ocp_preflight_drift_report** - Preflight checks and drift reporting
- **ocp_operands_lifecycle** - Operand lifecycle management
- **ocp_cost_management** - Cost management and reporting
- **ocp_serverless_knative** - Serverless/Knative configuration

## 🚀 Quick Start (Drop-In Deployment)

This platform supports **drop-in deployment**. Get started in 3 steps:

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your OpenShift cluster details

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

Use tags to deploy specific components:

```bash
# Deploy only RBAC configuration
ansible-playbook -i inventory site.yml --tags rbac

# Deploy only network policies
ansible-playbook -i inventory site.yml --tags network

# Deploy only security/PSA settings
ansible-playbook -i inventory site.yml --tags security

# Deploy GitOps (ArgoCD)
ansible-playbook -i inventory site.yml --tags gitops

# Deploy compliance (Gatekeeper)
ansible-playbook -i inventory site.yml --tags compliance
```

### Prerequisites

- Ansible 2.12.0 or higher
- `kubernetes.core` collection (version 2.3.0+)
- `redhat.openshift` collection (version 2.2.0+)
- Valid OpenShift cluster or installation environment
- `oc` CLI tool installed
- Kubeconfig with cluster-admin privileges

### Manual Installation (Alternative)

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
# Set up user workload monitoring
ansible-playbook -i inventory site.yml --tags monitoring
```

3. **Apply Policy Enforcement:**

```bash
# Apply Gatekeeper/PSA controls
ansible-playbook -i inventory site.yml --tags security,compliance
```

## 📁 Directory Structure

```text
openshift/
├── README.md                           # This file
├── roles/                              # OpenShift roles (45 total)
│   ├── ocp_upgrade_channel/
│   ├── ocp_machine_configs/
│   ├── ocp_rbac_baseline/
│   ├── ocp_group_sync/
│   ├── ocp_psa_enforce/
│   ├── ocp_gatekeeper_policies/
│   ├── ocp_network_policies_baseline/
│   ├── ocp_argocd_gitops/
│   ├── ocp_pipelines_tekton/
│   ├── ocp_acm_hub/
│   ├── ocp_acm_cluster_sets/
│   ├── ocp_acm_governance/
│   ├── ocp_cost_management/
│   └── [32 more roles...]
└── tasks/                              # Standalone task files
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

### Use Case 1: Configure RBAC and Policy Enforcement

```yaml
---
# playbook_security_baseline.yml
- name: Apply OpenShift Security Baseline
  hosts: localhost
  connection: local

  tasks:
    - name: Configure RBAC baseline
      include_role:
        name: ocp_rbac_baseline

    - name: Enforce Pod Security Admission
      include_role:
        name: ocp_psa_enforce

    - name: Apply Gatekeeper policies
      include_role:
        name: ocp_gatekeeper_policies

    - name: Set up GitOps
      include_role:
        name: ocp_argocd_gitops
```

### Use Case 2: Configure Group Sync and SSO

```bash
# Configure LDAP group sync
ansible-playbook -i inventory site.yml --tags group_sync
```

### Use Case 3: Configure GitOps and Pipelines

```bash
# Deploy ArgoCD and Tekton
ansible-playbook -i inventory site.yml --tags gitops
```

### Use Case 4: Multi-Cluster with ACM

```bash
# Configure Red Hat Advanced Cluster Management
ansible-playbook -i inventory site.yml --tags acm
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
# Run preflight checks and drift report
ansible-playbook -i inventory site.yml --tags preflight

# Run Gatekeeper policy compliance check
ansible-playbook -i inventory site.yml --tags compliance
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

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team
**OpenShift Versions Supported:** 4.12, 4.13, 4.14, 4.15

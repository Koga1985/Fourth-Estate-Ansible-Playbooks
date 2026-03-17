# OpenShift Roles

This directory contains **45 Ansible roles** for Red Hat OpenShift Container Platform (OCP) day-2 operations, covering cluster configuration, security hardening, GitOps, monitoring, multi-cluster management, storage, and compliance.

## Roles

### Advanced Cluster Management (ACM)

| Role | Description |
|------|-------------|
| **ocp_acm_hub** | Installs and configures the Red Hat Advanced Cluster Management (RHACM) hub operator, including MultiClusterHub CR and initial configuration. |
| **ocp_acm_cluster_sets** | Defines ACM ManagedClusterSets, placements, and placement decisions for multi-cluster policy targeting. |
| **ocp_acm_governance** | Applies ACM governance policies (ConfigurationPolicy, CertificatePolicy) and remediates findings across managed clusters. |

### GitOps and CI/CD

| Role | Description |
|------|-------------|
| **ocp_argocd_gitops** | Installs the OpenShift GitOps operator, configures ArgoCD instances, and bootstraps Application and ApplicationSet resources. |
| **ocp_pipelines_tekton** | Installs the OpenShift Pipelines operator and applies Tekton Pipeline, Task, and TriggerTemplate resources. |
| **ocp_build_configs** | Manages OpenShift BuildConfig resources for S2I and Dockerfile-based image builds. |

### Security and Compliance

| Role | Description |
|------|-------------|
| **ocp_audit_config** | Configures the cluster audit policy profile and forwards audit logs to external collectors via ClusterLogForwarder. |
| **ocp_gatekeeper_policies** | Deploys OPA Gatekeeper ConstraintTemplates and Constraint objects to enforce policy as code across namespaces. |
| **ocp_psa_enforce** | Applies Pod Security Admission labels to namespaces to enforce baseline or restricted pod security standards. |
| **ocp_scc_legacy_mgmt** | Audits and remediates legacy SecurityContextConstraint role bindings during PSA migration. |
| **ocp_rbac_baseline** | Bootstraps cluster-level and namespace-level RBAC: ClusterRoles, RoleBindings, and service account grants. |
| **ocp_image_signing_policy** | Configures image signature verification policies and trusted registries via ImageContentSourcePolicy and cluster-wide signing configuration. |
| **ocp_secrets_management** | Deploys sealed secrets or integrates an external secrets operator for secrets injection from Vault or AWS Secrets Manager. |
| **ocp_network_policies_baseline** | Applies a baseline set of Kubernetes NetworkPolicy objects providing default-deny and selective allow rules per namespace. |

### Monitoring and Observability

| Role | Description |
|------|-------------|
| **ocp_monitoring_user_workloads** | Enables user workload monitoring, configures Prometheus retention and storage, and deploys custom PrometheusRules and Alertmanager routes. |
| **ocp_events_exporter** | Deploys a Kubernetes events exporter to forward cluster events to external observability platforms. |
| **ocp_log_forwarding** | Configures the OpenShift Logging ClusterLogForwarder to route container, audit, and infrastructure logs to Splunk, Elasticsearch, or syslog targets. |

### Operators and Lifecycle

| Role | Description |
|------|-------------|
| **ocp_operands_lifecycle** | Manages OLM Subscription and OperatorGroup objects, controlling operator installation, update channel, and approval strategy. |
| **ocp_cert_manager_operator** | Installs the cert-manager operator and configures ClusterIssuer or Issuer objects for certificate lifecycle management. |
| **ocp_csi_operators** | Installs and configures CSI driver operators (e.g., AWS EBS, vSphere, ODF) with StorageClass creation. |
| **ocp_serverless_knative** | Installs the OpenShift Serverless operator and configures KnativeServing and KnativeEventing instances with custom domain mapping. |
| **ocp_service_mesh** | Installs the OpenShift Service Mesh operator and configures ServiceMeshControlPlane with mTLS policies and member rolls. |

### Cluster Configuration

| Role | Description |
|------|-------------|
| **ocp_machine_configs** | Applies MachineConfig snippets for node-level OS customization, managing rollout via MachineConfigPool. |
| **ocp_node_tuning** | Deploys TuningProfile resources via the Node Tuning Operator for kernel parameter and ulimit adjustments. |
| **ocp_autoscaling** | Configures ClusterAutoscaler and MachineAutoscaler resources for dynamic node scaling. |
| **ocp_hpa_vpa_autoscaling** | Deploys HorizontalPodAutoscaler and VerticalPodAutoscaler objects for workload-level scaling. |
| **ocp_upgrade_channel** | Sets the cluster update channel, pauses or resumes the upgrade, and runs pre-flight health checks before version transitions. |
| **ocp_maintenance_windows** | Creates PodDisruptionBudgets and annotates nodes for maintenance scheduling coordination. |
| **ocp_proxy_trust_bundle** | Configures cluster-wide proxy settings and distributes custom CA trust bundles via ConfigMap injection. |
| **ocp_sso_tuning** | Tunes OAuth server configuration including session token lifetimes and identity provider settings. |

### Namespace and Workload Management

| Role | Description |
|------|-------------|
| **ocp_namespace_blueprints** | Applies a namespace blueprint (ResourceQuota, LimitRange, NetworkPolicy, RBAC, labels) from a reusable template. |
| **ocp_project_request_template** | Installs a custom ProjectRequestTemplate that stamps every new project with a baseline set of resources. |
| **ocp_resource_quotas_limits** | Manages ResourceQuota and LimitRange objects across namespaces defined in a quota catalog. |
| **ocp_labels_annotations** | Applies label and annotation sets to nodes, namespaces, or workloads from a fleet-wide definition. |
| **ocp_group_sync** | Deploys the Group Sync operator and configures LDAP group synchronization schedules. |

### Storage

| Role | Description |
|------|-------------|
| **ocp_odf_baseline** | Deploys OpenShift Data Foundation (ODF) with StorageCluster creation and StorageClass defaults. |
| **ocp_storage_classes** | Manages StorageClass objects, default annotations, and volume binding mode settings. |
| **ocp_snapshot_policies** | Creates VolumeSnapshotClass objects and schedules snapshot jobs for persistent volume protection. |
| **ocp_internal_registry** | Configures the OpenShift internal image registry, sets storage backend, and enables pruning jobs. |
| **ocp_icsp_mirroring** | Manages ImageContentSourcePolicy resources for disconnected or air-gapped registry mirroring. |
| **ocp_quay_external_registry** | Integrates an external Quay registry with cluster pull-secret updates and robot account setup. |

### Cost and Governance

| Role | Description |
|------|-------------|
| **ocp_cost_management** | Configures the Cost Management metrics operator and applies label rules for showback and chargeback reporting. |
| **ocp_routes_tls_policy** | Enforces TLS edge or re-encrypt termination on OpenShift Routes and applies ingress-level TLS policies. |
| **ocp_multicluster_services** | Configures ServiceExport and ServiceImport objects for cross-cluster service discovery via Submariner or RHACM. |
| **ocp_preflight_drift_report** | Runs a pre-execution drift check comparing current cluster state to the desired state manifest and emits a diff report. |

## Requirements

- Ansible 2.12+
- `kubernetes.core` collection (2.3.0+)
- `redhat.openshift` collection (2.2.0+)
- Valid kubeconfig with cluster-admin privileges or equivalent RBAC
- OpenShift 4.12 or later

```bash
ansible-galaxy collection install kubernetes.core redhat.openshift
```

## Quick Start

```bash
ansible-playbook -i inventory site.yml \
  --tags rbac,network,monitoring \
  --ask-vault-pass
```

## Example Playbook

```yaml
---
- name: Apply OpenShift day-2 baseline
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    ocp_kubeconfig: "{{ lookup('env', 'KUBECONFIG') }}"

  roles:
    - role: openshift/roles/ocp_rbac_baseline
    - role: openshift/roles/ocp_network_policies_baseline
    - role: openshift/roles/ocp_monitoring_user_workloads
    - role: openshift/roles/ocp_audit_config
```

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team
**OpenShift Versions Supported:** 4.12, 4.13, 4.14, 4.15

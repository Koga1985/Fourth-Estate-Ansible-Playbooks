# OpenShift Tasks

This directory contains **70+ standalone task files** for OpenShift Container Platform operations. These files can be included in any playbook with `ansible.builtin.include_tasks` for granular day-2 cluster management without requiring the full role structure.

## Task Files by Category

### ACM (Advanced Cluster Management)
| File | Description |
|------|-------------|
| `ocp_acm__clustersets_placements.yml` | Creates or updates ACM ManagedClusterSets and Placement resources. |
| `ocp_acm__governance_apply.yml` | Applies ACM governance policies to managed clusters. |
| `ocp_acm__hub_install.yml` | Installs the RHACM operator and creates the MultiClusterHub CR. |

### ArgoCD / GitOps
| File | Description |
|------|-------------|
| `ocp_argocd__apps_and_appsets.yml` | Creates or syncs ArgoCD Application and ApplicationSet resources. |
| `ocp_argocd__install_and_bootstrap.yml` | Installs the OpenShift GitOps operator and configures the initial ArgoCD instance. |

### Audit and Compliance
| File | Description |
|------|-------------|
| `ocp_audit__policy_and_forward.yml` | Sets the cluster audit policy profile and configures ClusterLogForwarder for audit log export. |
| `ocp_preflight__drift_report.yml` | Compares current cluster state to desired state and emits a drift report artifact. |

### Autoscaling
| File | Description |
|------|-------------|
| `ocp_autoscale__hpa_vpa.yml` | Applies HPA and VPA objects from a workload autoscaling catalog. |
| `ocp_autoscaling__cluster_and_machines.yml` | Configures ClusterAutoscaler and MachineAutoscaler for node-level scaling. |

### Backup
| File | Description |
|------|-------------|
| `ocp_backup__etcd_snapshots.yml` | Triggers etcd snapshot backup on the control-plane nodes. |
| `ocp_backup__oadp_baseline.yml` | Configures the OADP (OpenShift API for Data Protection) operator with a Velero backup location. |

### Build and Registry
| File | Description |
|------|-------------|
| `ocp_build__configs_apply.yml` | Applies BuildConfig manifests from a directory. |
| `ocp_icsp__apply_policies.yml` | Applies ImageContentSourcePolicy resources for registry mirroring. |
| `ocp_images__signature_policy.yml` | Configures cluster-wide image signature verification. |
| `ocp_registry__internal_config.yml` | Configures the internal image registry storage backend and availability. |
| `ocp_registry__prune_jobs.yml` | Creates CronJobs for scheduled image pruning in the internal registry. |
| `ocp_quay__operator_and_registry.yml` | Installs the Quay operator and creates a QuayRegistry instance. |
| `ocp_quay__orgs_robots_replication.yml` | Manages Quay organizations, robot accounts, and replication targets. |

### Certificates
| File | Description |
|------|-------------|
| `ocp_cert_manager__install.yml` | Installs the cert-manager operator via OLM. |
| `ocp_cert_manager__issuers.yml` | Creates ClusterIssuer or Issuer objects for certificate provisioning. |

### Cost Management
| File | Description |
|------|-------------|
| `ocp_cost__labels_and_rules.yml` | Applies cost-management label rules and project metadata for chargeback. |

### CSI and Storage
| File | Description |
|------|-------------|
| `ocp_csi__install_operator.yml` | Installs a named CSI driver operator via OLM subscription. |
| `ocp_odf__deploy_basics.yml` | Deploys OpenShift Data Foundation with a minimal StorageCluster. |
| `ocp_sc__apply.yml` | Creates or updates StorageClass objects from a catalog definition. |
| `ocp_snapshot__classes.yml` | Creates VolumeSnapshotClass objects for CSI snapshot support. |
| `ocp_snapshot__schedules.yml` | Creates recurring snapshot schedule jobs for selected PVCs. |

### Events
| File | Description |
|------|-------------|
| `ocp_events__export_pipeline.yml` | Deploys a Kubernetes events exporter and configures its output pipeline. |

### Gatekeeper
| File | Description |
|------|-------------|
| `ocp_gatekeeper__constraints_apply.yml` | Applies OPA Gatekeeper ConstraintTemplate and Constraint objects. |

### Group Sync
| File | Description |
|------|-------------|
| `ocp_groupsync__deploy.yml` | Deploys the Group Sync operator and configures an LDAP GroupSync schedule. |

### Labels and Annotations
| File | Description |
|------|-------------|
| `ocp_labels__fleet_apply.yml` | Applies label and annotation sets to nodes, namespaces, or workloads fleet-wide. |

### Logging
| File | Description |
|------|-------------|
| `ocp_logging__clf_apply.yml` | Applies a ClusterLogForwarder configuration to route logs to external targets. |

### Machine Config
| File | Description |
|------|-------------|
| `ocp_machineconfig__apply_snippets.yml` | Renders and applies MachineConfig snippets, managing MachineConfigPool rollout. |

### Maintenance
| File | Description |
|------|-------------|
| `ocp_maintenance__freeze_and_pdb.yml` | Applies PodDisruptionBudgets and cordons nodes for scheduled maintenance windows. |

### Monitoring
| File | Description |
|------|-------------|
| `ocp_monitoring__alertmanager_routes.yml` | Configures Alertmanager routing rules and receiver definitions. |
| `ocp_monitoring__enable_uwm.yml` | Enables user workload monitoring in the cluster monitoring stack. |
| `ocp_monitoring__prom_rules.yml` | Applies PrometheusRule objects for custom alerting conditions. |

### Namespace Management
| File | Description |
|------|-------------|
| `ocp_namespace__blueprint_apply.yml` | Stamps a namespace with the full blueprint (quota, limits, netpol, RBAC). |
| `ocp_projectreq__template_apply.yml` | Installs a custom ProjectRequestTemplate for new project bootstrapping. |
| `ocp_quota__apply_namespace_sets.yml` | Applies ResourceQuota and LimitRange objects to a list of namespaces. |

### Network Policy
| File | Description |
|------|-------------|
| `ocp_netpol__baseline.yml` | Applies the baseline default-deny and selective-allow NetworkPolicy set. |

### Node Management
| File | Description |
|------|-------------|
| `ocp_nodes__label_taint.yml` | Applies labels and taints to nodes based on a node role catalog. |

### OAuth and Identity
| File | Description |
|------|-------------|
| `ocp_oauth__providers_and_tokens.yml` | Configures OAuth identity providers and manages service account token settings. |

### OLM Operators
| File | Description |
|------|-------------|
| `ocp_olm__subscriptions_lifecycle.yml` | Manages OLM Subscription and OperatorGroup lifecycle (create, update channel, approval). |
| `ocp_wait__operators_ready.yml` | Waits for all Subscription-managed operators to report Succeeded status. |
| `ocp_wait__resources_applied.yml` | Polls until specified Kubernetes resources reach a ready state. |

### Pod Security
| File | Description |
|------|-------------|
| `ocp_psa__enforce_labels.yml` | Applies Pod Security Admission labels (enforce/audit/warn) to namespaces. |
| `ocp_scc__rolebindings_curate.yml` | Audits and cleans up over-permissive SCC role bindings. |

### Proxy and Trust
| File | Description |
|------|-------------|
| `ocp_proxy__cluster_wide.yml` | Applies cluster-wide proxy configuration and trust bundle ConfigMap injection. |
| `ocp_trust__user_ca_bundle.yml` | Distributes custom CA certificates to the cluster trust bundle. |

### RBAC
| File | Description |
|------|-------------|
| `ocp_rbac__bootstrap.yml` | Creates foundational ClusterRoles, RoleBindings, and service account permissions. |

### Reports and Exports
| File | Description |
|------|-------------|
| `ocp_report__export_csv.yml` | Exports cluster resource inventory to CSV for asset management or auditing. |

### Routes and TLS
| File | Description |
|------|-------------|
| `ocp_routes__tls_policy.yml` | Enforces TLS termination settings on OpenShift Routes. |

### Secrets
| File | Description |
|------|-------------|
| `ocp_secrets__sealed_or_external.yml` | Creates SealedSecret or ExternalSecret objects depending on the active secrets backend. |

### Serverless
| File | Description |
|------|-------------|
| `ocp_serverless__domain_mapping.yml` | Creates custom domain mappings for Knative Services. |
| `ocp_serverless__install.yml` | Installs the OpenShift Serverless operator and configures KnativeServing. |

### Service Mesh
| File | Description |
|------|-------------|
| `ocp_servicemesh__install.yml` | Installs the OpenShift Service Mesh operator and creates a ServiceMeshControlPlane. |
| `ocp_servicemesh__mtls_policies.yml` | Applies PeerAuthentication and DestinationRule resources to enforce mTLS. |

### Upgrade
| File | Description |
|------|-------------|
| `ocp_upgrade__channel_pause.yml` | Sets the cluster update channel or pauses the upgrade process. |
| `ocp_upgrade__preflight_health.yml` | Validates cluster health and operator readiness before initiating an upgrade. |

### Utility
| File | Description |
|------|-------------|
| `ocp_artifacts__ensure_dirs.yml` | Creates the local artifacts directory for report and export output. |
| `ocp_data__load_from_yaml.yml` | Loads variable data from YAML files into the playbook fact space. |
| `ocp_mcs__export_import.yml` | Exports or imports MachineConfig objects for cross-cluster configuration portability. |

## Usage

```yaml
---
- name: OpenShift day-2 operations
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    ocp_kubeconfig: "{{ lookup('env', 'KUBECONFIG') }}"

  tasks:
    - name: Enable user workload monitoring
      ansible.builtin.include_tasks: openshift/tasks/ocp_monitoring__enable_uwm.yml

    - name: Apply namespace blueprints
      ansible.builtin.include_tasks: openshift/tasks/ocp_namespace__blueprint_apply.yml
      vars:
        namespace_blueprints: "{{ namespaces }}"
```

## Requirements

- Ansible 2.12+
- `kubernetes.core` and `redhat.openshift` collections
- Valid kubeconfig in scope (`KUBECONFIG` env var or `ocp_kubeconfig` variable)
- OpenShift 4.12+

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

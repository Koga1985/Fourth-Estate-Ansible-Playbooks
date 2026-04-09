# ocp_audit_config

Configures the OpenShift API Server and OVN audit policy, log retention, and log forwarding. Implements NIST 800-53 AU-2/AU-9/AU-12 and DISA STIG audit logging requirements for OpenShift clusters.

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core` (`ansible-galaxy collection install kubernetes.core`)
- `KUBECONFIG` environment variable set, or kubeconfig at `~/.kube/config`
- Cluster-admin privileges

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `kubeconfig` | `$KUBECONFIG` or `~/.kube/config` | No | Path to kubeconfig file |
| `context` | `""` | No | kubeconfig context to use; empty uses the current context |
| `namespace` | `"openshift-config"` | No | Namespace where audit ConfigMaps are applied |
| `apply_wait` | `true` | No | Wait for APIServer rollout after applying audit policy |
| `artifacts_dir` | `"/tmp/ocp-artifacts"` | No | Directory for generated manifests and reports |
| `apiserver_audit_policy_cm` | `{}` | No | Full `ConfigMap` manifest for the APIServer audit policy (applied to `openshift-config`) |
| `audit_forward_config` | `{}` | No | `ClusterLogForwarder` or equivalent manifest for forwarding audit logs to an external SIEM |

### `apiserver_audit_policy_cm` structure

Provide a complete ConfigMap manifest. The `data.policy` key must contain a valid Kubernetes audit policy YAML:

```yaml
apiserver_audit_policy_cm:
  apiVersion: v1
  kind: ConfigMap
  metadata:
    name: audit-policy
    namespace: openshift-config
  data:
    policy: |
      apiVersion: audit.k8s.io/v1
      kind: Policy
      rules:
        - level: RequestResponse
          resources:
            - group: ""
              resources: ["secrets", "configmaps"]
        - level: Metadata
```

### `audit_forward_config` structure

Provide a `ClusterLogForwarder` manifest targeting your SIEM:

```yaml
audit_forward_config:
  apiVersion: logging.openshift.io/v1
  kind: ClusterLogForwarder
  metadata:
    name: instance
    namespace: openshift-logging
  spec:
    outputs:
      - name: splunk-audit
        type: splunk
        url: "https://splunk.agency.gov:8088"
    pipelines:
      - name: audit-to-splunk
        inputRefs: [audit]
        outputRefs: [splunk-audit]
```

## Example Playbook

```yaml
- name: Configure OCP audit policy and log forwarding
  hosts: localhost
  gather_facts: false
  roles:
    - role: openshift/roles/ocp_audit_config
      vars:
        namespace: openshift-config
        apiserver_audit_policy_cm:
          apiVersion: v1
          kind: ConfigMap
          metadata:
            name: audit-policy
            namespace: openshift-config
          data:
            policy: |
              apiVersion: audit.k8s.io/v1
              kind: Policy
              rules:
                - level: RequestResponse
```

## Tags

| Tag | Description |
|-----|-------------|
| `audit-policy` | Apply APIServer audit policy ConfigMap |
| `log-forward` | Apply log forwarding configuration |

## Compliance Controls

| Framework | Control ID | Description |
|-----------|-----------|-------------|
| NIST 800-53 | AU-2 | Audit Events |
| NIST 800-53 | AU-9 | Protection of Audit Information |
| NIST 800-53 | AU-12 | Audit Record Generation |

## Notes

- Applying a new audit policy triggers an APIServer rollout; expect brief API unavailability.
- `apply_wait: true` blocks until the rollout completes. Set to `false` for non-blocking runs.
- Both `apiserver_audit_policy_cm` and `audit_forward_config` default to empty (`{}`); providing neither makes this role a no-op.

## License

MIT

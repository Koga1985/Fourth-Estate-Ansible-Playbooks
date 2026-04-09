# ocp_hpa_vpa_autoscaling

Applies Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA) resources to an OpenShift cluster. Manages autoscaling configuration for workloads, implementing scaling defaults and recommendations aligned with capacity planning requirements.

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core` (`ansible-galaxy collection install kubernetes.core`)
- `KUBECONFIG` environment variable set, or kubeconfig at `~/.kube/config`
- Cluster-admin or namespace-admin privileges
- VPA Operator installed on the cluster when using `vpa_objects`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `kubeconfig` | `$KUBECONFIG` or `~/.kube/config` | No | Path to kubeconfig file |
| `context` | `""` | No | kubeconfig context to use; empty uses the current context |
| `namespace` | `"openshift-config"` | No | Default namespace for resources that omit `metadata.namespace` |
| `apply_wait` | `true` | No | Wait for HPA/VPA objects to be accepted by the API server |
| `artifacts_dir` | `"/tmp/ocp-artifacts"` | No | Directory for generated manifests and reports |
| `hpa_objects` | `[]` | No | List of `HorizontalPodAutoscaler` (autoscaling/v2) manifests to apply |
| `vpa_objects` | `[]` | No | List of `VerticalPodAutoscaler` CR manifests to apply (requires VPA Operator) |

### `hpa_objects` structure

Each entry is a full `HorizontalPodAutoscaler` manifest using `autoscaling/v2`:

```yaml
hpa_objects:
  - apiVersion: autoscaling/v2
    kind: HorizontalPodAutoscaler
    metadata:
      name: my-app-hpa
      namespace: production
    spec:
      scaleTargetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: my-app
      minReplicas: 2
      maxReplicas: 10
      metrics:
        - type: Resource
          resource:
            name: cpu
            target:
              type: Utilization
              averageUtilization: 70
```

### `vpa_objects` structure

Each entry is a full `VerticalPodAutoscaler` CR manifest:

```yaml
vpa_objects:
  - apiVersion: autoscaling.k8s.io/v1
    kind: VerticalPodAutoscaler
    metadata:
      name: my-app-vpa
      namespace: production
    spec:
      targetRef:
        apiVersion: apps/v1
        kind: Deployment
        name: my-app
      updatePolicy:
        updateMode: "Auto"
```

## Example Playbook

```yaml
- name: Apply HPA and VPA autoscaling configuration
  hosts: localhost
  gather_facts: false
  roles:
    - role: openshift/roles/ocp_hpa_vpa_autoscaling
      vars:
        hpa_objects:
          - apiVersion: autoscaling/v2
            kind: HorizontalPodAutoscaler
            metadata:
              name: frontend-hpa
              namespace: production
            spec:
              scaleTargetRef:
                apiVersion: apps/v1
                kind: Deployment
                name: frontend
              minReplicas: 3
              maxReplicas: 20
              metrics:
                - type: Resource
                  resource:
                    name: cpu
                    target:
                      type: Utilization
                      averageUtilization: 65
```

## Tags

| Tag | Description |
|-----|-------------|
| `hpa` | Apply HorizontalPodAutoscaler resources |
| `vpa` | Apply VerticalPodAutoscaler resources |

## Notes

- VPA objects require the [VPA Operator](https://docs.openshift.com/container-platform/latest/nodes/pods/nodes-pods-vertical-autoscaler.html) to be installed. The role will fail if VPA CRDs are absent and `vpa_objects` is non-empty.
- HPA and VPA should not both be set to `Auto` update mode on the same workload for CPU/memory metrics — this can cause scaling conflicts. Use VPA in `Off` or `Initial` mode alongside HPA.
- All operations are idempotent; re-running with the same objects is safe.

## License

MIT

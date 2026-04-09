# ocp_maintenance_windows

Manages OpenShift upgrade freeze windows, PodDisruptionBudgets (PDBs), and disruption budget defaults. Prevents unplanned cluster upgrades during maintenance blackout periods and ensures workloads have appropriate disruption budgets applied before upgrades proceed.

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
| `apply_wait` | `true` | No | Wait for applied resources to reach ready state |
| `artifacts_dir` | `"/tmp/ocp-artifacts"` | No | Directory for generated manifests and reports |
| `freeze_objects` | `[]` | No | List of `MachineConfigPool` patch objects that set pause=true to freeze upgrades |
| `pdb_objects` | `[]` | No | List of `PodDisruptionBudget` manifests to apply |

### `freeze_objects` structure

Each entry is a patch applied to a `MachineConfigPool`:

```yaml
freeze_objects:
  - name: worker
    paused: true
  - name: master
    paused: true
```

### `pdb_objects` structure

Each entry is a full `PodDisruptionBudget` manifest:

```yaml
pdb_objects:
  - apiVersion: policy/v1
    kind: PodDisruptionBudget
    metadata:
      name: my-app-pdb
      namespace: my-namespace
    spec:
      minAvailable: 1
      selector:
        matchLabels:
          app: my-app
```

## Example Playbook

```yaml
- name: Freeze OCP upgrades and apply PDBs before maintenance window
  hosts: localhost
  gather_facts: false
  roles:
    - role: openshift/roles/ocp_maintenance_windows
      vars:
        apply_wait: true
        freeze_objects:
          - name: worker
            paused: true
        pdb_objects:
          - apiVersion: policy/v1
            kind: PodDisruptionBudget
            metadata:
              name: critical-app-pdb
              namespace: production
            spec:
              minAvailable: 2
              selector:
                matchLabels:
                  app: critical-app
```

## Tags

| Tag | Description |
|-----|-------------|
| `freeze` | Apply/remove MachineConfigPool upgrade freezes |
| `pdb` | Apply PodDisruptionBudgets |

## Notes

- Set `freeze_objects[].paused: false` and re-run to unfreeze a pool after the maintenance window.
- PDB application is idempotent; re-running with the same objects is safe.
- `apply_changes` is not used by this role; all operations write to the cluster directly. Test changes in a non-production cluster first.

## License

MIT

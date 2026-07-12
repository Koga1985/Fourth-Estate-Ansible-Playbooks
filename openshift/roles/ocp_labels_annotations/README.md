# Role: ocp_labels_annotations

Fleetwide labels (owner, cost center), taints/tolerations.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `kubeconfig` | `"{{ lookup('env','KUBECONFIG') \| default('~/.kube/config', true) }}"` | No | Common connection settings for kubernetes.core.k8s |
| `context` | `""` | No | — |
| `apply_wait` | `true` | No | — |
| `artifacts_dir` | `"/tmp/ocp-artifacts"` | No | — |
| `label_targets` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use ocp_labels_annotations
  hosts: all
  gather_facts: false
  roles:
    - role: ocp_labels_annotations
```

## License

MIT

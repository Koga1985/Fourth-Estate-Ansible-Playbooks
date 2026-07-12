# Role: ocp_csi_operators

Deploy/configure CSI drivers & snapshot controller CRDs.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `kubeconfig` | `"{{ lookup('env','KUBECONFIG') \| default('~/.kube/config', true) }}"` | No | Connection for kubernetes.core.k8s |
| `context` | `""` | No | — |
| `namespace` | `"openshift-config"` | No | — |
| `apply_wait` | `true` | No | — |
| `artifacts_dir` | `"/tmp/ocp-artifacts"` | No | — |
| `csi_manifests` | `[]` | No | — |
| `snapshot_classes` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use ocp_csi_operators
  hosts: all
  gather_facts: false
  roles:
    - role: ocp_csi_operators
```

## License

MIT

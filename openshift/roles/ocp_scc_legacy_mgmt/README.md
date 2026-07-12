# Role: ocp_scc_legacy_mgmt

Curate SCC use; report drift; migrate to PSA where possible.

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
| `scc_bindings` | `[]` | No | — |
| `report_path` | `"{{ artifacts_dir }}/scc_report.csv"` | No | — |

## Example Playbook

```yaml
- name: Use ocp_scc_legacy_mgmt
  hosts: all
  gather_facts: false
  roles:
    - role: ocp_scc_legacy_mgmt
```

## License

MIT

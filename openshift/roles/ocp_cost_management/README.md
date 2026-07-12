# Role: ocp_cost_management

Cost metrics: labels/annotations per project, scrape rules or cost operator CRs.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `kubeconfig` | `"{{ lookup('env','KUBECONFIG') \| default('~/.kube/config', true) }}"` | No | Common connection settings for kubernetes.core.k8s |
| `context` | `""` | No | — |
| `namespace` | `"openshift-config"` | No | — |
| `apply_wait` | `true` | No | — |
| `artifacts_dir` | `"/tmp/ocp-artifacts"` | No | — |
| `cost_labels` | `[]` | No | list of { namespace, labels: { owner: 'team', cost: 'center' } } |
| `cost_crs` | `[]` | No | Cost management operator CRs / PrometheusRules |

## Example Playbook

```yaml
- name: Use ocp_cost_management
  hosts: all
  gather_facts: false
  roles:
    - role: ocp_cost_management
```

## License

MIT

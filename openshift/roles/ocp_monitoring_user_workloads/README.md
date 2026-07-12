# Role: ocp_monitoring_user_workloads

Enable user-workload monitoring; alert routes (PagerDuty/Slack), recording/alerting rules.

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
| `uwm_enable` | `true` | No | — |
| `alertmanager_config` | `{}` | No | Alertmanager CR data/secret for routes (PagerDuty/Slack) |
| `recording_rules` | `[]` | No | list of PrometheusRule objects |

## Example Playbook

```yaml
- name: Use ocp_monitoring_user_workloads
  hosts: all
  gather_facts: false
  roles:
    - role: ocp_monitoring_user_workloads
```

## License

MIT

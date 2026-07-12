# Role: ocp_log_forwarding

Configure ClusterLogForwarder to Loki/Elastic/Splunk; index/tenant settings.

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
| `clf` | `{}` | No | ClusterLogForwarder object |
| `logging_ns` | `"openshift-logging"` | No | — |

## Example Playbook

```yaml
- name: Use ocp_log_forwarding
  hosts: all
  gather_facts: false
  roles:
    - role: ocp_log_forwarding
```

## License

MIT

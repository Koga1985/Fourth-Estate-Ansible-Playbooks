# Role: ocp_routes_tls_policy

Enforce TLS versions/ciphers, HSTS, route types (reencrypt/edge/passthrough).

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
| `routes` | `[]` | No | list of Route objects with desired tls policy |

## Example Playbook

```yaml
- name: Use ocp_routes_tls_policy
  hosts: all
  gather_facts: false
  roles:
    - role: ocp_routes_tls_policy
```

## License

MIT

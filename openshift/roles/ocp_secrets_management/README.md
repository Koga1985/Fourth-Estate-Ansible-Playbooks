# Role: ocp_secrets_management

Sealed-Secrets or External Secrets Operator; KMS integration scaffolding.

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
| `secrets_operator_manifests` | `[]` | No | Operators/CRDs for sealed-secrets or ESO |
| `secrets_objects` | `[]` | No | SealedSecret/ExternalSecret/SecretStore objects |

## Example Playbook

```yaml
- name: Use ocp_secrets_management
  hosts: all
  gather_facts: false
  roles:
    - role: ocp_secrets_management
```

## License

MIT

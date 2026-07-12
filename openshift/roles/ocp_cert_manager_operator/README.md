# Role: ocp_cert_manager_operator

Deploy cert-manager; create issuers/clusterissuers (ACME/CA/Vault).

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
| `cert_manager_manifests` | `[]` | No | Operator/Subscription/CertManager CRs |
| `issuers` | `[]` | No | Issuer/ClusterIssuer objects |

## Example Playbook

```yaml
- name: Use ocp_cert_manager_operator
  hosts: all
  gather_facts: false
  roles:
    - role: ocp_cert_manager_operator
```

## License

MIT

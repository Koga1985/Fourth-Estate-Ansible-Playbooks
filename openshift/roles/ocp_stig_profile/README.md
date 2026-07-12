# OpenShift 4.x STIG Profile (`ocp_stig_profile`)

Production-ready Ansible role that hardens and assesses a **Red Hat OpenShift
Container Platform 4.x** cluster to the DISA **OCP 4.x STIG (Ver 2, Rel 4)**
(`CNTR-OS-XXXXXX`) using the certified **`kubernetes.core`** collection.

It consolidates the high-impact cluster- and namespace-scoped STIG controls into
a single runnable profile. For broader day-2 controls (log forwarding, image
signing, SCC management, RBAC baseline, registry policy) see the companion
`ocp_*` roles in this directory.

## Requirements

- Ansible 2.15+
- Collection: `kubernetes.core` (`ansible-galaxy collection install kubernetes.core`)
- Collection: `redhat.openshift` (`ansible-galaxy collection install redhat.openshift`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `kubeconfig` | `"{{ lookup('env', 'KUBECONFIG') \| default('~/.kube/config', true) }}"` | No | Cluster access |
| `apply_changes` | `false` | No | Deployment control |
| `artifacts_dir` | `"/tmp/ocp-stig-artifacts"` | No | — |
| `stig_cluster_config` | `true` | No | Control-area toggles |
| `stig_namespace_security` | `true` | No | — |
| `stig_compliance_report` | `true` | No | — |
| `ocp_audit_profile` | `WriteRequestBodies` | No | CNTR-OS-000100 - API server audit profile Default \| WriteRequestBodies \| AllRequestBodies |
| `ocp_encryption_type` | `aescbc` | No | CNTR-OS-000800 - etcd / API encryption at rest aescbc \| aesgcm |
| `ocp_tls_security_profile` | `Intermediate` | No | CNTR-OS-000440 - TLS security profile Old \| Intermediate \| Modern |
| `ocp_token_inactivity_timeout` | `"10m0s"` | No | CNTR-OS-000070 - OAuth token lifetimes (seconds) |
| `ocp_token_max_age_seconds` | `28800` | No | 8 hours |
| `ocp_disable_self_provisioner` | `true` | No | CNTR-OS-000200 - Remove cluster self-provisioner from authenticated users |
| `ocp_target_namespaces` | `(see defaults/main.yml)` | No | Namespace security (PSA + default-deny network policy) CNTR-OS-000180 (network policy) \| CNTR-OS-001xxx (PSA restricted) Namespaces to enforce restricted Pod Security Admission + default-deny netpol. Exclude platform namespaces (openshift-*, kube-*, default). |
| `ocp_psa_level` | `restricted` | No | restricted \| baseline |
| `ocp_apply_default_deny_netpol` | `true` | No | — |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Red Hat OpenShift Container Platform 4.x STIG"` | No | — |
| `stig_version` | `"V2R4"` | No | — |

## Example Playbook

```yaml
- name: Use ocp_stig_profile
  hosts: all
  gather_facts: false
  roles:
    - role: ocp_stig_profile
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags cluster`, `namespace`, `report`, plus `stig_cat2` and per-rule tags
(e.g. `--tags CNTR-OS-000800`).

## Why "grab and go"

* Certified `kubernetes.core` over your existing `KUBECONFIG`.
* **Safe by default**: `apply_changes=false` runs every change as a server-side
  check (no persistence) and writes a JSON findings artifact. Nothing is applied
  until `-e apply_changes=true`.
* Idempotent strategic-merge patches — reruns are no-ops once compliant.

## Quick start

```bash
cd openshift/roles/ocp_stig_profile/playbooks
ansible-galaxy collection install kubernetes.core redhat.openshift
pip install kubernetes openshift
export KUBECONFIG=~/.kube/config   # cluster-admin context

# DRY-RUN (assessment)
ansible-playbook run.yml
cat /tmp/ocp-stig-artifacts/ocp_stig_profile.json

# ENFORCE
ansible-playbook run.yml -e apply_changes=true -e @vars.example.yml
```

## Controls implemented

| STIG ID | Control |
|---------|---------|
| CNTR-OS-000070 | OAuth access-token inactivity timeout + max age |
| CNTR-OS-000100 | API server audit profile (`WriteRequestBodies`) |
| CNTR-OS-000180 | Default-deny ingress/egress NetworkPolicy per workload namespace |
| CNTR-OS-000200 | Remove `self-provisioners` from authenticated users |
| CNTR-OS-000440 | Cluster-wide TLS security profile (`Intermediate`) |
| CNTR-OS-000800 | etcd/API encryption at rest (`aescbc`) |
| CNTR-OS-001050 | Pod Security Admission `restricted` enforcement per namespace |

## ⚠️ Pre-flight before enforcing

* Requires a **cluster-admin** `KUBECONFIG`.
* Enabling **encryption at rest** triggers a rolling re-encryption of etcd —
  expect API server rollouts; run during a maintenance window.
* **PSA `restricted`** can break workloads that need elevated privileges — verify
  your `ocp_target_namespaces` workloads are compatible (the dry-run + audit/warn
  labels surface violations first).
* **Default-deny NetworkPolicy** blocks all traffic until you add explicit
  allow policies — stage carefully.
* Changing the **TLS profile** restarts the API/ingress operators.

## License

MIT

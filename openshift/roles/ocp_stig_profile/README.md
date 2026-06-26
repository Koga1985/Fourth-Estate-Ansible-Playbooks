# OpenShift 4.x STIG Profile (`ocp_stig_profile`)

Production-ready Ansible role that hardens and assesses a **Red Hat OpenShift
Container Platform 4.x** cluster to the DISA **OCP 4.x STIG (Ver 2, Rel 4)**
(`CNTR-OS-XXXXXX`) using the certified **`kubernetes.core`** collection.

It consolidates the high-impact cluster- and namespace-scoped STIG controls into
a single runnable profile. For broader day-2 controls (log forwarding, image
signing, SCC management, RBAC baseline, registry policy) see the companion
`ocp_*` roles in this directory.

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

## Tags

`--tags cluster`, `namespace`, `report`, plus `stig_cat2` and per-rule tags
(e.g. `--tags CNTR-OS-000800`).

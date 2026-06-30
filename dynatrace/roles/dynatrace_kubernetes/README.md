# Dynatrace Kubernetes / OpenShift (`dynatrace_kubernetes`)

Deploys **Dynatrace full-stack observability** to Kubernetes/OpenShift by
creating the token `Secret` and the **DynaKube** custom resource that the
Dynatrace Operator reconciles. Uses the certified `kubernetes.core` collection.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` runs every change as a server-side
  dry-run (no persistence) and writes a findings artifact. `apply_changes=true`
  applies. Tokens are `no_log`.

## Prerequisite
Install the **Dynatrace Operator** first (Helm recommended):
```bash
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \
  -n dynatrace --create-namespace --atomic
```
…or set `dynatrace_operator_manifest_url` to apply the release manifest.

## Quick start
```bash
cd dynatrace/roles/dynatrace_kubernetes/playbooks
ansible-galaxy collection install kubernetes.core
pip install kubernetes
export KUBECONFIG=~/.kube/config
ansible-playbook run.yml -e @vars.example.yml                       # DRY-RUN
ansible-playbook run.yml -e @vars.example.yml -e apply_changes=true # APPLY
```

## What it creates
* `dynatrace` namespace, a `dynakube` token `Secret` (apiToken + dataIngestToken),
  and a `DynaKube` CR with the chosen OneAgent mode and ActiveGate capabilities
  (kubernetes-monitoring, routing, dynatrace-api).

## Key variables
`dynakube_oneagent_mode` (`cloudNativeFullStack` | `classicFullStack` |
`applicationMonitoring` | `hostMonitoring`), `dynakube_activegate_capabilities`,
`dynakube_network_zone`, `dynakube_api_version`.

## Tags
`--tags k8s`, `operator`, `secret`, `dynakube`, `report`.

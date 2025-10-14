# Role: cp_threat_prevention

Build and operate Check Point Threat Prevention: baseline profile, TP rules, exceptions, IPS update channel, and publish/install.

## Requirements
- Connection: `httpapi` to the Management Server
- Collection: `check_point.mgmt`

## Defaults
```yaml
tp_layer: "Threat Prevention"
policy_package: "Standard"
install_targets: []
publish_changes: false
parallel_batches: 1
artifacts_dir: "/tmp/checkpoint-artifacts"
tp_profile_name: "TP-Baseline"
tp_profile_desc: "Baseline: recommended protections; Prevent medium+"
tp_profile_mode: "optimized"
tp_managed_tag: "tp-managed"
```

## Typical Vars
```yaml
tp_rules:
  - name: "Prod Servers TP"
    position: "top"
    destination: ["prod-servers"]
    protected_scope: ["prod-servers"]
    action: "Optimized"
    profile: "{{ tp_profile_name }}"
    tags: ["tp-managed","owner:secops"]

tp_exceptions:
  - name: "Allow Legacy SMB Scanner"
    source: ["legacy-scanner"]
    destination: ["fileservers"]
    service: ["microsoft-ds"]
    protections: ["IPS","Anti-Virus"]
    expiration: "2026-03-31"
    comments: "CHG-12345 temporary exception"
```
## Usage
```yaml
- hosts: checkpoint_mgmt
  gather_facts: false
  roles:
    - role: cp_threat_prevention
      vars:
        publish_changes: true
        install_targets: ["gw1","gw2"]
        tp_rules: "{{ lookup('file', 'vars/tp_rules.yml') | from_yaml }}"
        tp_exceptions: "{{ lookup('file', 'vars/tp_exceptions.yml') | from_yaml }}"
```

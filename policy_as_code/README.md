# Policy as Code Framework for Fourth Estate

## Overview

This Policy as Code framework implements DoD STIG and NIST 800-53 security controls as executable, testable Ansible code. All policies are production-ready, tested, and designed for drop-in deployment in Fourth Estate environments.

## Compliance Standards

- **DoD STIG** (Security Technical Implementation Guides)
- **NIST 800-53 Rev 5** (Security and Privacy Controls)
- **NIST 800-171** (Protecting Controlled Unclassified Information)
- **FISMA** (Federal Information Security Management Act)
- **FedRAMP** (Federal Risk and Authorization Management Program)

## Directory Structure

```
policy_as_code/
├── library/                    # Reusable policy modules
│   ├── compliance_common.yml   # Common compliance tasks
│   └── artifact_generator.yml  # Compliance artifact generation
├── policies/                   # Policy implementations
│   ├── access_control/         # NIST AC Family
│   ├── identification_auth/    # NIST IA Family
│   ├── audit_accountability/   # NIST AU Family
│   ├── system_communications/  # NIST SC Family
│   └── configuration_mgmt/     # NIST CM Family
├── tests/                      # Policy validation tests
│   ├── test_policies.yml       # Main test playbook
│   └── test_reports/           # Test results
└── artifacts/                  # Compliance artifacts
    └── .gitkeep
```

## Policy Implementation Pattern

Each policy follows this structure:

```yaml
---
# Control ID and metadata
# NIST 800-53 Control: XX-YY
# DoD STIG Finding: V-XXXXXX
# Severity: Category I/II/III

- name: Control implementation
  module.name:
    parameter: "{{ secure_default }}"
    state: present
  check_mode: "{{ not (apply_changes | default(false) | bool) }}"
  register: result
  tags: [nist_xx_yy, stig_catX, policy_domain]

- name: Generate compliance artifact
  ansible.builtin.include_tasks: ../../library/artifact_generator.yml
  vars:
    control_id: "XX-YY"
    stig_findings: ["V-XXXXXX"]
    severity: "Category I"
    implementation_details: "{{ result }}"
```

## Usage

### Dry-Run Mode (Default - Fourth Estate Safe)

```bash
# Check what would be applied without making changes
ansible-playbook policies/identification_auth/password_policy.yml \
  -i inventory/production.yml \
  --check
```

### Apply Policies

```bash
# Apply with explicit flag
ansible-playbook policies/identification_auth/password_policy.yml \
  -i inventory/production.yml \
  -e "apply_changes=true"
```

### Selective Execution by Tag

```bash
# Apply only Category I (High) severity findings
ansible-playbook site.yml --tags stig_cat1 -e "apply_changes=true"

# Apply specific NIST control family
ansible-playbook site.yml --tags nist_ia -e "apply_changes=true"

# Run compliance check only
ansible-playbook site.yml --tags compliance_check
```

### Run Functional Tests

```bash
# Test all policies
ansible-playbook tests/test_policies.yml -i inventory/test.yml

# Test specific policy
ansible-playbook tests/test_policies.yml -i inventory/test.yml --tags test_ia_5
```

## Security Features

### 1. Default to Dry-Run
All policies use `check_mode` by default. Changes only apply when `apply_changes=true`.

### 2. Least Privilege
- File permissions: 0640 (files), 0750 (directories)
- No world-readable files
- Owner/group explicitly set

### 3. Comprehensive Validation
- Input validation with assertions
- Symlink attack prevention
- Path traversal protection
- Type checking

### 4. Audit Trail
- SHA-256 checksums for all artifacts
- Timestamped compliance reports
- Change tracking and attribution

### 5. Idempotency
- All tasks are idempotent
- Safe to run repeatedly
- No side effects on re-execution

## Compliance Artifacts

Each policy execution generates:

```
artifacts/
├── YYYY-MM-DD_HHmmss/
│   ├── nist_<control_id>_<component>.json
│   ├── nist_<control_id>_<component>.json.sha256
│   ├── stig_findings_summary.json
│   └── compliance_report.html
```

Artifacts include:
- Control ID and description
- STIG finding IDs
- Implementation details
- Compliance status
- Timestamp and executor
- SHA-256 checksums

## Integration with Existing Roles

These policies can be integrated with existing roles:

```yaml
# In cisco/roles/ucs_security_hardening/tasks/main.yml
- name: Apply policy-as-code controls
  ansible.builtin.include_role:
    name: policy_as_code/policies/identification_auth
  vars:
    target_system: "cisco_ucs"
    apply_changes: "{{ apply_changes | default(false) }}"
```

## Change Control

All policy changes must:
1. Be peer-reviewed via pull request
2. Pass functional tests
3. Generate compliance artifacts
4. Be approved by security team
5. Be deployed to test environment first

## Support

For issues or questions:
- Review logs in `artifacts/`
- Check test results in `tests/test_reports/`
- Verify NIST/STIG mappings in policy comments
- Consult role-specific README files

## Version

Policy Framework Version: 1.0.0
Last Updated: 2026-01-15

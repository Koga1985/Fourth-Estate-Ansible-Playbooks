# ans_content_qa_ci

Run ansible-lint/yamllint/molecule; optional SBOM/vuln scans; deprecations & changelog bundles.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | — |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `qa_lint_enabled` | `true` | No | QA Configuration |
| `qa_syntax_check_enabled` | `true` | No | — |
| `qa_security_scan_enabled` | `true` | No | — |
| `qa_ansible_lint_strict` | `false` | No | — |
| `qa_yamllint_enabled` | `true` | No | — |
| `ci_integration_enabled` | `true` | No | CI Integration |
| `ci_platform` | `"gitlab"` | No | — |
| `ci_webhook_enabled` | `true` | No | — |
| `molecule_test_enabled` | `true` | No | Testing |
| `ansible_test_enabled` | `true` | No | — |
| `pytest_enabled` | `true` | No | — |
| `qa_min_coverage` | `80` | No | Quality Gates |
| `qa_max_complexity` | `10` | No | — |
| `qa_fail_on_warnings` | `false` | No | — |
| `fourth_estate_security_scan` | `true` | No | Fourth Estate |
| `fourth_estate_compliance_check` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_content_qa_ci
  hosts: all
  gather_facts: false
  roles:
    - role: ans_content_qa_ci
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

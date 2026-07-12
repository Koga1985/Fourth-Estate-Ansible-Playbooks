# ans_content_trust_and_lock

Allow/block namespaces, version pinning via lockfiles, optional signing service hooks.

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
| `signing_enabled` | `true` | No | Content Signing |
| `signing_key_id` | `""` | No | — |
| `signing_service` | `"ansible-default"` | No | — |
| `gpg_key_path` | `"/etc/pulp/certs/signing-service.key"` | No | — |
| `lock_collections` | `true` | No | Collection Locking |
| `requirements_lock_file` | `"requirements.lock"` | No | — |
| `lock_on_publish` | `true` | No | — |
| `trusted_namespaces` | `(see defaults/main.yml)` | No | Trust Configuration |
| `fourth_estate_mandatory_signing` | `true` | No | Fourth Estate |
| `fourth_estate_signature_verification` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_content_trust_and_lock
  hosts: all
  gather_facts: false
  roles:
    - role: ans_content_trust_and_lock
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

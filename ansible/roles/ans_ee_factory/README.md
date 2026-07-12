# ans_ee_factory

Build/pin Execution Environments, optional sign and push.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | Common settings |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `ee_registry` | `"{{ lookup('env', 'EE_REGISTRY') \| default('registry.example.mil') }}"` | No | Container Registry |
| `ee_registry_username` | `"{{ lookup('env', 'REGISTRY_USERNAME') \| default('') }}"` | No | — |
| `ee_registry_password` | `"{{ lookup('env', 'REGISTRY_PASSWORD') \| default('') }}"` | No | — |
| `ee_registry_namespace` | `"fourth-estate"` | No | — |
| `registry_push` | `true` | No | — |
| `registry_verify_ssl` | `true` | No | — |
| `ee_builder_version` | `"3"` | No | Build Configuration |
| `ee_base_image` | `"quay.io/ansible/ansible-runner:latest"` | No | — |
| `ee_builder_image` | `"quay.io/ansible/ansible-builder:latest"` | No | — |
| `ee_build_arg_defaults` | `(see defaults/main.yml)` | No | — |
| `ee_definitions` | `(see defaults/main.yml)` | No | Execution Environment Definitions |
| `ee_signing_enabled` | `true` | No | Image Signing |
| `ee_signing_command` | `"cosign"` | No | — |
| `ee_signing_key` | `""` | No | — |
| `ee_signature_registry_path` | `"signatures"` | No | — |
| `ee_scanning_enabled` | `true` | No | Image Scanning |
| `ee_scanner` | `"trivy"` | No | trivy, clair, anchore |
| `ee_scan_severity_threshold` | `"HIGH"` | No | — |
| `ee_scan_fail_on_critical` | `true` | No | — |
| `ee_cache_enabled` | `true` | No | Cache Configuration |
| `ee_cache_path` | `"/var/cache/ansible-builder"` | No | — |
| `ee_parallel_builds` | `false` | No | Build Optimization |
| `ee_max_parallel` | `3` | No | — |
| `ee_build_timeout` | `3600` | No | seconds |
| `ee_prune_on_success` | `true` | No | — |
| `ee_keep_failed_builds` | `false` | No | — |
| `ee_register_in_controller` | `true` | No | Controller Integration |
| `controller_host` | `"{{ lookup('env', 'CONTROLLER_HOST') \| default('https://controller....` | No | — |
| `controller_oauthtoken` | `"{{ lookup('env', 'CONTROLLER_OAUTH_TOKEN') \| default('') }}"` | No | — |
| `controller_username` | `"{{ lookup('env', 'CONTROLLER_USERNAME') \| default('') }}"` | No | — |
| `controller_password` | `"{{ lookup('env', 'CONTROLLER_PASSWORD') \| default('') }}"` | No | — |
| `fourth_estate_hardened_images` | `true` | No | Fourth Estate Specific |
| `fourth_estate_fips_mode` | `true` | No | — |
| `fourth_estate_minimal_base` | `true` | No | — |
| `fourth_estate_compliance_scan` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_ee_factory
  hosts: all
  gather_facts: false
  roles:
    - role: ans_ee_factory
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

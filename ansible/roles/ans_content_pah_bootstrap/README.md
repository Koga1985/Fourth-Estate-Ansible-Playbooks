# ans_content_pah_bootstrap

Bootstrap Private Automation Hub: SSO/groups, remotes/mirrors, sync & promote.

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
| `ah_url` | `"{{ lookup('env', 'AH_HOST') \| default('https://pah.example.mil') }}"` | No | Private Automation Hub connection |
| `ah_username` | `"{{ lookup('env', 'AH_USERNAME') \| default('admin') }}"` | No | — |
| `ah_password` | `"{{ lookup('env', 'AH_PASSWORD') \| default('') }}"` | No | — |
| `ah_token` | `"{{ lookup('env', 'AH_TOKEN') \| default('') }}"` | No | — |
| `ah_repositories` | `(see defaults/main.yml)` | No | Repository Configuration |
| `ah_remotes` | `(see defaults/main.yml)` | No | Remote Repositories |
| `ah_groups` | `(see defaults/main.yml)` | No | Groups and RBAC |
| `ah_content_promotion` | `(see defaults/main.yml)` | No | Content Promotion Pipeline |
| `ah_collection_signing_enabled` | `true` | No | Collection Signing |
| `ah_signing_service` | `"ansible-default"` | No | — |
| `ah_gpg_key_id` | `""` | No | — |
| `ah_namespaces` | `(see defaults/main.yml)` | No | Namespace Configuration |
| `ah_sso_enabled` | `false` | No | SSO Configuration |
| `ah_sso_settings` | `{}` | No | — |
| `ah_backup_enabled` | `true` | No | Backup and Sync |
| `ah_backup_path` | `"{{ artifacts_dir }}/pah_backup"` | No | — |
| `ah_sync_on_bootstrap` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_content_pah_bootstrap
  hosts: all
  gather_facts: false
  roles:
    - role: ans_content_pah_bootstrap
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT

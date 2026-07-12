# pure_fa_provisioning

Pure Fa Provisioning role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `fa_url` | `"10.0.0.10"` | No | — |
| `api_token` | `"{{ lookup('env','PURE_FA_TOKEN') }}"` | No | — |
| `validate_certs` | `false` | No | — |
| `artifacts_dir` | `"/tmp/pure-artifacts"` | No | — |
| `volumes` | `[]` | No | — |
| `hosts` | `[]` | No | — |
| `hostgroups` | `[]` | No | — |
| `mappings` | `[]` | No | — |
| `pods` | `[]` | No | — |
| `dirsvc` | `{}` | No | — |
| `iscsi` | `[]` | No | — |
| `fc` | `[]` | No | — |
| `nvme_tcp` | `{}` | No | — |
| `cert_bundle` | `{}` | No | — |

## Example Playbook

```yaml
---
- name: Pure Fa Provisioning
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_fa_provisioning
```

## License

MIT

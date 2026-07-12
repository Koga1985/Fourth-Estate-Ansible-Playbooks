# pure_fb_provisioning

Pure Fb Provisioning role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `fb_url` | `"https://flashblade.example.com"` | No | — |
| `fb_token` | `"{{ lookup('env','PURE_FB_TOKEN') }}"` | No | — |
| `fb_validate_certs` | `false` | No | — |
| `artifacts_dir` | `"/tmp/pure-artifacts"` | No | — |
| `filesystems` | `[]` | No | — |
| `buckets` | `[]` | No | — |
| `users` | `[]` | No | — |
| `groups` | `[]` | No | — |
| `dirsvc` | `{}` | No | — |
| `smb_shares` | `[]` | No | — |
| `nfs_policies` | `[]` | No | — |
| `certs` | `{}` | No | — |

## Example Playbook

```yaml
---
- name: Pure Fb Provisioning
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_fb_provisioning
```

## License

MIT

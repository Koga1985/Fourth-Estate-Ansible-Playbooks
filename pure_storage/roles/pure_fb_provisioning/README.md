# pure_fb_provisioning

Pure Fb Provisioning role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `fb_url` | `"https://flashblade.example.com"` |  |
| `fb_token` | `"{{ lookup('env','PURE_FB_TOKEN') }}"` |  |
| `fb_validate_certs` | `false` |  |
| `artifacts_dir` | `"/tmp/pure-artifacts"` |  |
| `filesystems` | `[]` |  |
| `buckets` | `[]` |  |
| `users` | `[]` |  |
| `groups` | `[]` |  |
| `dirsvc` | `{}` |  |
| `smb_shares` | `[]` |  |
| `nfs_policies` | `[]` |  |
| `certs` | `{}` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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

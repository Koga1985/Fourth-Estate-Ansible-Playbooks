# pure_fb_ops

Pure Fb Ops role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `fb_url` | `"https://flashblade.example.com"` |  |
| `fb_token` | `"{{ lookup('env','PURE_FB_TOKEN') }}"` |  |
| `fb_validate_certs` | `false` |  |
| `artifacts_dir` | `"/tmp/pure-artifacts"` |  |
| `alerts` | `{}` |  |
| `upgrade` | `{"dry_run": true}` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Pure Fb Ops
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_fb_ops
```

## License

MIT

# pure_fb_data_protection

Pure Fb Data Protection role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `fb_url` | `"https://flashblade.example.com"` |  |
| `fb_token` | `"{{ lookup('env','PURE_FB_TOKEN') }}"` |  |
| `fb_validate_certs` | `false` |  |
| `snap_policies` | `[]` |  |
| `replication` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Pure Fb Data Protection
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_fb_data_protection
```

## License

MIT

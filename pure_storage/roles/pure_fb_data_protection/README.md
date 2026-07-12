# pure_fb_data_protection

Pure Fb Data Protection role for Fourth Estate infrastructure automation.

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
| `snap_policies` | `[]` | No | — |
| `replication` | `[]` | No | — |

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

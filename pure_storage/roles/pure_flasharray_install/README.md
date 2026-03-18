# pure_flasharray_install

Pure Flasharray Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` |  |
| `flasharray_name` | `"{{ inventory_hostname_short }}-fa"` |  |
| `flasharray_dns_domain` | `"{{ domain_name | default('example.com') }}"` |  |
| `flasharray_timezone` | `"America/New_York"` |  |
| `flasharray_phonehome_enabled` | `true` |  |
| `flasharray_support_proxy_enabled` | `false` |  |
| `flasharray_smtp_enabled` | `true` |  |
| `flasharray_smtp_sender_domain` | `"{{ domain_name | default('example.com') }}"` |  |
| `flasharray_smtp_relay_host` | `"{{ smtp_relay | default('smtp.example.com') }}"` |  |
| `flasharray_idle_timeout` | `30` |  |
| `flasharray_auto_update` | `false` |  |
| `flasharray_organization` | `"Fourth Estate"` |  |
| `flasharray_location` | `"{{ datacenter_name | default('DC1') }}"` |  |
| `flasharray_contact` | `"storage-team@{{ domain_name | default('example...` |  |
| `flasharray_fips_mode` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Pure Flasharray Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_install
```

## License

MIT

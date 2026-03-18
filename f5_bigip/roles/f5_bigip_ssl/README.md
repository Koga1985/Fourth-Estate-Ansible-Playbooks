# f5_bigip_ssl

F5 Bigip Ssl role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `f5_bigip/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `f5_bigip_ssl_certificates` | `[]` |  |
| `f5_bigip_ssl_keys` | `[]` |  |
| `f5_bigip_client_ssl_profiles` | `[]` |  |
| `f5_bigip_server_ssl_profiles` | `[]` |  |
| `f5_bigip_ssl_default_ciphers` | `"ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-G...` |  |
| `f5_bigip_ocsp_enabled` | `true` |  |
| `f5_bigip_ocsp_stapling` | `true` |  |
| `f5_bigip_ssl_cert_bundles` | `[]` |  |
| `f5_bigip_sni_enabled` | `true` |  |
| `f5_bigip_sni_require` | `false` |  |
| `f5_bigip_ssl_renegotiation` | `false` |  |
| `f5_bigip_ssl_secure_renegotiation` | `require-strict` |  |
| `f5_bigip_cert_expiry_warning_days` | `30` |  |
| `f5_bigip_ssl_insert_empty_fragments` | `true` |  |
| `f5_bigip_ssl_single_dh_use` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `f5networks.f5_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: F5 Bigip Ssl
  hosts: localhost
  gather_facts: false
  roles:
    - role: f5_bigip/roles/f5_bigip_ssl
```

## License

MIT

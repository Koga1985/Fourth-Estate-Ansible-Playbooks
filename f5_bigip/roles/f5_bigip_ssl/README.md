# f5_bigip_ssl

F5 Bigip Ssl role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `f5_bigip/README.md`

## Requirements

- Ansible 2.15+
- Collection: `f5networks.f5_modules`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `f5_bigip_provider` | `(see defaults/main.yml)` | No | F5 BIG-IP Connection Details |
| `f5_bigip_ssl_certificates` | `[]` | No | SSL Certificates Configuration |
| `f5_bigip_ssl_keys` | `[]` | No | SSL Key Management |
| `f5_bigip_client_ssl_profiles` | `[]` | No | Client SSL Profiles |
| `f5_bigip_server_ssl_profiles` | `[]` | No | Server SSL Profiles |
| `f5_bigip_ssl_default_ciphers` | `"ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-...` | No | Default SSL Cipher Suite (DISA STIG Compliant) |
| `f5_bigip_ssl_protocols` | `(see defaults/main.yml)` | No | SSL Protocol Versions (TLS 1.2+ only) |
| `f5_bigip_ocsp_enabled` | `true` | No | OCSP Configuration |
| `f5_bigip_ocsp_stapling` | `true` | No | — |
| `f5_bigip_ssl_cert_bundles` | `[]` | No | Certificate Bundles (CA bundles) |
| `f5_bigip_sni_enabled` | `true` | No | SNI Configuration |
| `f5_bigip_sni_require` | `false` | No | — |
| `f5_bigip_ssl_renegotiation` | `false` | No | Session Renegotiation |
| `f5_bigip_ssl_secure_renegotiation` | `require-strict` | No | — |
| `f5_bigip_cert_expiry_warning_days` | `30` | No | Certificate Expiration Monitoring |
| `f5_bigip_ssl_insert_empty_fragments` | `true` | No | SSL Options |
| `f5_bigip_ssl_single_dh_use` | `true` | No | — |
| `f5_bigip_ssl_session_ticket` | `false` | No | Session Tickets |
| `f5_bigip_save_config` | `true` | No | Save Configuration |

## Example Playbook

```yaml
---
- name: F5 Bigip Ssl
  hosts: localhost
  gather_facts: false
  roles:
    - role: f5_bigip/roles/f5_bigip_ssl
```

## Tags

| Tag | Description |
|-----|-------------|
| `f5_ca_bundles` | Tasks tagged `f5_ca_bundles` |
| `f5_cert_check` | Tasks tagged `f5_cert_check` |
| `f5_certificates` | Tasks tagged `f5_certificates` |
| `f5_client_ssl_profiles` | Tasks tagged `f5_client_ssl_profiles` |
| `f5_keys` | Tasks tagged `f5_keys` |
| `f5_ocsp` | Tasks tagged `f5_ocsp` |
| `f5_save` | Tasks tagged `f5_save` |
| `f5_server_ssl_profiles` | Tasks tagged `f5_server_ssl_profiles` |
| `f5_ssl` | Tasks tagged `f5_ssl` |
| `f5_verify` | Tasks tagged `f5_verify` |

## License

MIT

# splunk_enterprise_install

Installs and configures Splunk Enterprise with full DoD STIG and NIST 800-53 compliance. Covers package installation, TLS hardening, LDAP/SAML authentication, FIPS mode, session controls, file permissions, clustering configuration, and audit logging.

## Requirements

- Ansible 2.15+
- `ansible.posix` collection: `ansible-galaxy collection install ansible.posix`
- Target: RHEL 8/9, CentOS, Rocky, AlmaLinux, Ubuntu, Debian (x86_64)
- Minimum hardware: 12 GB RAM, 500 GB disk

## Role Variables

### Required (no defaults — must be set in vault.yml)

| Variable | Description |
|----------|-------------|
| `vault_splunk_admin_password` | Splunk admin UI password (minimum 15 characters) |

### Minimum Viable Configuration

To run a basic install with default settings, you only need:

```yaml
# group_vars/all/vault.yml
vault_splunk_admin_password: "YourStrongPassword15chars+"

# inventory or playbook vars
splunk_accept_license: true   # Must be explicitly set to true
```

### Key Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `splunk_accept_license` | `false` | **Yes** | Must be `true` to proceed with installation |
| `splunk_version` | `"9.2.1"` | No | Splunk Enterprise version to install |
| `splunk_home` | `"/opt/splunk"` | No | Splunk installation directory |
| `splunk_admin_password` | `{{ vault_splunk_admin_password }}` | **Yes** | Admin password |
| `splunk_auth_type` | `"LDAP"` | No | Authentication type: `Splunk`, `LDAP`, or `SAML` |
| `splunk_enable_fips` | `true` | No | Enable FIPS 140-2 mode |
| `splunk_cluster_mode` | `"none"` | No | Clustering: `none`, `master`, `peer`, `searchhead` |
| `splunk_tls_min_version` | `"tls1.2"` | No | Minimum TLS version |
| `splunk_use_default_tls_certs` | `false` | No | Use self-signed certs (not for production) |

See `defaults/main.yml` for the full variable list with STIG finding references.

## Example Playbook

```yaml
---
- name: Install Splunk Enterprise
  hosts: splunk_servers
  become: true
  roles:
    - role: splunk/roles/splunk_enterprise_install
      vars:
        splunk_accept_license: true
        splunk_version: "9.2.1"
        splunk_auth_type: "LDAP"
        splunk_enable_fips: true
        splunk_cluster_mode: "none"
```

## Tags

| Tag | Description |
|-----|-------------|
| `install` | Package download and installation |
| `config` | Initial configuration |
| `tls` | TLS certificate setup |
| `ldap` | LDAP/authentication configuration |
| `fips` | FIPS mode configuration |
| `hardening` | STIG security hardening |
| `clustering` | Cluster configuration |
| `firewall` | Firewall port rules |

## License

MIT

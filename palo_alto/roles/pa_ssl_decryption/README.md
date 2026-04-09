# pa_ssl_decryption

Configures SSL/TLS decryption on Palo Alto Networks firewalls. Imports forward-trust and forward-untrust certificates, creates decryption profiles, manages SSL decryption rules, and maintains a URL bypass list. Supports a staged enforcement workflow: deploy rules in `log only` mode before switching to `decryption_enforce: true`.

## Requirements

- Ansible 2.15+
- Collection: `paloaltonetworks.panos` (`ansible-galaxy collection install paloaltonetworks.panos`)
- PAN-OS 10.1 or higher
- Forward-trust CA certificate issued by your organization's PKI
- Admin credentials for the target device or Panorama

## Role Variables

### Connection / Panorama

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `pa_use_panorama` | `false` | No | Target Panorama instead of a direct device |
| `device_group` | `null` | No | Panorama device group |
| `vsys` | `"vsys1"` | No | Virtual system to target |
| `template` | `null` | No | Panorama template name |
| `template_stack` | `null` | No | Panorama template stack name |
| `artifacts_dir` | `"/tmp/pan-artifacts"` | No | Local directory for generated reports |
| `commit_after_changes` | `true` | No | Commit candidate config after all changes |
| `commit_description` | `"Apply SSL Decryption via Ansible"` | No | Commit description string |

### Forward-Trust Certificate

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `forward_trust_cert.enabled` | `false` | No | Import and configure the forward-trust certificate |
| `forward_trust_cert.name` | `"Forward-Trust"` | No | Certificate name on the firewall |
| `forward_trust_cert.certificate_file` | `null` | **Yes if enabled** | Local path to the PEM certificate file |
| `forward_trust_cert.private_key_file` | `null` | **Yes if enabled** | Local path to the PEM private key file |
| `forward_trust_cert.passphrase` | `null` | No | Private key passphrase (vault-protected) |

### Forward-Untrust Certificate

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `forward_untrust_cert.enabled` | `false` | No | Import and configure the forward-untrust certificate |
| `forward_untrust_cert.name` | `"Forward-Untrust"` | No | Certificate name on the firewall |
| `forward_untrust_cert.certificate_file` | `null` | **Yes if enabled** | Local path to the PEM certificate file |
| `forward_untrust_cert.private_key_file` | `null` | **Yes if enabled** | Local path to the PEM private key file |
| `forward_untrust_cert.passphrase` | `null` | No | Private key passphrase (vault-protected) |

### Decryption Profiles

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `decryption_profiles` | `[]` | No | List of decryption profile objects (see structure below) |

Each profile:

```yaml
decryption_profiles:
  - name: "strict-decrypt"
    ssl_forward_proxy:
      block_expired_certificate: true
      block_untrusted_issuer: true
      block_unknown_cert: true
      min_version: "tls1-2"
```

### Bypass List

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `decrypt_bypass_category` | `"NoDecrypt-BYPASS"` | No | Name of the custom URL category used for bypass |
| `bypass_urls` | `[]` | No | List of URL patterns to exempt from decryption |

### Decryption Rules

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `decryption_rules` | `[]` | No | List of decryption rule objects (see structure below) |
| `decryption_enforce` | `false` | No | When `false`, rules are created in log-only/no-decrypt mode. Set `true` to enforce decryption. |

Each rule:

```yaml
decryption_rules:
  - name: "decrypt-outbound"
    source_zone: ["trust"]
    destination_zone: ["untrust"]
    profile: "strict-decrypt"
    action: "decrypt"
```

## Example Playbook

```yaml
- name: Configure SSL decryption (staged — log only)
  hosts: palo_alto_firewalls
  gather_facts: false
  roles:
    - role: palo_alto/roles/pa_ssl_decryption
      vars:
        forward_trust_cert:
          enabled: true
          name: "Corp-Forward-Trust"
          certificate_file: "/etc/pki/pan/forward-trust.pem"
          private_key_file: "/etc/pki/pan/forward-trust-key.pem"
          passphrase: "{{ vault_fwd_trust_passphrase }}"
        bypass_urls:
          - "*.agency.gov"
          - "windowsupdate.microsoft.com"
        decryption_rules:
          - name: "decrypt-outbound-web"
            source_zone: ["trust"]
            destination_zone: ["untrust"]
            profile: "strict-decrypt"
            action: "decrypt"
        decryption_enforce: false   # change to true to move from log-only to enforce
```

## Tags

| Tag | Description |
|-----|-------------|
| `certificates` | Import forward-trust and forward-untrust certs |
| `profiles` | Create/update decryption profiles |
| `bypass` | Manage the URL bypass category and entries |
| `rules` | Create/update decryption rules |

## Compliance Controls

| Framework | Control ID | Description |
|-----------|-----------|-------------|
| NIST 800-53 | SC-8 | Transmission Confidentiality and Integrity |
| NIST 800-53 | SC-13 | Cryptographic Protection |
| NIST 800-53 | SI-3 | Malware Protection (decrypt to inspect) |

## Notes

- `decryption_enforce: false` is the recommended starting point. Deploy, verify bypass completeness, then flip to `true` in a follow-up run.
- SSL decryption breaks certificate pinning; test with known pin-using apps before enforcing.
- Private key files must be accessible on the Ansible control node; use Vault-encrypted files in production.
- `commit_after_changes: false` can be used to batch this role with others before a single commit.

## License

MIT

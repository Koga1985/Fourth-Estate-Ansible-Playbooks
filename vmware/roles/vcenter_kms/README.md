# vcenter_kms (role)

Create/maintain **Standard Key Providers** in vCenter, establish **trust** with
your external KMS, and optionally mark a provider as **default**. Designed to
pair with your **VM encryption enforcement** role.

## Requirements
- Ansible >= 2.15
- Collection: `community.vmware` (see `requirements.yml`)
- vCenter must be licensed and hosts compatible for encryption.

## Variables (`defaults/main.yml`)
```yaml
vcenter_hostname: ""
vcenter_username: ""
vcenter_password: ""
vcenter_validate_certs: false

key_providers:
  - name: "corp-kp"
    state: present
    mark_default: true
    kms_info:
      - { kms_name: "corp-kms1", kms_ip: "10.10.10.50", kms_port: 5696 }
      - { kms_name: "corp-kms2", kms_ip: "10.10.10.51", kms_port: 5696 }
    trust:
      upload_client_cert: "/secure/vc_client_cert.pem"
      upload_client_key:  "/secure/vc_client_key.pem"

gather_info_after: true
```

### Trust options
Pick exactly one (module-supported):
- `upload_client_cert` + `upload_client_key`
- CSR flow: `download_client_csr` + `upload_kms_signed_client_csr`
- Self-signed: `download_self_signed_cert`

## Example Play
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vcenter_kms
      vars:
        vcenter_hostname: "vcenter.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false

        key_providers:
          - name: "corp-kp"
            state: present
            mark_default: true
            kms_info:
              - { kms_name: "corp-kms1", kms_ip: "10.10.10.50", kms_port: 5696 }
            trust:
              upload_client_cert: "/secure/vc_client_cert.pem"
              upload_client_key:  "/secure/vc_client_key.pem"
```

## Tips
- Run this role **before** applying your VM Encryption storage policy role.
- If you rotate keys or certs, re-run with updated `trust` inputs.
- To remove a provider, set `state: absent` for that entry.

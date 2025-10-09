# vcenter_certificates (role)

Rotate **vCenter (VCSA)** certificates with Ansible:
- **Machine SSL** cert (VMCA-signed or custom CA-signed)
- **Solution User** certs (VMCA bulk replace; custom optional/advanced)
- Optional **CSR generation** helper using `certool`

This role drives the native **`certificate-manager`** tool on the VCSA using
non-interactive input/`expect`, which keeps it consistent across vCenter 7/8.

## Requirements
- SSH access to the **VCSA** (default: `root@vcsa.example.local`).
- Your CA-signed certs and keys if using `custom` mode.
- Run first in a maintenance window or lab; services may restart.

## Variables (see `defaults/main.yml`)
- `delegate_host`, `delegate_user`, `delegate_ssh_port`
- `rotate_machine_ssl`, `rotate_solution_users`
- `machine_ssl_mode`: `vmca` or `custom`
- `solution_users_mode`: `vmca` or `custom` (custom is advanced; prompts vary)
- Custom cert paths: `machine_ssl_cert`, `machine_ssl_key`, `machine_ssl_chain`
- `solution_user_certs`: map of solution users → cert/key/chain (advanced)
- `generate_csrs`: produce CSR/key on the VCSA (helper)
- `csr_subject`: CSR DN values
- `post_restart_services`: run `services-control --restart --all` after rotation

## Example (VMCA everywhere)
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vcenter_certificates
      vars:
        delegate_host: "vcsa01.example.local"
        rotate_machine_ssl: true
        rotate_solution_users: true
        machine_ssl_mode: "vmca"
        solution_users_mode: "vmca"
```

## Example (custom Machine SSL, VMCA solution users)
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vcenter_certificates
      vars:
        delegate_host: "vcsa01.example.local"
        machine_ssl_mode: "custom"
        machine_ssl_cert: "/secure/mssl.crt"
        machine_ssl_key: "/secure/mssl.key"
        machine_ssl_chain: "/secure/chain.pem"
        solution_users_mode: "vmca"
```

> **Note:** Custom solution user rotation (option 5 in certificate-manager) is
> environment-specific because it prompts for each user certificate. If you need
> that fully automated, tell me which solution users you have enabled and I’ll
> tailor the `expect` prompts for your environment.

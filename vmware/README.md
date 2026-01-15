# VMware Automation (Ansible)

This directory contains **35+ Ansible roles** for automating **VMware vSphere** and **NSX-T** operations (vCenter, ESXi, clusters, VMs, networking, snapshots, RBAC, software-defined networking, and security/STIG tasks).

## What this folder provides

### vSphere Operations (27 existing roles)
- vCenter & ESXi inventory and facts collection
- Datacenter/cluster baseline tasks (create/update clusters, add hosts)
- VM lifecycle (create from template/ISO, reconfigure CPU/RAM/Disk/NICs, customize guest)
- Power & snapshot operations
- Templates & content library operations
- RBAC hardening (users/roles, least-privilege, break-glass)
- Network & storage tasks (portgroups, vSwitch/Distributed Switch, datastores)
- Security baselines and STIG/compliance helpers

### NSX-T Software-Defined Networking (8 NEW roles)
- **nsx_t_networking** - NSX-T Manager deployment and configuration
- **nsx_t_security** - Distributed firewall and security policies
- **nsx_t_load_balancer** - NSX-T load balancer configuration
- **nsx_t_edge_cluster** - Edge cluster deployment
- **nsx_t_segments** - Network segments (overlay networking)
- **nsx_t_firewall** - Gateway and distributed firewall rules
- **nsx_t_tier_gateways** - Tier-0 and Tier-1 gateway configuration
- **nsx_t_vpn** - IPsec and L2 VPN configuration

Tip: run `ls -1 *.yml` in this folder to see available playbooks.

## Prerequisites

- Ansible 2.14+ (Automation Platform 2.x compatible)
- Collections: `community.vmware` and/or `vmware.vmware`
- Python packages: `pyvmomi`, `requests`

Install the essentials on your control host:

```bash
ansible-galaxy collection install community.vmware vmware.vmware
python -m pip install --user --upgrade pyvmomi requests
```

If you're using Execution Environments (EE), include these collections and packages in the EE definition.

## Credentials & connectivity

Keep credentials vaulted or stored in a secrets manager. Example `group_vars/vmware.yml`:

```yaml
vcenter_hostname: "vcsa.example.mil"
vcenter_username: "svc_ansible@example.mil"
vcenter_password: "{{ vault_vcenter_password }}"
vcenter_validate_certs: true
```

Best practices:

- Use Ansible Vault for secrets or inject them from environment/CI.
- Run API-driven tasks from `hosts: localhost` with `connection: local`.
- Use `serial` when performing bulk operations.

## Inventory & layout

Minimal API inventory:

```ini
[localhost]
127.0.0.1 ansible_connection=local
```

Suggested layout:

```text
vmware/
├── group_vars/
│   └── vmware.yml
├── playbooks/
├── roles/
├── files/
└── README.md
```

## Common variables (examples)

```yaml
# group_vars/vmware.yml
vcenter_hostname: "vcsa.example.mil"
vcenter_username: "svc_ansible@example.mil"
vcenter_password: "{{ vault_vcenter_password }}"
vcenter_validate_certs: true

vsphere_datacenter: "DC1"
vsphere_cluster: "Prod-Cluster"
vsphere_datastore: "Datastore01"
vsphere_network: "VM Network"

# VM defaults
vm_guest_os: "rhel9_64Guest"
vm_folder: "Prod/Servers"
vm_hw_version: 20
vm_cpu: 4
vm_ram_mb: 8192
vm_disk_gb: 60
```

## Usage examples

Below are short, runnable examples. Edit values in `group_vars/vmware.yml` before running.

### Create a VM from a template

```yaml
- name: Create VM from template
  hosts: localhost
  gather_facts: false
  collections:
    - community.vmware
  vars_files:
    - ../group_vars/vmware.yml
  tasks:
    - name: Clone VM from template
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: "{{ vcenter_validate_certs }}"
        datacenter: "{{ vsphere_datacenter }}"
        cluster: "{{ vsphere_cluster }}"
        folder: "{{ vm_folder }}"
        template: "rhel9-gold"
        name: "web-01"
        state: poweredon
        hardware:
          memory_mb: "{{ vm_ram_mb }}"
          num_cpus: "{{ vm_cpu }}"
        networks:
          - name: "{{ vsphere_network }}"
            type: static
            ip: 10.10.20.51
            netmask: 255.255.255.0
            gateway: 10.10.20.1
        disk:
          - size_gb: "{{ vm_disk_gb }}"
            type: thin
            autoselect_datastore: true
```

Run it:

```bash
ansible-playbook playbooks/vm_create_from_template.yml -e @group_vars/vmware.yml --ask-vault-pass
```

### Power operations

```yaml
- name: Ensure VM powered off
  hosts: localhost
  gather_facts: false
  collections: [community.vmware]
  vars_files:
    - ../group_vars/vmware.yml
  tasks:
    - name: Ensure VM is powered off
      community.vmware.vmware_guest_powerstate:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: "{{ vcenter_validate_certs }}"
        name: "web-01"
        state: powered-off
```

### Snapshot create

```yaml
- name: Create snapshot before patch
  hosts: localhost
  gather_facts: false
  collections: [community.vmware]
  vars_files:
    - ../group_vars/vmware.yml
  vars:
    vm_name: "web-01"
    snap_name: "pre_patch_{{ lookup('pipe', 'date +%Y%m%d') }}"
  tasks:
    - community.vmware.vmware_guest_snapshot:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: "{{ vcenter_validate_certs }}"
        name: "{{ vm_name }}"
        state: present
        snapshot_name: "{{ snap_name }}"
        description: "Automated snapshot before patching"
```

## Compliance & STIG notes

- Prefer read-only service accounts for discovery and audit playbooks.
- Use `--check --diff` for previews and always schedule changes within approved windows.
- Consider integrating OpenSCAP or other image-level compliance tools into guest pipelines.

## Running & tagging

Playbooks are tagged; filter by function during runs. Example:

```bash
ansible-playbook playbooks/vmware_master.yml --tags "power,snapshot" -e @group_vars/vmware.yml
```

Tips:

- Use `--limit` to scope operations
- Start with `--check` where supported
- Use `serial` for bulk operations to reduce blast radius

## Troubleshooting

- TLS / certificate errors: check `vcenter_validate_certs` and CA chain.
- Session / token errors: verify account permissions and API limits.
- Module compatibility: ensure `community.vmware` and `vmware.vmware` versions match your vCenter.

## Contributing

- Document required variables in the playbook header or role README.
- Include sanitized `-vvv` logs and environment details in issues or PRs.

## References

- community.vmware docs: <https://docs.ansible.com/ansible/latest/collections/community/vmware/index.html>
- vmware.vmware collection: <https://github.com/ansible-collections/vmware.vmware>
- Intro to Ansible on VMware: <https://docs.ansible.com/ansible/4/scenario_guides/vmware_scenarios/vmware_intro.html>

## License

MIT (unless otherwise noted in specific roles or upstream modules).

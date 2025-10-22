# VMware Automation (Ansible)

> **BLUF:** This folder contains production‑ready Ansible playbooks and roles to automate common VMware vSphere operations (vCenter, ESXi, clusters, VMs, networking, snapshots, RBAC, and security/STIG tasks). Use these playbooks to provision, configure, audit, and operate VMware at scale with DoD/NIST/STIG‑minded defaults.

---

## What’s in here

Typical scenarios supported by the playbooks in this folder include:

- vCenter & ESXi inventory and info‑gathering
- Datacenter/cluster baseline tasks (create/update clusters, add hosts)
- VM lifecycle (create from template/ISO, reconfigure CPU/RAM/Disk/NICs, customize guest)
- Power & snapshot operations (on/off/reset, create/restore/delete snapshots)
- Templates & content library operations
- RBAC hardening (users/roles, least‑privilege, break‑glass)
- Network & storage tasks (portgroups, vSwitch/Distributed Switch tweaks, datastore ops)
- Security baselines (disable SSH where required, enforce VM encryption/secure‑boot where supported, audit for STIG controls)
- Compliance, audit, and reporting helpers (facts collection, drift checks)

> **Tip:** Run `ls -1 *.yml` in this folder to see the available playbooks and start points. Many playbooks are organized with clear names like `vm_create.yml`, `vm_power.yml`, `snapshot_manage.yml`, `cluster_baseline.yml`, `vcenter_deploy.yml`, `stig_audit.yml`, etc.

---

## Prerequisites

- **Ansible** 2.14+ (Ansible Automation Platform 2.x is fine)
- **Collections** (both are commonly used across VMware playbooks):
  - `community.vmware` – broad community‑supported VMware modules
  - `vmware.vmware` – Red Hat Ansible Certified Content for VMware (REST modules)
- **Python packages** (installed on the control node): `pyvmomi`, `requests`

Install requirements:

```bash
ansible-galaxy collection install community.vmware vmware.vmware
python -m pip install --upgrade pyvmomi requests
```

> If you’re running on Ansible Automation Platform, make sure your Execution Environment contains these collections and Python wheels.

---

## Credentials & Connectivity

Define your vSphere access in **vaulted vars** or environment variables. Example (group_vars or extra vars):

```yaml
vcenter_hostname: "vcsa.example.mil"
vcenter_username: "DOD\svc_ansible"
vcenter_password: "{{ lookup('env', 'VCENTER_PASSWORD') }}"
vcenter_validate_certs: false  # true in production with trusted CA
```

Recommended practices:

- Prefer **environment variables** + **Ansible Vault** for secrets; never commit passwords.
- For most tasks use `hosts: localhost` with `connection: local` and API‑driven modules.
- When acting **against many VMs**, consider `serial` to rate‑limit operations.

---

## Inventory & Layout

Minimal inventory (API‑only workflows):

```ini
[localhost]
127.0.0.1 ansible_connection=local
```

Suggested structure (excerpt):

```
vmware/
├── group_vars/
│   └── vmware.yml                # shared defaults (vCenter host, auth, datacenter)
├── host_vars/                    # per‑target overrides (optional)
├── files/                        # ISO, OVF, templates metadata (optional)
├── templates/                    # cloud‑init, customization specs, notes
├── roles/                        # reusable role(s) for vm CRUD, RBAC, compliance
└── *.yml                         # playbooks (vm_create, vm_power, snapshot, etc.)
```

---

## Common Variables

```yaml
# group_vars/vmware.yml
vcenter_hostname: "vcsa.example.mil"
vcenter_username: "DOD\svc_ansible"
vcenter_password: "{{ vault_vcenter_password }}"
vcenter_validate_certs: true

# Placement
vsphere_datacenter: "DC1"
vsphere_cluster: "Prod-Cluster"
vsphere_datastore: "Datastore01"
vsphere_network: "VM Network"

# VM Defaults
vm_guest_os: "rhel9_64Guest"
vm_folder: "Prod/Servers"
vm_hw_version: 20
vm_cpu: 4
vm_ram_mb: 8192
vm_disk_gb: 60
```

---

## Usage Examples

### 1) Create a VM from a template (with customization)

```yaml
---
- name: Create VM from template
  hosts: localhost
  gather_facts: false
  collections:
    - community.vmware
  vars:
    vm_name: web-01
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
        name: "{{ vm_name }}"
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
ansible-playbook vm_create_from_template.yml -e @group_vars/vmware.yml --ask-vault-pass
```

### 2) Power operations (safe by default)

```yaml
- name: Power operations
  hosts: localhost
  gather_facts: false
  collections: [community.vmware]
  vars: { vm_name: "web-01" }
  tasks:
    - name: Ensure VM is powered off
      community.vmware.vmware_guest_powerstate:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: "{{ vcenter_validate_certs }}"
        name: "{{ vm_name }}"
        state: powered-off
```

### 3) Snapshot management

```yaml
- name: Snapshot create with retention tag
  hosts: localhost
  gather_facts: false
  collections: [community.vmware]
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

### 4) RBAC hardening (role/user examples)

Use modules from `community.vmware`/`vmware.vmware` to create least‑privilege roles and bind to users/groups. Keep **break‑glass** accounts separate and vaulted.

---

## Compliance & STIG Notes

- Prefer **read‑only service accounts** for discovery playbooks.
- Enable **change windows** and use `--check` + `--diff` for previews.
- Where applicable, disable ESXi SSH and enforce secure defaults (e.g., VM encryption, secure‑boot, signed drivers).
- Consider pairing with OpenSCAP/SCAP Security Guide in your guest OS pipelines and keeping evidence ZIPs in your artifact store.

---

## Running & Tagging

All playbooks are **tagged** so you can filter by function:

```bash
ansible-playbook vmware_master.yml --tags "power,snapshot" -e @group_vars/vmware.yml
```

Safety:

- Use `--limit` to scope by host group or a CSV list of VMs.
- Start with `--check` (dry run) where modules support it.
- Use `serial` in destructive workflows.

---

## Troubleshooting

- `validate_certs: false` is convenient for labs; **use true in prod** with a trusted CA.
- If you see session or token errors, ensure the account has **Global Permissions** in vCenter and avoid exceeding API limits.
- For REST modules (`vmware.vmware_rest`), confirm the vCenter version supports the given endpoint.

---

## Contributing

PRs and issues welcome. Please include:

- The exact playbook, variables, and sanitized logs (`-vvv`) that reproduce the issue.
- Environment details (vCenter/ESXi versions, Ansible version, collections versions).

---

## References

- Ansible **community.vmware** collection (modules & usage): https://docs.ansible.com/ansible/latest/collections/community/vmware/index.html
- Ansible **vmware.vmware** (certified content): https://github.com/ansible-collections/vmware.vmware
- Intro to Ansible on VMware: https://docs.ansible.com/ansible/4/scenario_guides/vmware_scenarios/vmware_intro.html

---

## License

MIT (unless otherwise noted in specific roles or upstream modules).


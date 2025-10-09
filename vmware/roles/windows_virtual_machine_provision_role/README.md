# vmware_win_provision (role)

Clone a Windows VM from a vSphere template, place it on the desired portgroup, and join it to Active Directory.
Supports **two domain-join methods**:
1) via `community.vmware.vmware_guest` customization (sysprep) and
2) via Ansible `microsoft.ad.membership` over WinRM.

## Requirements
- Ansible 2.15+
- Collections: community.vmware, ansible.windows, microsoft.ad (see `requirements.yml`)
- Control node Python: `pyvmomi` for VMware modules
- Windows template prepared with:
  - VMware Tools
  - WinRM enabled (for `join_method: ansible`)
  - Local Administrator credentials available or custom image account

## Variables (see `defaults/main.yml` for all)
- vCenter: `vcenter_hostname`, `vcenter_username`, `vcenter_password`, `vcenter_datacenter`, `vcenter_cluster`, `vcenter_folder`, `vcenter_datastore`
- Template + VM: `vm_template`, `vm_name`, `vm_cpu`, `vm_memory_mb`, `vm_disk_gb`, `vm_networks`
- Join method: `join_method` = `vmware` or `ansible`
- AD: `ad_domain`, `ad_domain_user`, `ad_domain_password`, `ad_domain_ou`
- WinRM (for ansible method): `win_user`, `win_password`, `win_port`, `win_use_https`, `win_validate_certs`

## Example Play
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vmware_win_provision
      vars:
        vcenter_hostname: "vcenter.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false
        vcenter_datacenter: "DC1"
        vcenter_cluster: "Cluster01"
        vcenter_folder: "/DC1/vm/Prod"
        vcenter_datastore: "vsanDatastore"

        vm_template: "Win2019-Base"
        vm_name: "win2019-ans-001"
        vm_networks:
          - name: "Prod-VLAN10"
            type: dhcp
            device_type: vmxnet3

        # Choose one method:
        join_method: "ansible"   # or "vmware"

        ad_domain: "example.local"
        ad_domain_user: "EXAMPLE\\joinuser"
        ad_domain_password: "{{ vault_ad_join_password }}"
        ad_domain_ou: "OU=Servers,DC=example,DC=local"

        # Needed for ansible method (WinRM)
        win_user: "Administrator"
        win_password: "{{ vault_local_admin_password }}"
```

## Notes
- If using `join_method: vmware`, `community.vmware.vmware_guest` will pass sysprep values (`customization.joindomain`, `domainadmin`, `domainadminpassword`) to vCenter, which joins the domain during guest customization.
- If using `join_method: ansible`, the role waits for WinRM and runs `microsoft.ad.membership` on the new VM, then reboots.
- `vm_networks` attaches the clone to the specified **portgroup**. Ensure the portgroup exists (vSS or VDS) and hosts in the cluster have access.
- For static IP addressing, set `type: static` and provide `ip`, `netmask`, `gateway`, and optional `dns_servers` in the first `vm_networks` entry.

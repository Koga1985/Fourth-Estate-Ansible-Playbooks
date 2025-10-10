# template_pipeline (role)

Keep **gold images** fresh by ingesting **Packer outputs** (OVA/OVF) into a vSphere
**Content Library**, **versioning** items, updating a **pin/alias** (like `current`),
and **pruning** older versions. Produces a JSON report.

## Requirements
- Controller/jump host with **PowerShell Core (`pwsh`)** and **VMware PowerCLI**
- vCenter permissions for Content Library and item/import operations
- If creating a library, specify a valid **datastore**

## Variables (see `defaults/main.yml`)
```yaml
vcenter_hostname: "vcsa.example.local"
vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
vcenter_validate_certs: false

content_library:
  name: "Gold-Images"
  create_if_missing: true
  datastore: "vsanDatastore"
  publication: false
  description: "Golden images managed by template_pipeline"

intake:
  - name: "ubuntu-24.04"
    version: ""                 # blank => auto date (yyyy.MM.dd)
    source_type: "ova"          # ova | ovf
    source_path: "/mnt/packer/out/ubuntu-24.04-2025.10.10.ova"
    pin_alias: "current"        # create/update <name>-current alias
    keep_versions: 3            # keep last 3 versions per template

report_path: "/tmp/template-pipeline-report.json"
```

## Example Play
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: template_pipeline
      vars:
        vcenter_hostname: "vcsa.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false

        content_library:
          name: "Gold-Images"
          create_if_missing: true
          datastore: "vsanDatastore"

        intake:
          - { name: "win2022-core", version: "", source_type: "ova", source_path: "/exports/win2022-core.ova", pin_alias: "current", keep_versions: 4 }
          - { name: "ubuntu-24.04", version: "", source_type: "ovf", source_path: "/exports/ubuntu-24.04/", pin_alias: "current", keep_versions: 3 }

        report_path: "/tmp/template-pipeline-report.json"
```

## Notes
- **Versioning**: item names are `<name>-<version>`; alias is `<name>-<alias>` (default alias: `current`).
- **Version sort** is lexicographic; use `yyyy.MM.dd` or semver-like names for correct pruning order.
- **Import** expects local filesystem paths on the controller host.
- To convert a Content Library item to a **VM Template**, deploy from the library then mark as template,
  or use downstream automation—this role focuses on intake, versioning, and catalog hygiene.

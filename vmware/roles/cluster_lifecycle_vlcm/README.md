# cluster_lifecycle_vlcm

Configure a vSphere cluster’s **vLCM Desired Image** using **PowerCLI**, then run **health** and **compliance** checks and (optionally) **remediate**. The role also writes a compact **JSON compliance report** to disk.

> Designed to live in `Koga1985/Ansible-Playbooks/vmware/roles/cluster_lifecycle_vlcm`.

---

## Features

- ✅ Set/Update **Desired Image**:
  - Base Image (ESXi release), optional **Vendor AddOn**, optional **Components**
  - Or import a previously **exported desired-state JSON**
- 🔎 **Pre-checks**: run `Test-LcmClusterHealth` (hardware/firmware/compat signals)
- 📋 **Compliance**: run `Test-LcmClusterCompliance` and save a JSON report
- 🛠️ **Remediation (optional)**: `Set-Cluster -Remediate -AcceptEULA`
- 🧩 Safe by default: **remediation off** unless explicitly enabled

---

## Requirements

- Ansible ≥ **2.15**
- A controller/jump host with:
  - **PowerShell Core** (`pwsh`)
  - **VMware PowerCLI** (12.1+ recommended for vLCM cmdlets)
- vCenter privileges to manage **Lifecycle Manager** and **Cluster remediation**
- Network reachability from the controller to vCenter

> This role drives PowerCLI via `command:` — no Ansible VMware collection is required for the core workflow.

---

## Variables

All variables can be set in your play or inventory; defaults are in `defaults/main.yml`.

```yaml
# vCenter connection
vcenter_hostname: ""           # e.g., "vcsa.example.local"
vcenter_username: ""           # e.g., "administrator@vsphere.local"
vcenter_password: ""           # secret (prefer vault/env lookup)
vcenter_validate_certs: false  # set true if you use trusted certs

# Target cluster
cluster_name: ""               # e.g., "Compute-Cluster"

# Option A: Build Desired Image from parts
vlcm_image: {}                 # if empty, no change unless Option B provided
# Example:
# vlcm_image:
#   base_image_version: "8.0 U3c"   # matches Get-LcmImage -Type BaseImage -Version
#   vendor_addon_name: ""           # fuzzy match on DisplayName
#   components: ["VMware Tools"]    # fuzzy match on DisplayName/Version

# Option B: Import a saved desired-state JSON (Export-LcmClusterDesiredState)
vlcm_desired_state_file: ""    # absolute path on controller (e.g., "/tmp/desired.json")

# Health/Compliance/Remediation
run_prechecks: true            # Test-LcmClusterHealth before compliance
remediate: false               # if true => Set-Cluster -Remediate -AcceptEULA
compliance_report_path: "/tmp/{{ cluster_name }}-vlcm-compliance.json"
```

### Choosing between Option A & Option B

- **Option A (vlcm_image)**: good for declarative “parts” in vars/repos.
- **Option B (vlcm_desired_state_file)**: good for importing a previously **exported** spec (golden image) verbatim.
- If **both** are set, Option B (file) takes precedence.

---

## Example Play

```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: cluster_lifecycle_vlcm
      vars:
        vcenter_hostname: "vcsa.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false
        cluster_name: "Compute-Cluster"

        # Option A: build image from parts
        vlcm_image:
          base_image_version: "8.0 U3c"
          vendor_addon_name: ""
          components: ["VMware Tools"]

        # Option B (instead of Option A):
        # vlcm_desired_state_file: "/tmp/desired-state.json"

        run_prechecks: true
        remediate: false
        compliance_report_path: "/tmp/Compute-Cluster-vlcm-compliance.json"
```

---

## What gets created

- **Desired Image** set on the target cluster (if provided)
- **Compliance JSON** written to `compliance_report_path`, like:

```json
{
  "vcenter": "vcsa.example.local",
  "cluster": "Compute-Cluster",
  "precheck": { /* Test-LcmClusterHealth output */ },
  "compliance": { /* Test-LcmClusterCompliance output */ },
  "remediated": false,
  "timestamp": "2025-10-10T12:34:56"
}
```

Use this file in CI/CD or change-management reports.

---

## Operational Notes

- **Dry safety**: `remediate: false` by default. Turn on deliberately.
- **Maintenance Mode**: vLCM remediation may need host maintenance windows. The role doesn’t toggle MM; vLCM manages remediation steps, evacuations, and reboots if needed.
- **Matching images**:
  - `base_image_version` must exist via `Get-LcmImage -Type BaseImage`.
  - `vendor_addon_name` and `components` are **fuzzy** matched by display name/version (first match wins). Pin more precisely if you have multiple candidates.
- **Image-managed prerequisite**: If the cluster isn’t image-managed, `Set-Cluster` switches it to Desired Image automatically when a valid image is supplied.

---

## Security & Secrets

- Prefer `ansible-vault` or environment lookups for `vcenter_password`:
  ```yaml
  vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
  vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
  ```
- Consider setting `vcenter_validate_certs: true` when your VCSA uses trusted certs.

---

## Troubleshooting

- **PowerCLI not found**: Ensure `pwsh` is on PATH and `Install-Module VMware.PowerCLI` has been done on the controller/jump host.
- **Image lookups are empty**:
  - Validate strings with `Get-LcmImage` interactively to see exact names/versions.
  - Vendor AddOn availability depends on hardware vendor integration and LCM depot sync.
- **EULA blocks remediation**: This role passes `-AcceptEULA`. If you still see prompts, check interactive policies on your host.
- **Compliance remains out-of-date**:
  - Ensure the cluster can reach depots (online or cached).
  - Check hardware compatibility and firmware requirements flagged by **pre-checks**.

---

## Roadmap / Extensions

- “Plan-only” mode that resolves the image and **prints the diff** without applying.
- Integration with **host maintenance** guardrails (e.g., abort during business hours).
- Export the in-use image to JSON for golden-image **promotion** between environments.

---

## License

MIT — see `meta/main.yml`.

---

## Author

Dewain Smith — contributions welcome!

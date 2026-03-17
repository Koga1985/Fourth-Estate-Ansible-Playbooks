# pa_objects_catalog

Manages the Palo Alto Networks objects catalog: administrative tags, address objects, address groups, service objects, and service groups. Includes a guarded prune phase that can identify and optionally delete objects no longer in the desired catalog, with a dry-run mode to prevent accidental removals.

## Requirements

- Ansible 2.12+
- `paloaltonetworks.panos` collection:
  ```bash
  ansible-galaxy collection install paloaltonetworks.panos
  ```
- PAN-OS credentials with configuration commit rights
- For Panorama-managed devices: valid `device_group`

## Role Variables

### Connection and Scope

| Variable | Default | Description |
|----------|---------|-------------|
| `pa_use_panorama` | `false` | Set to `true` when targeting a Panorama-managed device. |
| `device_group` | `null` | Panorama device group name (Panorama mode only). |
| `vsys` | `"vsys1"` | Virtual system for direct firewall management. |

### Output and Commit

| Variable | Default | Description |
|----------|---------|-------------|
| `artifacts_dir` | `"/tmp/pan-artifacts"` | Directory for prune report and diff artifacts. |
| `commit_after_changes` | `true` | Commit all changes after applying the catalog. |
| `commit_description` | `"Apply objects catalog via Ansible"` | Commit description string. |

### Tags

`tags` is a list of administrative tag definitions:

| Key | Description |
|-----|-------------|
| `name` | Tag name. Required. |
| `color` | PAN-OS color name (e.g. `color1`, `color14`). |
| `comments` | Tag description. |

```yaml
tags:
  - name: "dmz"
    color: color6
    comments: "DMZ zone tag"
  - name: "critical-asset"
    color: color1
```

### Address Objects

`address_objects` is a list of address object definitions:

| Key | Description |
|-----|-------------|
| `name` | Object name. Required. |
| `value` | IP address, prefix, FQDN, or IP range. Required. |
| `type` | `ip-netmask`, `ip-range`, `fqdn`. Default: `ip-netmask`. |
| `description` | Object description. |
| `tag` | List of tags to apply. |

```yaml
address_objects:
  - name: "web-server-01"
    value: "10.10.1.10/32"
    type: ip-netmask
    tag: ["dmz"]
  - name: "corp-subnet"
    value: "192.168.0.0/16"
    type: ip-netmask
```

### Address Groups

`address_groups` is a list of address group definitions:

| Key | Description |
|-----|-------------|
| `name` | Group name. Required. |
| `static_value` | List of address object names (static group). |
| `dynamic_value` | Tag-based filter expression (dynamic group). |
| `description` | Group description. |
| `tag` | List of tags to apply. |

```yaml
address_groups:
  - name: "web-servers"
    static_value: ["web-server-01", "web-server-02"]
    description: "All web servers in DMZ"
```

### Service Objects

`service_objects` is a list of service definitions:

| Key | Description |
|-----|-------------|
| `name` | Service name. Required. |
| `protocol` | `tcp` or `udp`. Required. |
| `destination_port` | Port or port range (e.g. `443`, `8080-8090`). Required. |
| `source_port` | Optional source port restriction. |
| `description` | Service description. |

```yaml
service_objects:
  - name: "svc-https-8443"
    protocol: tcp
    destination_port: "8443"
    description: "Custom HTTPS on 8443"
```

### Service Groups

`service_groups` is a list of service group definitions:

| Key | Description |
|-----|-------------|
| `name` | Group name. Required. |
| `value` | List of service object names. Required. |

```yaml
service_groups:
  - name: "svc-web"
    value: ["service-http", "service-https", "svc-https-8443"]
```

### Prune Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `prune.dry_run` | `true` | When `true`, reports objects that would be deleted without removing them. Set to `false` to enable actual deletion. |
| `prune.allow_delete` | `false` | Master switch: objects are only deleted when both `dry_run: false` and `allow_delete: true`. |
| `prune.protected_names` | `["any","application-default"]` | List of object names that are never pruned regardless of other settings. |

## Dependencies

None.

## Example Playbook

```yaml
---
- name: Apply Palo Alto objects catalog
  hosts: palo_alto_firewalls
  gather_facts: false
  connection: local

  vars:
    vsys: vsys1
    artifacts_dir: "/opt/pan/artifacts"
    commit_after_changes: true

    tags:
      - name: "production"
        color: color1
      - name: "dmz"
        color: color6

    address_objects:
      - name: "app-server-01"
        value: "10.20.1.10/32"
        tag: ["production"]
      - name: "db-subnet"
        value: "10.30.0.0/24"
        tag: ["production"]

    address_groups:
      - name: "app-servers"
        static_value: ["app-server-01"]

    service_objects:
      - name: "svc-app-tcp-8080"
        protocol: tcp
        destination_port: "8080"

    prune:
      dry_run: true
      allow_delete: false
      protected_names: ["any", "application-default", "svc-app-tcp-8080"]

  roles:
    - role: palo_alto/roles/pa_objects_catalog
```

## Output Artifacts

- `{{ artifacts_dir }}/prune_report.txt` — Lists objects present on the device but absent from the catalog, with deletion status (would-delete or deleted).

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

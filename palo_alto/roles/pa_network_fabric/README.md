# pa_network_fabric

Builds and manages the full network fabric on Palo Alto Networks firewalls and Panorama, including Ethernet/aggregate/loopback interfaces, security zones, virtual routers, static and dynamic routes, and IPSec/GRE tunnels. An optional commit step applies all changes at the end of the run.

## Requirements

- Ansible 2.12+
- `paloaltonetworks.panos` collection:
  ```bash
  ansible-galaxy collection install paloaltonetworks.panos
  ```
- PAN-OS credentials with configuration commit rights
- For Panorama-managed devices: Panorama admin credentials and a valid `device_group` / `template` / `template_stack`

## Role Variables

### Connection and Scope

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `pa_use_panorama` | `false` | No | Set to `true` when targeting a Panorama-managed device. Changes the scope of all API calls. |
| `device_group` | `null` | No | Panorama device group name (Panorama mode only). |
| `vsys` | `"vsys1"` | No | Virtual system context for direct firewall management. |
| `template` | `null` | No | Panorama template name for network configuration (Panorama mode only). |
| `template_stack` | `null` | No | Panorama template stack name (Panorama mode only). |

### Commit

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `commit_after_changes` | `true` | No | Commit all changes to the running configuration after applying the fabric. Set to `false` to stage changes without committing (useful when combining with other roles). |
| `commit_description` | `"Apply network fabric via Ansible"` | No | Commit description string. |

### Interfaces

`interfaces` is a list of interface definition dictionaries. Each entry supports the following keys (all optional unless noted):

| Key | Description |
|-----|-------------|
| `name` | Interface name (e.g. `ethernet1/1`). Required. |
| `mode` | Interface mode: `layer3`, `layer2`, `virtual-wire`, `tap`, `ha`, `decrypt-mirror`. |
| `ip` | List of IP addresses with prefix length for Layer 3 interfaces. |
| `zone` | Security zone to assign. |
| `comment` | Interface description. |
| `mtu` | MTU value. |
| `link_speed` | Link speed (`10`, `100`, `1000`, `auto`). |
| `link_duplex` | Link duplex (`full`, `half`, `auto`). |

```yaml
interfaces:
  - name: ethernet1/1
    mode: layer3
    ip: ["10.0.0.1/30"]
    zone: untrust
    comment: "WAN uplink"
  - name: ethernet1/2
    mode: layer3
    ip: ["192.168.10.1/24"]
    zone: trust
```

### Zones

`zones` is a list of security zone definition dictionaries:

| Key | Description |
|-----|-------------|
| `name` | Zone name. Required. |
| `mode` | Zone mode: `layer3`, `layer2`, `virtual-wire`, `tap`, `external`. |
| `enable_user_identification` | Enable User-ID for the zone. |

```yaml
zones:
  - name: trust
    mode: layer3
  - name: untrust
    mode: layer3
```

### Virtual Routers

`virtual_routers` is a list of virtual router definitions:

| Key | Description |
|-----|-------------|
| `name` | Virtual router name. Required. |
| `interfaces` | List of interface names to assign to this virtual router. |

```yaml
virtual_routers:
  - name: default
    interfaces: ["ethernet1/1", "ethernet1/2"]
```

### Static Routes

`static_routes` is a list of static route definitions:

| Key | Description |
|-----|-------------|
| `name` | Route name. Required. |
| `destination` | Destination prefix (e.g. `0.0.0.0/0`). Required. |
| `nexthop` | Next-hop IP address. Required. |
| `virtual_router` | Virtual router to add the route to. Default: `default`. |
| `admin_distance` | Administrative distance. |
| `metric` | Route metric. |

```yaml
static_routes:
  - name: default-route
    destination: "0.0.0.0/0"
    nexthop: "10.0.0.2"
    virtual_router: default
```

### Tunnels

`tunnels` is a list of tunnel interface definitions (IPSec or GRE):

| Key | Description |
|-----|-------------|
| `name` | Tunnel interface name (e.g. `tunnel.1`). Required. |
| `ip` | Optional IP address for the tunnel interface. |
| `zone` | Security zone for the tunnel. |
| `comment` | Description. |

```yaml
tunnels:
  - name: tunnel.1
    ip: ["10.100.0.1/30"]
    zone: vpn
    comment: "Site-to-site VPN to Branch A"
```

## Dependencies

None.

## Example Playbook

```yaml
---
- name: Apply Palo Alto network fabric
  hosts: palo_alto_firewalls
  gather_facts: false
  connection: local

  vars:
    provider:
      ip_address: "{{ inventory_hostname }}"
      username: "{{ vault_pa_user }}"
      password: "{{ vault_pa_password }}"

    vsys: vsys1
    commit_after_changes: true
    commit_description: "Ansible fabric run {{ lookup('pipe','date +%Y%m%d-%H%M') }}"

    interfaces:
      - name: ethernet1/1
        mode: layer3
        ip: ["203.0.113.1/30"]
        zone: untrust
      - name: ethernet1/2
        mode: layer3
        ip: ["10.0.1.1/24"]
        zone: trust

    zones:
      - name: untrust
        mode: layer3
      - name: trust
        mode: layer3

    virtual_routers:
      - name: default
        interfaces: ["ethernet1/1", "ethernet1/2"]

    static_routes:
      - name: default-route
        destination: "0.0.0.0/0"
        nexthop: "203.0.113.2"
        virtual_router: default

  roles:
    - role: palo_alto/roles/pa_network_fabric
```

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team

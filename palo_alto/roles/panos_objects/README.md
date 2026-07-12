# panos_objects

Panos Objects role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `palo_alto/README.md`

## Requirements

- Ansible 2.15+
- Collection: `paloaltonetworks.panos`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `panos_provider` | `(see defaults/main.yml)` | No | PAN-OS provider connection details |
| `panos_address_objects` | `(see defaults/main.yml)` | No | Address objects (IP, netmask) |
| `panos_fqdn_objects` | `(see defaults/main.yml)` | No | FQDN address objects |
| `panos_ip_range_objects` | `(see defaults/main.yml)` | No | IP range objects |
| `panos_ip_wildcard_objects` | `[]` | No | IP wildcard objects |
| `panos_static_address_groups` | `(see defaults/main.yml)` | No | Static address groups |
| `panos_dynamic_address_groups` | `(see defaults/main.yml)` | No | Dynamic address groups (filter-based) |
| `panos_tcp_service_objects` | `(see defaults/main.yml)` | No | TCP service objects |
| `panos_udp_service_objects` | `(see defaults/main.yml)` | No | UDP service objects |
| `panos_service_groups` | `(see defaults/main.yml)` | No | Service groups |
| `panos_custom_applications` | `(see defaults/main.yml)` | No | Custom application objects |
| `panos_application_groups` | `(see defaults/main.yml)` | No | Application groups |
| `panos_application_filters` | `(see defaults/main.yml)` | No | Application filters |
| `panos_tags` | `(see defaults/main.yml)` | No | Tags for object categorization |
| `panos_edl_ip_lists` | `(see defaults/main.yml)` | No | External Dynamic Lists (IP) |
| `panos_edl_url_lists` | `(see defaults/main.yml)` | No | External Dynamic Lists (URL) |
| `panos_edl_domain_lists` | `(see defaults/main.yml)` | No | External Dynamic Lists (Domain) |
| `panos_custom_url_categories` | `(see defaults/main.yml)` | No | Custom URL categories |
| `panos_schedules` | `(see defaults/main.yml)` | No | Schedule objects |
| `panos_registered_ips` | `[]` | No | Registered IPs (for region-based policies) |
| `panos_security_zones` | `(see defaults/main.yml)` | No | Security zones |
| `panos_log_forwarding_profiles` | `(see defaults/main.yml)` | No | Log forwarding profiles |

## Example Playbook

```yaml
---
- name: Panos Objects
  hosts: localhost
  gather_facts: false
  roles:
    - role: palo_alto/roles/panos_objects
```

## Tags

| Tag | Description |
|-----|-------------|
| `address_groups` | Tasks tagged `address_groups` |
| `addresses` | Tasks tagged `addresses` |
| `application_filters` | Tasks tagged `application_filters` |
| `application_groups` | Tasks tagged `application_groups` |
| `applications` | Tasks tagged `applications` |
| `domain` | Tasks tagged `domain` |
| `dynamic` | Tasks tagged `dynamic` |
| `edl` | Tasks tagged `edl` |
| `fqdn` | Tasks tagged `fqdn` |
| `ip` | Tasks tagged `ip` |
| `log_forwarding` | Tasks tagged `log_forwarding` |
| `objects` | Tasks tagged `objects` |
| `range` | Tasks tagged `range` |
| `regions` | Tasks tagged `regions` |
| `registered_ips` | Tasks tagged `registered_ips` |
| `schedules` | Tasks tagged `schedules` |
| `service_groups` | Tasks tagged `service_groups` |
| `services` | Tasks tagged `services` |
| `static` | Tasks tagged `static` |
| `tags` | Tasks tagged `tags` |
| `tcp` | Tasks tagged `tcp` |
| `udp` | Tasks tagged `udp` |
| `url` | Tasks tagged `url` |
| `url_categories` | Tasks tagged `url_categories` |
| `wildcard` | Tasks tagged `wildcard` |
| `zones` | Tasks tagged `zones` |

## License

MIT

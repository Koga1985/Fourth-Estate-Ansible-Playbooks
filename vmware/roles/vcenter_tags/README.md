# vcenter_tags (role)

Create/maintain **tag categories & tags** in vCenter and **apply/enforce** a
golden tag set on objects.

## Highlights
- Idempotently creates categories (cardinality, associable types) and tags.
- Applies tag assignments to objects.
- **Exclusive mode** per-object: remove any other tags from that category that
  appear in your defined golden set.

## Requirements
- Ansible >= 2.15
- Collection: `community.vmware` (see `requirements.yml`)

## Example
```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: vcenter_tags
      vars:
        vcenter_hostname: "vcenter.example.local"
        vcenter_username: "{{ lookup('env','VCENTER_USERNAME') }}"
        vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
        vcenter_validate_certs: false

        tag_categories:
          - { name: "environment", description: "Env", cardinality: MULTIPLE, associable_types: ["VirtualMachine","Datastore"] }
          - { name: "app_tier", description: "Tier", cardinality: SINGLE, associable_types: ["VirtualMachine"] }

        tags:
          - { category: "environment", tags: ["prod","dev","qa"] }
          - { category: "app_tier", tags: ["web","app","db"] }

        tag_bindings:
          - object_type: "VirtualMachine"
            object_name: "app01"
            assignments:
              - { category: "environment", tags: ["prod"] }
              - { category: "app_tier", tags: ["app"] }
            enforce_exclusive: true
```

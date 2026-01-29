# infoblox_dhcp_failover

Create/update **Infoblox DHCP failover** peerings and optionally attach them to networks, shared networks, and ranges.

- Supports **load-balance** (with `split`) and **hot-standby**
- Auto-detects WAPI endpoint: `dhcpfailover` vs `failoverassociation`
- Best-effort across NIOS versions; records results to a JSON artifact

## Requirements
- Ansible collection: `infoblox.nios_modules`
- WAPI user with DHCP failover admin rights

## Variables (defaults)
```yaml
nios_host: ""
nios_username: ""
nios_password: ""
nios_validate_certs: false
nios_wapi_version: "v2.12"

network_view: "default"
artifact_dir: "/tmp/infoblox-dhcp-failover"
dhcp_failover_pairs: []
```

## Pair schema examples
```yaml
dhcp_failover_pairs:
  # Load-balance with 60/40 split
  - name: "Branch-Pair-01"
    mode: "load_balance"                 # "load_balance" | "hot_standby"
    primary_member: "gridmember-a01"     # member "name" or "host_name"
    secondary_member: "gridmember-a02"
    split: 153                           # 0–255 (128 ≈ 50/50)
    max_outage: 3600
    enable_bidir: true
    comment: "Branch site 01 LB pair"
    networks: ["10.10.1.0/24","10.10.2.0/24"]      # optional
    shared_networks: ["Branch01-Shared"]           # optional
    ranges: ["10.10.1.50-10.10.1.200"]             # optional

  # Hot-standby with longer outage tolerance
  - name: "DC-HS-01"
    mode: "hot_standby"
    primary_member: "dc-dhcp-1"
    secondary_member: "dc-dhcp-2"
    max_outage: 7200
    enable_bidir: true
    comment: "Datacenter hot-standby"
    networks: ["10.20.0.0/23"]
```

## Example Playbook
```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: infoblox_dhcp_failover
      vars:
        nios_host: "nios.example.local"
        nios_username: "{{ lookup('env','NIOS_USER') }}"
        nios_password: "{{ lookup('env','NIOS_PASS') }}"
        nios_validate_certs: false
        nios_wapi_version: "v2.12"
        network_view: "default"
        dhcp_failover_pairs:
          - name: "Branch-Pair-01"
            mode: "load_balance"
            primary_member: "gridmember-a01"
            secondary_member: "gridmember-a02"
            split: 153
            networks: ["10.10.1.0/24"]
          - name: "DC-HS-01"
            mode: "hot_standby"
            primary_member: "dc-dhcp-1"
            secondary_member: "dc-dhcp-2"
            max_outage: 7200
```

## Outputs
- `dhcp_failover_summary.json` — selected endpoint, members, and before/after snapshot of failover associations

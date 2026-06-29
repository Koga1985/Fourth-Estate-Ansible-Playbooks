# Juniper Junos STIG (`junos_stig`)

Hardens **Juniper Junos** devices to the DISA **Junos NDM** (`JUNI-ND-*`) and
**Junos Router** (`JUNI-RT-*`) STIGs via the certified **`junipernetworks.junos`**
collection (set-format config over NETCONF/CLI).

## Why "grab and go"
* **Safe by default**: `apply_changes=false` loads the candidate config in check
  mode and shows the **diff without committing**. `apply_changes=true` commits.
* Per-host JSON evidence artifact.

## Quick start
```bash
cd juniper/roles/junos_stig/playbooks
ansible-galaxy collection install -r ../../../juniper/requirements.yml
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml                       # DRY-RUN (candidate diff)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE (commit)
cat /tmp/junos-stig-artifacts/mx-01_junos_stig.json
```

## Controls
NDM: DoD banner, login retry/lockout, idle timeout, password policy, AAA
(TACACS+), SSHv2-only ciphers/MACs, Telnet off, remote syslog, authenticated NTP.
Router: BGP neighbor authentication + max-prefix, OSPF interface MD5 auth (both
data-driven via `junos_bgp_peers` / `junos_ospf_auth_interfaces`).

## ⚠️ Pre-flight
* Restricting SSH/AAA can affect access — keep console access during the change.
* Routing-plane tasks run only when peers/interfaces are defined.

## Tags
`--tags ndm`, `rtr`, `report`, plus `stig_cat2` / `stig_cat3` and per-rule tags.

# Cisco ISE NDM STIG (`cisco_ise_stig`)

Production-ready Ansible role that assesses and remediates **Cisco Identity
Services Engine (ISE)** to the DISA **Cisco ISE NDM STIG** (`CISC-ND-*`) through
the ISE **ERS** and **OpenAPI** REST interfaces. Uses `ansible.builtin.uri`
only — no extra collection.

Most ISE NDM controls (admin banner, session timeout, password policy, remote
syslog, NTP, SNMPv3, external admin authentication) live in ISE **System
Settings**. A subset is exposed through the ISE OpenAPI; the rest are verified
via read-only ERS objects. This role therefore **assesses** posture safely and
**enforces** a data-driven set of OpenAPI operations you define for your ISE
version. It complements the 28 functional `ise_*` roles in `cisco/roles/`.

## Why "grab and go"

* Assessment runs out of the box against any ERS-enabled ISE and writes a JSON
  artifact — no write risk.
* `apply_changes=false` (default) performs **zero** writes.
* Enforcement operations are explicit per-call definitions validated against your
  ISE OpenAPI explorer, not guessed endpoints.

## Quick start

```bash
cd cisco/roles/cisco_ise_stig/playbooks
cp inventory.example inventory && $EDITOR inventory   # ISE host + vaulted ERS creds

# ASSESS (read-only)
ansible-playbook -i inventory run.yml
cat /tmp/cisco-ise-artifacts/ise.example.mil_ise_stig.json

# ENFORCE (after defining ise_stig_operations for your ISE version)
ansible-playbook -i inventory run.yml -e apply_changes=true -e @vars.example.yml
```

## Controls covered

| Control | Handling |
|---------|----------|
| CISC-ND-000010 banner, 000280 timeout, 000380 password policy, 000090 syslog, 000470 NTP, 000150 SNMPv3, 000160 external admin auth | Assessed + manual-review flagged; enforce via `ise_stig_operations` (OpenAPI) |
| Deployment / admin / NAD inventory | Read-only ERS assessment (nodes, admin users, network devices) |

## ⚠️ Notes

* Enable **ERS** first: Administration ▸ System ▸ Settings ▸ ERS Settings.
* The ISE OpenAPI explorer (`https://<ise>/api/swagger`) documents exact
  paths/bodies for your release — validate `ise_stig_operations` there.
* `ise_validate_certs: true` by default — trust the ISE admin cert on the
  control node.

## Tags

`--tags assess` (read-only), `apply`, `report`.

# Cisco FTD STIG via FMC (`cisco_ftd_stig`)

Production-ready Ansible role that assesses and remediates **Cisco Firepower
Threat Defense (FTD)** to DISA STIG, driven through the **Firepower Management
Center (FMC) REST API**.

FTD devices under FMC management are not configured from an on-box config CLI —
their STIG controls (banner, session timeout, syslog, NTP, SNMPv3, SSH access
list, AAA, access-control/intrusion policy) live in **FMC Platform Settings**,
**Access Control**, and **Intrusion** policies. This role works the way the
platform actually works:

1. **Authenticate** to FMC (token flow — stable since FMC 6.1).
2. **Assess** posture with read-only GET calls — managed devices, platform
   settings policy presence, off-box syslog alerts, access policies. This is
   100% safe and is what runs by default.
3. **Enforce** a data-driven list of STIG operations (`ftd_stig_operations`),
   only when `apply_changes=true`. After enforcement, deploy the changed
   policies to the FTD devices from FMC.

It uses only `ansible.builtin.uri` — no extra collection or SDK.

## Why "grab and go"

* The assessment runs out of the box against any FMC 6.1+ and produces a JSON
  findings artifact — no write risk.
* `apply_changes=false` (default) performs **zero** write operations.
* Enforcement operations are explicit per-call definitions so they stay correct
  across FMC versions instead of guessing undocumented endpoints.

## Quick start

```bash
cd cisco/roles/cisco_ftd_stig/playbooks
cp inventory.example inventory && $EDITOR inventory   # set FMC host + vault creds

# ASSESS (read-only) — produces the findings artifact
ansible-playbook -i inventory run.yml

# Review findings
cat /tmp/cisco-ftd-artifacts/fmc.example.mil_ftd_stig.json

# ENFORCE — after defining ftd_stig_operations for your FMC version
ansible-playbook -i inventory run.yml -e apply_changes=true -e @vars.example.yml
```

## Controls covered

| Control | How |
|---------|-----|
| CISC-ND mgmt plane (banner, timeout, SSH ACL, SNMPv3, NTP) | Platform Settings policy — assessed for presence; enforced via `ftd_stig_operations` |
| CISC-ND-000090 (off-box audit) | Syslog alert objects — assessed; enforced via operations |
| CISC-ND-000160 (AAA) | External authentication object — assessed via platform settings |
| CISC-FW / CISC-IDPS | Access control + intrusion policies — assessed for presence |

## ⚠️ Notes

* The FMC API explorer at `https://<fmc>/api/api-explorer` documents the exact
  request bodies for your version — validate `ftd_stig_operations` there before
  enforcing.
* Policy changes are not effective on the FTD sensors until **deployed** from
  FMC (Deploy ▸ Deployment), or via the FMC deployment API.
* `fmc_validate_certs: true` by default — install the FMC CA on the control node
  or set it to `false` only in a lab.

## Tags

`--tags assess` (read-only), `apply` (enforcement), `report`, `auth`.

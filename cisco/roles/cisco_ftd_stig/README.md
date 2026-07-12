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

## Requirements

- Ansible 2.15+
- Collection: `ansible.utils` (`ansible-galaxy collection install ansible.utils`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ansible_connection` | `local` | No | Run on the control node (API automation) |
| `fmc_host` | `"{{ vault_fmc_host \| default('fmc.example.mil') }}"` | No | FMC connection (set in inventory / group_vars, use Ansible Vault) |
| `fmc_username` | `"{{ vault_fmc_username \| default('apiuser') }}"` | No | — |
| `fmc_password` | `"{{ vault_fmc_password \| default('CHANGE_ME') }}"` | **Yes** | — |
| `fmc_validate_certs` | `true` | No | — |
| `fmc_api_version` | `v1` | No | — |
| `apply_changes` | `false` | No | Deployment control |
| `artifacts_dir` | `"/tmp/cisco-ftd-artifacts"` | No | — |
| `stig_assess` | `true` | No | Control toggles |
| `stig_apply_operations` | `true` | No | — |
| `stig_compliance_report` | `true` | No | — |
| `ftd_required_platform_settings_assigned` | `true` | No | Expected STIG posture (used by the assessment to flag findings) Every managed FTD device must have a Platform Settings policy assigned that implements banner, session timeout, syslog, NTP, SNMPv3 and SSH access list. |
| `ftd_required_syslog_alert` | `true` | No | At least one external syslog alert must exist (CISC-ND-000090 off-box audit). |
| `ftd_stig_operations` | `[]` | No | CISC-ND-XXXXXX - Enforcement operations (data-driven) Each item: { id, title, severity, method, endpoint, body } `endpoint` is appended to the domain base https://{{fmc_host}}/api/fmc_config/{{fmc_api_version}}/domain/{{domain}}/ Defaults ship empty; populate per your FMC version (see vars.example.yml). This keeps writes explicit and version-safe - nothing is pushed unless you define it and pass apply_changes=true. |
| `ftd_login_banner` | `(multi-line text — see defaults/main.yml)` | No | DoD login banner text (referenced from vars.example.yml operations) |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Cisco Firepower Threat Defense (FTD) NDM + Firewall STIG"` | No | — |
| `stig_version` | `"V1R3"` | No | — |

## Example Playbook

```yaml
- name: Use cisco_ftd_stig
  hosts: all
  gather_facts: false
  roles:
    - role: cisco_ftd_stig
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags assess` (read-only), `apply` (enforcement), `report`, `auth`.

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

## License

MIT

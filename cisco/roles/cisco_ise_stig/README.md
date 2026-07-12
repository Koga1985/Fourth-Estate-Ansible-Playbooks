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

## Requirements

- Ansible 2.15+
- Collection: `ansible.utils` (`ansible-galaxy collection install ansible.utils`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ansible_connection` | `local` | No | Run on the control node |
| `ise_host` | `"{{ vault_ise_host \| default('ise.example.mil') }}"` | No | ISE connection (vault these) |
| `ise_ers_port` | `9060` | No | — |
| `ise_username` | `"{{ vault_ise_ers_user \| default('ersadmin') }}"` | No | — |
| `ise_password` | `"{{ vault_ise_ers_password \| default('CHANGE_ME') }}"` | **Yes** | — |
| `ise_validate_certs` | `true` | No | — |
| `apply_changes` | `false` | No | Deployment control |
| `artifacts_dir` | `"/tmp/cisco-ise-artifacts"` | No | — |
| `stig_assess` | `true` | No | Control toggles |
| `stig_apply_operations` | `true` | No | — |
| `stig_compliance_report` | `true` | No | — |
| `ise_expected_external_admin_auth` | `true` | No | Expected NDM posture (used by assessment to flag findings) CISC-ND-000160 - external admin authentication should be configured; ISE should have remote AAA / identity sources beyond just internal admins. |
| `ise_expected_remote_logging` | `true` | No | CISC-ND-000090 - at least one remote logging target must exist. |
| `ise_stig_operations` | `[]` | No | CISC-ND-* enforcement operations (data-driven OpenAPI calls) Each item: { id, title, method, path, body, status_code } `path` is appended to https://{{ise_host}}/api/ (OpenAPI base). Defaults empty; populate per ISE version (see vars.example.yml). |
| `ise_login_banner` | `(multi-line text — see defaults/main.yml)` | No | DoD banner text (referenced from operations) |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Reporting metadata |
| `stig_benchmark` | `"Cisco ISE NDM STIG"` | No | — |
| `stig_version` | `"V1R1"` | No | — |

## Example Playbook

```yaml
- name: Use cisco_ise_stig
  hosts: all
  gather_facts: false
  roles:
    - role: cisco_ise_stig
      vars:
        apply_changes: false   # set true to apply
```

## Tags

`--tags assess` (read-only), `apply`, `report`.

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

## License

MIT

# sdwan_security_hardening

## Overview

Hardens Cisco SD-WAN components — vManage, vBond, vSmart, and vEdge/cEdge edge devices — against the **Cisco IOS XE SD-WAN Router NDM STIG V2R1** and **Cisco SD-WAN vManage NDM STIG V1R1**. All controls are mapped to NIST SP 800-53 Rev 5. This is Phase 19 of the Fourth Estate Cisco SD-WAN deployment.

## Features

- **STIG CAT I** — Authentication (TACACS+/RADIUS), Password Policy (15-char min), TLS 1.2+, FIPS 140-2
- **STIG CAT II** — RBAC/Least Privilege, Account Lockout (3 attempts / 15 min), Session Timeout (10 min idle), SNMPv3 authPriv, Audit Logging to SIEM, Authenticated NTP, SSH v2 hardening, Disable unused services
- **STIG CAT III** — DoD Warning Banner (AC-8)
- Generates JSON and text STIG compliance reports in `sdwan_artifacts_dir`
- Defaults to **dry-run mode** (`apply_changes: false`) — safe to run without impacting production

## Requirements

- Ansible 2.15+
- Collections: `ansible.builtin`, `ansible.utils`
- Python: `requests`
- vManage reachable from Ansible control node on port 443
- Valid vault variables for credentials (see defaults)

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sdwan_vmanage_host` | `{{ vault_sdwan_vmanage_host }}` | **Yes** | vManage hostname or IP |
| `sdwan_vmanage_username` | `{{ vault_sdwan_vmanage_username }}` | **Yes** | vManage admin username |
| `sdwan_vmanage_password` | `{{ vault_sdwan_vmanage_password }}` | **Yes** | vManage admin password |
| `apply_changes` | `false` | No | Set `true` to apply changes; `false` = dry run |
| `sdwan_auth_method` | `tacacs` | No | AAA auth method: `tacacs`, `radius`, `local` |
| `sdwan_tacacs_servers` | see defaults | **Yes** (if tacacs) | List of TACACS+ server configs |
| `sdwan_password_min_length` | `15` | No | Minimum password length (DoD min: 15) |
| `sdwan_lockout_max_attempts` | `3` | No | Failed attempts before lockout (DoD max: 3) |
| `sdwan_lockout_duration_seconds` | `900` | No | Lockout duration in seconds (DoD min: 900) |
| `sdwan_session_idle_timeout` | `600` | No | Idle session timeout in seconds (DoD max: 600) |
| `sdwan_snmp_v1_enabled` | `false` | No | Must remain false per STIG |
| `sdwan_snmp_v2c_enabled` | `false` | No | Must remain false per STIG |
| `sdwan_snmp_v3_enabled` | `true` | No | SNMPv3 authPriv required |
| `sdwan_fips_enabled` | `true` | No | Enable FIPS 140-2 mode |
| `sdwan_min_tls_version` | `TLSv1.2` | No | Minimum TLS version |
| `sdwan_disable_http_server` | `true` | No | Disable plain HTTP |
| `sdwan_disable_telnet` | `true` | No | Disable telnet (SSH v2 only) |
| `sdwan_ntp_authenticate` | `true` | No | Require NTP authentication |
| `sdwan_artifacts_dir` | `/tmp/sdwan-artifacts` | No | Directory for compliance reports |
| `compliance_frameworks` | see defaults | No | List of applicable frameworks |

## Dependencies

None. Runs standalone against vManage REST API.

## Example Playbook

```yaml
- name: Cisco SD-WAN STIG Hardening
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    apply_changes: true   # Remove this line for dry-run

  tasks:
    - name: Apply SD-WAN STIG hardening
      ansible.builtin.include_role:
        name: sdwan_security_hardening
```

Run dry-run first:
```bash
ansible-playbook -i inventory cisco/playbooks/06_sdwan_phase5_security_hardening.yml --ask-vault-pass
```

Apply changes:
```bash
ansible-playbook -i inventory cisco/playbooks/06_sdwan_phase5_security_hardening.yml \
  -e apply_changes=true --ask-vault-pass
```

Run specific STIG category only:
```bash
# CAT I controls only
ansible-playbook -i inventory cisco/playbooks/06_sdwan_phase5_security_hardening.yml \
  --tags stig_cat1 --ask-vault-pass

# Authentication and logging only
ansible-playbook -i inventory cisco/playbooks/06_sdwan_phase5_security_hardening.yml \
  --tags "authentication,logging" -e apply_changes=true --ask-vault-pass
```

## Tags

| Tag | Description |
|-----|-------------|
| `sdwan` | All SD-WAN tasks |
| `security` | All security hardening tasks |
| `stig` | All STIG controls |
| `stig_cat1` | STIG CAT I (High) controls only |
| `stig_cat2` | STIG CAT II (Medium) controls only |
| `stig_cat3` | STIG CAT III (Low) controls only |
| `authentication` | AAA / TACACS+ / RADIUS |
| `passwords` | Password policy |
| `sessions` | Session management |
| `banners` | DoD login banner |
| `snmp` | SNMPv3 configuration |
| `logging` | Audit / syslog configuration |
| `ntp` | NTP authentication |
| `ssh` | SSH hardening |
| `crypto` / `tls` | TLS and cryptographic controls |
| `fips` | FIPS 140-2 mode |
| `rbac` | Role-based access control |
| `services` | Unused service disable |
| `phase19` | All Phase 19 tasks |
| `report` | Generate compliance report only |

## Compliance

### DISA STIG Controls Implemented

| STIG ID | Title | CAT | NIST Control |
|---------|-------|-----|--------------|
| CISC-ND-000080 | DoD Login Banner | III | AC-8 |
| CISC-ND-000090 | SNMPv3 Required (disable v1/v2c) | II | SC-8 |
| CISC-ND-000200 | Session Idle Timeout (10 min) | II | AC-12 |
| CISC-ND-000360 | RBAC Least Privilege | II | AC-2, AC-3, AC-6 |
| CISC-ND-000370 | Account Lockout (3 attempts) | II | AC-7 |
| CISC-ND-000390 | Idle Timeout Enforcement | II | AC-11 |
| CISC-ND-000530 | Password Complexity | I | IA-5 |
| CISC-ND-000570 | Password Minimum Length (15 chars) | I | IA-5 |
| CISC-ND-000700 | Audit Event Logging | II | AU-2 |
| CISC-ND-000710 | Audit Record Content | II | AU-3 |
| CISC-ND-000720 | Audit Log Protection | II | AU-9 |
| CISC-ND-001190 | TACACS+/RADIUS Authentication | I | IA-2, IA-3 |
| CISC-ND-001200 | Disable Unused Services | II | CM-7 |
| CISC-ND-001290 | Authenticated NTP | II | AU-8 |
| CISC-ND-001400 | SSH v2 / Disable Telnet | II | SC-8, AC-17 |
| CISC-ND-001420 | NTP Trusted Servers | II | AU-8 |
| CISC-ND-001440 | TLS 1.2+ / Disable HTTP / FIPS | I | SC-8, SC-13 |

### NIST SP 800-53 Rev 5 Controls

`AC-2`, `AC-3`, `AC-6`, `AC-7`, `AC-8`, `AC-11`, `AC-12`, `AC-17`, `AU-2`, `AU-3`, `AU-8`, `AU-9`, `AU-12`, `CM-6`, `CM-7`, `IA-2`, `IA-3`, `IA-5`, `SC-8`, `SC-13`, `SC-17`, `SC-28`

## Artifacts Generated

| File | Description |
|------|-------------|
| `sdwan_stig_compliance_<epoch>.json` | Machine-readable compliance status for all STIG controls |
| `sdwan_stig_summary_<epoch>.txt` | Human-readable STIG compliance summary |

## Author

Fourth Estate Infrastructure Team

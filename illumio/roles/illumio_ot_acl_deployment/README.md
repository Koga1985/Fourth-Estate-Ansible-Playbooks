# illumio_ot_acl_deployment

Illumio OT ACL Deployment role for Fourth Estate infrastructure automation.

Provides **event-driven detection** and **manually-gated deployment** of Illumio
security rules (ACLs) for Operational Technology (OT) / Industrial Control System
(ICS) environments. Follows the Purdue model for zone-boundary enforcement and
supports both VEN-managed workloads (label-based rules) and agentless OT devices
(IP list-based rules — PLCs, RTUs, sensors with no Illumio VEN).

---

## How It Works

```
 PCE drafts new rule          Cron / AAP schedule
        │                            │
        ▼                            ▼
 ┌──────────────────────────────────────┐
 │  Playbook 01 — Monitor               │  Runs automatically
 │  • Polls PCE pending policy          │  (set-and-forget)
 │  • Diffs against saved baseline      │
 │  • Alerts network team via email     │
 │    and/or webhook if new items found │
 └──────────────────┬───────────────────┘
                    │  Alert fires
                    ▼
        Network team reviews alert
        and pending ACL report
                    │
                    ▼
 ┌──────────────────────────────────────┐
 │  Playbook 02 — Deploy                │  Run manually
 │  • Validates ACLs (protocol,         │  by network team
 │    Purdue boundary checks)           │
 │  • dry_run=true by default           │
 │  • apply_changes=true → writes       │
 │    rules to PCE draft                │
 │  • promote_policy=true → provisions  │
 │    draft to active enforcement       │
 │  • Notifies team on completion       │
 └──────────────────────────────────────┘
```

---

## Quick Start (5 Steps)

**Step 1 — Install collections**
```bash
ansible-galaxy collection install -r illumio/requirements.yml
```

**Step 2 — Create inventory**
```bash
cp illumio/inventory_ot.example illumio/inventory_ot
vi illumio/inventory_ot          # Set pce_url, org_id, ACLs, email address
```

**Step 3 — Create and encrypt vault**
```bash
mkdir -p illumio/group_vars/all
cp illumio/vault_ot.yml.example illumio/group_vars/all/vault_ot.yml
vi illumio/group_vars/all/vault_ot.yml    # Set API keys, SMTP, webhook URL
ansible-vault encrypt illumio/group_vars/all/vault_ot.yml
```

**Step 4 — Test the monitor (detects pending ACLs, alerts team)**
```bash
ansible-playbook illumio/playbooks/01_illumio_ot_acl_monitor.yml \
  -i illumio/inventory_ot --ask-vault-pass
```

**Step 5 — Deploy ACLs (after receiving an alert)**
```bash
# Dry run first — always
ansible-playbook illumio/playbooks/02_illumio_ot_acl_deploy.yml \
  -i illumio/inventory_ot --ask-vault-pass

# Apply (rules written to PCE draft, not yet enforced)
ansible-playbook illumio/playbooks/02_illumio_ot_acl_deploy.yml \
  -i illumio/inventory_ot --ask-vault-pass \
  -e "apply_changes=true"

# Apply AND promote (rules go live — traffic affected)
ansible-playbook illumio/playbooks/02_illumio_ot_acl_deploy.yml \
  -i illumio/inventory_ot --ask-vault-pass \
  -e "apply_changes=true promote_policy=true"
```

---

## Scheduling the Monitor (Playbook 01)

**Linux cron** (every 15 minutes):
```cron
*/15 * * * * ansible-playbook /opt/playbooks/illumio/playbooks/01_illumio_ot_acl_monitor.yml \
  -i /opt/playbooks/illumio/inventory_ot \
  --vault-password-file /opt/.vault_pass \
  2>&1 | logger -t illumio-ot-monitor
```

**Ansible Automation Platform / AWX:**
1. Create a Job Template pointing to `01_illumio_ot_acl_monitor.yml`
2. Add an AAP Schedule on the Job Template (e.g. every 15 minutes)
3. No cron line needed — AAP handles scheduling

---

## Defining ACLs (`ot_acls` variable)

Define ACLs in your `inventory_ot` file under `[localhost:vars]`. Two formats
are supported for `providers` and `consumers`:

### Label-based (workloads with Illumio VEN)
```yaml
ot_acls:
  - name: "Allow HMI to PLC — Modbus TCP"
    description: "SCADA HMI reads/writes PLC registers via Modbus TCP."
    rule_set_name: "OT Control Zone Rules"
    ticket_ref: "CHG0012345"           # optional — for audit trail
    services:
      - port: 502
        proto: tcp
    providers:
      - type: label
        key: app
        value: field                   # matches Illumio app-label value
    consumers:
      - type: label
        key: app
        value: control
    enabled: true
    purdue_src: "2"                    # optional — enables boundary check
    purdue_dst: "1"
```

### IP-list-based (OT devices WITHOUT Illumio VEN — PLCs, RTUs, sensors)
```yaml
ot_acls:
  - name: "Allow PLC to Remote I/O — EtherNet/IP"
    description: "PLC controls remote I/O modules via EtherNet/IP."
    rule_set_name: "OT Field Device Rules"
    services:
      - port: 44818
        proto: tcp
      - port: 2222
        proto: udp
    providers:
      - type: ip_list
        name: "Remote IO Modules Building A"   # created in PCE if absent
        ranges:
          - from_ip: "10.20.1.0"
            to_ip: "10.20.1.63"
            description: "Building A rack 1-4"
    consumers:
      - type: label
        key: app
        value: control
    enabled: true
    purdue_src: "2"
    purdue_dst: "1"
```

---

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `pce_url` | *(required)* | Illumio PCE base URL |
| `org_id` | *(required)* | PCE organisation ID |
| `api_user` | `{{ vault_illumio_api_user }}` | PCE API user (from vault) |
| `api_key` | `{{ vault_illumio_api_key }}` | PCE API key (from vault) |
| `ot_artifacts_dir` | `/tmp/illumio-ot-artifacts` | Directory for reports and baselines |
| `verify_ssl` | `true` | Verify PCE TLS certificate |
| `dry_run` | `true` | Preview only — no PCE writes |
| `apply_changes` | `false` | Write rules to PCE draft |
| `promote_policy` | `false` | Provision draft → active enforcement |
| `brownout_enabled` | `true` | Check traffic impact before promoting |
| `deny_threshold` | `0` | Max newly-blocked flows before abort |
| `reset_baseline` | `false` | Treat all current pending as new |
| `ot_email_enabled` | `true` | Send email alerts |
| `ot_alert_email_to` | `{{ vault_network_team_email }}` | Alert recipient(s) |
| `ot_alert_email_from` | `ansible-ot@network.local` | Alert sender address |
| `ot_smtp_host` | `{{ vault_smtp_host }}` | SMTP server |
| `ot_smtp_port` | `{{ vault_smtp_port }}` | SMTP port |
| `ot_webhook_enabled` | `false` | Send webhook notifications |
| `ot_webhook_url` | `{{ vault_ot_webhook_url }}` | Webhook endpoint |
| `ot_syslog_enabled` | `false` | Log events to syslog |
| `ot_enforce_purdue_boundaries` | `true` | Validate Purdue level jumps |
| `ot_purdue_max_level_jump` | `1` | Maximum allowed Purdue level span |
| `ot_strict_protocol_validation` | `false` | Fail (vs warn) on unknown protocols |
| `ot_acls` | `[]` | **List of ACL entries to deploy** |
| `ot_zones` | *(see defaults)* | Purdue zone → Illumio label mapping |
| `ot_allowed_protocols` | *(see defaults)* | OT protocol allowlist |

---

## Tags

| Tag | Playbook | What it runs |
|-----|----------|-------------|
| `detect` | 01 | Query PCE and compare baseline |
| `alert` | 01 | Send notifications |
| `validate` | 02 | ACL field and protocol validation |
| `apply` | 02 | Create rules in PCE draft |
| `promote` | 02 | Provision draft → active |
| `notify` | 02 | Send completion notifications |

```bash
# Monitor: scan only, skip alerts
ansible-playbook illumio/playbooks/01_illumio_ot_acl_monitor.yml \
  -i illumio/inventory_ot --ask-vault-pass --tags detect

# Deploy: validate only (no PCE calls)
ansible-playbook illumio/playbooks/02_illumio_ot_acl_deploy.yml \
  -i illumio/inventory_ot --ask-vault-pass --tags validate
```

---

## OT Protocol Allowlist

The default allowlist covers common OT/ICS protocols. Validation warns (or fails
with `ot_strict_protocol_validation: true`) when an ACL uses an unlisted port.

| Protocol | Port | Transport |
|----------|------|-----------|
| Modbus TCP | 502 | TCP |
| DNP3 | 20000 | TCP/UDP |
| EtherNet/IP | 44818 | TCP |
| EtherNet/IP | 2222 | UDP |
| OPC-UA | 4840 | TCP |
| OPC-DA (DCOM) | 135 | TCP |
| PROFINET | 34964 | UDP |
| BACnet | 47808 | UDP |
| IEC 60870-5-104 | 2404 | TCP |
| ICMP | — | ICMP |
| HTTPS | 443 | TCP |
| SSH | 22 | TCP |

Add site-specific protocols to `ot_allowed_protocols` in your inventory.

---

## Vault Variables Required

| Vault variable | Description |
|---------------|-------------|
| `vault_illumio_api_user` | PCE API user ID |
| `vault_illumio_api_key` | PCE API secret key |
| `vault_network_team_email` | Alert recipient email |
| `vault_smtp_host` | SMTP relay hostname |
| `vault_smtp_port` | SMTP port (25 / 587) |
| `vault_smtp_username` | SMTP auth username (if required) |
| `vault_smtp_password` | SMTP auth password (if required) |
| `vault_ot_webhook_url` | Webhook endpoint URL (optional) |
| `vault_syslog_server` | Syslog server IP/hostname (optional) |

---

## Artifact Files

| File | Description |
|------|-------------|
| `acl_baseline.json` | HREFs of pending items at last monitor scan |
| `acl_pending.json` | Full pending policy objects (latest scan) |
| `acl_report_YYYY-MM-DD.json` | Timestamped detection report |
| `acl_apply_YYYY-MM-DD.json` | Record of rules written to PCE |
| `acl_promotion_YYYY-MM-DD.json` | Record of policy promotion |
| `deploy_start_YYYY-MM-DD.txt` | Deployment run metadata |

---

## Security Considerations

- All credentials are stored in Ansible Vault (`vault_ot.yml`) — never in plaintext
- `dry_run: true` is the default; operators must explicitly pass `-e "apply_changes=true"`
- `promote_policy: true` is a separate gate requiring a second explicit flag
- `brownout_enabled: true` with `deny_threshold: 0` enforces zero-tolerance for
  unexpected traffic blocking before promotion
- Purdue boundary validation catches cross-zone rules that violate ICS security design
- All PCE API calls use `no_log: true` to prevent credentials appearing in logs
- Artifacts are written with mode `0640` to restrict read access

---

## Requirements

- Ansible 2.9+
- Network access from the Ansible control node to the Illumio PCE API (port 8443)
- Illumio PCE 22.x or later
- Python `requests` library on the control node (for `ansible.builtin.uri`)
- For email alerts: SMTP relay accessible from control node
- For webhook alerts: HTTPS connectivity to the webhook endpoint

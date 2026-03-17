# illumio_ven_fleet

Manages the lifecycle of Illumio Virtual Enforcement Node (VEN) agents across a fleet of Linux and Windows workloads: downloads VEN installers from the PCE, installs and pairs agents on Linux hosts, installs and pairs agents on Windows hosts, triggers rolling PCE-driven upgrades in configurable batches, and unpairs or decommissions agents. Each operation is individually gated by its own variable so a single playbook invocation can perform one or several actions.

## Requirements

- Ansible 2.12 or later
- For Linux install/pair tasks: SSH connectivity to target Linux hosts and sudo/become privileges
- For Windows install/pair tasks: WinRM connectivity to target Windows hosts
- For upgrade and unpair tasks: network connectivity from the Ansible controller to the PCE API (`pce_url`)
- The following variables must be supplied at runtime:
  - `pce_url` — base URL of the PCE (e.g. `https://pce.example.mil:8443`)
  - `org_id` — PCE organization ID (integer)
  - `api_user` — PCE API username
  - `api_key` — PCE API key (store in Ansible Vault)

## Role Variables

All variables are defined in `defaults/main.yml`.

| Variable | Default | Description |
|---|---|---|
| `verify_ssl` | `true` | Verify TLS certificates when calling the PCE API. |
| `artifacts_dir` | `/tmp/illumio-artifacts` | Directory on the Ansible controller where downloaded installers are stored. |
| `platforms` | `[]` | List of platform identifiers (e.g. `linux-rhel8-x86_64`) for which VEN installers are downloaded from the PCE. When non-empty, the download task runs. |
| `pairing_key` | `""` | PCE pairing key used to pair VEN agents during installation. Required for Linux and Windows install tasks. Store in Ansible Vault. |
| `ven_installer` | `""` | Path to the VEN installer package on the Ansible controller. Used by the Linux install task to push the installer to target hosts. |
| `upgrade_targets` | `[]` | List of workload identifiers (PCE hrefs or hostnames) to upgrade. When non-empty, the upgrade task runs. |
| `batch_size` | `50` | Number of VEN agents to upgrade per batch when `upgrade_targets` is set. |
| `batch_pause` | `60` | Pause in seconds between upgrade batches to limit blast radius. |
| `decom_targets` | `[]` | List of workload identifiers to unpair and decommission. When non-empty, the unpair/decom task runs. |

### Runtime-only variables (no defaults)

| Variable | Description |
|---|---|
| `pce_url` | Base URL of the PCE. |
| `org_id` | PCE organization ID integer. |
| `api_user` | PCE API authentication username. |
| `api_key` | PCE API key. Store in Ansible Vault. |
| `extra_flags` | Optional extra command-line flags passed to the VEN installer on Linux (e.g. `--enforcement-mode illuminated`). |

## Example Playbook

### Download installers and pair Linux hosts

```yaml
- name: Install and pair Illumio VEN on Linux
  hosts: linux_workloads
  become: true
  gather_facts: false
  roles:
    - role: illumio_ven_fleet
      vars:
        pce_url: "https://pce.dc1.example.mil:8443"
        org_id: 1
        api_user: "{{ vault_illumio_api_user }}"
        api_key: "{{ vault_illumio_api_key }}"
        pairing_key: "{{ vault_illumio_pairing_key }}"
        ven_installer: "/opt/illumio/illumio-ven-rhel8.pkg"
        install_linux: true
```

### Rolling upgrade of existing VEN fleet

```yaml
- name: Upgrade Illumio VEN fleet
  hosts: localhost
  gather_facts: false
  roles:
    - role: illumio_ven_fleet
      vars:
        pce_url: "https://pce.dc1.example.mil:8443"
        org_id: 1
        api_user: "{{ vault_illumio_api_user }}"
        api_key: "{{ vault_illumio_api_key }}"
        upgrade_targets:
          - "/orgs/1/workloads/abc123"
          - "/orgs/1/workloads/def456"
        batch_size: 25
        batch_pause: 120
```

### Unpair and decommission agents

```yaml
- name: Decommission Illumio VEN agents
  hosts: localhost
  gather_facts: false
  roles:
    - role: illumio_ven_fleet
      vars:
        pce_url: "https://pce.dc1.example.mil:8443"
        org_id: 1
        api_user: "{{ vault_illumio_api_user }}"
        api_key: "{{ vault_illumio_api_key }}"
        decom_targets:
          - "/orgs/1/workloads/abc123"
```

## Notes and Dependencies

- Each operation is independently gated: download runs when `platforms` is non-empty; Linux install runs when `install_linux: true`; Windows install runs when `install_windows: true`; upgrade runs when `upgrade_targets` is non-empty; decom runs when `decom_targets` is non-empty. Multiple operations can be combined in a single role invocation.
- All PCE API calls use `no_log: true` to prevent credentials from appearing in Ansible output.
- `pairing_key` and `api_key` are sensitive credentials and must be stored in Ansible Vault. Never define them in plaintext inventory files.
- The Linux install task pushes the installer to `/tmp/illumio-ven-installer.pkg` on each target host, executes it with `--pair`, then communicates with the PCE via `pce_url`. Ensure the target hosts can reach the PCE on the configured port.
- The upgrade task sends a batch upgrade request to the PCE API. The PCE orchestrates the actual upgrade on each VEN; Ansible does not directly touch the endpoints during an upgrade.
- The role makes direct HTTPS calls to the PCE API using `ansible.builtin.uri` and `ansible.builtin.get_url`. No Illumio Ansible collection is required.

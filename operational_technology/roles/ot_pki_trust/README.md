# ot_pki_trust
Distribute trust bundles/certs with a default dry-run; outputs expiry reports.

## Requirements

- Ansible 2.14+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `/tmp/ot-artifacts` | No | — |
| `dry_run` | `true` | No | — |
| `certs` | `[]` | No | [{ path: /etc/pki/tls/certs/server.crt }, ...] |
| `trust_bundles` | `[]` | No | [{ src: files/ca-bundle.crt, dest: /etc/pki/ca-trust/source/anchors/ca-bundle.crt }] |

## Example Playbook

```yaml
- name: Use ot_pki_trust
  hosts: all
  gather_facts: false
  roles:
    - role: ot_pki_trust
```

## License

MIT

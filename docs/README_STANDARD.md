# Role README Standard

All roles in this repository must include a README.md that follows this standard. The goal is consistent, accurate documentation so operators can use any role confidently without reading the source code.

---

## Required Sections (in order)

### 1. Title and One-Line Description

```markdown
# role_name

One sentence describing what this role does and its primary use case.
```

### 2. Requirements

List the minimum Ansible version, required collections, host/inventory prerequisites, and any privilege requirements.

```markdown
## Requirements

- Ansible 2.15+
- Collection: `namespace.collection` (install via `ansible-galaxy collection install namespace.collection`)
- Hosts must be in the `inventory_group` group
- `become: true` required
```

### 3. Role Variables

Every variable that exists in `defaults/main.yml` **must** appear here. Every variable documented here **must** exist in `defaults/main.yml` or be explicitly passed at invocation. No exceptions.

Use a Markdown table:

```markdown
## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `var_name` | `"value"` | No | What this controls |
| `vault_var` | `{{ vault_secret }}` | **Yes** | Vault-protected credential |
```

Rules:
- If the default is vault-referenced, show the vault variable name as the default.
- If there is no safe default (the operator must supply the value), set Required to **Yes**.
- Group related variables under `###` sub-headings when there are more than ~8 variables.
- Nested dict/list variables: document the top-level key and describe its structure inline or in a sub-table.

### 4. Example Playbook

A working, copy-paste example showing the most common use case. Use realistic values. Show both plan mode and apply mode if the role supports `apply_changes`.

```markdown
## Example Playbook

```yaml
- name: Example usage
  hosts: target_group
  become: true
  roles:
    - role: platform/roles/role_name
      vars:
        key_variable: value
        apply_changes: false   # set true to apply
```
```

### 5. Tags (if applicable)

```markdown
## Tags

| Tag | Description |
|-----|-------------|
| `tag_name` | What tasks run under this tag |
```

### 6. Compliance Controls (if applicable)

If the role implements STIG findings or NIST 800-53 controls, list them. Only list controls that are **actually implemented** in the task files — do not list aspirational or planned controls.

```markdown
## Compliance Controls

| Framework | Control ID | Description | Task File |
|-----------|-----------|-------------|-----------|
| DISA STIG | V-230502 | Password minimum length | tasks/password_policy.yml |
| NIST 800-53 | IA-5 | Authenticator Management | tasks/password_policy.yml |
```

### 7. Notes / Known Limitations

Document any behavior that is surprising, destructive, or requires operator action (reboots, manual steps, dry-run defaults).

```markdown
## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan/audit mode.
- Enabling X requires a manual reboot.
- Task Y is not idempotent; running twice may produce duplicate entries.
```

### 8. License

```markdown
## License

MIT
```

---

## Minimum Viable README (small/simple roles)

At minimum, a README must contain sections 1, 2, 3, and 4. Omitting sections 5–7 is acceptable only if none apply.

A README that only says "See defaults/main.yml" **does not meet this standard** and must be updated before the role is merged to main.

---

## Enforcement

CI validates the following automatically (see `.github/workflows/readme-lint.yml`):
- Every variable in `defaults/main.yml` has a matching entry in `README.md`.
- Every variable documented in `README.md` exists in `defaults/main.yml`.
- README.md is at least 20 lines long.

Violations block merge.

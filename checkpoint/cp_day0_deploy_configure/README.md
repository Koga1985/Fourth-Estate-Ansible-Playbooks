
# Day 0 Check Point — Turnkey Ansible Package

Run a first-day deployment against Check Point Management with a single play:
```bash
cd checkpoint_day0
ansible-playbook -i inventory.ini playbooks/checkpoint/day0.deploy.yml
```

> Install `ansible-galaxy collection install check_point.mgmt` and ensure `httpapi` access to your Management Server.

## What it does
1) Inventory: hosts/networks/groups.
2) Services: TCP/UDP + App/URL.
3) Access Policy: sections + rules → publish + install.
4) Threat Prevention: profile + rules + exceptions → publish + install.
5) Identity Awareness: enable IA, Access Roles, identity rules.
6) Prune (safe): CSV previews only by default (no deletes).

Tune `vars/` files, `group_vars/checkpoint_mgmt.yml`, and `inventory.ini`.

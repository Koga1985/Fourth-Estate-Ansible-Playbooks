# Web Browser STIGs — Edge / Chrome / Firefox (`win_browsers_stig`)

Applies the DISA **Microsoft Edge** (`EDGE-00-*`), **Google Chrome** (`DTBC-*`),
and **Mozilla Firefox** (`DTBF-*`) STIGs as Windows machine policies (registry)
via `ansible.windows.win_regedit`.

## Why "grab and go"
* **Safe by default**: `apply_changes=false` runs `win_regedit` in check mode
  (reports drift, no change). A per-host JSON artifact is written either way.
* Per-browser toggles (`stig_edge` / `stig_chrome` / `stig_firefox`) — enable
  only the browsers installed on the host. Fully data-driven settings lists.

## Quick start
```bash
cd windows/roles/win_browsers_stig/playbooks
ansible-galaxy collection install ansible.windows
cp inventory.example inventory && $EDITOR inventory
ansible-playbook -i inventory run.yml                       # DRY-RUN (report)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE
cat /tmp/win-browsers-stig-artifacts/ws-01_win_browsers_stig.json
```

## Controls (representative)
* **Edge**: `SSLVersionMin=tls1.2`, SmartScreen on + no override, password
  manager off, autoplay off, background mode off, block popups, InPrivate off.
* **Chrome**: `SSLVersionMin=tls1.2`, password manager off, block popups,
  Incognito disabled, SafeBrowsing on, remote-access firewall traversal off,
  download restrictions.
* **Firefox**: telemetry/studies/Pocket/form-history disabled, extension updates.

Edit/extend the `*_settings` lists in `defaults/main.yml` to match your STIG
release. Firefox also supports `policies.json`; the registry policies require
Firefox policy/ADMX support enabled.

## Tags
`--tags edge`, `chrome`, `firefox`, `report`, `stig_cat2`.

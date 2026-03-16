# Cisco Cyber Vision Playbooks

Phase-based playbooks for targeted Cyber Vision deployments.

## Playbooks

| Playbook | Purpose |
|----------|---------|
| `01_cv_full_deployment.yml` | Full end-to-end deployment (all phases) |
| `02_cv_phase1_center.yml` | Phase 1: Center initial setup |
| `03_cv_phase2_sensors.yml` | Phase 2: Sensor enrollment and configuration |
| `04_cv_phase3_assets.yml` | Phase 3: OT asset management |
| `05_cv_phase4_security.yml` | Phase 4: DoD STIG/NIST security hardening |
| `06_cv_phase5_monitoring.yml` | Phase 5: Monitoring and integrations |

## Usage

```bash
# Full deployment (dry-run)
ansible-playbook -i inventory playbooks/01_cv_full_deployment.yml --ask-vault-pass

# Apply specific phase
ansible-playbook -i inventory playbooks/05_cv_phase4_security.yml \
  -e "apply_changes=true" --ask-vault-pass

# Apply only CAT I security controls
ansible-playbook -i inventory playbooks/05_cv_phase4_security.yml \
  --tags stig_cat1 -e "apply_changes=true" --ask-vault-pass
```

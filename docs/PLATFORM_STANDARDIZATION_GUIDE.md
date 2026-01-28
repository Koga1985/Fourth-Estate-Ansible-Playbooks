# Platform Standardization Implementation Guide

**Purpose**: Guide for standardizing all 41+ platforms to meet Fourth Estate customer requirements
**Target Audience**: Repository maintainers and contributors
**Estimated Effort**: 2-6 weeks depending on platform complexity

---

## Table of Contents
1. [Overview](#overview)
2. [Standardization Requirements](#standardization-requirements)
3. [Implementation Process](#implementation-process)
4. [Platform Categories](#platform-categories)
5. [Step-by-Step Guide](#step-by-step-guide)
6. [Testing Checklist](#testing-checklist)
7. [Quality Assurance](#quality-assurance)

---

## Overview

### Why Standardization?

Fourth Estate agencies require:
- **Independence**: Deploy any platform without dependencies on others
- **Customizability**: Easy variable configuration for unique environments
- **Testing**: Functional tests to verify deployment success
- **Consistency**: Uniform structure across all platforms

### Current State (from audit)
- ✅ **11 platforms** (Category A): Production-ready structure, need tests
- ⚠️ **16 platforms** (Category B): Need orchestration playbooks
- ❌ **12 platforms** (Category C): Need complete structure
- ⚠️ **2 platforms** (Category D): Special cases, need documentation

### Target State
All 41 platforms will have:
1. Standardized directory structure
2. Complete documentation (README.md)
3. Orchestration playbooks (deploy, configure, validate, uninstall)
4. Functional tests
5. Customer-friendly variable templates
6. CI/CD integration

---

## Standardization Requirements

### 1. Directory Structure (MANDATORY)

```
platform-name/
├── README.md                    ✓ REQUIRED
├── requirements.yml             ✓ REQUIRED (if using collections)
├── inventory.example            ✓ REQUIRED
├── playbooks/
│   ├── deploy.yml              ✓ REQUIRED
│   ├── configure.yml           ✓ REQUIRED
│   ├── validate.yml            ✓ REQUIRED
│   ├── uninstall.yml           ✓ RECOMMENDED
│   └── tests/
│       └── test_deployment.yml ✓ REQUIRED
├── roles/                       ✓ REQUIRED (at least one role)
├── tasks/                       ○ OPTIONAL
├── vars/
│   └── example.yml             ✓ REQUIRED
└── docs/                        ○ OPTIONAL
```

### 2. Documentation (MANDATORY)

**README.md must include**:
- Quick start guide (< 5 minute read)
- Required variables table
- Optional variables table with defaults
- Deployment examples
- Troubleshooting section
- Fourth Estate features explanation

### 3. Testing (MANDATORY)

**Minimum test coverage**:
- Syntax validation (`--syntax-check`)
- Dry-run test (`--check`)
- Functional test (verify installation, configuration, connectivity)
- CI/CD integration

### 4. Variables (MANDATORY)

**vars/example.yml must include**:
- All customer-customizable variables
- Clear labels: REQUIRED vs OPTIONAL
- Default values for optional variables
- Vault encryption examples for secrets
- Platform-specific configuration options

---

## Implementation Process

### Phase 1: Planning (Day 1-2)
1. Review platform audit report (`docs/PLATFORM_AUDIT_REPORT.md`)
2. Prioritize platforms by customer demand
3. Identify maintainers for each platform
4. Schedule implementation sprints

### Phase 2: Standardization (Week 1-4)
1. Apply templates to platforms
2. Create missing playbooks
3. Document variables
4. Write functional tests
5. Update README

### Phase 3: Testing (Week 5)
1. Run syntax validation
2. Execute functional tests
3. Test in isolation (no other platforms)
4. Verify variable customization
5. Check CI/CD integration

### Phase 4: Documentation Review (Week 6)
1. Peer review README files
2. Validate quick start guides
3. Test troubleshooting procedures
4. Customer UAT (if possible)

---

## Platform Categories

### Category A: Full-Featured (11 platforms) - PRIORITY 1
**Platforms**: aws, azure, cisco, cohesity, crowdstrike, kubernetes, rhel, sentinelone, splunk, vast, veeam, windows

**Status**: ✅ Have playbooks + roles + tasks
**Missing**: Tests (except crowdstrike, kubernetes, sentinelone, splunk)
**Effort**: 1-2 days per platform

**Action Items**:
1. Add `playbooks/tests/test_deployment.yml` (use template)
2. Update README.md with variable documentation
3. Create `vars/example.yml` if missing
4. Add CI/CD integration

**Priority Order**:
1. vmware (high demand)
2. veeam (backup critical)
3. cohesity (backup critical)
4. aws (cloud)
5. azure (cloud)
6. cisco (networking)
7. windows (OS)
8. rhel (OS)
9. vast (storage)

---

### Category B: Task-Based (16 platforms) - PRIORITY 2
**Platforms**: ansible, arista, checkpoint, claroty, dragos, google_cloud_platform, illumio, infoblocks, openshift, operational_technology, palo_alto, pure, sciencelogic, vmware

**Status**: ⚠️ Have roles + tasks, NO orchestration playbooks
**Missing**: Playbooks directory with deploy/configure/validate/test
**Effort**: 2-3 days per platform

**Action Items**:
1. Create `playbooks/` directory
2. Create `playbooks/deploy.yml` (orchestrate existing tasks)
3. Create `playbooks/configure.yml`
4. Create `playbooks/validate.yml`
5. Create `playbooks/tests/test_deployment.yml`
6. Create `vars/example.yml`
7. Update README.md

**Priority Order**:
1. openshift (high demand, K8s alternative)
2. vmware (if not in Category A)
3. palo_alto (security)
4. checkpoint (security)
5. fortinet (security)
6. claroty (OT security)
7. dragos (OT security)
8. operational_technology (OT)
9. illumio (microsegmentation)
10. google_cloud_platform (cloud)
11. arista (networking)
12. pure (storage)
13. sciencelogic (monitoring)
14. infoblocks/infoblox (DDI)
15. ansible (meta)

---

### Category C: Roles-Only (12 platforms) - PRIORITY 3
**Platforms**: ansible_tower, elk_stack, f5_bigip, fortinet, gcp, hashicorp_vault, infoblox, netapp, paloalto, prometheus_grafana, pure_storage, servicenow, tenable

**Status**: ❌ Have ONLY roles, NO playbooks or tasks
**Missing**: Complete deployment automation
**Effort**: 3-4 days per platform

**Action Items**:
1. Create `playbooks/` directory
2. Create `playbooks/deploy.yml` (include all roles)
3. Create `tasks/` directory with task files
4. Create `playbooks/configure.yml`
5. Create `playbooks/validate.yml`
6. Create `playbooks/tests/test_deployment.yml`
7. Create `vars/example.yml`
8. Create complete README.md
9. Create `inventory.example`
10. Create `requirements.yml`

**Priority Order**:
1. hashicorp_vault (secrets management)
2. elk_stack (logging)
3. prometheus_grafana (monitoring)
4. f5_bigip (load balancing)
5. fortinet (if not in Category B)
6. tenable (vulnerability scanning)
7. ansible_tower (automation platform)
8. netapp (storage)
9. servicenow (ITSM)
10. gcp (cloud, may be duplicate of google_cloud_platform)
11. paloalto (may be duplicate of palo_alto)
12. pure_storage (may be duplicate of pure)
13. infoblox (DDI)

**Note**: Check for duplicate platforms (gcp/google_cloud_platform, paloalto/palo_alto, pure/pure_storage)

---

### Category D: Special Structure (2 platforms) - PRIORITY 4
**Platforms**: policy_as_code, databases

**Status**: ⚠️ Non-standard architecture
**Effort**: 1-2 days per platform

**policy_as_code**:
- Has `site.yml` instead of `playbooks/deploy.yml`
- Has `tests/` directory (good!)
- Action: Document unique structure, ensure README explains usage

**databases**:
- Has subdirectories: mysql, postgresql, oracle, elk_stack, fortinet, netapp, prometheus_grafana
- Action: Standardize each sub-platform independently OR create wrapper playbooks

---

## Step-by-Step Guide

### For Category A Platforms (Add Tests)

#### Step 1: Create Test Structure
```bash
cd [platform-name]
mkdir -p playbooks/tests
```

#### Step 2: Create Functional Test
```bash
cp docs/platform_template/test_deployment.yml.example \
   playbooks/tests/test_deployment.yml
```

#### Step 3: Customize Test
Edit `playbooks/tests/test_deployment.yml`:
- Replace `[PLATFORM_NAME]` with actual name
- Update service names (line 87, 113)
- Update config file paths (line 173)
- Update API endpoints (line 283)
- Customize security checks (line 237-264)

#### Step 4: Create/Update vars/example.yml
```bash
cp docs/platform_template/vars_example.yml vars/example.yml
```

Edit to include platform-specific variables from `roles/*/defaults/main.yml`

#### Step 5: Update README.md
Add sections:
- Required Variables table
- Optional Variables table
- Testing section
- Troubleshooting

Use `docs/platform_template/README_TEMPLATE.md` as reference

#### Step 6: Add CI/CD Integration
Edit `.github/workflows/test-new-platforms.yml`:
```yaml
matrix:
  platform:
    - existing-platforms...
    - [your-platform-name]  # ADD THIS
```

#### Step 7: Test
```bash
# Syntax check
ansible-playbook playbooks/deploy.yml --syntax-check

# Run functional test
ansible-playbook playbooks/tests/test_deployment.yml --check

# Verify CI/CD
git add .
git commit -m "feat: Add tests for [platform]"
git push
# Check GitHub Actions
```

---

### For Category B Platforms (Add Playbooks)

#### Step 1: Create Playbook Directory
```bash
cd [platform-name]
mkdir -p playbooks/tests
```

#### Step 2: Create Deploy Playbook
```bash
cp docs/platform_template/deploy.yml.example playbooks/deploy.yml
```

Edit `playbooks/deploy.yml`:
- Replace `[PLATFORM_NAME]` with actual name
- Update `hosts:` group name
- Include existing roles from `roles/` directory
- Include existing tasks from `tasks/` directory

Example:
```yaml
roles:
  - role: ../roles/existing-role-1
    tags: [install]

  - role: ../roles/existing-role-2
    tags: [configure]

post_tasks:
  - name: Execute existing tasks
    ansible.builtin.include_tasks: ../tasks/configure.yml
    tags: [configure]
```

#### Step 3: Create Configuration Playbook
```bash
cat > playbooks/configure.yml <<'EOF'
---
- name: Configure [Platform Name]
  hosts: platform_servers
  gather_facts: true
  become: true

  vars_files:
    - ../vars/{{ environment | default('production') }}.yml

  roles:
    - role: ../roles/configure  # If exists
      tags: [configure]

  tasks:
    - name: Include configuration tasks
      ansible.builtin.include_tasks: ../tasks/configure.yml
      when: ansible.builtin.stat(path='../tasks/configure.yml').stat.exists
EOF
```

#### Step 4: Create Validation Playbook
```bash
cat > playbooks/validate.yml <<'EOF'
---
- name: Validate [Platform Name] Deployment
  hosts: platform_servers
  gather_facts: true

  tasks:
    - name: Include validation tasks
      ansible.builtin.include_tasks: ../tasks/validate.yml
      when: ansible.builtin.stat(path='../tasks/validate.yml').stat.exists

    - name: Display validation summary
      ansible.builtin.debug:
        msg: "Validation complete - Platform is operational"
EOF
```

#### Step 5: Create Functional Test
```bash
cp docs/platform_template/test_deployment.yml.example \
   playbooks/tests/test_deployment.yml
```

Customize as in Category A Step 3

#### Step 6: Create vars/example.yml
```bash
# Extract variables from roles/*/defaults/main.yml
cat roles/*/defaults/main.yml > /tmp/all_defaults.yml

# Create example based on template
cp docs/platform_template/vars_example.yml vars/example.yml

# Merge platform-specific variables into example.yml
```

#### Step 7: Update README.md
Follow Category A Step 5

#### Step 8: Create inventory.example
```bash
cat > inventory.example <<'EOF'
[platform_servers]
server1.example.gov ansible_host=10.0.1.10
server2.example.gov ansible_host=10.0.1.11

[platform_servers:vars]
ansible_user=ansible-svc
ansible_become=true
ansible_become_method=sudo
EOF
```

#### Step 9: Test
Follow Category A Step 7

---

### For Category C Platforms (Complete Structure)

#### Step 1: Create Full Structure
```bash
cd [platform-name]
mkdir -p playbooks/tests tasks vars docs
```

#### Step 2: Analyze Existing Roles
```bash
ls -la roles/
cat roles/*/defaults/main.yml  # Identify variables
cat roles/*/tasks/main.yml      # Understand functionality
```

#### Step 3: Create Task Files
```bash
# Create prereq.yml
cp docs/platform_template/prereq.yml.example tasks/prereq.yml

# Create validate.yml
cat > tasks/validate.yml <<'EOF'
---
- name: Validate - Check service is running
  ansible.builtin.service:
    name: [service-name]
    state: started
  check_mode: true

- name: Validate - Check config file exists
  ansible.builtin.stat:
    path: /etc/[platform]/config.yml
  register: config_check
  failed_when: not config_check.stat.exists

- name: Validate - Display success
  ansible.builtin.debug:
    msg: "Validation successful"
EOF
```

#### Step 4-9: Follow Category B Steps 2-9

---

## Testing Checklist

Use this checklist for every platform after standardization:

### Pre-Deployment Tests
- [ ] Syntax check passes: `ansible-playbook playbooks/deploy.yml --syntax-check`
- [ ] YAML lint passes: `yamllint playbooks/ roles/`
- [ ] All CHANGE_THIS placeholders replaced in templates
- [ ] Requirements.yml includes all needed collections
- [ ] Inventory.example is valid and documented

### Dry-Run Tests
- [ ] Deploy dry-run: `ansible-playbook playbooks/deploy.yml --check`
- [ ] Configure dry-run: `ansible-playbook playbooks/configure.yml --check`
- [ ] Validate dry-run: `ansible-playbook playbooks/validate.yml --check`
- [ ] Test dry-run: `ansible-playbook playbooks/tests/test_deployment.yml --check`

### Functional Tests
- [ ] Prerequisites check runs successfully
- [ ] Deployment completes without errors
- [ ] Configuration applies correctly
- [ ] Validation confirms success
- [ ] All test categories pass (6/6)

### Independence Tests
- [ ] Can deploy without other platforms installed
- [ ] No hardcoded references to other platforms
- [ ] Variables don't depend on other platform variables
- [ ] Roles import paths are relative (../roles/...)

### Documentation Tests
- [ ] README.md follows template structure
- [ ] Quick start example is copy-paste ready
- [ ] Required variables clearly labeled
- [ ] Optional variables have defaults shown
- [ ] Troubleshooting section addresses common issues
- [ ] Fourth Estate features documented

### Variable Tests
- [ ] vars/example.yml contains all customizable variables
- [ ] Required variables marked with CHANGE_THIS
- [ ] Optional variables have sensible defaults
- [ ] Vault encryption examples included
- [ ] Variable names follow naming convention

### CI/CD Tests
- [ ] Platform added to test matrix in `.github/workflows/`
- [ ] GitHub Actions run successfully
- [ ] Test results visible in CI/CD output
- [ ] No security warnings from secret scanning

---

## Quality Assurance

### Peer Review Checklist

Before marking a platform as "complete", have another team member review:

#### Structure Review
- [ ] All required directories exist
- [ ] All required files present
- [ ] File naming follows conventions
- [ ] No unnecessary files (*.retry, *.pyc, etc.)

#### Code Review
- [ ] Playbooks are idempotent
- [ ] Tasks have descriptive names
- [ ] Variables use consistent naming
- [ ] No hardcoded credentials
- [ ] Proper use of tags
- [ ] Handlers defined where needed

#### Documentation Review
- [ ] README is comprehensive
- [ ] Examples are accurate
- [ ] Troubleshooting is helpful
- [ ] Variables are fully documented
- [ ] Fourth Estate features explained

#### Testing Review
- [ ] Tests cover all deployment steps
- [ ] Tests verify security controls
- [ ] Tests check compliance requirements
- [ ] Test output is clear and actionable
- [ ] Tests are reproducible

### Customer Acceptance Criteria

Platform is customer-ready when:

1. **Can deploy in isolation**
   - No dependencies on other platforms
   - All requirements documented
   - Prerequisites validated automatically

2. **Variables are customizable**
   - Example file provided
   - Required vs optional clearly marked
   - Vault encryption documented
   - Defaults are sensible

3. **Testing proves functionality**
   - Installation verified
   - Configuration verified
   - Security controls verified
   - Compliance requirements verified

4. **Documentation enables self-service**
   - Customer can deploy without support
   - Troubleshooting resolves common issues
   - Quick start takes < 30 minutes

5. **Meets Fourth Estate requirements**
   - Journalist source protection
   - Data classification handling
   - Audit logging (2-year retention)
   - Compliance framework support

---

## Tracking Progress

### Platform Status Dashboard

Create a tracking spreadsheet:

| Platform | Category | Structure | Playbooks | Tests | Variables | README | CI/CD | Status |
|----------|----------|-----------|-----------|-------|-----------|--------|-------|--------|
| crowdstrike | A | ✓ | ✓ | ✓ | ⚠️ | ⚠️ | ✓ | 85% |
| kubernetes | A | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |
| vmware | B | ✓ | ✗ | ✗ | ⚠️ | ⚠️ | ✗ | 35% |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Legend**:
- ✓ Complete
- ⚠️ Partial
- ✗ Missing

### Weekly Standup Questions
1. How many platforms completed this week?
2. Any blockers encountered?
3. Customer feedback received?
4. Priority changes needed?

### Milestones
- **Milestone 1** (Week 2): All Category A platforms have tests
- **Milestone 2** (Week 4): All Category B platforms have playbooks
- **Milestone 3** (Week 5): 50% of Category C platforms complete
- **Milestone 4** (Week 6): All platforms standardized and tested
- **Milestone 5** (Week 7): Customer UAT and feedback incorporation

---

## Getting Help

### Resources
- **Templates**: `/docs/platform_template/`
- **Examples**: `crowdstrike/`, `kubernetes/`, `splunk/`
- **Audit Report**: `/docs/PLATFORM_AUDIT_REPORT.md`
- **Structure Guide**: `/docs/platform_template/STRUCTURE.md`

### Support Channels
- **GitHub Issues**: Repository issues for bugs/questions
- **Pull Requests**: Submit for peer review
- **Documentation**: Update this guide as you learn

### Common Questions

**Q: What if my platform has a unique structure?**
A: Document it in README.md. Follow the template as closely as possible, but explain deviations.

**Q: What if I can't test without production credentials?**
A: Use check mode (`--check`) and mock API responses where possible. Document testing limitations.

**Q: What if variables conflict with existing customer deployments?**
A: Maintain backwards compatibility. Add new variables with defaults that preserve existing behavior.

**Q: How do I handle platform-specific package repositories?**
A: Document in requirements.yml and README.md. Provide alternative installation methods if possible.

---

## Success Criteria

### Platform-Level Success
Each platform is considered "standardized" when it passes all items in the Testing Checklist and Quality Assurance sections.

### Repository-Level Success
The repository is considered "customer-ready" when:
- 100% of platforms meet standardization requirements
- All platforms tested in CI/CD
- Customer documentation reviewed and approved
- At least 3 successful customer deployments

### Business-Level Success
- Reduced support burden (self-service)
- Faster customer onboarding (< 1 day per platform)
- Increased platform adoption (measured in deployments)
- Positive customer feedback

---

## Appendix: Quick Reference Commands

### Setup
```bash
# Clone repository
git clone https://github.com/your-org/ansible-playbooks-2.0.git
cd ansible-playbooks-2.0

# Checkout feature branch
git checkout -b standardize/[platform-name]
```

### Standardization
```bash
# Create structure
mkdir -p [platform]/playbooks/tests [platform]/tasks [platform]/vars

# Copy templates
cp docs/platform_template/deploy.yml.example [platform]/playbooks/deploy.yml
cp docs/platform_template/test_deployment.yml.example [platform]/playbooks/tests/test_deployment.yml
cp docs/platform_template/vars_example.yml [platform]/vars/example.yml
cp docs/platform_template/README_TEMPLATE.md [platform]/README.md
```

### Testing
```bash
# Syntax check
ansible-playbook [platform]/playbooks/deploy.yml --syntax-check

# YAML lint
yamllint [platform]/

# Dry-run
ansible-playbook [platform]/playbooks/deploy.yml --check -i [platform]/inventory.example

# Functional test
ansible-playbook [platform]/playbooks/tests/test_deployment.yml
```

### Commit and Push
```bash
# Stage changes
git add [platform]/

# Commit
git commit -m "feat: Standardize [platform] with tests and documentation"

# Push
git push origin standardize/[platform-name]

# Create PR
gh pr create --title "Standardize [platform]" --body "Addresses platform independence requirements"
```

# Standard Platform Directory Structure

This document defines the required directory structure for all platforms in the Fourth Estate Ansible Playbooks repository.

## Purpose
- **Consistency**: All platforms follow the same structure for easier navigation
- **Independence**: Each platform is self-contained and deployable standalone
- **Customer-Friendly**: Clear entry points for deployment and customization
- **Maintainability**: Standardized testing and documentation

---

## Required Directory Structure

```
platform-name/
├── README.md                           # Platform documentation (see README_TEMPLATE.md)
├── requirements.yml                    # Ansible Galaxy collections/roles needed
├── inventory.example                   # Example inventory file
│
├── playbooks/                          # Orchestration playbooks (REQUIRED)
│   ├── deploy.yml                     # Main deployment playbook
│   ├── configure.yml                  # Configuration update playbook
│   ├── validate.yml                   # Post-deployment validation
│   ├── uninstall.yml                  # Rollback/removal playbook
│   │
│   └── tests/                         # Functional tests (REQUIRED)
│       ├── test_deployment.yml        # Integration test
│       ├── test_connectivity.yml      # Connection test
│       └── test_compliance.yml        # Compliance validation test
│
├── roles/                             # Ansible roles (REQUIRED)
│   ├── role-name-1/
│   │   ├── defaults/
│   │   │   └── main.yml              # Default variables
│   │   ├── tasks/
│   │   │   └── main.yml              # Task implementation
│   │   ├── handlers/
│   │   │   └── main.yml              # Event handlers
│   │   ├── templates/
│   │   │   └── config.j2             # Jinja2 templates
│   │   ├── files/
│   │   │   └── static_file.conf      # Static files
│   │   ├── vars/
│   │   │   └── main.yml              # Role-specific variables
│   │   ├── meta/
│   │   │   └── main.yml              # Role metadata & dependencies
│   │   └── README.md                 # Role documentation
│   │
│   └── role-name-2/
│       └── [same structure]
│
├── tasks/                             # Reusable task files (OPTIONAL)
│   ├── prereq.yml                    # Prerequisites check
│   ├── install.yml                   # Installation tasks
│   ├── configure.yml                 # Configuration tasks
│   └── validate.yml                  # Validation tasks
│
├── vars/                              # Variable files (REQUIRED)
│   ├── example.yml                   # Example variables for customers
│   ├── development.yml               # Dev environment variables
│   ├── staging.yml                   # Staging environment variables
│   └── production.yml.example        # Production template (gitignored actual)
│
├── inventories/                       # Environment inventories (OPTIONAL)
│   ├── development/
│   │   ├── hosts.yml
│   │   └── group_vars/
│   ├── staging/
│   │   ├── hosts.yml
│   │   └── group_vars/
│   └── production.example/           # Example production inventory
│       ├── hosts.yml
│       └── group_vars/
│
├── templates/                         # Global templates (OPTIONAL)
│   └── platform_config.j2            # Platform-level config templates
│
├── files/                             # Static files (OPTIONAL)
│   └── platform_static_config.conf
│
└── docs/                              # Additional documentation (OPTIONAL)
    ├── architecture.md               # Architecture diagrams
    ├── troubleshooting.md            # Extended troubleshooting
    └── compliance/                   # Compliance mappings
        ├── nist_800_53.md
        └── stig.md
```

---

## Required Files Explanation

### `README.md` (REQUIRED)
**Purpose**: Primary documentation for customers
**Template**: Use `docs/platform_template/README_TEMPLATE.md`
**Contents**:
- Quick start guide
- Required vs. optional variables
- Deployment examples
- Troubleshooting guide

### `requirements.yml` (REQUIRED if using collections)
**Purpose**: Document Ansible Galaxy dependencies

Example:
```yaml
---
collections:
  - name: community.general
    version: ">=6.0.0"
  - name: ansible.posix
    version: ">=1.5.0"

roles: []  # External roles if needed
```

### `inventory.example` (REQUIRED)
**Purpose**: Show customers how to structure their inventory

Example:
```ini
[platform_servers]
server1.example.gov ansible_host=10.0.1.10
server2.example.gov ansible_host=10.0.1.11

[platform_servers:vars]
ansible_user=ansible-svc
ansible_become=true
```

### `playbooks/deploy.yml` (REQUIRED)
**Purpose**: Main entry point for deployment
**Must be idempotent**: Can run multiple times safely

Example:
```yaml
---
- name: Deploy [Platform Name]
  hosts: platform_servers
  gather_facts: true

  vars_files:
    - ../vars/{{ environment | default('production') }}.yml

  pre_tasks:
    - name: Validate prerequisites
      ansible.builtin.include_tasks: ../tasks/prereq.yml
      tags: [prereq, always]

  roles:
    - role: ../roles/platform_install
      tags: [install]

    - role: ../roles/platform_configure
      tags: [configure]

    - role: ../roles/platform_harden
      tags: [harden]
      when: fourth_estate_enabled | default(true)

  post_tasks:
    - name: Validate deployment
      ansible.builtin.include_tasks: ../tasks/validate.yml
      tags: [validate, always]
```

### `playbooks/tests/test_deployment.yml` (REQUIRED)
**Purpose**: Automated functional testing

Example:
```yaml
---
- name: Test [Platform] Deployment
  hosts: platform_servers
  gather_facts: true

  tasks:
    - name: Test - Platform service is running
      ansible.builtin.service:
        name: platform-service
        state: started
      check_mode: true
      register: service_test
      failed_when: service_test is changed

    - name: Test - Platform API is accessible
      ansible.builtin.uri:
        url: "https://{{ platform_hostname }}/api/health"
        validate_certs: true
        status_code: 200
      register: api_test

    - name: Test - Configuration file exists
      ansible.builtin.stat:
        path: /etc/platform/config.yml
      register: config_test
      failed_when: not config_test.stat.exists

    - name: Display test results
      ansible.builtin.debug:
        msg: "All tests passed! Platform is operational."
```

### `roles/[role-name]/` (REQUIRED)
**Purpose**: Self-contained role for specific functionality

**Required role files**:
- `defaults/main.yml` - Default variables with comments
- `tasks/main.yml` - Task implementation
- `meta/main.yml` - Role metadata

**Optional role files**:
- `handlers/main.yml` - Event handlers (if needed)
- `templates/` - Jinja2 templates (if needed)
- `files/` - Static files (if needed)
- `README.md` - Role-specific documentation (recommended)

### `vars/example.yml` (REQUIRED)
**Purpose**: Customer-facing variable template

Example:
```yaml
---
# [Platform Name] - Example Variables
# Copy this file to production.yml and customize for your environment

# ============================================================================
# REQUIRED VARIABLES - Must be customized
# ============================================================================

# Platform Connection
platform_hostname: "platform.example.gov"           # CHANGE_THIS
platform_port: 443
platform_username: "{{ vault_platform_username }}"  # Encrypted in vault
platform_password: "{{ vault_platform_password }}"  # Encrypted in vault

# Organization
organization_name: "Your Agency Name"               # CHANGE_THIS
org_abbreviation: "YAN"                             # CHANGE_THIS

# ============================================================================
# OPTIONAL VARIABLES - Have sensible defaults
# ============================================================================

# SSL/TLS
platform_validate_certs: true
platform_tls_min_version: "1.2"

# Fourth Estate Features
fourth_estate_enabled: true
journalist_source_protection: true

# Audit and Compliance
audit_log_enabled: true
audit_log_retention_days: 730  # 2 years

# Performance
platform_timeout: 60
platform_retries: 3

# ============================================================================
# VAULT VARIABLES - Encrypt these with ansible-vault
# ============================================================================

# Run: ansible-vault encrypt_string 'your-username' --name 'vault_platform_username'
vault_platform_username: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          [encrypted content]

vault_platform_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          [encrypted content]
```

---

## Directory Structure by Platform Category

### Category A: Full Production Platform
**Example**: CrowdStrike, Kubernetes, VMware

**Must Have**:
- ✅ All required files/directories
- ✅ Complete test suite
- ✅ Multiple deployment scenarios
- ✅ Comprehensive documentation

### Category B: Moderate Platform
**Example**: Cisco, Palo Alto, Splunk

**Must Have**:
- ✅ All required files/directories
- ✅ Basic test suite (at minimum: syntax, dry-run, connectivity)
- ✅ Standard deployment playbook
- ✅ README with quick start

### Category C: Minimal Platform
**Example**: Single-purpose utilities, integrations

**Must Have**:
- ✅ README.md
- ✅ playbooks/deploy.yml
- ✅ At least one role
- ✅ vars/example.yml
- ✅ Basic test (playbooks/tests/test_deployment.yml)

---

## File Naming Conventions

### Playbooks
- Use descriptive names: `deploy_falcon_sensors.yml` not `deploy.yml` alone
- Use underscores: `test_connectivity.yml` not `test-connectivity.yml`
- Main playbooks: `deploy.yml`, `configure.yml`, `validate.yml`, `uninstall.yml`

### Roles
- Use hyphens: `platform-install` not `platform_install`
- Be specific: `k8s-cluster-hardening` not `hardening`
- Include platform prefix if needed: `vmware-vcenter-config`

### Variables Files
- Use lowercase: `production.yml` not `Production.yml`
- Environment naming: `development.yml`, `staging.yml`, `production.yml`
- Examples: `example.yml` or `*.yml.example`

### Task Files
- Use verbs: `install.yml`, `configure.yml`, `validate.yml`
- Be specific: `install_agent.yml` not `agent.yml`

---

## Git Ignore Patterns

Add to `.gitignore` for platform directories:

```gitignore
# Customer-specific variable files (keep examples)
*/vars/production.yml
*/vars/development.yml
*/vars/staging.yml

# Customer-specific inventories
*/inventories/production/
*/inventories/development/
*/inventories/staging/

# Ansible runtime
*.retry
.ansible/
*.log

# Vault password files
.vault_pass*
**/vault_password*

# Test artifacts
**/tests/.pytest_cache/
**/tests/__pycache__/
```

---

## Migration Guide for Existing Platforms

### Step 1: Assess Current Structure
```bash
cd [platform-name]
ls -la
# Compare with standard structure above
```

### Step 2: Create Missing Directories
```bash
mkdir -p playbooks/tests roles tasks vars inventories docs
```

### Step 3: Create Required Files

If `playbooks/deploy.yml` missing:
```bash
cp docs/platform_template/deploy.yml.example [platform]/playbooks/deploy.yml
# Edit to include your roles
```

If `playbooks/tests/test_deployment.yml` missing:
```bash
cp docs/platform_template/test_deployment.yml.example [platform]/playbooks/tests/test_deployment.yml
# Edit to test your platform
```

If `vars/example.yml` missing:
```bash
# Extract variables from roles/*/defaults/main.yml
# Create vars/example.yml with all customizable variables
```

### Step 4: Update README.md
```bash
# Use README_TEMPLATE.md as reference
# Fill in platform-specific details
```

### Step 5: Add to CI/CD
Update `.github/workflows/test-new-platforms.yml`:
```yaml
matrix:
  platform:
    - [your-platform-name]
```

### Step 6: Test
```bash
# Syntax check
ansible-playbook [platform]/playbooks/deploy.yml --syntax-check

# Dry-run
ansible-playbook [platform]/playbooks/deploy.yml --check

# Run tests
ansible-playbook [platform]/playbooks/tests/test_deployment.yml
```

---

## Validation Checklist

Use this checklist when creating or migrating a platform:

### Required Structure
- [ ] `README.md` exists and follows template
- [ ] `requirements.yml` lists all dependencies
- [ ] `inventory.example` shows inventory structure
- [ ] `playbooks/deploy.yml` exists
- [ ] `playbooks/configure.yml` exists (or tasks in deploy.yml)
- [ ] `playbooks/validate.yml` exists
- [ ] `playbooks/tests/test_deployment.yml` exists
- [ ] At least one role in `roles/` directory
- [ ] `vars/example.yml` with customer-customizable variables

### Documentation Quality
- [ ] Quick start section with copy-paste example
- [ ] Required variables clearly labeled
- [ ] Optional variables have defaults shown
- [ ] Troubleshooting section exists
- [ ] Fourth Estate features documented

### Testing
- [ ] Syntax check passes: `ansible-playbook ... --syntax-check`
- [ ] Dry-run passes: `ansible-playbook ... --check`
- [ ] Functional test exists and passes
- [ ] CI/CD integration configured

### Independence
- [ ] No hard dependencies on other platforms
- [ ] All roles contained within platform directory
- [ ] Variables don't reference other platform variables
- [ ] Can deploy without other platforms present

### Customer Readiness
- [ ] Variable customization documented
- [ ] Example deployment shown in README
- [ ] Vault encryption explained
- [ ] Support contact information provided

---

## Questions or Issues?

- **Template Issues**: Open issue at [repository]/issues
- **Structure Questions**: See `/docs/PLATFORM_AUDIT_REPORT.md`
- **Migration Help**: Contact repository maintainers

# Ansible Tower / Automation Platform (AAP)

This directory contains **8 Ansible roles** for automating **Ansible Tower** (now Red Hat Ansible Automation Platform) deployment including installation, configuration, organizations, projects, inventories, job templates, workflows, and RBAC management.

## 📋 Roles

### Installation & Configuration (2 roles)
- **ansible_tower_install** - Tower/AAP installation and setup
- **ansible_tower_config** - Global configuration and settings

### Resource Management (4 roles)
- **ansible_tower_organizations** - Organization management
- **ansible_tower_projects** - Project (Git/SCM) configuration
- **ansible_tower_inventories** - Inventory and host management
- **ansible_tower_job_templates** - Job template creation

### Automation & Security (2 roles)
- **ansible_tower_workflows** - Workflow template automation
- **ansible_tower_rbac** - Role-Based Access Control

## 🚀 Quick Start

```bash
# Install Ansible Tower
ansible-playbook playbooks/tower_install.yml \
  -e "tower_version=3.8.6" \
  -e "tower_admin_password=SecurePassword123"

# Configure Tower organization
ansible-playbook playbooks/tower_setup.yml \
  -e "org_name=Fourth Estate" \
  -e "tower_host=tower.example.com"
```

## ⚙️ Configuration

### Tower Installation

```yaml
# Ansible Tower installation
tower_version: "3.8.6"  # or AAP 2.4
tower_admin_username: "admin"
tower_admin_password: "{{ vault_tower_admin_password }}"
tower_admin_email: "admin@example.com"

# Installation paths
tower_install_dir: "/opt/ansible-tower"
tower_backup_dir: "/var/backups/tower"

# Database configuration
tower_db_type: "postgresql"
tower_db_host: "localhost"
tower_db_port: 5432
tower_db_name: "awx"
tower_db_username: "awx"
tower_db_password: "{{ vault_tower_db_password }}"

# Redis (for AAP 2.x)
tower_redis_host: "localhost"
tower_redis_port: 6379
```

### Tower Connection

```yaml
# Tower API connection
tower_host: "tower.example.com"
tower_username: "admin"
tower_password: "{{ vault_tower_password }}"
tower_verify_ssl: true
tower_api_version: "v2"
```

### Organization Configuration

```yaml
# Organizations
tower_organizations:
  - name: "Fourth Estate"
    description: "Fourth Estate Infrastructure Team"
    max_hosts: 1000
    default_environment: "production"

  - name: "Development"
    description: "Development Team"
    max_hosts: 100
    default_environment: "development"
```

### Project Configuration

```yaml
# Projects (SCM repositories)
tower_projects:
  - name: "Infrastructure Playbooks"
    description: "Main infrastructure automation"
    organization: "Fourth Estate"
    scm_type: "git"
    scm_url: "https://github.com/example/ansible-playbooks.git"
    scm_branch: "main"
    scm_credential: "GitHub Token"
    scm_update_on_launch: true
    scm_update_cache_timeout: 0

  - name: "Security Compliance"
    description: "STIG and compliance playbooks"
    organization: "Fourth Estate"
    scm_type: "git"
    scm_url: "https://github.com/example/compliance-playbooks.git"
    scm_branch: "master"
    scm_credential: "GitHub SSH"
```

### Inventory Configuration

```yaml
# Static inventories
tower_inventories:
  - name: "Production Servers"
    description: "Production environment"
    organization: "Fourth Estate"
    variables:
      ansible_connection: "ssh"
      ansible_user: "automation"
      env: "production"

  - name: "AWS Dynamic Inventory"
    description: "AWS EC2 instances"
    organization: "Fourth Estate"
    source: "ec2"
    source_vars:
      regions:
        - "us-east-1"
        - "us-west-2"
      filters:
        tag:Environment:
          - "production"
    update_on_launch: true
    update_cache_timeout: 300

# Inventory sources (dynamic)
tower_inventory_sources:
  - name: "VMware vCenter"
    inventory: "Production Servers"
    source: "vmware"
    credential: "vCenter Credentials"
    source_vars:
      hostname: "vcenter.example.com"
      username: "automation@vsphere.local"
      validate_certs: false
```

### Credential Configuration

```yaml
# Credentials
tower_credentials:
  # Machine credentials
  - name: "SSH Automation Account"
    credential_type: "Machine"
    organization: "Fourth Estate"
    inputs:
      username: "automation"
      ssh_key_data: "{{ lookup('file', 'keys/automation_id_rsa') }}"
      become_method: "sudo"
      become_username: "root"

  # Cloud credentials
  - name: "AWS Credentials"
    credential_type: "Amazon Web Services"
    organization: "Fourth Estate"
    inputs:
      username: "{{ vault_aws_access_key }}"
      password: "{{ vault_aws_secret_key }}"

  - name: "Azure Credentials"
    credential_type: "Microsoft Azure"
    organization: "Fourth Estate"
    inputs:
      subscription: "{{ vault_azure_subscription_id }}"
      username: "{{ vault_azure_client_id }}"
      password: "{{ vault_azure_secret }}"
      tenant: "{{ vault_azure_tenant }}"

  # SCM credentials
  - name: "GitHub Token"
    credential_type: "Source Control"
    organization: "Fourth Estate"
    inputs:
      username: "git"
      password: "{{ vault_github_token }}"

  # Vault credentials
  - name: "HashiCorp Vault"
    credential_type: "Vault"
    organization: "Fourth Estate"
    inputs:
      vault_server: "https://vault.example.com"
      vault_token: "{{ vault_hc_vault_token }}"
```

### Job Template Configuration

```yaml
# Job templates
tower_job_templates:
  - name: "Deploy Web Application"
    description: "Deploy web application to production"
    organization: "Fourth Estate"
    project: "Infrastructure Playbooks"
    playbook: "playbooks/deploy_web_app.yml"
    inventory: "Production Servers"
    credentials:
      - "SSH Automation Account"
      - "AWS Credentials"
    job_type: "run"
    verbosity: 1
    limit: "webservers"
    extra_vars:
      app_version: "latest"
      rolling_update: true
    ask_variables_on_launch: true
    concurrent_jobs_enabled: false

  - name: "Patch Linux Servers"
    description: "Apply OS patches to Linux servers"
    organization: "Fourth Estate"
    project: "Infrastructure Playbooks"
    playbook: "playbooks/patch_linux.yml"
    inventory: "Production Servers"
    credentials:
      - "SSH Automation Account"
    forks: 5
    job_slice_count: 10
    timeout: 7200

  - name: "STIG Compliance Check"
    description: "Run STIG compliance scan"
    organization: "Fourth Estate"
    project: "Security Compliance"
    playbook: "playbooks/stig_scan.yml"
    inventory: "Production Servers"
    survey_enabled: true
    survey_spec:
      name: "STIG Options"
      description: "Select STIG options"
      spec:
        - question_name: "Target OS"
          question_description: "Select target operating system"
          required: true
          type: "multiplechoice"
          variable: "target_os"
          choices:
            - "RHEL 8"
            - "Ubuntu 20.04"
            - "Windows Server 2019"
```

### Workflow Configuration

```yaml
# Workflow templates
tower_workflows:
  - name: "Full Application Deployment"
    description: "Complete deployment workflow"
    organization: "Fourth Estate"
    workflow_nodes:
      # Step 1: Provision infrastructure
      - identifier: "provision"
        unified_job_template: "Provision AWS Infrastructure"
        success_nodes:
          - "configure"

      # Step 2: Configure servers
      - identifier: "configure"
        unified_job_template: "Configure Web Servers"
        success_nodes:
          - "deploy"
          - "monitoring"

      # Step 3: Deploy application
      - identifier: "deploy"
        unified_job_template: "Deploy Web Application"
        success_nodes:
          - "test"
        failure_nodes:
          - "rollback"

      # Step 4: Run tests
      - identifier: "test"
        unified_job_template: "Run Integration Tests"
        success_nodes:
          - "notify_success"
        failure_nodes:
          - "rollback"

      # Step 5: Setup monitoring
      - identifier: "monitoring"
        unified_job_template: "Configure Monitoring"

      # Rollback on failure
      - identifier: "rollback"
        unified_job_template: "Rollback Deployment"
        always_nodes:
          - "notify_failure"

      # Notifications
      - identifier: "notify_success"
        unified_job_template: "Send Success Notification"

      - identifier: "notify_failure"
        unified_job_template: "Send Failure Notification"
```

### RBAC Configuration

```yaml
# Teams and RBAC
tower_teams:
  - name: "Infrastructure Team"
    organization: "Fourth Estate"
    description: "Infrastructure engineers"

  - name: "Security Team"
    organization: "Fourth Estate"
    description: "Security and compliance team"

  - name: "Application Developers"
    organization: "Fourth Estate"
    description: "Application development team"

# Role assignments
tower_role_assignments:
  # Infrastructure team - admin access
  - team: "Infrastructure Team"
    role: "admin"
    target_type: "organization"
    target: "Fourth Estate"

  # Security team - execute compliance jobs
  - team: "Security Team"
    role: "execute"
    target_type: "job_template"
    target: "STIG Compliance Check"

  # Developers - use specific templates
  - team: "Application Developers"
    role: "execute"
    target_type: "job_template"
    target: "Deploy Web Application"

  - team: "Application Developers"
    role: "read"
    target_type: "inventory"
    target: "Production Servers"
```

### Notification Configuration

```yaml
# Notification templates
tower_notifications:
  - name: "Slack - Infrastructure"
    notification_type: "slack"
    organization: "Fourth Estate"
    notification_configuration:
      token: "{{ vault_slack_token }}"
      channels:
        - "#infrastructure"
      hex_color: "#FF0000"

  - name: "Email - Operations"
    notification_type: "email"
    organization: "Fourth Estate"
    notification_configuration:
      host: "smtp.example.com"
      port: 587
      use_tls: true
      username: "tower@example.com"
      password: "{{ vault_smtp_password }}"
      sender: "tower@example.com"
      recipients:
        - "ops-team@example.com"

  - name: "PagerDuty - Critical"
    notification_type: "pagerduty"
    organization: "Fourth Estate"
    notification_configuration:
      token: "{{ vault_pagerduty_token }}"
      subdomain: "example"
      service_key: "{{ vault_pagerduty_service_key }}"
```

## 📖 Common Use Cases

### Use Case 1: Deploy Ansible Tower

```yaml
---
# playbooks/tower_install.yml
- name: Install Ansible Tower
  hosts: tower_servers
  become: true

  roles:
    - role: ansible_tower_install
      vars:
        tower_version: "3.8.6"
        tower_admin_password: "{{ vault_admin_password }}"
```

### Use Case 2: Configure Tower Resources

```bash
ansible-playbook playbooks/tower_configure.yml \
  -e "tower_host=tower.example.com" \
  -e "org_name=Fourth Estate"
```

### Use Case 3: Create Job Template

```bash
ansible-playbook playbooks/tower_job_template.yml \
  -e "template_name=Deploy Application" \
  -e "project=Infrastructure" \
  -e "playbook=deploy.yml"
```

### Use Case 4: Setup Workflow

```bash
ansible-playbook playbooks/tower_workflow.yml \
  -e "workflow_name=CI/CD Pipeline" \
  -e "workflow_file=workflows/cicd.json"
```

## 🔄 Integration Examples

### Integration with Git (GitLab CI/CD)

```yaml
# .gitlab-ci.yml
deploy_production:
  stage: deploy
  script:
    - |
      curl -X POST https://tower.example.com/api/v2/job_templates/10/launch/ \
        -H "Authorization: Bearer $TOWER_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{"extra_vars": {"git_commit": "'$CI_COMMIT_SHA'"}}'
  only:
    - main
```

### Integration with ServiceNow

```yaml
# Tower job template with ServiceNow integration
- name: Update ServiceNow change request
  servicenow.servicenow.snow_record:
    instance: "{{ snow_instance }}"
    table: "change_request"
    number: "{{ change_number }}"
    state: present
    data:
      state: "3"  # Implement
      work_notes: "Ansible Tower job {{ tower_job_id }} completed"
```

### Integration with Vault

```yaml
# Tower credential sourcing from Vault
tower_credentials:
  - name: "Database Password from Vault"
    credential_type: "Machine"
    inputs:
      username: "dbadmin"
      password: "{{ lookup('hashi_vault', 'secret=database/creds/admin') }}"
```

## 🛡️ Security Best Practices

1. **Enable HTTPS** - Always use TLS/SSL for Tower UI and API
2. **RBAC** - Implement least privilege with teams and roles
3. **Credential Isolation** - Use Tower's credential system, never hardcode
4. **Audit Logging** - Enable activity stream and integrate with SIEM
5. **MFA** - Enable multi-factor authentication for admin accounts
6. **API Token Management** - Use short-lived API tokens
7. **Isolated Execution** - Use execution environments for job isolation
8. **Network Segmentation** - Isolate Tower in management network
9. **Regular Backups** - Automate Tower database backups
10. **Version Control** - Track Tower configuration as code

## 🔧 Troubleshooting

### Issue: Tower Installation Failed

**Symptoms:** Installation script fails

**Resolution:**
```bash
# Check system requirements
./setup.sh -h

# Review installation log
tail -f /var/log/tower/setup.log

# Verify database connectivity
psql -h localhost -U awx -d awx -c "SELECT 1"
```

### Issue: Job Execution Fails

**Symptoms:** Job stuck in "pending" or fails immediately

**Resolution:**
```bash
# Check Tower services
sudo systemctl status ansible-tower

# Review job logs
awx-manage check_license
awx-manage inventory_import --source=/var/lib/awx/projects

# Check capacity
tower-cli setting list | grep capacity
```

### Issue: Project Sync Failing

**Symptoms:** Cannot sync project from Git

**Resolution:**
```bash
# Test SCM access
git ls-remote https://github.com/example/repo.git

# Check credential
tower-cli credential get --name "GitHub Token"

# Manual project update
tower-cli project update --name "Infrastructure Playbooks" --wait
```

## 📚 Additional Resources

- [Ansible Tower Documentation](https://docs.ansible.com/ansible-tower/)
- [AAP 2 Documentation](https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/2.4)
- [Tower API Documentation](https://docs.ansible.com/ansible-tower/latest/html/towerapi/)
- [AWX (Open Source)](https://github.com/ansible/awx)
- [Ansible Galaxy](https://galaxy.ansible.com/)
- [Tower/AAP Best Practices](https://www.ansible.com/products/tower)

## 🤝 Contributing

When contributing to Tower/AAP automation:
- Test in development Tower instance first
- Use tower-cli or awx CLI for validation
- Document RBAC requirements
- Version control Tower configuration
- Include rollback procedures
- Test workflow error paths
- Validate credentials work before deployment

---

**Last Updated:** 2026-01-16
**Maintained By:** Fourth Estate Infrastructure Team
**Versions Supported:** Ansible Tower 3.8+, Red Hat AAP 2.0+, AWX 21.0+

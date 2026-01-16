# ServiceNow CMDB Integration

This directory contains **8 Ansible roles** for automating **ServiceNow** integration including CMDB discovery, configuration item updates, incident management, change management, asset tracking, and automated workflows.

## 📋 Roles

### Configuration (1 role)
- **servicenow_cmdb_config** - CMDB configuration and setup

### Discovery & Updates (2 roles)
- **servicenow_ci_discovery** - Automated CI discovery from infrastructure
- **servicenow_ci_updates** - Configuration item synchronization

### ITSM Integration (3 roles)
- **servicenow_incident_management** - Automated incident creation and updates
- **servicenow_change_management** - Change request automation
- **servicenow_asset_management** - Asset lifecycle management

### Integration & Reporting (2 roles)
- **servicenow_integration** - API integration and webhooks
- **servicenow_reporting** - Custom dashboard and report generation

## 🚀 Quick Start

```bash
# Configure CMDB integration
ansible-playbook playbooks/servicenow_setup.yml \
  -e "snow_instance=dev12345" \
  -e "snow_user=ansible_api"

# Discover and sync infrastructure
ansible-playbook playbooks/servicenow_discovery.yml \
  -e "discovery_source=aws" \
  -e "cmdb_class=cmdb_ci_server"
```

## ⚙️ Configuration

### ServiceNow Connection

```yaml
# ServiceNow instance connection
snow_instance: "dev12345"  # or prod12345
snow_hostname: "{{ snow_instance }}.service-now.com"
snow_username: "ansible_api"
snow_password: "{{ vault_snow_password }}"
snow_client_id: "{{ vault_snow_client_id }}"
snow_client_secret: "{{ vault_snow_client_secret }}"

# API settings
snow_api_version: "v1"
snow_timeout: 30
snow_validate_certs: true
```

### CMDB Configuration

```yaml
# CMDB configuration
cmdb_config:
  enable_auto_discovery: true
  discovery_frequency: "daily"
  reconciliation_rules:
    - field: "serial_number"
      priority: 1
    - field: "mac_address"
      priority: 2
    - field: "hostname"
      priority: 3

  # CI class mapping
  class_mapping:
    aws_ec2: "cmdb_ci_ec2_instance"
    vmware_vm: "cmdb_ci_vmware_instance"
    physical_server: "cmdb_ci_server"
    network_device: "cmdb_ci_netgear"
```

### CI Discovery Configuration

```yaml
# Automated discovery sources
discovery_sources:
  - name: "AWS Discovery"
    type: "aws"
    enabled: true
    schedule: "0 2 * * *"  # Daily at 2 AM
    regions:
      - "us-east-1"
      - "us-west-2"
    cmdb_class: "cmdb_ci_ec2_instance"
    attributes:
      - "instance_id"
      - "instance_type"
      - "private_ip_address"
      - "tags"

  - name: "VMware Discovery"
    type: "vmware"
    enabled: true
    schedule: "0 3 * * *"
    vcenter_host: "vcenter.example.com"
    cmdb_class: "cmdb_ci_vmware_instance"

  - name: "Network Device Discovery"
    type: "snmp"
    enabled: true
    schedule: "0 4 * * *"
    community_string: "{{ vault_snmp_community }}"
    cmdb_class: "cmdb_ci_netgear"
```

### CI Update Configuration

```yaml
# CI synchronization
ci_sync_config:
  update_strategy: "merge"  # merge, overwrite, or skip
  sync_frequency: "hourly"

  # Fields to sync
  sync_fields:
    - "name"
    - "ip_address"
    - "os"
    - "os_version"
    - "cpu_count"
    - "ram"
    - "disk_space"
    - "location"
    - "operational_status"

  # Relationship mapping
  relationships:
    - type: "Hosted on::Hosts"
      parent_class: "cmdb_ci_esx_server"
      child_class: "cmdb_ci_vmware_instance"
```

### Incident Management Configuration

```yaml
# Incident automation
incident_config:
  # Auto-create incidents
  auto_create_incidents:
    - trigger: "monitoring_alert"
      severity_mapping:
        critical: "1"
        high: "2"
        medium: "3"
        low: "4"
      assignment_group: "Network Operations"
      category: "Infrastructure"

  # Incident templates
  templates:
    - name: "Server Down"
      short_description: "Server {{ ci_name }} is down"
      description: |
        Server {{ ci_name }} ({{ ip_address }}) is not responding.
        Time: {{ timestamp }}
        Alert: {{ alert_message }}
      urgency: "1"
      impact: "1"
      assignment_group: "Server Team"

    - name: "Disk Space Alert"
      short_description: "Low disk space on {{ ci_name }}"
      urgency: "3"
      impact: "2"
      assignment_group: "Storage Team"
```

### Change Management Configuration

```yaml
# Change request automation
change_config:
  # Change templates
  templates:
    - name: "Standard Change - Patching"
      type: "standard"
      category: "Software"
      risk: "low"
      approval_required: false
      change_window: "maintenance"

    - name: "Normal Change - Infrastructure"
      type: "normal"
      category: "Infrastructure"
      risk: "moderate"
      approval_required: true
      approvers:
        - "Change Advisory Board"
        - "Infrastructure Manager"

  # Auto-approval rules
  auto_approve:
    - condition: "type == 'standard' AND risk == 'low'"
      auto_close: true
    - condition: "scheduled_time IN maintenance_window"
      skip_cab: true
```

### Asset Management Configuration

```yaml
# Asset lifecycle tracking
asset_config:
  # Asset categories
  categories:
    - name: "Hardware"
      subcategories:
        - "Server"
        - "Network Equipment"
        - "Storage"
    - name: "Software"
      subcategories:
        - "Operating System"
        - "Application"
        - "Database"

  # Lifecycle stages
  lifecycle:
    - stage: "ordered"
      next_stage: "received"
    - stage: "received"
      next_stage: "in_stock"
    - stage: "in_stock"
      next_stage: "deployed"
    - stage: "deployed"
      next_stage: "retired"

  # Auto-retire rules
  retire_rules:
    - condition: "age > 5 years AND type == 'server'"
      notify: "Asset Manager"
    - condition: "last_discovered > 90 days ago"
      status: "missing"
```

## 📖 Common Use Cases

### Use Case 1: Sync AWS Infrastructure to CMDB

```yaml
---
# playbooks/servicenow_aws_sync.yml
- name: Sync AWS EC2 Instances to ServiceNow CMDB
  hosts: localhost
  connection: local
  gather_facts: false

  tasks:
    - name: Get AWS EC2 instances
      amazon.aws.ec2_instance_info:
        region: "{{ aws_region }}"
      register: ec2_instances

    - name: Update ServiceNow CMDB
      include_role:
        name: servicenow_ci_updates
      vars:
        ci_class: "cmdb_ci_ec2_instance"
        ci_data: "{{ ec2_instances.instances }}"
```

### Use Case 2: Create Incident from Monitoring Alert

```bash
ansible-playbook playbooks/servicenow_create_incident.yml \
  -e "alert_severity=critical" \
  -e "ci_name=web-server-01" \
  -e "alert_message=Server not responding"
```

### Use Case 3: Automated Change Request

```bash
ansible-playbook playbooks/servicenow_change_request.yml \
  -e "change_type=standard" \
  -e "change_category=patching" \
  -e "affected_cis=prod-servers" \
  -e "scheduled_time=2026-01-20T02:00:00"
```

### Use Case 4: Asset Discovery and Registration

```bash
ansible-playbook playbooks/servicenow_asset_discovery.yml \
  -e "discovery_method=network_scan" \
  -e "network_range=10.0.0.0/16" \
  -e "asset_category=hardware"
```

## 🔄 Integration Examples

### Integration with Ansible Tower

```yaml
# Tower job template posts to ServiceNow
- name: Update ServiceNow after deployment
  servicenow.servicenow.snow_record:
    instance: "{{ snow_instance }}"
    username: "{{ snow_username }}"
    password: "{{ snow_password }}"
    table: "change_request"
    state: present
    data:
      number: "{{ change_number }}"
      state: "3"  # Implement
      work_notes: "Ansible Tower job {{ tower_job_id }} completed successfully"
```

### Integration with Monitoring (Prometheus)

```yaml
# Create incident from Prometheus alert
- name: Create ServiceNow incident from alert
  servicenow.servicenow.snow_record:
    table: "incident"
    state: present
    data:
      short_description: "{{ alert.labels.alertname }}"
      description: "{{ alert.annotations.description }}"
      severity: "{{ alert.labels.severity | map_severity }}"
      assignment_group: "NOC"
      configuration_item: "{{ alert.labels.instance }}"
```

### Integration with Git/CI/CD

```yaml
# Update change request from Git commit
- name: Link Git commits to change request
  servicenow.servicenow.snow_record:
    table: "change_request"
    state: present
    number: "{{ change_number }}"
    data:
      work_notes: |
        Git commit: {{ git_commit_hash }}
        Author: {{ git_author }}
        Message: {{ git_commit_message }}
        Files changed: {{ git_files_changed }}
```

## 🛡️ Security Best Practices

1. **API Access Control** - Use dedicated service account with minimal permissions
2. **OAuth Authentication** - Prefer OAuth 2.0 over basic auth
3. **Credential Management** - Store credentials in Ansible Vault
4. **Network Security** - Use TLS/SSL for all API calls
5. **Rate Limiting** - Respect ServiceNow API rate limits
6. **Audit Logging** - Enable audit logs for all API transactions
7. **Data Validation** - Validate data before creating/updating records
8. **Error Handling** - Implement retry logic with exponential backoff
9. **Least Privilege** - Grant minimum required table permissions
10. **Regular Reviews** - Audit ServiceNow integration accounts regularly

## 🔧 Troubleshooting

### Issue: Authentication Failed

**Symptoms:** "Invalid user credentials" error

**Resolution:**
```bash
# Test ServiceNow credentials
curl -u "username:password" \
  "https://dev12345.service-now.com/api/now/table/incident?sysparm_limit=1"

# Verify OAuth token
ansible-playbook playbooks/test_snow_auth.yml -vvv
```

### Issue: CI Not Found in CMDB

**Symptoms:** Cannot find configuration item

**Resolution:**
```bash
# Search for CI
curl "https://dev12345.service-now.com/api/now/table/cmdb_ci_server?sysparm_query=name=web-server-01"

# Run discovery
ansible-playbook playbooks/servicenow_ci_discovery.yml \
  -e "force_discovery=true" \
  -e "ci_name=web-server-01"
```

### Issue: API Rate Limit Exceeded

**Symptoms:** HTTP 429 Too Many Requests

**Resolution:**
```yaml
# Implement rate limiting in playbook
- name: Update CIs with rate limiting
  servicenow.servicenow.snow_record:
    # ... configuration ...
  loop: "{{ ci_list }}"
  throttle: 5  # Max 5 concurrent requests
  delay: 2     # 2 second delay between requests
```

## 📚 Additional Resources

- [ServiceNow REST API Documentation](https://developer.servicenow.com/dev.do#!/reference/api/latest/rest)
- [ServiceNow CMDB Documentation](https://docs.servicenow.com/bundle/latest/page/product/configuration-management/concept/c_ITILConfigurationManagement.html)
- [Ansible ServiceNow Collection](https://galaxy.ansible.com/servicenow/servicenow)
- [ServiceNow Developer Portal](https://developer.servicenow.com/)
- [ServiceNow Community](https://community.servicenow.com/)

## 🤝 Contributing

When contributing to ServiceNow automation:
- Test against ServiceNow Personal Developer Instance
- Follow ServiceNow CMDB best practices
- Document table schemas and field mappings
- Include error handling for API failures
- Test with rate limiting enabled
- Validate CMDB relationships
- Include rollback procedures

---

**Last Updated:** 2026-01-16
**Maintained By:** Fourth Estate Infrastructure Team
**ServiceNow Versions Supported:** Tokyo, Utah, Vancouver, Washington

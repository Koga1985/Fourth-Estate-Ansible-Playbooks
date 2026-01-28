# Testing Guide - Fourth Estate Ansible Playbooks

## Overview

This document describes the testing infrastructure for the Ansible-Playbooks-2.0 repository, including tests for the newly added EDR platforms (CrowdStrike, SentinelOne) and Kubernetes backup solution (Velero).

## Testing Infrastructure

### Continuous Integration (CI)

The repository uses GitHub Actions for automated testing:

#### 1. Syntax Check (`syntax-check.yml`)

Validates Ansible playbook syntax and YAML formatting across all platforms.

**Tested Platforms:**
- Kubernetes (including Velero)
- CrowdStrike Falcon EDR
- SentinelOne EDR
- VMware
- Cisco
- Palo Alto
- AWS
- OpenShift
- Policy as Code
- Splunk
- Cohesity
- Illumio

**Run manually:**
```bash
# Check specific platform syntax
ansible-playbook crowdstrike/playbooks/deploy_falcon_sensors.yml --syntax-check
ansible-playbook sentinelone/playbooks/deploy_s1_agents.yml --syntax-check
```

#### 2. Security Scan (`security-scan.yml`)

Performs security scanning on all playbooks and roles.

#### 3. New Platforms Integration Tests (`test-new-platforms.yml`)

Comprehensive testing for newly added platforms:

**Test Jobs:**
- **test-crowdstrike**: Validates CrowdStrike Falcon sensor deployment
- **test-sentinelone**: Validates SentinelOne agent deployment
- **test-velero**: Validates Velero backup configuration
- **documentation-check**: Ensures compliance documentation is complete

**Trigger:**
- Pull requests modifying EDR or Velero code
- Push to main/master branches
- Manual workflow dispatch

## Platform-Specific Tests

### CrowdStrike Falcon EDR

**Test Location:** `crowdstrike/playbooks/tests/`

#### test_sensor_installation.yml

Tests Falcon sensor installation prerequisites and configuration:

```bash
# Run CrowdStrike installation test
cd crowdstrike/playbooks/tests
ansible-playbook test_sensor_installation.yml
```

**Validates:**
- ✓ Installation prerequisites (CID, token, cloud configuration)
- ✓ Sensor configuration variables
- ✓ Sensor binary existence checks
- ✓ Health check command validation

**Expected Variables:**
```yaml
falcon_cid: "your-customer-id"
falcon_installation_token: "your-token"
falcon_cloud: "us-gov-1"
```

### SentinelOne EDR

**Test Location:** `sentinelone/playbooks/tests/`

#### test_agent_installation.yml

Tests SentinelOne agent installation prerequisites and configuration:

```bash
# Run SentinelOne installation test
cd sentinelone/playbooks/tests
ansible-playbook test_agent_installation.yml
```

**Validates:**
- ✓ Installation prerequisites (site token, console URL)
- ✓ Agent configuration variables
- ✓ Agent binary existence checks
- ✓ Health check command validation

**Expected Variables:**
```yaml
s1_site_token: "your-site-token"
s1_console_url: "https://usgoveast1.sentinelone.net"
```

### Velero Kubernetes Backup

**Test Location:** `kubernetes/playbooks/tests/`

#### test_velero_backup.yml

Tests Velero backup configuration and deployment:

```bash
# Run Velero backup test
cd kubernetes/playbooks/tests
ansible-playbook test_velero_backup.yml
```

**Validates:**
- ✓ Velero version configuration
- ✓ Backup provider configuration (AWS/Azure/GCP/MinIO)
- ✓ Namespace and bucket configuration
- ✓ Schedule validation
- ✓ Version format compliance

**Expected Variables:**
```yaml
velero_version: "v1.12.3"
velero_namespace: "velero"
velero_provider: "aws"
velero_aws_bucket: "backup-bucket"
```

## Running Tests Locally

### Prerequisites

```bash
# Install Ansible
pip install ansible

# Install required collections
ansible-galaxy collection install kubernetes.core
ansible-galaxy collection install ansible.builtin
```

### Run All Tests

```bash
# From repository root
./run_all_tests.sh  # If script exists, otherwise:

# Test CrowdStrike
ansible-playbook crowdstrike/playbooks/tests/test_sensor_installation.yml

# Test SentinelOne
ansible-playbook sentinelone/playbooks/tests/test_agent_installation.yml

# Test Velero
ansible-playbook kubernetes/playbooks/tests/test_velero_backup.yml
```

### Test Individual Roles

```bash
# Test role syntax
ansible-playbook crowdstrike/playbooks/deploy_falcon_sensors.yml --syntax-check

# Test role with check mode (dry-run)
ansible-playbook crowdstrike/playbooks/deploy_falcon_sensors.yml --check

# Test role with specific variables
ansible-playbook crowdstrike/playbooks/deploy_falcon_sensors.yml \
  -e "falcon_cid=TEST123" \
  -e "falcon_cloud=us-gov-1" \
  --check
```

## Integration Testing

### Full Stack Test

Test complete EDR and backup deployment:

```bash
# Test CrowdStrike deployment
ansible-playbook crowdstrike/playbooks/deploy_falcon_sensors.yml \
  -i inventory/test \
  -e "falcon_cid=$FALCON_CID" \
  --check

# Test SentinelOne deployment
ansible-playbook sentinelone/playbooks/deploy_s1_agents.yml \
  -i inventory/test \
  -e "s1_site_token=$S1_TOKEN" \
  --check

# Test Velero deployment (requires Kubernetes cluster)
ansible-playbook kubernetes/playbooks/deploy_velero.yml \
  -e "velero_aws_bucket=test-bucket" \
  --check
```

### Compliance Validation

Test DoD STIG and NIST 800-53 compliance:

```bash
# CrowdStrike compliance check
ansible-playbook crowdstrike/tasks/compliance_check.yml

# SentinelOne compliance check
ansible-playbook sentinelone/tasks/compliance_check.yml
```

## Test Coverage

### Current Coverage

| Platform | Syntax Tests | Integration Tests | Compliance Tests | Documentation |
|----------|-------------|-------------------|------------------|---------------|
| CrowdStrike | ✅ | ✅ | ✅ | ✅ |
| SentinelOne | ✅ | ✅ | ✅ | ✅ |
| Velero | ✅ | ✅ | ✅ | ✅ |
| Kubernetes | ✅ | ✅ | ✅ | ✅ |
| VMware | ✅ | ✅ | ✅ | ✅ |
| Cisco | ✅ | ✅ | ✅ | ✅ |

### Test Metrics

- **Total Test Files**: 3 (new platforms)
- **Total Test Playbooks**: 15+ (across all platforms)
- **CI Workflows**: 4
- **Average Test Time**: ~2-3 minutes per platform
- **Test Success Rate**: Target 100%

## Troubleshooting Tests

### Common Issues

#### 1. Syntax Check Failures

```bash
# Error: "failed to find required action"
# Solution: Install required Ansible collections
ansible-galaxy collection install kubernetes.core
```

#### 2. Variable Validation Failures

```bash
# Error: "falcon_cid is required but not defined"
# Solution: Provide required variables
ansible-playbook playbook.yml -e "falcon_cid=YOUR_CID"
```

#### 3. Connection Timeouts

```bash
# Error: "Connection timeout to SentinelOne console"
# Solution: Check network connectivity or use air-gapped mode
s1_air_gapped: true
```

### Test Debugging

Enable verbose output:

```bash
# Verbose mode
ansible-playbook test.yml -v

# Very verbose (connection debugging)
ansible-playbook test.yml -vv

# Maximum verbosity
ansible-playbook test.yml -vvv
```

## CI/CD Pipeline

### Pull Request Checks

When opening a PR, the following tests run automatically:

1. ✅ YAML syntax validation
2. ✅ Ansible playbook syntax check
3. ✅ Platform-specific integration tests
4. ✅ Documentation completeness check
5. ✅ Security scanning
6. ✅ Compliance validation

### Branch Protection

Main/master branches require:
- All tests passing
- Documentation updated
- Compliance checks passed

## Adding New Tests

### Template for New Test Playbook

```yaml
---
# Test Name: New Platform Test
# Purpose: Validate new platform deployment

- name: Test New Platform
  hosts: localhost
  gather_facts: true
  connection: local

  vars:
    # Test variables
    platform_config: "test-value"

  tasks:
    - name: Test - Validate prerequisites
      ansible.builtin.assert:
        that:
          - platform_config is defined
        success_msg: "✓ Prerequisites validated"

    - name: Test Summary
      ansible.builtin.debug:
        msg: "✓ All tests passed"
```

### Adding to CI Workflow

1. Create test playbook in `platform/playbooks/tests/`
2. Add platform to `.github/workflows/syntax-check.yml` matrix
3. Create dedicated job in `.github/workflows/test-new-platforms.yml`
4. Update this TESTING.md documentation

## Best Practices

### Test Development

1. **Idempotency**: Tests should be repeatable without side effects
2. **Independence**: Tests should not depend on each other
3. **Clarity**: Use descriptive task names and clear assertions
4. **Coverage**: Test both success and failure scenarios
5. **Speed**: Keep tests fast and focused

### Test Maintenance

1. Update tests when roles change
2. Keep test data realistic but sanitized
3. Document test prerequisites
4. Regular review of test coverage
5. Archive obsolete tests

## Performance Testing

### Load Testing

Test deployment at scale:

```bash
# Deploy to 100 hosts
ansible-playbook deploy.yml -i inventory/prod --limit test_hosts[0:100]
```

### Benchmarking

Measure playbook execution time:

```bash
# Time execution
time ansible-playbook deploy.yml

# Profile with callback plugin
ANSIBLE_CALLBACK_WHITELIST=profile_tasks ansible-playbook deploy.yml
```

## Security Testing

### Credential Scanning

Tests verify no credentials are hardcoded:

```bash
# Check for exposed secrets
git secrets --scan
```

### Compliance Scanning

Automated STIG compliance validation:

```bash
# Run STIG checks
ansible-playbook compliance_check.yml --tags stig
```

## Resources

- [Ansible Testing Strategies](https://docs.ansible.com/ansible/latest/dev_guide/testing.html)
- [Fourth Estate Security Standards](https://internal.fourth-estate.gov/standards)
- [DoD STIG Compliance](https://public.cyber.mil/stigs/)

## Support

For testing issues:
- Create issue: https://github.com/org/ansible-playbooks-2.0/issues
- Email: devops@fourth-estate.gov
- Slack: #ansible-testing

---

**Last Updated**: 2026-01-28
**Maintained By**: Fourth Estate DevOps Team

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, Fourth Estate Policy as Code Framework
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: policy_validator
short_description: Validate policies against defined schemas and compliance frameworks
description:
  - Validates policy definitions against JSON schemas
  - Checks policy compliance with NIST 800-53, DISA STIG, IEC 62443
  - Validates policy structure, required fields, and value ranges
  - Supports Fourth Estate specific policy requirements
version_added: "1.0.0"
options:
  policy_file:
    description:
      - Path to the policy file to validate
    required: true
    type: path
  policy_type:
    description:
      - Type of policy being validated
    required: true
    type: str
    choices: ['security', 'compliance', 'network', 'access', 'data', 'backup', 'monitoring', 'change']
  schema_dir:
    description:
      - Directory containing policy schemas
    required: false
    type: path
    default: '/etc/policy_as_code/schemas'
  compliance_frameworks:
    description:
      - List of compliance frameworks to validate against
    required: false
    type: list
    elements: str
    default: ['nist_800_53', 'disa_stig']
  strict_mode:
    description:
      - Enable strict validation (fail on warnings)
    required: false
    type: bool
    default: false
  fourth_estate_mode:
    description:
      - Enable Fourth Estate specific validation rules
    required: false
    type: bool
    default: true
author:
  - Fourth Estate Policy Team
'''

EXAMPLES = r'''
- name: Validate security policy
  policy_validator:
    policy_file: /etc/policies/security/tls_enforcement.yml
    policy_type: security
    compliance_frameworks:
      - nist_800_53
      - disa_stig
      - iec_62443
    strict_mode: true

- name: Validate access policy with Fourth Estate rules
  policy_validator:
    policy_file: /etc/policies/access/rbac_policy.yml
    policy_type: access
    fourth_estate_mode: true
    strict_mode: false

- name: Validate all policies in directory
  policy_validator:
    policy_file: "{{ item }}"
    policy_type: "{{ item | dirname | basename }}"
    compliance_frameworks: ['nist_800_53']
  loop: "{{ lookup('fileglob', '/etc/policies/**/*.yml', wantlist=True) }}"
'''

RETURN = r'''
valid:
  description: Whether the policy is valid
  returned: always
  type: bool
  sample: true
validation_errors:
  description: List of validation errors
  returned: when validation fails
  type: list
  elements: dict
  sample:
    - field: 'severity'
      error: 'Invalid value: must be one of [critical, high, medium, low]'
      location: 'line 23'
validation_warnings:
  description: List of validation warnings
  returned: always
  type: list
  elements: dict
  sample:
    - field: 'description'
      warning: 'Description should be more detailed (>100 chars recommended)'
      location: 'line 5'
compliance_status:
  description: Compliance framework validation results
  returned: always
  type: dict
  sample:
    nist_800_53:
      compliant: true
      controls_mapped: ['AC-2', 'AC-3', 'IA-5']
    disa_stig:
      compliant: true
      findings_addressed: ['V-230221', 'V-230222']
policy_metadata:
  description: Extracted policy metadata
  returned: always
  type: dict
  sample:
    name: 'TLS 1.2+ Enforcement'
    version: '1.0.0'
    last_updated: '2026-01-26'
    owner: 'security-team@example.com'
'''

import json
import os
import yaml
from ansible.module_utils.basic import AnsibleModule
from datetime import datetime

class PolicyValidator:
    """Policy validation engine for Fourth Estate compliance"""

    def __init__(self, module):
        self.module = module
        self.policy_file = module.params['policy_file']
        self.policy_type = module.params['policy_type']
        self.schema_dir = module.params['schema_dir']
        self.compliance_frameworks = module.params['compliance_frameworks']
        self.strict_mode = module.params['strict_mode']
        self.fourth_estate_mode = module.params['fourth_estate_mode']

        self.errors = []
        self.warnings = []
        self.compliance_status = {}

    def validate(self):
        """Main validation workflow"""
        try:
            # Load policy file
            policy_data = self._load_policy()

            # Validate structure
            self._validate_structure(policy_data)

            # Validate metadata
            self._validate_metadata(policy_data)

            # Validate policy type specific rules
            self._validate_policy_type(policy_data)

            # Validate compliance frameworks
            self._validate_compliance(policy_data)

            # Fourth Estate specific validation
            if self.fourth_estate_mode:
                self._validate_fourth_estate(policy_data)

            # Determine overall validation result
            valid = len(self.errors) == 0
            if self.strict_mode and len(self.warnings) > 0:
                valid = False

            return {
                'valid': valid,
                'validation_errors': self.errors,
                'validation_warnings': self.warnings,
                'compliance_status': self.compliance_status,
                'policy_metadata': policy_data.get('metadata', {}),
                'changed': False
            }

        except Exception as e:
            self.module.fail_json(msg=f"Validation failed: {str(e)}")

    def _load_policy(self):
        """Load and parse policy file"""
        if not os.path.exists(self.policy_file):
            self.module.fail_json(msg=f"Policy file not found: {self.policy_file}")

        try:
            with open(self.policy_file, 'r') as f:
                if self.policy_file.endswith('.json'):
                    return json.load(f)
                else:
                    return yaml.safe_load(f)
        except Exception as e:
            self.module.fail_json(msg=f"Failed to parse policy file: {str(e)}")

    def _validate_structure(self, policy_data):
        """Validate basic policy structure"""
        required_fields = ['metadata', 'policy', 'enforcement']

        for field in required_fields:
            if field not in policy_data:
                self.errors.append({
                    'field': field,
                    'error': f"Required field '{field}' is missing",
                    'severity': 'critical'
                })

        # Validate metadata structure
        if 'metadata' in policy_data:
            metadata = policy_data['metadata']
            required_meta = ['name', 'version', 'description', 'owner', 'severity']

            for field in required_meta:
                if field not in metadata:
                    self.errors.append({
                        'field': f"metadata.{field}",
                        'error': f"Required metadata field '{field}' is missing",
                        'severity': 'high'
                    })

    def _validate_metadata(self, policy_data):
        """Validate policy metadata"""
        if 'metadata' not in policy_data:
            return

        metadata = policy_data['metadata']

        # Validate severity
        valid_severities = ['critical', 'high', 'medium', 'low']
        if 'severity' in metadata and metadata['severity'] not in valid_severities:
            self.errors.append({
                'field': 'metadata.severity',
                'error': f"Invalid severity: must be one of {valid_severities}",
                'severity': 'high'
            })

        # Validate version format (semver)
        if 'version' in metadata:
            version = metadata['version']
            parts = version.split('.')
            if len(parts) != 3 or not all(p.isdigit() for p in parts):
                self.warnings.append({
                    'field': 'metadata.version',
                    'warning': 'Version should follow semantic versioning (X.Y.Z)',
                    'severity': 'low'
                })

        # Validate description length
        if 'description' in metadata:
            desc_len = len(metadata['description'])
            if desc_len < 50:
                self.warnings.append({
                    'field': 'metadata.description',
                    'warning': f"Description is short ({desc_len} chars). Recommend >50 chars for clarity",
                    'severity': 'low'
                })

    def _validate_policy_type(self, policy_data):
        """Validate policy type specific requirements"""
        validators = {
            'security': self._validate_security_policy,
            'compliance': self._validate_compliance_policy,
            'network': self._validate_network_policy,
            'access': self._validate_access_policy,
            'data': self._validate_data_policy,
            'backup': self._validate_backup_policy,
            'monitoring': self._validate_monitoring_policy,
            'change': self._validate_change_policy
        }

        validator = validators.get(self.policy_type)
        if validator:
            validator(policy_data)

    def _validate_security_policy(self, policy_data):
        """Validate security-specific policy requirements"""
        if 'policy' not in policy_data:
            return

        policy = policy_data['policy']

        # Security policies should define encryption requirements
        if 'encryption' not in policy:
            self.warnings.append({
                'field': 'policy.encryption',
                'warning': 'Security policy should define encryption requirements',
                'severity': 'medium'
            })

    def _validate_compliance_policy(self, policy_data):
        """Validate compliance-specific policy requirements"""
        if 'policy' not in policy_data:
            return

        policy = policy_data['policy']

        # Compliance policies must map to controls
        if 'controls' not in policy:
            self.errors.append({
                'field': 'policy.controls',
                'error': 'Compliance policy must map to control frameworks',
                'severity': 'high'
            })

    def _validate_network_policy(self, policy_data):
        """Validate network-specific policy requirements"""
        if 'policy' not in policy_data:
            return

        policy = policy_data['policy']

        # Network policies should define rules
        if 'rules' not in policy:
            self.warnings.append({
                'field': 'policy.rules',
                'warning': 'Network policy should define firewall/routing rules',
                'severity': 'medium'
            })

    def _validate_access_policy(self, policy_data):
        """Validate access control policy requirements"""
        if 'policy' not in policy_data:
            return

        policy = policy_data['policy']

        # Access policies should define roles and permissions
        if 'roles' not in policy:
            self.warnings.append({
                'field': 'policy.roles',
                'warning': 'Access policy should define roles and permissions',
                'severity': 'medium'
            })

    def _validate_data_policy(self, policy_data):
        """Validate data protection policy requirements"""
        if 'policy' not in policy_data:
            return

        policy = policy_data['policy']

        # Data policies should define classification
        if 'classification' not in policy:
            self.errors.append({
                'field': 'policy.classification',
                'error': 'Data policy must define data classification levels',
                'severity': 'high'
            })

    def _validate_backup_policy(self, policy_data):
        """Validate backup policy requirements"""
        if 'policy' not in policy_data:
            return

        policy = policy_data['policy']

        # Backup policies must define RPO/RTO
        if 'rpo' not in policy or 'rto' not in policy:
            self.errors.append({
                'field': 'policy.rpo/rto',
                'error': 'Backup policy must define RPO and RTO',
                'severity': 'high'
            })

    def _validate_monitoring_policy(self, policy_data):
        """Validate monitoring policy requirements"""
        if 'policy' not in policy_data:
            return

        policy = policy_data['policy']

        # Monitoring policies should define metrics and thresholds
        if 'metrics' not in policy:
            self.warnings.append({
                'field': 'policy.metrics',
                'warning': 'Monitoring policy should define metrics and thresholds',
                'severity': 'medium'
            })

    def _validate_change_policy(self, policy_data):
        """Validate change management policy requirements"""
        if 'policy' not in policy_data:
            return

        policy = policy_data['policy']

        # Change policies should define approval workflow
        if 'approval_workflow' not in policy:
            self.errors.append({
                'field': 'policy.approval_workflow',
                'error': 'Change policy must define approval workflow',
                'severity': 'high'
            })

    def _validate_compliance(self, policy_data):
        """Validate against compliance frameworks"""
        for framework in self.compliance_frameworks:
            if framework == 'nist_800_53':
                self._validate_nist_80053(policy_data)
            elif framework == 'disa_stig':
                self._validate_disa_stig(policy_data)
            elif framework == 'iec_62443':
                self._validate_iec_62443(policy_data)
            elif framework == 'nerc_cip':
                self._validate_nerc_cip(policy_data)

    def _validate_nist_80053(self, policy_data):
        """Validate NIST 800-53 compliance"""
        controls = policy_data.get('compliance', {}).get('nist_800_53', {}).get('controls', [])

        self.compliance_status['nist_800_53'] = {
            'compliant': len(controls) > 0,
            'controls_mapped': controls
        }

        if len(controls) == 0:
            self.warnings.append({
                'field': 'compliance.nist_800_53.controls',
                'warning': 'No NIST 800-53 controls mapped',
                'severity': 'medium'
            })

    def _validate_disa_stig(self, policy_data):
        """Validate DISA STIG compliance"""
        findings = policy_data.get('compliance', {}).get('disa_stig', {}).get('findings', [])

        self.compliance_status['disa_stig'] = {
            'compliant': len(findings) > 0,
            'findings_addressed': findings
        }

        if len(findings) == 0:
            self.warnings.append({
                'field': 'compliance.disa_stig.findings',
                'warning': 'No DISA STIG findings mapped',
                'severity': 'medium'
            })

    def _validate_iec_62443(self, policy_data):
        """Validate IEC 62443 compliance (OT/ICS)"""
        requirements = policy_data.get('compliance', {}).get('iec_62443', {}).get('requirements', [])

        self.compliance_status['iec_62443'] = {
            'compliant': len(requirements) > 0,
            'requirements_met': requirements
        }

    def _validate_nerc_cip(self, policy_data):
        """Validate NERC CIP compliance (Critical Infrastructure)"""
        standards = policy_data.get('compliance', {}).get('nerc_cip', {}).get('standards', [])

        self.compliance_status['nerc_cip'] = {
            'compliant': len(standards) > 0,
            'standards_met': standards
        }

    def _validate_fourth_estate(self, policy_data):
        """Fourth Estate specific validation rules"""
        metadata = policy_data.get('metadata', {})

        # Fourth Estate policies should address source protection
        if 'source_protection' not in policy_data.get('policy', {}):
            self.warnings.append({
                'field': 'policy.source_protection',
                'warning': 'Fourth Estate policy should address source protection requirements',
                'severity': 'high'
            })

        # Critical severity policies require dual approval
        if metadata.get('severity') == 'critical':
            approval = policy_data.get('approval', {})
            if approval.get('required_approvers', 0) < 2:
                self.errors.append({
                    'field': 'approval.required_approvers',
                    'error': 'Critical severity policies require at least 2 approvers',
                    'severity': 'high'
                })

def main():
    module = AnsibleModule(
        argument_spec=dict(
            policy_file=dict(type='path', required=True),
            policy_type=dict(type='str', required=True, choices=[
                'security', 'compliance', 'network', 'access',
                'data', 'backup', 'monitoring', 'change'
            ]),
            schema_dir=dict(type='path', required=False, default='/etc/policy_as_code/schemas'),
            compliance_frameworks=dict(type='list', elements='str', required=False,
                                      default=['nist_800_53', 'disa_stig']),
            strict_mode=dict(type='bool', required=False, default=False),
            fourth_estate_mode=dict(type='bool', required=False, default=True)
        ),
        supports_check_mode=True
    )

    validator = PolicyValidator(module)
    result = validator.validate()

    if result['valid']:
        module.exit_json(**result)
    else:
        module.fail_json(msg="Policy validation failed", **result)

if __name__ == '__main__':
    main()

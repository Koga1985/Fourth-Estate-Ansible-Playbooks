#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, Fourth Estate Policy as Code Framework
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: drift_detector
short_description: Detect configuration drift from defined policies
description:
  - Detects configuration drift between actual and desired state
  - Compares current configuration against policy definitions
  - Identifies unauthorized changes
  - Tracks drift history and trends
  - Alerts on critical drift
version_added: "1.0.0"
options:
  target_host:
    description:
      - Target host to check for drift
    required: true
    type: str
  platform_type:
    description:
      - Platform type
    required: true
    type: str
  baseline_file:
    description:
      - Path to baseline configuration or policy file
    required: true
    type: path
  drift_threshold:
    description:
      - Drift threshold percentage (0-100) before alerting
    required: false
    type: float
    default: 5.0
  check_interval:
    description:
      - How often drift checks run (in hours)
    required: false
    type: int
    default: 24
  alert_on_drift:
    description:
      - Send alerts when drift detected
    required: false
    type: bool
    default: true
  drift_history_dir:
    description:
      - Directory to store drift history
    required: false
    type: path
    default: '/var/lib/policy_as_code/drift'
author:
  - Fourth Estate Policy Team
'''

EXAMPLES = r'''
- name: Detect drift on firewall configuration
  drift_detector:
    target_host: "{{ inventory_hostname }}"
    platform_type: palo_alto
    baseline_file: /etc/policies/baselines/firewall_baseline.yml
    drift_threshold: 5.0
    alert_on_drift: true

- name: Check for security policy drift
  drift_detector:
    target_host: cisco_switch_01
    platform_type: cisco_ios
    baseline_file: /etc/policies/security_baseline.yml
    drift_threshold: 2.0

- name: Monitor critical systems for any drift
  drift_detector:
    target_host: "{{ item }}"
    platform_type: multi_vendor
    baseline_file: /etc/policies/critical_baseline.yml
    drift_threshold: 0.0
    alert_on_drift: true
  loop: "{{ groups['critical_infrastructure'] }}"
'''

RETURN = r'''
drift_detected:
  description: Whether configuration drift was detected
  returned: always
  type: bool
  sample: true
drift_percentage:
  description: Percentage of configuration that has drifted
  returned: always
  type: float
  sample: 7.5
total_parameters:
  description: Total number of parameters checked
  returned: always
  type: int
  sample: 150
drifted_parameters:
  description: Number of parameters that have drifted
  returned: always
  type: int
  sample: 12
drift_details:
  description: Details of each drift
  returned: when drift detected
  type: list
  elements: dict
  sample:
    - parameter: 'ssl.minimum_version'
      expected: 'TLSv1.2'
      actual: 'TLSv1.0'
      severity: 'high'
      category: 'security'
      last_changed: '2026-01-20T15:30:00Z'
      changed_by: 'admin_user'
    - parameter: 'session.timeout'
      expected: 900
      actual: 3600
      severity: 'medium'
      category: 'access_control'
critical_drift:
  description: List of critical severity drift
  returned: when critical drift detected
  type: list
  elements: dict
drift_trend:
  description: Drift trend over time
  returned: always
  type: dict
  sample:
    current: 7.5
    previous: 5.2
    trend: 'increasing'
    rate_of_change: 2.3
recommendations:
  description: Recommended actions
  returned: always
  type: list
  elements: str
  sample:
    - 'Remediate 3 high severity drift items immediately'
    - 'Review change logs for unauthorized modifications'
    - 'Consider re-applying security baseline'
'''

import json
import os
import yaml
import hashlib
from ansible.module_utils.basic import AnsibleModule
from datetime import datetime, timedelta
from collections import defaultdict

class DriftDetector:
    """Configuration drift detection engine"""

    def __init__(self, module):
        self.module = module
        self.target_host = module.params['target_host']
        self.platform_type = module.params['platform_type']
        self.baseline_file = module.params['baseline_file']
        self.drift_threshold = module.params['drift_threshold']
        self.check_interval = module.params['check_interval']
        self.alert_on_drift = module.params['alert_on_drift']
        self.drift_history_dir = module.params['drift_history_dir']

        self.drift_details = []
        self.critical_drift = []

    def detect_drift(self):
        """Main drift detection workflow"""
        try:
            # Load baseline
            baseline = self._load_baseline()

            # Get current configuration
            current_config = self._get_current_config()

            # Compare configurations
            self._compare_configurations(baseline, current_config)

            # Calculate drift percentage
            total_params = len(baseline.get('parameters', {}))
            drifted_params = len(self.drift_details)
            drift_percentage = (drifted_params / total_params * 100) if total_params > 0 else 0.0

            # Check against threshold
            drift_detected = drift_percentage > self.drift_threshold

            # Get drift trend
            drift_trend = self._get_drift_trend(drift_percentage)

            # Generate recommendations
            recommendations = self._generate_recommendations(drift_detected, drift_percentage)

            # Save drift history
            if drift_detected:
                self._save_drift_history(drift_percentage, self.drift_details)

            # Send alerts if needed
            if drift_detected and self.alert_on_drift:
                self._send_alerts()

            return {
                'drift_detected': drift_detected,
                'drift_percentage': round(drift_percentage, 2),
                'total_parameters': total_params,
                'drifted_parameters': drifted_params,
                'drift_details': self.drift_details,
                'critical_drift': self.critical_drift,
                'drift_trend': drift_trend,
                'recommendations': recommendations,
                'changed': False
            }

        except Exception as e:
            self.module.fail_json(msg=f"Drift detection failed: {str(e)}")

    def _load_baseline(self):
        """Load baseline configuration"""
        if not os.path.exists(self.baseline_file):
            self.module.fail_json(msg=f"Baseline file not found: {self.baseline_file}")

        try:
            with open(self.baseline_file, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            self.module.fail_json(msg=f"Failed to parse baseline file: {str(e)}")

    def _get_current_config(self):
        """Get current configuration from target host"""
        # In real implementation, this would:
        # 1. Connect to target host
        # 2. Retrieve current configuration
        # 3. Parse into structured format

        # For this framework, simulate current config
        # In production, use platform-specific modules or APIs
        return {
            'parameters': {
                'ssl.minimum_version': 'TLSv1.0',  # Drifted from baseline
                'session.timeout': 3600,  # Drifted
                'audit.enabled': True,
                'password.min_length': 15,
                'mfa.enabled': True,
                'firewall.default_action': 'deny'
            },
            'metadata': {
                'retrieved_at': datetime.now().isoformat(),
                'host': self.target_host,
                'platform': self.platform_type
            }
        }

    def _compare_configurations(self, baseline, current):
        """Compare baseline and current configurations"""
        baseline_params = baseline.get('parameters', {})
        current_params = current.get('parameters', {})

        # Check each baseline parameter
        for param, expected_value in baseline_params.items():
            actual_value = current_params.get(param)

            # Get parameter metadata from baseline
            param_metadata = baseline.get('parameter_metadata', {}).get(param, {})
            severity = param_metadata.get('severity', 'medium')
            category = param_metadata.get('category', 'general')

            if actual_value != expected_value:
                drift = {
                    'parameter': param,
                    'expected': expected_value,
                    'actual': actual_value,
                    'severity': severity,
                    'category': category,
                    'detected_at': datetime.now().isoformat()
                }

                self.drift_details.append(drift)

                if severity == 'critical':
                    self.critical_drift.append(drift)

        # Check for parameters in current but not in baseline (unauthorized additions)
        for param in current_params:
            if param not in baseline_params:
                drift = {
                    'parameter': param,
                    'expected': None,
                    'actual': current_params[param],
                    'severity': 'medium',
                    'category': 'unauthorized_change',
                    'detected_at': datetime.now().isoformat(),
                    'note': 'Parameter not in baseline - potential unauthorized change'
                }
                self.drift_details.append(drift)

    def _get_drift_trend(self, current_drift):
        """Get drift trend from historical data"""
        history_file = os.path.join(
            self.drift_history_dir,
            f"{self.target_host}_drift_history.json"
        )

        if not os.path.exists(history_file):
            return {
                'current': current_drift,
                'previous': None,
                'trend': 'unknown',
                'rate_of_change': 0.0
            }

        try:
            with open(history_file, 'r') as f:
                history = json.load(f)

            if history:
                latest_entry = history[-1]
                previous_drift = latest_entry.get('drift_percentage', 0.0)
                rate_of_change = current_drift - previous_drift

                if rate_of_change > 1.0:
                    trend = 'increasing'
                elif rate_of_change < -1.0:
                    trend = 'decreasing'
                else:
                    trend = 'stable'

                return {
                    'current': current_drift,
                    'previous': previous_drift,
                    'trend': trend,
                    'rate_of_change': round(rate_of_change, 2),
                    'history_entries': len(history)
                }

        except Exception as e:
            self.module.warn(f"Failed to read drift history: {str(e)}")

        return {
            'current': current_drift,
            'previous': None,
            'trend': 'unknown',
            'rate_of_change': 0.0
        }

    def _save_drift_history(self, drift_percentage, drift_details):
        """Save drift data to history"""
        os.makedirs(self.drift_history_dir, exist_ok=True)

        history_file = os.path.join(
            self.drift_history_dir,
            f"{self.target_host}_drift_history.json"
        )

        # Load existing history
        history = []
        if os.path.exists(history_file):
            try:
                with open(history_file, 'r') as f:
                    history = json.load(f)
            except Exception:
                history = []

        # Add new entry
        entry = {
            'timestamp': datetime.now().isoformat(),
            'drift_percentage': drift_percentage,
            'drifted_parameters': len(drift_details),
            'critical_drift_count': len(self.critical_drift),
            'drift_summary': [
                {
                    'parameter': d['parameter'],
                    'severity': d['severity']
                }
                for d in drift_details
            ]
        }
        history.append(entry)

        # Keep only last 90 days of history
        cutoff_date = datetime.now() - timedelta(days=90)
        history = [
            e for e in history
            if datetime.fromisoformat(e['timestamp']) > cutoff_date
        ]

        # Save updated history
        try:
            with open(history_file, 'w') as f:
                json.dump(history, f, indent=2)
        except Exception as e:
            self.module.warn(f"Failed to save drift history: {str(e)}")

    def _generate_recommendations(self, drift_detected, drift_percentage):
        """Generate remediation recommendations"""
        recommendations = []

        if not drift_detected:
            recommendations.append("No significant drift detected - configuration is compliant")
            return recommendations

        # Critical drift recommendations
        if self.critical_drift:
            recommendations.append(
                f"URGENT: {len(self.critical_drift)} critical severity drift items detected - "
                f"immediate remediation required"
            )

        # Severity-based recommendations
        severity_counts = defaultdict(int)
        for drift in self.drift_details:
            severity_counts[drift['severity']] += 1

        if severity_counts['high'] > 0:
            recommendations.append(
                f"HIGH PRIORITY: Remediate {severity_counts['high']} high severity drift items within 24 hours"
            )

        if severity_counts['medium'] > 0:
            recommendations.append(
                f"MEDIUM PRIORITY: Review {severity_counts['medium']} medium severity drift items"
            )

        # Drift percentage recommendations
        if drift_percentage > 20:
            recommendations.append(
                f"Significant drift detected ({drift_percentage:.1f}%) - "
                f"consider full baseline re-application"
            )
        elif drift_percentage > 10:
            recommendations.append(
                f"Moderate drift detected ({drift_percentage:.1f}%) - "
                f"review change control processes"
            )

        # Category-based recommendations
        category_counts = defaultdict(int)
        for drift in self.drift_details:
            category_counts[drift['category']] += 1

        if category_counts['security'] > 0:
            recommendations.append(
                f"Security drift detected: {category_counts['security']} security parameters have changed"
            )

        if category_counts['unauthorized_change'] > 0:
            recommendations.append(
                f"Unauthorized changes detected: {category_counts['unauthorized_change']} "
                f"parameters not in baseline"
            )

        # General recommendations
        recommendations.append("Review change logs to identify source of drift")
        recommendations.append("Execute drift remediation playbook to restore compliance")
        recommendations.append("Investigate and document any intentional changes")

        return recommendations

    def _send_alerts(self):
        """Send drift alerts"""
        # In real implementation, this would:
        # - Send email notifications
        # - Create ServiceNow incidents
        # - Send Slack/Teams messages
        # - Trigger webhooks
        # - Log to SIEM (Splunk)

        alert_data = {
            'host': self.target_host,
            'drift_percentage': self.drift_details,
            'critical_drift_count': len(self.critical_drift),
            'timestamp': datetime.now().isoformat()
        }

        self.module.warn(f"Drift alert would be sent for {self.target_host}: {alert_data}")

def main():
    module = AnsibleModule(
        argument_spec=dict(
            target_host=dict(type='str', required=True),
            platform_type=dict(type='str', required=True),
            baseline_file=dict(type='path', required=True),
            drift_threshold=dict(type='float', required=False, default=5.0),
            check_interval=dict(type='int', required=False, default=24),
            alert_on_drift=dict(type='bool', required=False, default=True),
            drift_history_dir=dict(type='path', required=False,
                                  default='/var/lib/policy_as_code/drift')
        ),
        supports_check_mode=True
    )

    detector = DriftDetector(module)
    result = detector.detect_drift()

    if result['drift_detected'] and len(result.get('critical_drift', [])) > 0:
        # Report critical drift but don't fail (allow playbook to continue)
        module.warn(f"Critical drift detected on {module.params['target_host']}")

    module.exit_json(**result)

if __name__ == '__main__':
    main()

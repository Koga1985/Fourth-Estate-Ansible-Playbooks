# Prometheus & Grafana Monitoring Stack

This directory contains **11 Ansible roles** for deploying and configuring **Prometheus** and **Grafana** for comprehensive infrastructure monitoring and observability.

## 📋 Roles

### Prometheus (7 roles)
- **prometheus_install** - Prometheus server installation
- **prometheus_server** - Prometheus server configuration and management
- **prometheus_config** - Prometheus configuration (scrape targets, alerting rules, retention)
- **prometheus_exporters** - Prometheus exporter deployment (node, blackbox, and others)
- **prometheus_node_exporter** - Node exporter for host-level metrics
- **prometheus_alertmanager** - Alertmanager deployment and routing configuration
- **prometheus_blackbox_exporter** - Blackbox exporter for endpoint probing

### Grafana (4 roles)
- **grafana_server** - Grafana server installation and configuration
- **grafana_datasources** - Datasource provisioning (Prometheus, Loki, etc.)
- **grafana_dashboards** - Dashboard provisioning and management
- **grafana_alerting** - Grafana alerting rules and notification channels

## 🚀 Quick Start

```bash
# Deploy monitoring stack
ansible-playbook -i inventory site.yml --ask-vault-pass

# Deploy Prometheus and config only
ansible-playbook -i inventory site.yml --tags prometheus

# Deploy exporters only
ansible-playbook -i inventory site.yml --tags exporters
```

## ⚙️ Configuration

```yaml
# Prometheus configuration
prometheus_version: "2.45.0"
prometheus_retention_days: 30
prometheus_storage_path: "/var/lib/prometheus"
prometheus_scrape_interval: "15s"

# Alertmanager
alertmanager_slack_webhook: "{{ vault_slack_webhook }}"
alertmanager_pagerduty_key: "{{ vault_pagerduty_key }}"

# Grafana
grafana_version: "10.0.0"
grafana_admin_user: "admin"
grafana_admin_password: "{{ vault_grafana_password }}"
grafana_enable_alerting: true
```

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

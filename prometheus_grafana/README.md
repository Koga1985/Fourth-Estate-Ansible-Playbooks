# Prometheus & Grafana Monitoring Stack

This directory contains **8 Ansible roles** for deploying and configuring **Prometheus** and **Grafana** for comprehensive infrastructure monitoring and observability.

## 📋 Roles

### Prometheus (4 roles)
- **prometheus_server** - Prometheus server installation and configuration
- **prometheus_alertmanager** - Alertmanager for alert routing
- **prometheus_node_exporter** - Node metrics collection
- **prometheus_blackbox_exporter** - Endpoint monitoring

### Grafana (4 roles)
- **grafana_server** - Grafana server installation
- **grafana_dashboards** - Dashboard provisioning
- **grafana_datasources** - Datasource configuration (Prometheus, Loki, etc.)
- **grafana_alerting** - Grafana alerting rules

## 🚀 Quick Start

```bash
# Deploy Prometheus stack
ansible-playbook playbooks/prometheus_stack.yml \
  -i inventory/monitoring.yml

# Configure Grafana with dashboards
ansible-playbook playbooks/grafana_setup.yml \
  -e "grafana_admin_password=SecurePass123!"
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

**Maintained By:** Fourth Estate Infrastructure Team

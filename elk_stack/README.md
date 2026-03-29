# ELK Stack (Elasticsearch, Logstash, Kibana)

This directory contains **12 Ansible roles** for deploying and configuring the **Elastic Stack** (Elasticsearch, Kibana, Logstash, Fleet, and metrics collection).

## 📋 Roles

### Elasticsearch (5 roles)
- **elasticsearch_install** - Elasticsearch cluster installation and node setup
- **elasticsearch_cluster** - Multi-node cluster configuration and management
- **elasticsearch_config** - Cluster configuration, index lifecycle, and tuning
- **elasticsearch_indices** - Index template and lifecycle policy management
- **elasticsearch_security** - TLS/SSL, X-Pack security, built-in user configuration

### Kibana (2 roles)
- **kibana_server** - Kibana server installation and configuration
- **kibana_dashboards** - Dashboard and visualization provisioning

### Logstash (2 roles)
- **logstash_pipelines** - Logstash pipeline configuration and management
- **logstash_filters** - Filter plugin configuration (grok, mutate, geoip)

### Fleet & Metrics (3 roles)
- **elastic_fleet** - Fleet Server deployment and agent policy management
- **elastic_security** - Elastic Security (SIEM) rules and detections
- **metricbeat** - Metricbeat deployment for infrastructure metrics collection

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your ELK servers

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Deploy Elasticsearch only
ansible-playbook -i inventory site.yml --tags elasticsearch

# Deploy Kibana only
ansible-playbook -i inventory site.yml --tags kibana

# Deploy Logstash only
ansible-playbook -i inventory site.yml --tags logstash
```

### Individual Role Execution (Alternative)

```bash
# Deploy ELK stack
ansible-playbook playbooks/elk_full_stack.yml \
  -i inventory/elk.yml

# Configure log collection
ansible-playbook playbooks/filebeat_setup.yml \
  -e "log_paths=['/var/log/syslog','/var/log/auth.log']"
```

## ⚙️ Configuration

```yaml
# Elasticsearch
elasticsearch_version: "8.10.0"
elasticsearch_cluster_name: "fourth-estate-logs"
elasticsearch_heap_size: "4g"
elasticsearch_data_nodes: 3

# Kibana
kibana_version: "8.10.0"
kibana_elasticsearch_hosts: ["http://es01:9200"]

# Filebeat
filebeat_prospectors:
  - paths: ["/var/log/syslog"]
    document_type: "syslog"
  - paths: ["/var/log/nginx/*.log"]
    document_type: "nginx"
```

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team

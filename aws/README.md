# Amazon Web Services (AWS)

This directory contains **40+ Ansible roles** for managing **Amazon Web Services (AWS)** infrastructure with emphasis on security, compliance (FedRAMP, NIST 800-53), and Fourth Estate requirements.

## Overview

Comprehensive AWS automation covering IAM, VPC networking, EC2 compute, EKS Kubernetes, storage (S3, EBS, EFS), databases (RDS, DynamoDB), serverless (Lambda), monitoring (CloudWatch), security services, and AWS GovCloud compliance.

## 📋 Role Categories

### Identity & Access Management (8 roles)
- **aws_iam_users** - User account lifecycle management
- **aws_iam_groups** - Group management and policies
- **aws_iam_roles** - IAM role creation and trust policies
- **aws_iam_policies** - Custom and managed policy attachment
- **aws_iam_service_accounts** - Service account automation
- **aws_organizations** - AWS Organizations and OU management
- **aws_sso** - AWS SSO (Identity Center) configuration
- **aws_iam_access_analyzer** - Access Analyzer for unused permissions

### Networking (8 roles)
- **aws_vpc** - VPC creation and management
- **aws_subnets** - Public/private subnet configuration
- **aws_route_tables** - Routing table management
- **aws_nat_gateway** - NAT Gateway for private subnets
- **aws_internet_gateway** - Internet Gateway configuration
- **aws_vpc_peering** - VPC peering connections
- **aws_transit_gateway** - Transit Gateway for multi-VPC
- **aws_direct_connect** - Direct Connect configuration

### Compute (7 roles)
- **aws_ec2_instances** - EC2 instance lifecycle
- **aws_launch_templates** - Launch template management
- **aws_autoscaling_groups** - Auto Scaling Groups
- **aws_ami_management** - Custom AMI creation and sharing
- **aws_elastic_ip** - Elastic IP allocation
- **aws_placement_groups** - Placement group strategies
- **aws_ec2_fleet** - EC2 Fleet management

### Container & Kubernetes (5 roles)
- **aws_eks_clusters** - EKS cluster deployment
- **aws_eks_node_groups** - Managed node groups
- **aws_eks_fargate** - Fargate profile configuration
- **aws_ecr** - Elastic Container Registry
- **aws_ecs** - Elastic Container Service

### Storage (6 roles)
- **aws_s3_buckets** - S3 bucket management and policies
- **aws_s3_lifecycle** - Lifecycle policies and transitions
- **aws_ebs_volumes** - EBS volume management
- **aws_ebs_snapshots** - Snapshot automation and retention
- **aws_efs** - Elastic File System
- **aws_fsx** - FSx for Windows/Lustre

### Databases (5 roles)
- **aws_rds** - RDS instance management (MySQL, PostgreSQL, etc.)
- **aws_rds_aurora** - Aurora cluster management
- **aws_dynamodb** - DynamoDB table management
- **aws_elasticache** - ElastiCache (Redis, Memcached)
- **aws_rds_snapshots** - Database backup automation

### Serverless & Lambda (4 roles)
- **aws_lambda_functions** - Lambda function deployment
- **aws_api_gateway** - API Gateway configuration
- **aws_eventbridge** - EventBridge rules and targets
- **aws_step_functions** - Step Functions state machines

### Security & Compliance (8 roles)
- **aws_security_groups** - Security group management
- **aws_nacl** - Network ACL configuration
- **aws_kms** - KMS key management and encryption
- **aws_secrets_manager** - Secrets Manager integration
- **aws_waf** - Web Application Firewall
- **aws_guardduty** - GuardDuty threat detection
- **aws_security_hub** - Security Hub aggregation
- **aws_config** - AWS Config compliance rules

### Monitoring & Logging (5 roles)
- **aws_cloudwatch_alarms** - CloudWatch alarm configuration
- **aws_cloudwatch_logs** - Log group management
- **aws_cloudtrail** - CloudTrail audit logging
- **aws_cloudwatch_dashboards** - Custom dashboards
- **aws_sns** - Simple Notification Service

### Cost & Governance (4 roles)
- **aws_cost_budgets** - Budget alerts and thresholds
- **aws_cost_explorer** - Cost analysis automation
- **aws_resource_tags** - Tagging strategy enforcement
- **aws_service_control_policies** - SCP management

### AWS GovCloud & Compliance (4 roles)
- **aws_govcloud_setup** - GovCloud region configuration
- **aws_fedramp_compliance** - FedRAMP baseline controls
- **aws_nist_compliance** - NIST 800-53 implementation
- **aws_hipaa_compliance** - HIPAA compliance automation

## 🚀 Quick Start (Drop-In Deployment)

This platform supports **drop-in deployment**. Get started in 3 steps:

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your AWS environment details

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

Use tags to deploy specific components:

```bash
# Deploy only IAM
ansible-playbook -i inventory site.yml --tags iam

# Deploy only networking
ansible-playbook -i inventory site.yml --tags network

# Deploy only security services
ansible-playbook -i inventory site.yml --tags security

# Deploy EKS cluster
ansible-playbook -i inventory site.yml --tags eks
```

### Prerequisites

- Ansible 2.12.0+
- Python 3.8+
- AWS CLI configured with credentials
- Python boto3 and botocore libraries

### Manual Installation (Alternative)

```bash
# Install required collections
ansible-galaxy collection install amazon.aws
ansible-galaxy collection install community.aws

# Install Python dependencies
pip install boto3 botocore
```

### AWS Credentials Configuration

**Option 1: Environment Variables**
```bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-east-1"
```

**Option 2: AWS CLI Configuration**
```bash
aws configure
# Enter access key, secret key, region, and output format
```

**Option 3: Ansible Vault (Recommended)**
```yaml
# group_vars/aws.yml
aws_access_key: "{{ vault_aws_access_key }}"
aws_secret_key: "{{ vault_aws_secret_key }}"
aws_region: "us-east-1"
```

### Basic Configuration

```yaml
# group_vars/aws.yml
aws_region: "us-east-1"
aws_account_id: "123456789012"
aws_environment: "production"

# Tagging strategy
aws_default_tags:
  Environment: "{{ aws_environment }}"
  ManagedBy: "Ansible"
  Owner: "Fourth Estate Infrastructure"
  CostCenter: "Engineering"
```

## 📖 Common Use Cases

### Use Case 1: Deploy Secure VPC with Public/Private Subnets

```yaml
---
# playbooks/aws_vpc_setup.yml
- name: Deploy AWS VPC Infrastructure
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: aws_vpc
      vars:
        vpc_name: "fourth-estate-prod"
        vpc_cidr: "10.0.0.0/16"
        enable_dns_hostnames: true
        enable_dns_support: true

    - role: aws_subnets
      vars:
        public_subnets:
          - cidr: "10.0.1.0/24"
            az: "us-east-1a"
          - cidr: "10.0.2.0/24"
            az: "us-east-1b"
        private_subnets:
          - cidr: "10.0.10.0/24"
            az: "us-east-1a"
          - cidr: "10.0.11.0/24"
            az: "us-east-1b"

    - role: aws_nat_gateway
    - role: aws_internet_gateway
    - role: aws_route_tables
```

```bash
ansible-playbook playbooks/aws_vpc_setup.yml
```

### Use Case 2: Deploy EKS Cluster with FedRAMP Compliance

```bash
ansible-playbook playbooks/aws_eks_cluster.yml \
  -e "cluster_name=fourth-estate-prod-eks" \
  -e "kubernetes_version=1.28" \
  -e "enable_private_endpoint=true" \
  -e "enable_fedramp_controls=true"
```

### Use Case 3: S3 Bucket with Encryption and Versioning

```yaml
---
# playbooks/aws_s3_secure_bucket.yml
- name: Create Secure S3 Bucket
  hosts: localhost
  connection: local

  tasks:
    - name: Create S3 bucket with encryption
      include_role:
        name: aws_s3_buckets
      vars:
        bucket_name: "fourth-estate-secure-data"
        enable_versioning: true
        enable_encryption: true
        kms_key_id: "alias/fourth-estate-s3"
        block_public_access: true
        enable_logging: true
        lifecycle_rules:
          - id: "transition-to-glacier"
            transition_days: 90
            storage_class: "GLACIER"
```

### Use Case 4: EC2 Instance with Auto-Scaling

```bash
ansible-playbook playbooks/aws_ec2_autoscaling.yml \
  -e "instance_type=t3.medium" \
  -e "min_size=2" \
  -e "max_size=10" \
  -e "desired_capacity=4"
```

### Use Case 5: RDS Database with Automated Backups

```bash
ansible-playbook playbooks/aws_rds_database.yml \
  -e "db_engine=postgres" \
  -e "db_version=15.3" \
  -e "instance_class=db.r6g.xlarge" \
  -e "multi_az=true" \
  -e "backup_retention=30"
```

## ⚙️ Configuration Variables

### Global AWS Configuration

```yaml
# AWS region and account
aws_region: "us-east-1"
aws_account_id: "123456789012"
aws_profile: "default"  # AWS CLI profile name

# Common tags applied to all resources
aws_common_tags:
  Environment: "production"
  ManagedBy: "Ansible"
  Project: "Fourth Estate"
  CostCenter: "Infrastructure"
  Compliance: "FedRAMP-Moderate"
```

### VPC Configuration

```yaml
vpc_name: "fourth-estate-vpc"
vpc_cidr: "10.0.0.0/16"
enable_dns_hostnames: true
enable_dns_support: true
enable_ipv6: false

# Subnets
public_subnets:
  - name: "public-1a"
    cidr: "10.0.1.0/24"
    az: "us-east-1a"
    map_public_ip: true
  - name: "public-1b"
    cidr: "10.0.2.0/24"
    az: "us-east-1b"
    map_public_ip: true

private_subnets:
  - name: "private-1a"
    cidr: "10.0.10.0/24"
    az: "us-east-1a"
  - name: "private-1b"
    cidr: "10.0.11.0/24"
    az: "us-east-1b"
```

### EKS Cluster Configuration

```yaml
eks_cluster_name: "fourth-estate-eks"
eks_version: "1.28"
eks_role_arn: "arn:aws:iam::123456789012:role/EKSClusterRole"

# Cluster networking
eks_vpc_id: "vpc-xxxxx"
eks_subnet_ids:
  - "subnet-xxxxx"
  - "subnet-yyyyy"

# Cluster security
eks_endpoint_private_access: true
eks_endpoint_public_access: false
eks_encryption_enabled: true
eks_kms_key_arn: "arn:aws:kms:us-east-1:123456789012:key/xxxxx"

# Node groups
eks_node_groups:
  - name: "general-purpose"
    instance_types: ["t3.large"]
    desired_size: 3
    min_size: 2
    max_size: 6
    disk_size: 100
```

### S3 Bucket Configuration

```yaml
s3_bucket_name: "fourth-estate-data"
s3_versioning: true
s3_encryption: "aws:kms"
s3_kms_key_id: "alias/s3-encryption"

# Block public access
s3_block_public_acls: true
s3_block_public_policy: true
s3_ignore_public_acls: true
s3_restrict_public_buckets: true

# Lifecycle policies
s3_lifecycle_rules:
  - id: "archive-old-data"
    enabled: true
    transitions:
      - days: 90
        storage_class: "STANDARD_IA"
      - days: 180
        storage_class: "GLACIER"
    expiration_days: 365
```

### RDS Database Configuration

```yaml
rds_instance_identifier: "fourth-estate-db"
rds_engine: "postgres"
rds_engine_version: "15.3"
rds_instance_class: "db.r6g.xlarge"
rds_allocated_storage: 100
rds_storage_type: "gp3"
rds_storage_encrypted: true
rds_kms_key_id: "alias/rds-encryption"

# High availability
rds_multi_az: true

# Backup
rds_backup_retention_period: 30
rds_backup_window: "03:00-04:00"
rds_maintenance_window: "sun:04:00-sun:05:00"

# Networking
rds_vpc_id: "vpc-xxxxx"
rds_subnet_ids:
  - "subnet-xxxxx"
  - "subnet-yyyyy"
rds_security_group_ids:
  - "sg-xxxxx"

# Monitoring
rds_enable_cloudwatch_logs: true
rds_monitoring_interval: 60
```

## 🛡️ Security & Compliance

### FedRAMP Compliance Controls

Implemented FedRAMP Moderate baseline controls:

| Control Family | Controls | Implementation |
|----------------|----------|----------------|
| **AC - Access Control** | AC-2, AC-3, AC-6 | IAM roles, policies, least privilege |
| **AU - Audit & Accountability** | AU-2, AU-3, AU-9 | CloudTrail, CloudWatch Logs |
| **CM - Configuration Management** | CM-2, CM-6, CM-7 | AWS Config, Systems Manager |
| **IA - Identification & Authentication** | IA-2, IA-5, IA-8 | MFA, IAM, AWS SSO |
| **SC - System & Communications** | SC-7, SC-8, SC-13 | Security groups, TLS, KMS encryption |

### NIST 800-53 Rev 5 Implementation

- **Encryption at Rest** - KMS encryption for EBS, S3, RDS, EFS
- **Encryption in Transit** - TLS 1.2+ for all API calls
- **Network Segmentation** - VPC isolation, security groups, NACLs
- **Audit Logging** - CloudTrail for all API activity
- **Access Control** - IAM policies with least privilege
- **Monitoring** - CloudWatch, GuardDuty, Security Hub

### AWS GovCloud Compliance

Special configuration for AWS GovCloud regions:

```yaml
# GovCloud-specific settings
aws_region: "us-gov-west-1"  # or us-gov-east-1
aws_govcloud: true
aws_compliance_framework: "FedRAMP-High"

# GovCloud requires different endpoints
aws_sts_endpoint: "sts.us-gov-west-1.amazonaws.com"
aws_iam_endpoint: "iam.us-gov.amazonaws.com"
```

### Security Best Practices

1. **Enable MFA** - Require MFA for all IAM users
2. **Use IAM Roles** - Prefer roles over access keys
3. **Encrypt Everything** - Enable encryption at rest and in transit
4. **Enable CloudTrail** - Log all API activity
5. **Use Security Hub** - Aggregate security findings
6. **Enable GuardDuty** - Threat detection
7. **Tag All Resources** - Enforce tagging strategy
8. **Use Private Subnets** - Deploy resources in private subnets when possible
9. **Enable VPC Flow Logs** - Network traffic monitoring
10. **Regular Backups** - Automate backup retention

## 🔧 Troubleshooting

### Issue: AWS Credentials Not Found

**Symptoms:** Playbooks fail with "Unable to locate credentials"

**Resolution:**
```bash
# Verify AWS CLI configuration
aws sts get-caller-identity

# Check environment variables
echo $AWS_ACCESS_KEY_ID
echo $AWS_SECRET_ACCESS_KEY

# Test with Ansible
ansible localhost -m amazon.aws.aws_caller_info
```

### Issue: VPC Limit Exceeded

**Symptoms:** "VpcLimitExceeded" error when creating VPC

**Resolution:**
```bash
# Check current VPC count
aws ec2 describe-vpcs --query 'Vpcs[*].VpcId' --output table

# Request limit increase via AWS Support
aws support create-case \
  --subject "VPC Limit Increase Request" \
  --service-code "vpc" \
  --category-code "general-guidance"
```

### Issue: EKS Cluster Creation Fails

**Symptoms:** EKS cluster stuck in "Creating" state

**Resolution:**
```bash
# Check CloudWatch Logs for EKS control plane
aws logs tail /aws/eks/cluster-name/cluster --follow

# Verify IAM role trust policy
aws iam get-role --role-name EKSClusterRole

# Check subnet requirements (minimum 2 AZs)
aws ec2 describe-subnets --subnet-ids subnet-xxxxx subnet-yyyyy
```

### Issue: S3 Bucket Access Denied

**Symptoms:** "Access Denied" when accessing S3 bucket

**Resolution:**
```bash
# Check bucket policy
aws s3api get-bucket-policy --bucket bucket-name

# Verify IAM permissions
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:user/username \
  --action-names s3:GetObject \
  --resource-arns arn:aws:s3:::bucket-name/*

# Check bucket public access block settings
aws s3api get-public-access-block --bucket bucket-name
```

## 📚 Additional Resources

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [FedRAMP on AWS](https://aws.amazon.com/compliance/fedramp/)
- [NIST 800-53 on AWS](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/nist-800-53-controls.html)
- [AWS Security Best Practices](https://docs.aws.amazon.com/security/)
- [AWS GovCloud Documentation](https://docs.aws.amazon.com/govcloud-us/)
- [Ansible AWS Collection Docs](https://docs.ansible.com/ansible/latest/collections/amazon/aws/)

## 🤝 Contributing

When contributing to AWS automation:
- Test in non-production AWS account first
- Follow AWS Well-Architected Framework principles
- Include cost estimates for resources created
- Document IAM permissions required
- Include rollback procedures for destructive operations
- Tag all resources appropriately
- Test with both AWS Commercial and GovCloud (where applicable)

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team
**AWS Regions Supported:** All commercial regions + GovCloud (us-gov-west-1, us-gov-east-1)

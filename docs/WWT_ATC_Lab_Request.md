# Fourth Estate Ansible Automation Lab — WWT ATC Resource Request

**Date:** February 10, 2026
**Classification:** UNCLASSIFIED
**Requested By:** Fourth Estate Automation Team
**Environment:** WWT Advanced Technology Center (ATC) — VMware vSphere

---

## 1. Purpose

This document outlines the resources required to stand up an Ansible automation lab within the WWT Advanced Technology Center (ATC). The lab will be used to host, test, and demonstrate an enterprise Ansible playbook repository containing 516+ roles across 39+ technology platforms with emphasis on DoD STIG, NIST 800-53, NIST 800-171, FedRAMP, and FISMA compliance automation.

The lab will be built incrementally. Phase 1 establishes the Ansible controller. Subsequent phases add worker nodes as individual technology domains come online for testing and demonstration.

---

## 2. Architecture Overview

```
                        ┌──────────────────────────────────┐
                        │         WWT ATC vSphere          │
                        │                                  │
  Outbound HTTPS ◄──────┤  ┌────────────────────────────┐  │
  (Cloud APIs,          │  │     Lab Port Group          │  │
   Collections,         │  │     (Single Flat Network)   │  │
   Packages)            │  │                              │  │
                        │  │  ┌──────────────────────┐   │  │
                        │  │  │  ansible-controller   │   │  │
                        │  │  │  Rocky/RHEL 9         │   │  │
                        │  │  │  2 vCPU | 4 GB | 60 GB│   │  │
                        │  │  └──────────┬───────────┘   │  │
                        │  │             │ SSH / WinRM    │  │
                        │  │     ┌───────┴───────┐       │  │
                        │  │     │               │       │  │
                        │  │     ▼               ▼       │  │
                        │  │  [Linux          [Windows   │  │
                        │  │   Workers]        Workers]  │  │
                        │  │  (Added per phase)          │  │
                        │  │                              │  │
                        │  └────────────────────────────┘  │
                        └──────────────────────────────────┘
```

---

## 3. Phase 1 — Ansible Controller (Initial Request)

Phase 1 is the minimum viable lab. A single virtual machine running the Ansible controller. This VM executes playbooks, manages inventories, and communicates with target systems. Many of the playbooks in this repository target cloud and appliance APIs over HTTPS using a local connection model, meaning the controller alone — with no worker nodes — can execute a significant portion of the automation library.

### 3.1 Virtual Machine Specification

| Attribute | Value |
|-----------|-------|
| **VM Name** | `ansible-controller` |
| **Guest OS** | Rocky Linux 9.x (preferred) or RHEL 9.x |
| **vCPU** | 2 |
| **Memory** | 4 GB |
| **Disk** | 60 GB, thin-provisioned |
| **Network** | 1 vNIC |
| **VMware Tools** | open-vm-tools (installed post-deploy) |

### 3.2 Network Requirements

| Requirement | Detail |
|-------------|--------|
| **Port Group** | 1 flat lab network (e.g., /24 subnet) |
| **Outbound Internet** | HTTPS (TCP 443) — required for package installation, Ansible Galaxy collection downloads, and API-based playbook execution against cloud and SaaS targets |
| **DNS** | Not required for Phase 1; `/etc/hosts` will be used for lab name resolution |

### 3.3 Software (Installed Post-Deploy)

| Component | Version | Purpose |
|-----------|---------|---------|
| Python | 3.9+ | Ansible runtime dependency |
| Ansible Core | 2.14+ | Playbook execution engine |
| ansible-lint | Latest | Playbook validation and linting |
| molecule | Latest | Role-level testing framework |
| Git | 2.x+ | Repository management |
| pip | Latest | Python package management |
| open-vm-tools | Latest | vSphere guest integration |
| sshpass | Latest | Password-based SSH for lab targets |

No additional licensed software is required for Phase 1.

### 3.4 Phase 1 Capabilities

With only the controller VM, the following activities are supported:

- Syntax validation and linting across the entire playbook repository
- Dry-run execution (`--check --diff`) against any defined inventory
- Full execution of API-based playbooks (connection: local) targeting:
  - Cloud platforms (AWS, Azure, GCP) with sandbox or evaluation credentials
  - Network appliances (Palo Alto, Check Point, Fortinet, F5, Arista) via API
  - Storage platforms (Pure Storage, NetApp, VAST Data) via API
  - Monitoring and ITSM (ScienceLogic, ServiceNow) via API
  - Secrets management (HashiCorp Vault in dev mode, locally)
- Role development, modification, and molecule testing
- Git-based workflow operations

### 3.5 Phase 1 Resource Summary

| Resource | Total |
|----------|-------|
| Virtual Machines | 1 |
| vCPU | 2 |
| Memory | 4 GB |
| Storage (thin) | 60 GB |
| Port Groups | 1 |

---

## 4. Subsequent Phases — Worker Nodes

As technology domains are brought online for testing, worker nodes will be added to the lab incrementally. Each worker is a target host that the Ansible controller manages over SSH (Linux) or WinRM (Windows). The following sections define the standard worker node specifications.

### 4.1 Linux Worker Node Template

Used for: RHEL STIG hardening, database deployment (PostgreSQL, MySQL, Oracle), Splunk/ELK agents, CrowdStrike/SentinelOne agents, Kubernetes nodes, and general Linux automation.

| Attribute | Value |
|-----------|-------|
| **Guest OS** | Rocky Linux 9.x or RHEL 9.x |
| **vCPU** | 2 |
| **Memory** | 2–4 GB (4 GB for database or log aggregation roles) |
| **Disk** | 40–60 GB, thin-provisioned |
| **Network** | 1 vNIC on the lab port group |
| **VMware Tools** | open-vm-tools |
| **Pre-requisites** | Python 3.9+, SSH enabled |

### 4.2 Windows Worker Node Template

Used for: Windows Server STIG hardening, Active Directory configuration, Group Policy automation, and Windows-based EDR agent deployment.

| Attribute | Value |
|-----------|-------|
| **Guest OS** | Windows Server 2022 Standard |
| **vCPU** | 2 |
| **Memory** | 4 GB |
| **Disk** | 60 GB, thin-provisioned |
| **Network** | 1 vNIC on the lab port group |
| **VMware Tools** | VMware Tools for Windows |
| **Pre-requisites** | WinRM / PowerShell Remoting enabled |

### 4.3 Kubernetes Cluster (When K8s/OpenShift Playbooks Come Online)

Used for: Kubernetes STIG V1R11 compliance, cluster hardening, application deployment, and OpenShift automation.

| Node | Guest OS | vCPU | Memory | Disk |
|------|----------|------|--------|------|
| k8s-control | Rocky/RHEL 9 | 2 | 4 GB | 50 GB |
| k8s-worker01 | Rocky/RHEL 9 | 2 | 4 GB | 50 GB |
| k8s-worker02 | Rocky/RHEL 9 | 2 | 4 GB | 50 GB |

### 4.4 Growth Projection

The following table projects cumulative ATC resource consumption as technology domains are added to the lab:

| Milestone | VMs | vCPU | Memory | Storage (Thin) |
|-----------|-----|------|--------|----------------|
| Phase 1 — Controller only | 1 | 2 | 4 GB | 60 GB |
| + 1 Linux worker | 2 | 4 | 8 GB | 120 GB |
| + 1 Windows worker | 3 | 6 | 12 GB | 180 GB |
| + 2nd Linux worker (databases, clustering) | 4 | 8 | 16 GB | 240 GB |
| + Kubernetes cluster (3 nodes) | 7 | 14 | 28 GB | 390 GB |
| + Log aggregation node (Splunk/ELK) | 8 | 18 | 36 GB | 590 GB |
| + Network virtual appliances (2 devices) | 10 | 22 | 44 GB | 690 GB |

---

## 5. Networking Requirements

All phases use the same flat network topology. No additional VLANs, routers, or inter-node firewalls are required.

| Flow | Protocol | Port | Direction |
|------|----------|------|-----------|
| Controller → Linux workers | SSH | TCP 22 | Internal |
| Controller → Windows workers | WinRM | TCP 5985 / 5986 | Internal |
| Controller → Internet | HTTPS | TCP 443 | Outbound |
| All VMs → Package repos | HTTPS | TCP 443 | Outbound |

### 5.1 DNS

- Phase 1: No DNS server required. The controller will use `/etc/hosts` for lab name resolution.
- Future phases: A local DNS server may be added if the node count grows beyond practical `/etc/hosts` management.

---

## 6. VM Template Request

To enable self-service provisioning of worker nodes as technologies come online, the following VM templates are requested in the ATC catalog:

| Template Name | Base OS | Pre-installed Components |
|---------------|---------|--------------------------|
| `tpl-rocky9-ansible` | Rocky Linux 9.x minimal | Python 3.9+, open-vm-tools, SSH enabled |
| `tpl-win2022-ansible` | Windows Server 2022 Standard | VMware Tools, WinRM enabled, PowerShell 5.1+ |

These templates allow rapid cloning of new worker nodes without repeating base OS configuration.

---

## 7. Licensing

| Software | License Type | Cost |
|----------|-------------|------|
| Rocky Linux 9 | Open source | $0 |
| RHEL 9 (if used) | Red Hat Developer Subscription | $0 |
| Windows Server 2022 | 180-day evaluation | $0 |
| Python, Ansible Core, Git | Open source | $0 |
| Ansible collections | Open source / community | $0 |
| VMware vSphere | Provided by WWT ATC | N/A |
| Network virtual appliances (future) | Vendor evaluation licenses | TBD per vendor |

No additional software licensing is required for Phase 1 or initial worker node deployment.

---

## 8. Summary of Initial Request (Phase 1)

| Item | Specification |
|------|---------------|
| **Virtual Machines** | 1 |
| **Guest OS** | Rocky Linux 9.x or RHEL 9.x |
| **vCPU** | 2 |
| **Memory** | 4 GB |
| **Storage** | 60 GB thin-provisioned |
| **Network** | 1 port group with outbound HTTPS |
| **Templates Requested** | Rocky 9 and Windows Server 2022 base images |
| **Licensed Software** | None (all open source) |

This is the bare minimum to stand up the Ansible automation lab and begin testing the Fourth Estate playbook repository. Worker nodes will be added incrementally as technology domains are prioritized and brought online.

---

## 9. Points of Contact

| Role | Name | Contact |
|------|------|---------|
| Lab Requestor | | |
| Technical Lead | | |
| WWT ATC Liaison | | |

---

*This document supports the Fourth Estate Ansible Automation initiative. All lab activities are UNCLASSIFIED.*

# cybervision_sensor_config

Ansible role for Cisco Cyber Vision sensor enrollment, zone (group) creation, reporting policy configuration, and capture mode setup.

## Quick Start

```bash
# Dry-run
ansible-playbook -i inventory site.yml --tags sensors --ask-vault-pass

# Apply
ansible-playbook -i inventory site.yml --tags sensors -e "apply_changes=true" --ask-vault-pass
```

## Features

| Module | Task File | Description |
|--------|-----------|-------------|
| Sensor Enrollment | `sensor_enrollment.yml` | Enrollment token generation and zone creation |
| Sensor Policies | `sensor_policies.yml` | Protocol decoders and reporting configuration |
| Capture Modes | `capture_modes.yml` | SPAN/TAP/IOx capture mode per sensor type |
| Validation | `validation.yml` | Sensor connectivity and status check |

## Sensor Types Supported

| Type | Capture Mode | Description |
|------|-------------|-------------|
| `hardware` | SPAN | Dedicated hardware sensor appliance |
| `software` | SPAN | Software sensor (VM or container) |
| `iol` | IOx | Cisco IOx sensor on Catalyst switches |

## Protocol Decoders

The default sensor policy enables OT/ICS protocol decoding for:
`modbus`, `dnp3`, `s7`, `bacnet`, `ethernet_ip`, `profinet`, `iec61850`, `opcua`

## Key Variables

```yaml
cv_sensor_enrollment_ttl_hours: 24

cv_sensor_zones:
  - name: "plant_floor"
    description: "Level 0/1 devices"
    color: "#e74c3c"

cv_sensor_policies:
  - name: "FourthEstate-Default"
    report_flows: true
    report_assets: true
    report_vulnerabilities: true
    protocol_decoders:
      - "modbus"
      - "dnp3"
```

## Inventory Setup

```ini
[cv_sensors]
cv-sensor-01 ansible_host=192.168.10.20 sensor_type=hardware sensor_zone=plant_floor
cv-sensor-02 ansible_host=192.168.10.21 sensor_type=iol sensor_zone=control_room
```

## Required Vault Variables

```yaml
vault_cv_center_hostname: "cybervision.example.com"
vault_cv_api_token: "your-api-bearer-token"
```

## Generated Artifacts

| Artifact | Description |
|----------|-------------|
| `cv_enrollment_token.json` | Enrollment token (restricted permissions) |
| `cv_sensor_enrollment.json` | Zone and sensor counts |
| `cv_sensor_policies.json` | Policy configuration |
| `cv_capture_modes.json` | Capture mode defaults and sensor count |
| `cv_sensor_validation.json` | Online/offline sensor status |

## Tags

```bash
--tags sensors       # All sensor config tasks
--tags enrollment    # Enrollment and zones only
--tags policies      # Sensor reporting policies only
--tags capture       # Capture mode config only
```

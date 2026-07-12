# rhel-hardening

Applies DoD STIG (RHEL 8 V1R14 / RHEL 9 V1R3) and NIST 800-53 Rev 5 system hardening to Red Hat Enterprise Linux servers. Covers FIPS mode, SSH configuration, kernel parameters, password policy, file permissions, and login banners.

## Requirements

- Ansible 2.15+
- `ansible.posix` collection
- Hosts in the `rhel_servers` inventory group
- `become: true` (sudo access required)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `rhel_stig_level` | `high` | No | Compliance level: low, medium, high, critical Determines which STIG controls are applied |
| `rhel_apply_nist_controls` | `true` | No | Enable NIST SP 800-53 controls |
| `rhel_apply_cis_benchmark` | `true` | No | Enable CIS Benchmark controls |
| `rhel_enable_fips` | `false` | No | Enable FIPS 140-2 mode (requires reboot) NIST SP 800-53: SC-13 |
| `rhel_check_fips_status` | `true` | No | FIPS mode status check only (no changes) |
| `rhel_ssh_permit_root_login` | `false` | No | SSH Daemon Configuration STIG V-204596: SSH root login must be disabled |
| `rhel_ssh_ciphers` | `(see defaults/main.yml)` | No | STIG V-204597: SSH must use strong ciphers |
| `rhel_ssh_macs` | `(see defaults/main.yml)` | No | STIG V-204598: SSH must use strong MACs |
| `rhel_ssh_kex_algorithms` | `(see defaults/main.yml)` | No | STIG V-204599: SSH must use strong key exchange algorithms |
| `rhel_ssh_password_authentication` | `false` | No | STIG V-204600: SSH password authentication configuration |
| `rhel_ssh_pubkey_authentication` | `true` | No | STIG V-204601: SSH public key authentication |
| `rhel_ssh_x11_forwarding` | `false` | No | STIG V-204602: SSH X11 forwarding must be disabled |
| `rhel_ssh_max_auth_tries` | `3` | No | STIG V-204603: SSH MaxAuthTries |
| `rhel_ssh_max_sessions` | `10` | No | STIG V-204604: SSH MaxSessions |
| `rhel_ssh_client_alive_interval` | `600` | No | STIG V-204605: SSH ClientAliveInterval |
| `rhel_ssh_client_alive_count_max` | `0` | No | STIG V-204606: SSH ClientAliveCountMax |
| `rhel_ssh_permit_user_environment` | `false` | No | STIG V-204607: SSH PermitUserEnvironment |
| `rhel_ssh_permit_empty_passwords` | `false` | No | STIG V-204608: SSH PermitEmptyPasswords |
| `rhel_ssh_hostbased_authentication` | `false` | No | STIG V-204609: SSH HostbasedAuthentication |
| `rhel_ssh_gssapi_authentication` | `false` | No | STIG V-204610: SSH GSSAPIAuthentication |
| `rhel_ssh_kerberos_authentication` | `false` | No | STIG V-204611: SSH KerberosAuthentication |
| `rhel_ssh_banner` | `/etc/issue.net` | No | STIG V-204612: SSH Banner |
| `rhel_ssh_protocol` | `2` | No | SSH Protocol version |
| `rhel_ssh_port` | `22` | No | SSH Port |
| `rhel_ssh_allowed_users` | `[]` | No | SSH allowed users (empty means all users allowed) |
| `rhel_ssh_allowed_groups` | `[]` | No | SSH allowed groups (empty means all groups allowed) |
| `rhel_password_min_length` | `14` | No | STIG V-204405: Password minimum length NIST SP 800-53: IA-5(1)(a) |
| `rhel_password_min_digit` | `1` | No | STIG V-204406: Password minimum digit characters |
| `rhel_password_min_upper` | `1` | No | STIG V-204407: Password minimum uppercase characters |
| `rhel_password_min_lower` | `1` | No | STIG V-204408: Password minimum lowercase characters |
| `rhel_password_min_special` | `1` | No | STIG V-204409: Password minimum special characters |
| `rhel_password_min_diff` | `8` | No | STIG V-204410: Password minimum difference from old password |
| `rhel_password_max_repeating` | `3` | No | STIG V-204411: Password maximum repeating characters |
| `rhel_password_max_consecutive` | `3` | No | STIG V-204412: Password maximum consecutive characters |
| `rhel_password_remember` | `5` | No | STIG V-204413: Password history (remember) |
| `rhel_password_max_days` | `60` | No | STIG V-204414: Password maximum age (days) NIST SP 800-53: IA-5(1)(d) |
| `rhel_password_min_days` | `1` | No | STIG V-204415: Password minimum age (days) NIST SP 800-53: IA-5(1)(d) |
| `rhel_password_warn_age` | `7` | No | STIG V-204416: Password warning age (days) |
| `rhel_account_inactive_days` | `35` | No | STIG V-204417: Account inactive period (days) |
| `rhel_password_hash_algorithm` | `sha512` | No | STIG V-204418: Password hashing algorithm |
| `rhel_failed_login_attempts` | `3` | No | STIG V-204419: Failed login attempts before lockout NIST SP 800-53: AC-7(a) |
| `rhel_account_lockout_duration` | `900` | No | STIG V-204420: Account lockout duration (seconds) |
| `rhel_failed_login_reset_interval` | `900` | No | STIG V-204421: Failed login attempts reset interval (seconds) |
| `rhel_login_fail_delay` | `4000000` | No | STIG V-204422: Delay after failed login (milliseconds) |
| `rhel_root_console_only` | `true` | No | STIG V-204423: Root login via console only |
| `rhel_root_allowed_consoles` | `(see defaults/main.yml)` | No | STIG V-204424: Allowed console devices for root |
| `rhel_lock_inactive_accounts` | `true` | No | STIG V-204425: Accounts must be locked after inactivity |
| `rhel_lock_system_accounts` | `true` | No | STIG V-204426: System accounts must be locked |
| `rhel_enforce_single_root_uid` | `true` | No | STIG V-204427: UID 0 reserved for root only |
| `rhel_home_dir_permissions` | `"0750"` | No | STIG V-204428: Home directory permissions |
| `rhel_user_init_files_permissions` | `"0740"` | No | STIG V-204429: User initialization files permissions |
| `rhel_fix_user_init_files` | `true` | No | STIG V-204430: Remove user initialization files with write permissions |
| `rhel_pam_files_owner` | `root` | No | STIG V-204431: PAM configuration files ownership |
| `rhel_pam_files_group` | `root` | No | — |
| `rhel_pam_files_permissions` | `"0644"` | No | STIG V-204432: PAM configuration files permissions |
| `rhel_use_pwquality` | `true` | No | STIG V-204433: System must use pwquality |
| `rhel_use_faillock` | `true` | No | STIG V-204434: System must use faillock |
| `rhel_faillock_enabled` | `true` | No | STIG V-204435: Disable account identifiers after excessive login failures |
| `rhel_session_timeout` | `600` | No | STIG V-204436: Session timeout (seconds) NIST SP 800-53: AC-12 |
| `rhel_tmout` | `600` | No | STIG V-204437: TMOUT shell timeout (seconds) |
| `rhel_configure_tmout_profile` | `true` | No | STIG V-204438: Configure TMOUT in profile |
| `rhel_tmout_readonly` | `true` | No | STIG V-204439: Configure TMOUT readonly |
| `rhel_disable_ctrl_alt_del` | `true` | No | STIG V-204440: Disable ctrl-alt-del NIST SP 800-53: AC-6(1) |
| `rhel_screen_lock_enabled` | `true` | No | STIG V-204441: Screen lock configuration |
| `rhel_screen_lock_delay` | `300` | No | — |
| `rhel_automatic_logout_enabled` | `true` | No | STIG V-204442: Automatic logout |
| `rhel_disable_usb_storage` | `true` | No | STIG V-204443: USB storage disable |
| `rhel_disable_automount` | `true` | No | STIG V-204444: Disable automounting NIST SP 800-53: MP-7 |
| `rhel_disable_bluetooth` | `false` | No | STIG V-204445: Disable Bluetooth |
| `rhel_check_separate_tmp` | `true` | No | STIG V-204446: Separate partition for /tmp |
| `rhel_check_separate_var` | `true` | No | STIG V-204447: Separate partition for /var |
| `rhel_check_separate_var_log` | `true` | No | STIG V-204448: Separate partition for /var/log |
| `rhel_check_separate_var_log_audit` | `true` | No | STIG V-204449: Separate partition for /var/log/audit |
| `rhel_check_separate_home` | `true` | No | STIG V-204450: Separate partition for /home |
| `rhel_tmp_mount_options` | `(see defaults/main.yml)` | No | STIG V-204451: /tmp mount options |
| `rhel_var_mount_options` | `(see defaults/main.yml)` | No | STIG V-204452: /var mount options |
| `rhel_var_log_mount_options` | `(see defaults/main.yml)` | No | STIG V-204453: /var/log mount options |
| `rhel_var_log_audit_mount_options` | `(see defaults/main.yml)` | No | STIG V-204454: /var/log/audit mount options |
| `rhel_home_mount_options` | `(see defaults/main.yml)` | No | STIG V-204455: /home mount options |
| `rhel_find_world_writable_files` | `true` | No | STIG V-204456: World-writable files |
| `rhel_fix_world_writable_files` | `false` | No | — |
| `rhel_find_unowned_files` | `true` | No | STIG V-204457: Unowned files |
| `rhel_fix_unowned_files` | `false` | No | — |
| `rhel_find_ungrouped_files` | `true` | No | STIG V-204458: Ungrouped files |
| `rhel_fix_ungrouped_files` | `false` | No | — |
| `rhel_system_files_permissions` | `(see defaults/main.yml)` | No | STIG V-204459: System files permissions |
| `rhel_find_suid_sgid_files` | `true` | No | STIG V-204460: Remove SUID/SGID from unnecessary files |
| `rhel_remove_unnecessary_suid_sgid` | `false` | No | — |
| `rhel_disable_core_dumps` | `true` | No | STIG V-204461: Disable core dumps NIST SP 800-53: SI-11 |
| `rhel_core_dump_dir` | `/var/lib/systemd/coredump` | No | STIG V-204462: Restrict core dumps to protected directory |
| `rhel_core_dump_dir_permissions` | `"0750"` | No | — |
| `rhel_systemd_coredump_storage` | `none` | No | STIG V-204463: systemd-coredump configuration |
| `rhel_kdump_enabled` | `false` | No | STIG V-204464: kdump configuration |
| `rhel_disable_suid_core_dumps` | `true` | No | STIG V-204465: Disable core dumps for SUID programs |
| `rhel_network_ip_forward` | `0` | No | Kernel network parameters STIG V-204480: IP forwarding NIST SP 800-53: CM-7(a) |
| `rhel_network_send_redirects` | `0` | No | STIG V-204481: Send packet redirects |
| `rhel_network_accept_source_route` | `0` | No | STIG V-204482: Source routed packets |
| `rhel_network_accept_redirects` | `0` | No | STIG V-204483: ICMP redirects |
| `rhel_network_secure_redirects` | `0` | No | STIG V-204484: Secure ICMP redirects |
| `rhel_network_log_martians` | `1` | No | STIG V-204485: Log martians |
| `rhel_network_ignore_icmp_broadcast` | `1` | No | STIG V-204486: Ignore ICMP broadcasts |
| `rhel_network_ignore_bogus_icmp` | `1` | No | STIG V-204487: Ignore bogus ICMP errors |
| `rhel_network_rp_filter` | `1` | No | STIG V-204488: Reverse path filtering |
| `rhel_network_tcp_syncookies` | `1` | No | STIG V-204489: TCP SYN cookies NIST SP 800-53: SC-5 |
| `rhel_network_ipv6_accept_ra` | `0` | No | STIG V-204490: IPv6 router advertisements |
| `rhel_network_ipv6_accept_redirects` | `0` | No | STIG V-204491: IPv6 redirects |
| `rhel_disable_ipv6` | `false` | No | STIG V-204492: IPv6 disable (if not used) |
| `rhel_disable_unused_interfaces` | `false` | No | STIG V-204493: Network interfaces disable |
| `rhel_disable_unnecessary_services` | `true` | No | STIG V-204494: Unnecessary services must be disabled NIST SP 800-53: CM-7(a) |
| `rhel_services_to_disable` | `(see defaults/main.yml)` | No | Services to disable |
| `rhel_services_to_enable` | `(see defaults/main.yml)` | No | Services to enable |
| `rhel_remove_x11_packages` | `false` | No | STIG V-204495: X11 packages must be removed if not required |
| `rhel_x11_packages` | `(see defaults/main.yml)` | No | X11 packages to remove |
| `rhel_packages_to_remove` | `[]` | No | STIG V-204496: Remove packages |
| `rhel_remove_telnet_client` | `true` | No | STIG V-204497: Telnet client must be removed |
| `rhel_remove_rsh_client` | `true` | No | STIG V-204498: rsh-client must be removed |
| `rhel_remove_ypbind` | `true` | No | STIG V-204499: ypbind must be removed |
| `rhel_disable_tftp_server` | `true` | No | STIG V-204500: tftp-server must be disabled |
| `rhel_kernel_randomize_va_space` | `2` | No | STIG V-204511: Address Space Layout Randomization (ASLR) NIST SP 800-53: SC-30(2) |
| `rhel_kernel_kptr_restrict` | `1` | No | STIG V-204512: Restrict kernel pointer exposure |
| `rhel_kernel_modules_disabled` | `false` | No | STIG V-204513: Disable kernel module loading |
| `rhel_kernel_yama_ptrace_scope` | `1` | No | STIG V-204514: Restrict ptrace scope |
| `rhel_kernel_dmesg_restrict` | `1` | No | STIG V-204515: Restrict dmesg access |
| `rhel_kernel_kexec_load_disabled` | `1` | No | STIG V-204516: Disable kexec |
| `rhel_kernel_unprivileged_userns_clone` | `0` | No | STIG V-204517: Disable user namespaces (if not needed) |
| `rhel_kernel_unprivileged_bpf_disabled` | `1` | No | STIG V-204518: Disable BPF JIT |
| `rhel_kernel_modules_blacklist` | `(see defaults/main.yml)` | No | STIG V-204519: Kernel modules to disable |
| `rhel_grub_password_enabled` | `true` | No | STIG V-204520: GRUB password protection |
| `rhel_grub_config_permissions` | `"0600"` | No | STIG V-204521: Bootloader configuration permissions |
| `rhel_grub_disable_recovery` | `false` | No | STIG V-204522: Disable GRUB rescue mode without password |
| `rhel_require_uefi` | `false` | No | STIG V-204523: System must use UEFI |
| `rhel_secure_boot_enabled` | `false` | No | STIG V-204524: Secure Boot enabled |
| `rhel_tpm_enabled` | `false` | No | STIG V-204525: TPM enabled |
| `rhel_sudoers_file_permissions` | `"0440"` | No | STIG V-204526: Sudoers file permissions |
| `rhel_sudo_timestamp_timeout` | `5` | No | STIG V-204527: Sudo authentication timeout |
| `rhel_sudo_use_pty` | `true` | No | STIG V-204528: Sudo use_pty required |
| `rhel_sudo_logfile` | `/var/log/sudo.log` | No | STIG V-204529: Sudo logfile |
| `rhel_sudo_authenticate` | `true` | No | STIG V-204530: Sudo password required for each command |
| `rhel_sudo_requiretty` | `false` | No | STIG V-204531: Sudo requiretty (deprecated in favor of use_pty) |
| `rhel_sudo_env_reset` | `true` | No | STIG V-204532: Sudo environment reset |
| `rhel_sudo_secure_path` | `/sbin:/bin:/usr/sbin:/usr/bin` | No | STIG V-204533: Sudo secure path |
| `rhel_sudo_passwd_tries` | `3` | No | STIG V-204534: Sudo passwd_tries |
| `rhel_sudoers_d_enabled` | `true` | No | STIG V-204535: Sudoers.d directory |
| `rhel_sudoers_d_permissions` | `"0750"` | No | — |
| `rhel_configure_login_banner` | `true` | No | STIG V-204536: Display login banner NIST SP 800-53: AC-8 |
| `rhel_banner_text` | `(multi-line text — see defaults/main.yml)` | No | STIG V-204537: Banner text |
| `rhel_configure_issue_banner` | `true` | No | STIG V-204538: /etc/issue banner |
| `rhel_configure_issue_net_banner` | `true` | No | STIG V-204539: /etc/issue.net banner |
| `rhel_configure_motd_banner` | `true` | No | STIG V-204540: /etc/motd banner |
| `rhel_time_sync_enabled` | `true` | No | STIG V-204541: Time synchronization required NIST SP 800-53: AU-8(1)(a) |
| `rhel_time_sync_service` | `chronyd` | No | STIG V-204542: Chronyd must be used |
| `rhel_ntp_servers` | `(see defaults/main.yml)` | No | STIG V-204543: NTP servers |
| `rhel_ntp_restrict_default` | `true` | No | STIG V-204544: NTP configuration |
| `rhel_chronyd_user` | `chrony` | No | STIG V-204545: Chronyd run as unprivileged user |
| `rhel_crypto_policy` | `DEFAULT:NO-SHA1` | No | Configure system-wide crypto policy |
| `rhel_install_security_packages` | `true` | No | Install security packages |
| `rhel_security_packages` | `(see defaults/main.yml)` | No | Security packages to install |
| `rhel_configure_aide` | `true` | No | Configure AIDE (Advanced Intrusion Detection Environment) |
| `rhel_aide_db_path` | `/var/lib/aide/aide.db.gz` | No | — |
| `rhel_aide_check_schedule` | `daily` | No | — |
| `rhel_configure_usbguard` | `false` | No | Configure USBGuard |
| `rhel_usbguard_policy` | `allow` | No | — |
| `rhel_check_subscription` | `true` | No | System must be registered with Red Hat |
| `rhel_configure_logging` | `true` | No | Configure system logging |
| `rhel_configure_audit_rules` | `true` | No | Configure audit rules |
| `rhel_run_preflight_checks` | `true` | No | Run pre-flight checks |
| `rhel_run_compliance_validation` | `false` | No | Run compliance validation after hardening |
| `rhel_generate_compliance_report` | `false` | No | Generate compliance report |
| `rhel_compliance_report_path` | `/tmp/rhel-compliance-report.txt` | No | Compliance report path |
| `rhel_fail_on_compliance_violations` | `false` | No | Fail on compliance violations |

## Example Playbook

```yaml
---
- name: RHEL STIG Hardening
  hosts: rhel_servers
  become: true
  roles:
    - role: rhel/roles/rhel-hardening
      vars:
        rhel_stig_level: high
        rhel_enable_fips: false      # set true and reboot for full STIG compliance
        rhel_ssh_permit_root_login: false
```

## Tags

| Tag | Description |
|-----|-------------|
| `hardening` | All hardening tasks |
| `ssh` | SSH configuration (V-230293 through V-230300) |
| `fips` | FIPS 140-2 configuration |
| `kernel` | Kernel parameter hardening |
| `banner` | Login banner configuration |

## License

MIT

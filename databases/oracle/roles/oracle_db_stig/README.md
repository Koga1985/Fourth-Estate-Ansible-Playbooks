# Oracle Database STIG (`oracle_db_stig`)

Hardens and assesses **Oracle Database** to the DISA **Oracle Database 12c STIG**
(`O121-*`, applicable to 19c). Runs on the DB host, becomes the Oracle OS owner,
and uses `sqlplus "/ as sysdba"`. No certified Oracle SQL module exists, so the
supported CLI path is used (the same model as the IBM DB2 role).

## Why "grab and go"
* **Safe by default**: `apply_changes=false` only queries `v$parameter`
  (assessment) and writes a per-host JSON artifact; nothing changes until
  `-e apply_changes=true`.
* No extra collections — SSH + `become` to the Oracle owner.

## Quick start
```bash
cd databases/oracle/roles/oracle_db_stig/playbooks
cp inventory.example inventory && $EDITOR inventory   # set ORACLE_HOME/SID
ansible-playbook -i inventory run.yml                       # DRY-RUN (assessment)
ansible-playbook -i inventory run.yml -e apply_changes=true # ENFORCE
cat /tmp/oracle-stig-artifacts/ora-01_oracle_db_stig.json
```

## Controls
System parameters (`AUDIT_TRAIL`, `O7_DICTIONARY_ACCESSIBILITY=FALSE`,
`REMOTE_OS_AUTHENT=FALSE`, `SEC_CASE_SENSITIVE_LOGON=TRUE`,
`SEC_MAX_FAILED_LOGIN_ATTEMPTS=3`, `GLOBAL_NAMES=TRUE`,
`REMOTE_LOGIN_PASSWORDFILE=EXCLUSIVE`) and the password profile
(`FAILED_LOGIN_ATTEMPTS=3`, `PASSWORD_LIFE_TIME=60`, `PASSWORD_REUSE_MAX/TIME`,
`PASSWORD_LOCK_TIME`, `INACTIVE_ACCOUNT_TIME`).

## ⚠️ Pre-flight
* `SCOPE=SPFILE` parameter changes require a **database restart** to take effect
  (flagged in the artifact) — schedule a window.
* Assign a `PASSWORD_VERIFY_FUNCTION` to the profile per password-complexity
  requirements (operator follow-up).

## Tags
`--tags assess`, `parameters`, `profile`, `report`, `stig_cat2`.

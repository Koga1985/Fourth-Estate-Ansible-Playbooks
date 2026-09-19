#!/usr/bin/env bash
# Prove the secret gate still detects what it exists for.
#
# A detection gate has a failure mode the other gates do not: it can go blind
# and still pass, quietly, forever. An over-eager allowlist in .gitleaks.toml,
# or a rule whose regex stops matching, turns a green build into no coverage at
# all -- and nothing about the build looks different.
#
# So this plants a credential of every shape the custom rules exist for, in a
# temporary directory, and asserts each one is found. It is the test for the
# gate, not for the repository.
#
#   ./scripts/check_secret_gate.sh
#
# The planted values live here rather than in .github/workflows/ci.yml because
# the gate scans that file too -- and correctly flagged them. This path is the
# single narrow allowlist entry in .gitleaks.toml.
set -euo pipefail

cd "$(dirname "$0")/.."

command -v gitleaks >/dev/null 2>&1 || {
  echo "gitleaks is not available. Install it first:" >&2
  echo "  https://github.com/gitleaks/gitleaks/releases" >&2
  exit 1
}

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
cp .gitleaks.toml "$work/"

# One line per shape the rules cover. Update EXPECTED when adding a line.
cat > "$work/planted.yml" <<'PLANT'
ansible_password: Summer2024!
api_token: "abc123def456ghi789"
ise_password=P@ssw0rd-Winter
vault_snmp_community: "public-but-not-really-9f3a"
PLANT
printf 'hunter2-the-vault-password\n' > "$work/.vault_pass"
EXPECTED=5

# And the indirection the repo actually uses, which must NOT be reported.
cat > "$work/allowed.yml" <<'ALLOWED'
ansible_password: "{{ vault_cp_password }}"
vcenter_password: "{{ lookup('env','VCENTER_PASSWORD') }}"
vault_ise_password: "CHANGE_ME"
password_required: true
token_ttl: 3600
password_hash_algorithm: sha512
private_key_path: /etc/ssl/private/server.key
aci_password: vault_aci_apic_password
alert_secret_contact: security@example.com
ALLOWED

gitleaks dir "$work" --config "$work/.gitleaks.toml" \
  --report-format json --report-path "$work/out.json" \
  --no-banner --exit-code 0 >/dev/null 2>&1 || true

found="$(python3 -c "import json,sys;print(len(json.load(open(sys.argv[1]))))" "$work/out.json")"
false_positives="$(python3 -c "
import json, sys
print(sum(1 for f in json.load(open(sys.argv[1])) if f['File'].endswith('allowed.yml')))
" "$work/out.json")"

echo "planted $EXPECTED credentials, gitleaks found $found"
echo "planted 9 non-secrets, gitleaks reported $false_positives"

status=0
if [ "$found" -lt "$EXPECTED" ]; then
  echo "" >&2
  echo "FAIL: .gitleaks.toml no longer detects credentials it is supposed to catch." >&2
  echo "A rule or allowlist change has made the secret gate blind." >&2
  echo "Fix the config rather than lowering EXPECTED in this script." >&2
  python3 -c "
import json, sys
seen = {f['StartLine'] for f in json.load(open(sys.argv[1])) if f['File'].endswith('planted.yml')}
for n, line in enumerate(open(sys.argv[2]), 1):
    if n not in seen:
        print('  MISSED  %s' % line.rstrip(), file=sys.stderr)
" "$work/out.json" "$work/planted.yml" || true
  status=1
fi

if [ "$false_positives" -ne 0 ]; then
  echo "" >&2
  echo "FAIL: .gitleaks.toml reported $false_positives value(s) that are not secrets." >&2
  echo "A rule has become too broad; every line in allowed.yml is indirection" >&2
  echo "or a placeholder this repository uses deliberately." >&2
  python3 -c "
import json, sys
for f in json.load(open(sys.argv[1])):
    if f['File'].endswith('allowed.yml'):
        print('  FALSE POSITIVE  line %s: %r' % (f['StartLine'], f['Secret']), file=sys.stderr)
" "$work/out.json" || true
  status=1
fi

[ "$status" -eq 0 ] && echo "The secret gate detects what it is for, and nothing it should not."
exit "$status"

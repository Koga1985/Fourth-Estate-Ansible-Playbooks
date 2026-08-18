#!/usr/bin/env bash
# Generate .ansible-lint-ignore-online on a machine that can reach Ansible Galaxy.
#
# Why this is separate from .ansible-lint-ignore
# ----------------------------------------------
# The required ansible-lint gate runs with --offline and no collections
# installed. In that mode `syntax-check[unknown-module]` fires for every
# non-builtin module, so those findings sit in .ansible-lint-ignore permanently
# and the rule can never catch a module that genuinely does not exist.
#
# With the collections installed the rule becomes meaningful, but it needs its
# own baseline because the finding set is different. Once
# .ansible-lint-ignore-online exists and is committed, the CI job
# "ansible-lint with collections" turns itself into a blocking gate -- no
# workflow edit required.
#
# Usage (needs network access to galaxy.ansible.com):
#     ./scripts/generate_online_baseline.sh
#     git add .ansible-lint-ignore-online && git commit
#
# Re-run it whenever the pinned ansible-core/ansible-lint versions change, the
# same way .ansible-lint-ignore is regenerated.
set -euo pipefail

ANSIBLE_CORE_VERSION="${ANSIBLE_CORE_VERSION:-2.19.11}"
ANSIBLE_LINT_VERSION="${ANSIBLE_LINT_VERSION:-26.6.0}"
BASELINE=".ansible-lint-ignore-online"

cd "$(dirname "$0")/.."

echo "==> Checking Galaxy reachability"
if ! ansible-galaxy collection list >/dev/null 2>&1; then
  echo "ansible-galaxy is not available. Install ansible-core first:" >&2
  echo "  pip install ansible-core==${ANSIBLE_CORE_VERSION} ansible-lint==${ANSIBLE_LINT_VERSION}" >&2
  exit 1
fi

echo "==> Installing declared collections from every requirements.yml"
# A requirements file may carry a "# automation-hub-only: <collections>" line
# to declare that it depends on collections with no stable community-Galaxy
# release (Red Hat Automation Hub only). Install failures for those files are
# expected on a Galaxy-only machine: their modules stay unresolvable, the
# resulting unknown-module findings are baselined once, and the gate still
# ratchets everything else. Any OTHER install failure aborts, because its
# findings would be install artifacts rather than repository defects.
failed_reqs=()
expected_failures=()
while read -r req; do
  echo "    -- $req"
  if ! ansible-galaxy collection install -r "$req"; then
    if grep -q '^# automation-hub-only:' "$req"; then
      expected_failures+=("$req")
    else
      failed_reqs+=("$req")
    fi
  fi
done < <(find . -path ./.git -prune -o -name 'requirements.yml' -print | sort)

if [ "${#expected_failures[@]}" -gt 0 ]; then
  echo ""
  echo "Expected failures (marked automation-hub-only, findings will be baselined):"
  printf '    %s\n' "${expected_failures[@]}"
fi

if [ "${#failed_reqs[@]}" -gt 0 ]; then
  echo "" >&2
  echo "${#failed_reqs[@]} requirements file(s) failed to install:" >&2
  printf '    %s\n' "${failed_reqs[@]}" >&2
  echo "The baseline would record findings caused by the missing collections" >&2
  echo "rather than by the repository, so it is not being written. Fix the" >&2
  echo "installs and re-run (or mark a file automation-hub-only if its" >&2
  echo "collection genuinely has no stable community-Galaxy release)." >&2
  exit 1
fi

echo "==> Generating $BASELINE"
dirs=$(ls -d */ | grep -vE '^(docs|\.vscode|scripts)/' | tr -d '/' | tr '\n' ' ')
# --generate-ignore always writes .ansible-lint-ignore, so redirect it via the
# documented env var and restore the offline baseline afterwards.
cp .ansible-lint-ignore /tmp/.ansible-lint-ignore.offline.bak
ANSIBLE_LINT_IGNORE_FILE="$BASELINE" ansible-lint --generate-ignore $dirs || true
cp /tmp/.ansible-lint-ignore.offline.bak .ansible-lint-ignore

if [ ! -s "$BASELINE" ]; then
  echo "No findings with collections installed -- writing an empty baseline."
  : > "$BASELINE"
fi

echo ""
echo "==> Wrote $BASELINE ($(grep -cvE '^\s*(#|$)' "$BASELINE" || echo 0) entries)"
echo "    Commit it to turn the 'ansible-lint with collections' CI job into a"
echo "    blocking gate. Compare against .ansible-lint-ignore to see which"
echo "    syntax-check[unknown-module] entries were only an offline artifact."
